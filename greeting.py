import random

greeting_emoji = ["👋", "🙋‍♂️", "✋", "🙏", "🙌"]

greeting_type = ["Hello", "Sup", "Howdy", "Hi", "Hola", "Greetings", "Namaste", "Hey"]

greeting_hope = [
    "Hope you're having a great week!",
    "Hope you're having a great day!",
    "Hope you're doing well!",
    "Hope you're doing good!",
]


def get_greeting(name):
    return f"{random.choice(greeting_emoji)} {random.choice(greeting_type)}, {name}. {random.choice(greeting_hope)}"
