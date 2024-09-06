#!/usr/bin/python3

"""
    For imports and stuff
"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.__init__ import storage
import json


class HBNBCommand(cmd.Cmd):
    intro = ""
    prompt = "(hbnb) "
    file = None
    models = ["BaseModel"]
    instances = []
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
            except Exception as Err:
                print(Err)

    def do_show(self, args):
        "Shows info of an instance using its id"

        list = args.split()
        if len(list) == 0:
            print('** class name missing **')
            return ''
        if list[0] != 'BaseModel':
            print('** class doesn\'t exist **')
            return ''
        if len(list) < 2:
            print('** instance id missing **')
            return ''
        try:
            with open ('file.json', 'r') as file:
                objs = json.load(file)
                i = 0
                for key,val in objs.items():
                    self.instances.append(BaseModel(**val))
        except Exception as Err:
            print(Err)
        ids = [el.id for el in self.instances]
        if list[1] not in ids:
            print('** no instance found **')
            return ''
        for ins in self.instances:
            if ins.id == list[1]:
                print(ins)

    def do_all(self, args=''):
        'Show all strs of instances of a model'
        list = args.split()
        if len(list) == 0:
            print('** class doesn\'t exist **')
            return ''
        if list[0] not in self.models:
            print('** class doesn\'t exist **')
            return ''
        
        try:
            with open ('file.json', 'r') as file:
                objs = json.load(file)
                i = 0
                for key,val in objs.items():
                    self.instances.append(eval(f'{list[0]}({val})'))
        except Exception as Err:
            print(Err)
        for ins in self.instances:
            print(ins)



if __name__ == "__main__":
    HBNBCommand().cmdloop()
