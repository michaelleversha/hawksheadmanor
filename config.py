inventory = []
user_name = input("Welcome to Hawkshead Manor! You are one of London's finest private investigators, but forgive me... what is your name? ")
import time

suspects = [
    ["Turners", True],
    ["Eleanor", True],
    ["Victor", True],
    ["Mohamed", True],
    ["Peter", True]
]
suspect = "String"
study_visit = False
drawing_room_visit = False
score = 0

def type_text(text):
    """Helper function to print text with a delay (typing effect)."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()