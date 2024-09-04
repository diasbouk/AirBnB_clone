#!/usr/bin/python3

"""
    For imports and stuff
"""
import cmd


class HBNBCommand(cmd.Cmd):
    intro = ''
    prompt = '(hbnb) '
    file = None

    def do_quit(self, args=None):
        'Quit command to exit the program'
        return True

    def do_EOF(self, args=None):
        'EOF command to exit the program'
        return True

    def emptyline(self):
        return ''


if __name__ == '__main__':
    HBNBCommand().cmdloop()
