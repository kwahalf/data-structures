
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Usage:
    dojo create_room (<room_type> <room_name>)...
    dojo add_person <first_name> <last_name> <Person_role> <id_no>
                    [--a=<wants_accomodation>] [--p=<priority>]
    dojo (-i | --interactive)

    Options:
    -i, --interactive  Interactive Mode
"""


import sys
import os
import cmd
from docopt import docopt, DocoptExit
from pyfiglet import figlet_format
from termcolor import cprint
from dojo import Dojo

dojo = Dojo()


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


def intro():
    cprint(figlet_format("DOJO VERSION 0", font='starwars'),
           'yellow', 'on_red', attrs=['bold'])
    print("Welcome to the DOJO!")
    cprint(__doc__, 'blue')


class DojoSystem(cmd.Cmd):
    prompt = '(Dojo) '
    file = None

    @docopt_cmd
    def do_create_room(self, args):
        """Usage: create_room (<room_type> <room_name>)..."""

        purposes = args["<room_type>"]
        rooms = args["<room_name>"]
        for room in rooms:
            purpose = purposes[rooms.index(room)]
            dojo.create_room(room.upper(), purpose.upper())

    @docopt_cmd
    def do_add_person(self, args):
        """
        Usage: add_person <first_name> <second_name> <Person_role> <id_no>
               [--a=<wants_accomodation>] [--p=<priority>]
        """
        first_name = args["<first_name>"]
        second_name = args["<second_name>"]
        role = args["<Person_role>"]
        id_no = args["<id_no>"]
        if args['--a'] is None:
            wants_accomodation = "N"
        else:
            wants_accomodation = str(args['--a'])
        if args['--p'] is None:
            priority = 1
        else:
            priority = int(args['--p'])
        dojo.add_person(
            first_name,
            second_name,
            role,
            wants_accomodation.upper(),
            id_no,
            priority)


    def do_clear(self, arg):
        """Clears screen"""
        os.system("clear")

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""
        print("You have exited dojo succesfuly. Welcome back again!")
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    os.system("clear")
    intro()
    DojoSystem().cmdloop()

print(opt)
