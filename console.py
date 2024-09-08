#!/usr/bin/python3

"""
    For imports and stuff
"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.__init__ import storage
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.city import City
import json


class HBNBCommand(cmd.Cmd):
    intro = ""
    prompt = "(hbnb) "
    file = None
    models = ["BaseModel", "User", "State",
              "Place", "Amenity", "Review", "City"]
    all_instances = []
    try:

        storage.reload()
        objs = storage.all()
        for key, val in objs.items():
            all_instances.append(val)
    except Exception as Err:
        print(Err)

    def check_arguments(self, args=''):
        """ Check for args valid"""
        list = args.split(' ')
        if len(list) == 0:
            print('** class name missing **')
            return False
        if list[0] not in self.models:
            print('** class doesn\'t exist **')
            return False
        if len(list) == 1:
            print('** instance id missing **')
            return False
        ids = [el.id for el in self.all_instances]
        if list[1] not in ids:
            print('** no instance found **')
            return False
        return True

    def do_quit(self, *args):
        "Quit command to exit the program"
        return True

    def do_EOF(self, args):
        "EOF command to exit the program"
        return True

    def emptyline(self):
        "When an emptyline is entered, no action is taken"
        return False

    def do_create(self, *args):
        "Creates an new instance"
        if args[0] == "":
            print("** class name missing **")
            return ""
        if args is not None:
            if args[0] not in self.models:
                print("** class doesn't exist **")
                return ""
            try:
                bm = eval(f"{args[0]}()")
                print(bm.id)
                bm.save()
                self.all_instances.append(bm)
            except Exception as Err:
                print(Err)

    def do_show(self, args=''):
        "Shows info of an instance using its id"

        list = args.split()
        if self.check_arguments(args) is False:
            return ''
        for ins in self.all_instances:
            if ins.id == list[1] and list[0] == ins.__class__.__name__:
                print(ins)
                return ''
        print('** no instance found **')

    def do_destroy(self, args=''):
        'Deletes an instance'
        list = args.split()
        if self.check_arguments(args) is False:
            return ''
        for el in self.all_instances:
            if el.id == list[1] and list[0] == el.__class__.__name__:
                index = self.all_instances.index(el)
                self.all_instances.pop(index)
                storage.destroy(el)
                return ''
        print('** no instance found **')

    def do_all(self, args=''):
        'Show all strs of base_model_instances of a model'

        if args == '':
            print('empty')
            for ins in self.all_instances:
                print(ins)
            return ''
        if args not in self.models:
            print('** class doesn\'t exist **')
            return ''
        for ins in self.all_instances:
            if ins.__class__.__name__ == args:
                print(ins)

    def do_update(self, args=''):
        'Updates an instance'
        list = args.split()
        if self.check_arguments(args) is False:
            return ''
        if len(list) == 2:
            print('** attribute name missing **')
            return ''
        if len(list) == 3:
            print('** value missing **')
            return ''
        for ins in self.all_instances:
            if ins.id == list[1] and ins.__class__.__name__ == list[0]:
                setattr(ins, list[2], list[3])
            return ''
        print('** no instance found **')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
