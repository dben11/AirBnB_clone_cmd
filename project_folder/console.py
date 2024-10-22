#!/usr/bin/env python3
import cmd
from models.user import User
from models.place import Place
from models.city import City
from models.review import Review
from models.engine.file_storage import FileStorage
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for HBNB."""
    prompt = 'Welcome to (hbnb)>>> '
    
    def __init__(self):
        super().__init__()
        print("Welcome to hbnb-command line")
        
    def do_create(self, class_name):
        """Create a new instance of a class.
        Usage: create <class_name>
        """
        if not class_name:
            print("** class name missing **")
            return
        
        try:
            # Dynamically create an instance of the class
            cls = eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return
        
        # Create a new instance, save it, and print its ID
        new_instance = cls()
        storage.new(new_instance)
        storage.save()
        print(new_instance.id)
        
        
    def do_show(self, args):
        """Show an instance based on the class name and id."""
        try:
            class_name, obj_id = args.split()
        except ValueError:
            print("** class name missing or id missing **")
            return

        # Check if class exists
        try:
            cls = eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return

        # Retrieve the object
        key = f"{class_name}.{obj_id}"
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")


    
    def do_destroy(self, args):
    # def do_destroy(self, args):
        try:
            class_name, obj_id = args.split()
            key = f"{class_name}.{obj_id}"
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")
        except ValueError:
            print("** class name missing or id missing **")
            
    def do_update(self, args):
        try:
            args_list = args.split()
            if len(args_list) < 4:
                print("** Usage: update <class name> <id> <attribute name> <attribute value> **")
                return
            class_name, obj_id, attr_name, attr_value = args_list[0], args_list[1], args_list[2], args_list[3]
            key = f"{class_name}.{obj_id}"
            
            #check if object exist in the storage
            if key in storage.all():
                obj = storage.all()[key]
                #update the attribute
                setattr(obj, attr_name, attr_value)
                #save the update object back to storage
                storage.save()
            
            else:
                print("** no instance found **")
                
        except Exception as e:
            print(f"*** Error: {e} **")
            

    def do_all(self, class_name=None):
        """Show all instance or all instance of a specific class."""
        if class_name is not None:
            objects = storage.all()
            for obj_id, obj in objects.items():
                print(obj)
            # instances = [str(obj) for key, in obj in storage.all().items() if key.startswith(class_name)]
            # print(instances)
            
        else:
            if class_name:
                try:
                    cls = eval(class_name)
                except NameError:
                    print("** class doesn't exist **")
                    return
            else:
                print("** class name missing **")
                return
            # print(storage.all())
    
    def do_quit(self, arg):
        print("Exiting... the program")
        return True
    
    def do_EOF(self, arg):
        return self.do_quit(arg)
    
    def emptyline(self):
        pass
    
    def help_command(self, arg):
        """Help command"""
        super().do_help(arg)
        
    def do_count(self, arg):
        """Retrieve the number of instances of a class.
        Usage: <class name>.count()
        """
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.split()[0]
        
        # Check if class exists
        try:
            cls = eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return
        
        # Retrieve all objects and count instances of the class
        objects = storage.all()
        count = sum(1 for key in objects if key.startswith(class_name + "."))
        
        print(count)
        
    def default(self, line):
        """Handle <class name>.<command>(<args>) format."""
        if '.' in line:
            parts = line.split('.')
            class_name = parts[0]
            
            # Check if the command contains parentheses
            if len(parts) > 1 and '(' in parts[1]:
                command = parts[1][:parts[1].find('(')]  # Extract the command
                args = parts[1][parts[1].find('(') + 1 : parts[1].find(')')]  # Extract the arguments

                # Dynamically handle commands
                if command == "show":
                    self.do_show(f"{class_name} {args}")
                elif command == "all":
                    self.do_all(class_name)
                elif command == "count":
                    self.do_count(class_name)
                elif command == "destroy":
                    self.do_destroy(class_name)
                elif command == "update":
                    self.do_update(f"{class_name} {args}")
                else:
                    print(f"*** Unknown command: {command}")
            else:
                print(f"*** Unknown syntax: {line}")
        else:
            print(f"*** Unknown syntax: {line}")




if __name__ == '__main__':
    HBNBCommand().cmdloop()
    
    
    
#    #define class
# class HBNBCommand(cmd.Cmd):
   
#    #dine methods
#    def do_quit():
       
    