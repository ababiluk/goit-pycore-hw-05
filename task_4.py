import sys

# Декоратор для обробки помилок (максимум 2-3 рівні вкладення)
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter the argument for the command."
    return wrapper

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    # Замість великого if/else використовуємо перевірку і вихід
    if name not in contacts:
        raise KeyError
    
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    name = args[0]
    return f"{name}: {contacts[name]}"

@input_error
def show_all(contacts):
    if not contacts:
        return "Contact list is empty."
    
    # Створюємо список рядків і з'єднуємо їх (пласка структура)
    lines = [f"{name}: {phone}" for name, phone in contacts.items()]
    return "\n".join(lines)

def parse_input(user_input):
    parts = user_input.split()
    # Ранній вихід, якщо ввід порожній
    if not parts:
        return "", []
    
    cmd = parts[0].strip().lower()
    args = parts[1:]
    return cmd, args

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ").strip()
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        if command == "hello":
            print("How can I help you?")
            continue # Повертаємось на початок циклу, уникаючи else

        if command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()