import time

def type_text(text):
    """Helper function to print text with a delay (typing effect)."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

def bed_choice():
    type_text("Do you: ")
    time.sleep(1)
    type_text("1. Turn over and try to catch a few more minutes sleep")
    time.sleep(1)
    type_text("OR")
    time.sleep(1)
    type_text("2. Crawl out of bed, shrug into something presentable, and answer the door")
    time.sleep(1)
    
    while True:
        user_choice = input("One (1) or Two (2): ").strip().lower()
        
        if user_choice in ["1", "one"]:
            type_text("The knocking doesn't stop. You keep tossing and turning, but they won't go away. You are forced to get out of bed and answer the door anyway.")
            time.sleep(1)
            type_text("You answer the door. There is a small shabby man in a soaking wet coat. 'What took you so long?' he asks, as he thrusts a telegram into your hands before hurriedly taking his leave.")
            time.sleep(1)
            type_text("You tear the telegram open. It reads:")
            time.sleep(1)
            type_text("URGENT STOP LORD HAWKSHEAD MURDERED STOP PLEASE COME AT ONCE STOP SENDING MOTORCAR TO COLLECT YOU IMMEDIATELY STOP. LADY ELEANOR HAWKSHEAD")
            time.sleep(1)
            type_text("Hawkshead Manor, the sprawling, isolated estate renowned for its dark history. You had heard the rumours, of course, but never imagined you would be drawn into its sinister web.")
            type_text("You hear a car pull up outside.")
            break
            # game_score += 1
        elif user_choice in ["2", "two"]:
            type_text("You answer the door. There is a small shabby man in a soaking wet coat. 'What took you so long?' he asks, as he thrusts a telegram into your hands before hurriedly taking his leave.")
            time.sleep(1)
            type_text("You tear the telegram open. It reads:")
            time.sleep(1)
            type_text("URGENT STOP LORD HAWKSHEAD MURDERED STOP PLEASE COME AT ONCE STOP SENDING MOTORCAR TO COLLECT YOU IMMEDIATELY STOP. LADY ELEANOR HAWKSHEAD")
            time.sleep(1)
            type_text("Hawkshead Manor, the sprawling, isolated estate renowned for its dark history. You had heard the rumours, of course, but never imagined you would be drawn into its sinister web.")
            type_text("You hear a car pull up outside.")
            break
        else:
            type_text("That's not a valid choice. Try again.")
            bed_choice()

def car_choice():
    type_text("Do you: ")
    time.sleep(1)
    type_text("1. Gather your things and make your way outside")
    time.sleep(1)
    type_text("OR")
    time.sleep(1)
    type_text("2. Decide you're having none of this nonsense and refuse to engage")
    while True:
                user_choice = input("One (1) or Two (2): ").strip().lower()
                
                if user_choice in ["1", "one"]:
                    type_text("You gather your investigative tools and pack some clothes and hurry outside to the waiting car.")
                    time.sleep(1)
                    type_text("As it rumbles to life and pulls away, the rain pelts down, almost as if the heavens themselves are mourning the tragedy that has befallen the Hawkshead Manor.")
                    time.sleep(1)
                    type_text("The journey seems to last an eternity and as morning turns to afternoon and afternoon to evening, you can only wonder what could possibly have happened to Lord Hawkshead?")
                    time.sleep(1)
                    type_text("As the towering silhouette of Hawkshead Manor emerges from the gloom, you steady your resolve. You are ready to uncover the truth, no matter what it takes.")
                    break
                elif user_choice in ["2", "two"]:
                    type_text("Are you sure? That's not really playing the game. That's not fun... Let's go outside anyway")
                    time.sleep(1)
                    type_text("You gather your investigative tools and pack some clothes and hurry outside to the waiting car.")
                    time.sleep(1)
                    type_text("As it rumbles to life and pulls away, the rain pelts down, almost as if the heavens themselves are mourning the tragedy that has befallen the Hawkshead Manor.")
                    time.sleep(1)
                    type_text("The journey seems to last an eternity and as morning turns to afternoon and afternoon to evening, you can only wonder what could possibly have happened to Lord Hawkshead?")
                    time.sleep(1)
                    type_text("As the towering silhouette of Hawkshead Manor emerges from the gloom, you steady your resolve. You are ready to uncover the truth, no matter what it takes.")
                    break
                else:
                    type_text("Invalid choice. Please choose '1' or '2'.")
                    car_choice()

