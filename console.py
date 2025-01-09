#!/usr/bin/python3
"""Command interpreter for AirBnB clone"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnB objects"""
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit the program"""
        return True

    def do_EOF(self, args):
        """Exit the program on EOF"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
