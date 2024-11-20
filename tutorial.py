import time
import config

user_name = config.user_name

type_text = config.type_text

def tutorial(skip_to_welcome=False):
    # global game_score
    # global user_name
    while True:
        if not skip_to_welcome:  # Only show tutorial question if it's not skipped
            type_text("Before you load into MYSTERY AT HAWKSHEAD MANOR, would you like to do a tutorial?")
            time.sleep(1)
            user_choice = input("Yes or No ").strip().title()

            if user_choice in ["Yes", "Y"]:
                type_text("Loading Day Zero...")
                time.sleep(1)
                type_text("...")
                time.sleep(1)
                type_text("...")
                time.sleep(1)
                skip_to_welcome = True
            elif user_choice in ["No", "N"]:
                type_text("Okay then! Let's get started.")
                return
            else: 
                type_text ("Huh? That's not a valid choice, Please choose yes or no.")    
                continue
        # Skip to the tutorial's "Welcome Rookie!" section if asked to restart
        type_text(f"Welcome {user_name}! It appears you need some brushing up on those detective skills ay? Well, that's why I'm here Now.. how about we do our example mystery question?")
        time.sleep(1)
        type_text("You have two suspects in front of you, one is the murderer and the other is innocent. You have to figure out who is the murderer through deciphering an answer.")
        time.sleep(1)
        type_text("So first we are going to question Bob!")
        time.sleep(1)
        type_text("You will be given two options. You can select your choice by typing '1' or '2' into the terminal.")
        time.sleep(1)

        while True:
            user_choice = input("(Option 1) What were you doing at the time of the crime? or (Option 2) What did you last eat for breakfast? ").strip()
            if user_choice in ["1", "One"]:
                type_text("Bob: I was watching television at the time.")
                time.sleep(1)
                type_text("Great question rookie!")
                time.sleep(1)
                break
            elif user_choice in ["2", "Two"]:
                type_text("Bob: That's a weird question, I was eating beans and toast but... why?")
                time.sleep(1)
                type_text(f"Uh oh {user_name}! Now they are questioning YOU! Questions like these are often unrelated to the topic and can lead to people questioning you.")
                time.sleep(1)
                type_text("But for now, we can solve that issue by simply saying...")
                time.sleep(1)
                type_text("Well sorry Bob, I was just looking into why you look so healthy today!")
                time.sleep(1)
                break
            else:
                type_text(f"That isn't one of the options I offered, {user_name}! Please choose 1 or 2.")

        type_text("Well, time for the next candidate! Jerry!")
        time.sleep(1)
        type_text("You will be given two options. You can select your choice by typing '1' or '2' into the terminal.")

        while True:
            user_choice = input("(Option 1) What were you doing at the time of the crime? or (Option 2) Are you the murderer? ")
            if user_choice in ["1", "One"]:
                type_text("Jerry: I was cooking in the kitchen.")
                time.sleep(1)
                type_text(f"Weird! {user_name} what do you think?")
                time.sleep(1)
                type_text("Well, that doesn't matter for now! we should pick an innocent and a murderer now!")
                time.sleep(1)
                break
            elif user_choice in ["2", "Two"]:
                type_text("Jerry: What are you insane?! I can't believe you'd frame me for a murder! I should sue you!")
                time.sleep(1)
                type_text(f"Maybe {user_name}, don't just point a finger without evidence! This could lead to disastrous consequences.")
                time.sleep(1)
                type_text("...")
                break
            else:
                (f"Those aren't the options I offered, {user_name}! Please choose '1' or '2'.")


                
        type_text("You will be given two options. You can select your choice by typing 'Bob' or 'Jerry' into the terminal.")

        while True:
                user_choice = input("'Bob' is the murderer or 'Jerry' is the murderer ").strip().title()
                if user_choice in ["Bob", "B"]:
                    type_text(f"Bob? are you serious? He's innocent... Come on {user_name} I can't believe you got this far to fail!")
                    time.sleep(1)
                    type_text("...")
                    break
                elif user_choice in ["Jerry", "J"]:
                    type_text("That's right rookie! you've found the murderer and saved everyone.. good job! you can now start the main game..")
                    time.sleep(1)
                    type_text("Loading...")
                    time.sleep(1)
                    type_text("...")
                    time.sleep(1)
                    return
                else:
                    type_text(f"Uhh {user_name}? That isn't either person. Please choose Bob or Jerry.")

        # Ask if the user wants to restart the tutorial or move on
        while True:
            type_text("\nWould you like to restart the tutorial or move on to the main game?")
            restart_choice = input("Type 'Restart' to do the tutorial again or 'Continue' to move on: ").strip().title()
            if restart_choice in ["Continue", "C"]:
                type_text("Moving on to the main game...")
                return
            elif restart_choice in ["Restart", "R"]:
                type_text("Restarting the tutorial...")
                skip_to_welcome = True  # Set this to True to skip to 'Welcome Rookie!' next time
                break
            else:
                type_text("Invalid choice, Please choose Restart or Continue.")
