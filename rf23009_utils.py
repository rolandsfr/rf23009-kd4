import random

# Generates a random compliment

def generate_compliment():
    adjectives = ["amazing", "incredible", "fantastic"]
    nouns = ["person", "friend", "human"]

    adjective = random.choice(adjectives)
    noun = random.choice(nouns)

    return f"You are an {adjective} {noun}!"

# Generates a random word of encouragement

def generate_encouragement():
    phrases = [
        "Keep going, you're doing great!",
        "Don't give up, you've got this!",
        "Believe in yourself and amazing things will happen!"
    ]

    return random.choice(phrases)