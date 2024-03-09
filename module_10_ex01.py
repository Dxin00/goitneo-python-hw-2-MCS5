def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Please provide a contact name."

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def show_all(contacts: dict):
    result_string = ""
    for name, phone in contacts.items():
        result_string += f"{name} - {phone}\n"
    return result_string

@input_error
def show_phone(args, contacts: dict):
    name = args[0]
    phone = contacts[name]
    return phone

@input_error
def change_contact(args, contacts):
    name, phone = args
    if contacts[name]:
        contacts[name] = phone
        return "Contact changed."


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "all":
            print(show_all(contacts=contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args,contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()