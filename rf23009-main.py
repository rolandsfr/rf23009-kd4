import random
from rf23009_utils import generate_compliment, generate_encouragement

# Generates a random motivational quote
def generate_quote():
    subjects = ["You", "Your determination", "Success"]
    verbs = ["can overcome", "will achieve", "inspires"]
    objects = ["any obstacle.", "greatness.", "the world."]

    subject = random.choice(subjects)
    verb = random.choice(verbs)
    obj = random.choice(objects)

    return f"{subject} {verb} {obj}"

if __name__ == "__main__":
    print("Here's your motivational quote:")
    print(generate_quote())

    print("\nAnd here's a compliment:")
    print(generate_compliment())

    print("\nFinally, some encouragement:")
    print(generate_encouragement())
