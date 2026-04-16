import random

# subjects
subjects = [
    "Shahrukh Khan",
    "Virat Kohli",
    "Nirmala Sitharaman",
    "A Mumbai cat",
    "A group of monkeys",
    "Prime Minister Modi",
    "Auto rickshaw driver from Delhi"
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
]

places_or_things = [
    "at Red Fort",
    "in Mumbai local",
    "a plate of samosa",
    "inside Parliament",
    "at Ganga ghat",
    "during IPL match",
    "at India Gate"
]

# headline generator loop
while True:
    sub = random.choice(subjects)
    act = random.choice(actions)
    place = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {sub} {act} {place}"
    print("\n" + headline)

    user_input = input("\nDo you want another headline? (yes/no): ").strip().lower()

    if user_input == "no":
        print("\nThanks for using the Fake News Headline Generator. Have a fun day!")
        break 
