import random

# Generates a random motivational quote

def generate_quote():
    parts = {
        "subjects": ["You", "Your determination", "Success"],
        "verbs": ["can overcome", "will achieve", "inspires"],
        "objects": ["any obstacle.", "greatness.", "the world."]
    }

    subject = random.choice(parts["subjects"])
    verb = random.choice(parts["verbs"])
    obj = random.choice(parts["objects"])

    return f"{subject} {verb} {obj}"

if __name__ == "__main__":
    print("Here's your motivational quote:")
    print(generate_quote())
