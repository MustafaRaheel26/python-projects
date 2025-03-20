import random

def mad_libs():
    stories = [
        "Today, I went to the {place}. I saw a {adjective} {animal} {verb} near the {object}.",
        "My best friend is a {adjective} {animal} who loves to {verb} at the {place}.",
        "Once upon a time, a {adjective} {animal} found a magical {object} at the {place} and decided to {verb}."
    ]
    
    story = random.choice(stories)

    words = {
        "place": input("Enter a place: "),
        "adjective": input("Enter an adjective: "),
        "animal": input("Enter an animal: "),
        "verb": input("Enter a verb: "),
        "object": input("Enter an object: ")
    }

    if any(not word.strip() for word in words.values()):
        print("Please fill in all the blanks!")
        return mad_libs()

    print("\nHere is your story:\n")
    print(story.format(**words))

mad_libs()
