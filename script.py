import redis
import readline

# Connect to Redis server
# r = redis.Redis(host='localhost', port=6379, db=0)

# # Create
# r.set('name', 'John')

# # Read
# name = r.get('name')
# print(name)

# # Update
# r.set('name', 'Jane')

# # Read again
# name = r.get('name')
# print(name)

# # Delete
# r.delete('name')

# # Read after deletion
# name = r.get('name')
# print(name)

# Define the completion options with arguments
options = {
    'quit': [],
    'list': ['users', 'products', 'orders'],
    'search': ['text', 'date', 'category']
}

def completer(text, state):
    option_texts = [option for option in options if option.startswith(text)]
    if state < len(option_texts):
        option = option_texts[state]
        if option in options:
            return option + ' '
    return None

# Set the completer function
readline.set_completer(completer)
readline.parse_and_bind('tab: complete')

while True:
    user_input = input("Enter something: ")

    if user_input == "quit":
        break

    parts = user_input.split()
    if parts:
        command = parts[0]
        if command in options:
            arguments = options[command]
            if len(parts) > 1 and parts[1] in arguments:
                print("Executing command:", command, "with argument:", parts[1])
            else:
                print("Valid arguments for", command, "are:", ", ".join(arguments))
        else:
            print("Invalid command:", command)