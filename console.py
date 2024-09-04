#!/usr/bin/python3

"""
    For imports and stuff
"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    intro = ''
    prompt = '(hbnb) '
    file = None
    models = ['BaseModel']
    storage.reload()
    reloaded_objs = storage.all()

    def do_quit(self, args=''):
        'Quit command to exit the program'
        return True

    def do_EOF(self, args=''):
        'EOF command to exit the program'
        return True

    def emptyline(self):
        'When an emptyline is entered, no action is taken'
        return ''

    def do_create(self, *args):
        'Creates an new instance'
        if args[0] == '':
            print('** class name missing **')
            return ''
        if args is not None:
            if args[0] not in self.models:
                print('** class doesn\'t exist **')
                return ''
            try:
                bm = eval(f'{args[0]}()')
                print(bm.id)
                bm.save()
            except Exception as Err:
                print(Err)

    def do_show(self, arg=''):

        print(el for el in self.reloaded_objs)
        print(self.reloaded_objs)

        # ids = [obj.get('id') for obj in self.reloaded_objs]
        # args = arg.split(' ')
        # if args[0] == '':
        #     print('** class name missing **')
        #     return ''
        # if args[0] not in self.models:
        #     print('** class doesn\'t exist **')
        # if args[1] is None:
        #     print('** instance id missing **')
        #     return ''
        # if args[1] not in ids:
        #     print('** no instance found **')
        # print(self.reloaded_objs)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
