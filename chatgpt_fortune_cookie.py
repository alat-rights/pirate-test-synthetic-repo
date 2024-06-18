import random

def get_fortune():
    fortunes = [
        "You will discover an unexpected treasure.",
        "Now is a good time to try something new.",
        "Your kindness will lead you to success.",
        "A thrilling time is in your near future.",
        "Someone has Googled you recently.",
        "You will receive pleasant news by mail."
    ]
    return random.choice(fortunes)

# Generate and display a random fortune
print(get_fortune())
