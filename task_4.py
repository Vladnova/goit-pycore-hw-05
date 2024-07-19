from typing import List, Tuple, Dict, Callable

def input_error(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Invalid command format. Please provide the correct input."
    return inner


def parse_input(user_input: str)->Tuple[str, List]:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args:Tuple[str, str], contacts:Dict[str, str])->str:
    name, phone = args

    contacts[name] = phone
    return "Contact added!"

@input_error
def change_contact(args:Tuple[str, str], contacts:Dict[str, str])->str:
    
    name, phone= args

    if name in contacts:
        contacts[name] = phone
        return 'Contact updated.'
    else:
        return f'Contact {name} not found'

@input_error
def show_phone(args:Tuple[str, str], contacts:Dict[str, str])->str:
    if not args:
        raise KeyError
    
    name = args[0]

    if name in contacts:
        return contacts[name] 
    else:
        return f'Contact {name} not found'


@input_error
def show_all(contacts:Dict[str, str])->Dict[str, str] | str:
    if not contacts:
        return 'No contacts added yet'
    return contacts


def main()->str:
    contacts = {}
    print("Welcome to the assistant bot!")


    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == 'hello':
            print("How can I help you?")
        elif command == 'add':
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(show_phone(args, contacts))      
        elif command == 'all':
            print(show_all(contacts)) 
        else:
            print('Invalid command.')



if __name__ == "__main__":
    main()