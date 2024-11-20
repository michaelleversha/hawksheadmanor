# Game Settings
# --------------
import time
import tutorial
import config

inventory = []
user_name = config.user_name
 
suspects = [
    ["Turners", True],
    ["Eleanor", True],
    ["Victor", True],
    ["Mohamed", True],
    ["Peter", True]
]
 
study_visit = False
drawing_room_visit = False
 
def type_text(text):
    """Helper function to print text with a delay (typing effect)."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()
 
# DAY ZERO

# def day_zero(skip_to_welcome=False):
#     # global game_score
#     while True:
#         if not skip_to_welcome:  # Only show tutorial question if it's not skipped
#             type_text("Before you load into MYSTERY AT HAWKSHEAD MANOR, would you like to do a tutorial?")
#             time.sleep(1)
#             user_choice = input("Yes or No ").strip().title()

#             if user_choice in ["Yes", "Y"]:
#                 type_text("Loading Day Zero...")
#                 time.sleep(1)
#                 type_text("...")
#                 time.sleep(1)
#                 type_text("...")
#                 time.sleep(1)
#                 skip_to_welcome = True
#             elif user_choice in ["No", "N"]:
#                 type_text("Okay then! Let's get started.")
#                 return
#             else: 
#                 type_text ("Huh? That's not a valid choice, Please choose yes or no.")    
#                 continue
#         # Skip to the tutorial's "Welcome Rookie!" section if asked to restart
#         type_text("Welcome Rookie! It appears you need some brushing up on those detective skills ay? Well, that's why I'm here Now.. how about we do our example mystery question?")
#         time.sleep(1)
#         type_text("You have two suspects in front of you, one is the murderer and the other is innocent. You have to figure out who is the murderer through deciphering an answer.")
#         time.sleep(1)
#         type_text("So first we are going to question Bob!")
#         time.sleep(1)
#         type_text("You will be given two options. You can select your choice by typing '1' or '2' into the terminal.")
#         time.sleep(1)

#         while True:
#             user_choice = input("(Option 1) What were you doing at the time of the crime? or (Option 2) What did you last eat for breakfast? ").strip()
#             if user_choice in ["1", "One"]:
#                 type_text("Bob: I was watching television at the time.")
#                 time.sleep(1)
#                 type_text("Great question rookie!")
#                 time.sleep(1)
#                 break
#             elif user_choice in ["2", "Two"]:
#                 type_text("Bob: That's a weird question, I was eating beans and toast but... why?")
#                 time.sleep(1)
#                 type_text("Uh oh rookie! Now they are questioning YOU! Questions like these are often unrelated to the topic and can lead to people questioning you.")
#                 time.sleep(1)
#                 type_text("But for now, we can solve that issue by simply saying...")
#                 time.sleep(1)
#                 type_text("Well sorry Bob, I was just looking into why you look so healthy today!")
#                 time.sleep(1)
#                 break
#             else:
#                 type_text("That isn't one of the options I offered rookie! Please choose 1 or 2.")

#         type_text("Well, time for the next candidate! Jerry!")
#         time.sleep(1)
#         type_text("You will be given two options. You can select your choice by typing '1' or '2' into the terminal.")

#         while True:
#             user_choice = input("(Option 1) What were you doing at the time of the crime? or (Option 2) Are you the murderer? ")
#             if user_choice in ["1", "One"]:
#                 type_text("Jerry: I was cooking in the kitchen.")
#                 time.sleep(1)
#                 type_text("Weird! Rookie what do you think?")
#                 time.sleep(1)
#                 type_text("Well, that doesn't matter for now! we should pick an innocent and a murderer now!")
#                 time.sleep(1)
#                 break
#             elif user_choice in ["2", "Two"]:
#                 type_text("Jerry: What are you insane?! I can't believe you'd frame me for a murder! I should sue you!")
#                 time.sleep(1)
#                 type_text("Maybe rookie, don't just point a finger without evidence! This could lead to disastrous consequences.")
#                 time.sleep(1)
#                 type_text("...")
#                 break
#             else:
#                 ("Those aren't the options I offered, rookie! Please choose '1' or '2'.")


                
#         type_text("You will be given two options. You can select your choice by typing 'Bob' or 'Jerry' into the terminal.")

#         while True:
#                 user_choice = input("'Bob' is the murderer or 'Jerry' is the murderer ").strip().title()
#                 if user_choice in ["Bob", "B"]:
#                     type_text("Bob? are you serious? He's innocent... Come on Rookie I can't believe you got this far to fail!")
#                     time.sleep(1)
#                     type_text("...")
#                     break
#                 elif user_choice in ["Jerry", "J"]:
#                     type_text("That's right rookie! you've found the murderer and saved everyone.. good job! you can now start the main game..")
#                     time.sleep(1)
#                     type_text("Loading...")
#                     time.sleep(1)
#                     type_text("...")
#                     time.sleep(1)
#                     return
#                 else:
#                     type_text("Uhh Rookie? That isn't either person. Please choose Bob or Jerry.")

#         # Ask if the user wants to restart the tutorial or move on
#         while True:
#             type_text("\nWould you like to restart the tutorial or move on to the main game?")
#             restart_choice = input("Type 'Restart' to do the tutorial again or 'Continue' to move on: ").strip().title()
#             if restart_choice in ["Continue", "C"]:
#                 type_text("Moving on to the main game...")
#                 return
#             elif restart_choice in ["Restart", "R"]:
#                 type_text("Restarting the tutorial...")
#                 skip_to_welcome = True  # Set this to True to skip to 'Welcome Rookie!' next time
#                 break
#             else:
#                 type_text("Invalid choice, Please choose Restart or Continue.")

# INTRO MINI  FUNCS

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


# INTRO FUNCS

def start_game():
    print(''' __  ____   ______ _____ _____ ______   __     _  _____    ''')
    print('''|  \\/  \\ \\ / / ___|_   _| ____|  _ \\ \\ / /    / \\|_   _|    ''')
    print('''| |\\/| |\\ \\V /\\___ \\ | | |  _| | |_) \\ \\V /    / _ \\ | |      ''')
    print('''| |  | | | |  ___) || | | |___|  _ < | |    / ___ \\| |      ''')
    print('''|_|  |_| |_|_|____/ |_|_|_____|_| \\_\\|_|___/_/   \\_\\_|____  ''')
    print('''| | | |  / \\ \\      / / |/ / ___|| | | | ____|  / \\  |  _ \\ ''')
    print('''| |_| | / _ \\ \\ /\\ / /| ' /\\___ \\| |_| |  _|   / _ \\ | | | |''')
    print('''|  _  |/ ___ \\ \\V  \\V / | . \\ ___) |  _  | |___ / ___ \\| |_| |''')
    print('''|_| |_/_/  _\\_\\_/\\_/_ |_|\\_\\____/|_| |_|_____/_/   \\_\\____/ ''')
    print('''|  \\/  |  / \\  | \\ | |/ _ \\|  _ \\                           ''')
    print('''| |\\/| | / _ \\ |  \\| | | | | |_) |                          ''')
    print('''| |  | |/ ___ \\| |\\  | |_| |  _ <                           ''')
    print('''|_|  |_/_/   \\_\\_| \\_|\\___/|_| \\_\\                          ''')
    print("...")
    time.sleep(1)
    print("Loading...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("Loading...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("Loading...")
    time.sleep(1)
    type_text(f"{user_name} is dozing in their bed. The steady patter of rain against the windowpane slowly pulls you from your slumber. You sit up in bed and rub the fatigue from your eyes. Another sleepless night, as the sound of the neighbours upstairs arguing and the laundry room next door woke you up time and again. There is a knock at the door.")
    time.sleep(1)
    bed_choice()
    car_choice()

# DAY ONE MINI FUNCS

def arrival_choice():
    type_text("What would you like to do first?")
    time.sleep(1)
    type_text("1. Ask Mr Filigree about the situation")
    time.sleep(1)
    type_text("OR")
    time.sleep(1)
    type_text("2. Waste no time and head inside the Manor.")
    
    user_choice = input("One (1) or Two (2): ").strip().lower()
    
    if user_choice in ["1", "one"]:
        type_text("'Mr. Filigree, can you tell me what happened?' you enquire, your gaze stern.")
        time.sleep(1)
        type_text(f"He lets out a heavy sigh. I'm afraid the situation is most dire, {user_name}'")
        time.sleep(1)
        type_text("'Late last night, we found Lord Hawkshead murdered in his study.'")
        time.sleep(1)
        type_text("Your eyes widen slightly at the news. 'Murdered? Do you have any idea who would want to harm him?'")
        time.sleep(1)
        type_text("Mr. Filigree shakes his head. I'm afraid I don't know. Lady Eleanor Hawkshead, Lord Hugo's second cousin, as well as the others, are all gathered in the drawing room. They're waiting to speak with you.'")
        time.sleep(1)
        type_text("You nod, mentally preparing yourself for the investigation ahead. 'Very well, let's not keep them waiting then.'")
        time.sleep(1)
        type_text("You go inside.")
    elif user_choice in ["2", "two"]:
        type_text("You follow Mr. Filigree through the cavernous foyer, the sound of your footsteps echoing off the high ceilings.")
        time.sleep(1)
        type_text("The air is thick with an uneasy silence, the usual grandeur of the manor dampened by the pall of tragedy.")
        time.sleep(1)
        type_text("As you reach the drawing room, Mr. Filigree turns to you. 'Lady Eleanor Hawkshead, Lord Hugo's second cousin, as well as the others, are all gathered in the drawing room. They're waiting to speak with you'")
    else:
        type_text("That's not a valid option. Try again.")
        arrival_choice()

def main_hall_choice():
    global study_visit
    global drawing_room_visit
    type_text("Do You:")
    time.sleep(1)
    type_text("1, First insist on inspecting the crime scene in Lord Hugo's study?")
    time.sleep(1)
    type_text("OR")
    time.sleep(1)
    type_text("2. Meet whoever these guests are in the drawing room?")
    
    user_choice = input("One (1) or Two (2): ").strip().lower()
    
    if user_choice in ["1", "one"]:
        study_visit = True
        study()
        if drawing_room_visit == False:
            drawing_room_visit = True
            time.sleep(1)
            drawing_room()
        else:
            type_text("")
    elif user_choice in ["2", "two"]:
        drawing_room_visit = True
        type_text("As you enter the drawing room, your eyes scan the faces of the assembled guests. They all turn to you, the air thick with tension.")
        time.sleep(1)
        drawing_room()
    else:
        type_text("That's not a valid choice. Try again.")
        main_hall_choice()

def study():
    global drawing_room_visit
    type_text("You follow the butler to Lord Hawkshead's study.")
    time.sleep(1)
    type_text("The room is in disarray, with papers scattered and a pool of dried blood on the floor. 'Tell me what happened.'") 
    time.sleep(1)
    type_text("Mr Filigree explains that he found Lord Hugo here, murdered by an ornate Egyptian dagger.")
    time.sleep(1)
    type_text("What would you like to do next?")
    time.sleep(1)
    type_text("1. Closely inspect the crime scene for clues.")
    time.sleep(1)
    type_text("OR")
    time.sleep(1)
    type_text("2. Ask the butler more questions about the incident.")
    
    user_choice = input("One (1) or Two (2): ").strip().lower()
    
    if user_choice in ["1", "one"]:
        type_text("You crouch down and carefully examine the study, taking in every detail.")
        time.sleep(1)
        type_text("The dagger appears to be part of Lord Hawkshead's private collection.")
        time.sleep(1)
        type_text("There are signs of a struggle, but no obvious signs of how the killer escaped.")
        if drawing_room_visit == True:
            type_text("Mr. Filigree, looking rather worn out, coughs politely. 'Pardon the interruption, but it really is getting awfully late")
            time.sleep(1)
            type_text("'I must insist on showing you to your quarters.'")
        else:
            type_text("Satisfied you've gathered what you can from the study, you decide it's time to meet the other guests.")
            time.sleep(1)
            type_text("As you enter the drawing room, your eyes scan the faces of the assembled guests. They all turn to you, the air thick with tension.")
    elif user_choice in ["2", "two"]:
        type_text("'Tell me what can you tell me about the events leading up to the murder?'' you ask.")
        time.sleep(1)
        type_text("'Well, I'm afraid I wasn't present at the time,'' he explains.")
        time.sleep(1)
        type_text("'I was finishing up my duties in the kitchen when I heard a commotion from the study.'")
        time.sleep(1)
        type_text("'That's when I discovered Lord Hugo's body.'")
        time.sleep(1)
        type_text("You nod, considering his words carefully. 'And where were the other guests at this time?'")
        time.sleep(1)
        type_text("'I believe that Mr Turner, Mohamed and Mr Smith were in the drawing room,' Mr. Filigree replies.")
        time.sleep(1)
        type_text("'They had gathered after dinner. Lady Hawkshead and Mrs Turner had retired early, as is their habit.' ")
        if drawing_room_visit == True:
            type_text("Mr. Filigree, looking rather worn out, coughs politely. 'Pardon the interruption, but it really is getting awfully late")
            time.sleep(1)
            type_text("'I must insist on showing you to your quarters.'")
        else:
            type_text("Satisfied you've gathered what you can from the study, you decide it's time to meet the other guests.")
            time.sleep(1)
            type_text("You head to the drawing room to question the assembled suspects.")
            time.sleep(1)
            type_text("As you enter the drawing room, your eyes scan the faces of the assembled guests. They all turn to you, the air thick with tension.")

def meet_a_suspect():
    global suspects
    type_text("Who would you like to speak with?")
    time.sleep(1)
    if suspects[0][1] == True:
        type_text("1. Oswald and Lorie Turner")
    time.sleep(1)
    if suspects[1][1] == True:
        type_text("2. Lady Eleanor Hawkshead")
    time.sleep(1)
    if suspects[2][1] == True:
        type_text("3. Dr. Victor Ashford")
    time.sleep(1)
    if suspects[3][1] == True:
        type_text("4. Mohamed Al-Jafar")
    time.sleep(1)
    if suspects[4][1] == True:
        type_text("5. Peter Smith")
    time.sleep(1)
    type_text("6. You decide you've had quite enough time with these people.")

# Dialogue functions for the first time you meet each character

def turner_dialogue_one():
     global suspects 
     suspects[0][1] = False
     type_text("You approach an elegantly dressed couple sitting near the fireplace.")
     time.sleep(1)
     type_text("The man has a somewhat nervous, comedic air about him, while the woman exudes a sense of sophistication.")
     time.sleep(1)
     type_text("'Ah, you must be the famous detective everyone's been talking about!' the man says, offering you an awkward but charming smile. 'I'm Oswald Turner, and this is my wife, Lorie.'")
     time.sleep(1)
     type_text(f"Lorie nods politely. 'Pleased to make your acquaintance, {user_name}. Oswald and I are close friends of the Hawkshead family.'")
     time.sleep(1)
     type_text("You can't help but notice the way Lorie's gaze lingers on you, as if sizing you up. 'And what is your connection to Lord Hugo?' you ask.")
     time.sleep(1)
     type_text("Oswald fidgets uncomfortably. 'Well, you see, I'm an artist, and Lord Hugo was a patron of the arts. Lorie is a researcher, and she's been helping him with some historical projects.'")
     time.sleep(1)
     type_text("Lorie interjects, 'We were actually here discussing a new exhibition we were planning when...when the terrible incident occurred.'")
     time.sleep(1)
     type_text("You nod, making a mental note of their relationship to the victim. 'I see. Thank you for your time. I may have some more questions for you later.'")

def hawkshead_dialogue_one():
     suspects[1][1] = False
     type_text("Your eyes settle on a regal-looking woman sitting alone in the corner of the room.")
     time.sleep(1)
     type_text("As you approach, she offers you a charming smile.")
     time.sleep(1)
     type_text(f"'You must be the famous {user_name},' she says, her voice smooth and cultured. 'I'm Eleanor Hawkshead, a distant relative of Lord Hugo Hawkshead.'")
     time.sleep(1)
     type_text("You raise an eyebrow. 'A relative, you say? I wasn't aware he had any living relatives.'")
     time.sleep(1)
     type_text("Eleanor's smile widens ever so slightly. 'Yes, well, it's a rather complicated family tree. I'm afraid I wasn't as close to dear Hugo as I might have liked.'")
     time.sleep(1)
     type_text("She pauses, her gaze studying you intently. 'But perhaps we can discuss that more later. For now, is there anything I can assist you with, detective?'")
     time.sleep(1)
     type_text("You consider her words carefully, sensing an underlying edge to her refined demeanour. 'Perhaps you can tell me where you were at the time of the murder?'")
     time.sleep(1)
     type_text("'Of course.' Eleanor nods. 'I was here in the drawing room, along with the others, when the tragedy occurred.'")
     time.sleep(1)
     type_text("You make a mental note of her alibi before excusing yourself to speak with the next guest.")

def ashford_dialogue_one():
    suspects[2][1] = False
    type_text("A calm, professional-looking man sits in a wingback chair, his hands folded neatly in his lap. As you approach, he rises to greet you.")
    time.sleep(1)
    type_text(f"'{user_name}, I presume?' he says, his voice level and controlled. 'I'm Dr. Victor Ashford, Hawkshead's personal physician.'")
    time.sleep(1)
    type_text("You nod in acknowledgment. 'Dr. Ashford. I understand you were present at the manor this evening?'")
    time.sleep(1)
    type_text("'Yes, unfortunately.' He sighs heavily. 'I had been tending to one of the horses that had taken ill when I heard the commotion.'")
    time.sleep(1)
    type_text("'By the time I arrived, it was already too late.'")
    time.sleep(1)
    type_text("You study him closely, searching for any signs of deception. 'And did you notice anything unusual about Lord Hugo's condition or the circumstances surrounding his death?'")
    time.sleep(1)
    type_text("'Nothing that I can say with certainty,' Dr. Ashford replies, his expression unreadable.")
    time.sleep(1)
    type_text(f"'I'm afraid the details are still rather unclear to me. But I assure you, I will cooperate fully with your investigation, {user_name}.'")
    time.sleep(1)
    type_text("You nod, making a mental note to follow up with the doctor later.")

def al_jafar_dialogue_one():
    suspects[3][1] = False
    type_text("Your gaze falls upon a man sitting quietly in the corner, his eyes fixed on the flickering fire. As you approach, he looks up, his expression calm and composed.")
    time.sleep(1)
    type_text(f"'{user_name},' he says, his voice soft and measured. 'I'm Mohamed Al-Jafar, Lord Hugo Hawkshead's private tutor.'")
    time.sleep(1)
    type_text("You incline your head slightly. 'Mr. Al-Jafar. Can you tell me where you were at the time of the murder?'")
    time.sleep(1)
    type_text("'I was in my quarters, preparing for my evening lessons.' He pauses, his brow furrowing slightly. 'I heard the commotion, of course, but by the time I arrived, the deed had already been done.'")
    time.sleep(1)
    type_text("You consider his words, sensing an underlying intelligence and wit behind his calm bearing. 'And did you notice anything unusual about Lord Hugo or the other guests that evening?'")
    time.sleep(1)
    type_text(f"Mohamed shakes his head slowly. 'I'm afraid I don't have much to offer, {user_name}. I keep mostly to myself, you see. But I will do whatever I can to assist in your investigation. Hugo was a dear friend.'")
    time.sleep(1)
    type_text("You nod, making a mental note to follow up with him later.")

def smith_dialogue_one():
     suspects[4][1] = False
     type_text("Your gaze settles on a somewhat shy-looking man sitting by himself in the corner of the room. As you approach, he looks up, his eyes widening slightly.")
     time.sleep(1)
     type_text(f"'{user_name}', he stammers, rising to his feet. 'I'm Peter Smith, the, uh, the IT engineer for Hawkshead Manor.'")
     time.sleep(1)
     type_text("You offer him a reassuring smile. 'It's a pleasure to meet you, Mr. Smith. Can you tell me where you were at the time of the incident?'")
     time.sleep(1)
     type_text("Peter fidgets nervously, his eyes darting around the room. 'I-I was in the servants' quarters, working on the security system. I, uh, I didn't hear anything until the commotion started.'")
     time.sleep(1)
     type_text("You nod, taking note of his anxious nature. 'And did you notice anything unusual about the manor's security or any of the other guests this evening?'")
     time.sleep(1)
     type_text(f"'N-not that I can recall,' he stammers, his gaze fixed on the floor. 'I-I'm sorry I can't be of more help, {user_name}'")
     time.sleep(1)
     type_text("You offer him an understanding nod, making a mental note to follow up with him later.")

# This is the function which happens when you get to the drawing room
def drawing_room():
    global study_visit
    meet_a_suspect()

    user_choice_one = input("Please enter a number from one to six: ").strip().lower()

    if user_choice_one in ["1", "one"]:
            turner_dialogue_one()
            drawing_room()
    elif user_choice_one in ["2", "two"]:
            hawkshead_dialogue_one()
            drawing_room()
    elif user_choice_one in ["3", "three"]:
            ashford_dialogue_one()
            drawing_room()
    elif user_choice_one in ["4", "four"]:
            al_jafar_dialogue_one()
            drawing_room()
    elif user_choice_one in ["5", "five"]:
            smith_dialogue_one()
            drawing_room()
    elif user_choice_one in ["6", "six"]:
            type_text("As you finish speaking with the guests, you can't help but feel a growing sense of unease")
            time.sleep(1)
            type_text("Each of them seems to have a connection to the victim, and their stories, while seemingly innocuous, leave you with more questions than answers.")
            time.sleep(1)
            type_text("With a deep breath, you steel yourself for the investigation ahead, determined to uncover the truth behind Lord Hugo Hawkshead's untimely demise.")
            if study_visit == True:
                type_text("Just then, the drawing room door opens, and the butler, Mr. Filigree, enters. 'Pardon the interruption, but it really is getting awfully late. I must insist on showing you to your quarters.'")
            else:
                 type_text(f"Just then, the drawing room door opens, and Mr. Filigree, enters. 'Pardon the interruption, {user_name}, but I thought you might like to see the crime scene in Lord Hawkshead's study.'")
                 time.sleep(1)
                 type_text("You nod, your gaze sweeping the room one last time before following Mr. Filigree out of the drawing room and down the dimly lit corridor.")
                 study()
    else:
         type_text("Hmm, that wasn't an option.")

# DAY ONE MAIN FUNCTION

def day_one():
    type_text("The motorcar pulls up to the grand, foreboding entrance of Hawkshead Manor, its Gothic architecture looming overhead. As you step out into the pouring rain, the heavy oak doors swing open and the butler, Mr. Filigree, greets you.")
    time.sleep(1)
    type_text(f"'Welcome to Hawkshead Manor, {user_name},' he says solemnly. 'We've been expecting you.'")
    time.sleep(1)
    arrival_choice()
    main_hall_choice()

# DAY TWO MINI FUNCS

### DAY TWO  INTERVIEW FUNCTIONS

def lorie_turner_day_two():
    type_text("You find Lorie Turner in the library, methodically going through some papers.")
    time.sleep(1)
    type_text("She seems more composed than her husband.")
    time.sleep(1)
    type_text("'Mrs. Turner, might I have a word?'")
    time.sleep(1)
    type_text("She looks up, her sharp eyes meeting yours. 'Of course, detective. I suppose you'd like to know more about my research work with Lord Hugo?'")
    time.sleep(1)
    type_text("Do you:")
    time.sleep(1)
    type_text("1. Ask about her research with Lord Hugo?")
    time.sleep(1)
    type_text("OR")
    time.sleep(1)
    type_text("2. Ask about her relationship with Eleanor")
    
    user_choice = input("One (1) or Two (2): ").strip().lower()
    
    if user_choice in ["1", "one"]:
        type_text("'My specialty is Egyptian artifacts,' she explains.")
        time.sleep(1)
        type_text("'Lord Hugo had quite the collection. I was helping him authenticate several pieces, including...' she pauses, 'including the dagger that was used to kill him.'")
        time.sleep(1)
        type_text("You make a note in your jotter. 'Thank you, Mrs Turner. That will be all for now.'")
        day_two_interviews()
    elif user_choice in ["2", "two"]:
        type_text("'Eleanor? Oh yes, she's been very... interested in my work here.'")
        time.sleep(1)
        type_text("'Particularly regarding Lord Hugo's collection. She seemed quite concerned about its future.'")
        time.sleep(1)
        type_text("You make a note in your jotter. 'Thank you, Mrs Turner. That will be all for now.'")
        day_two_interviews()
    else:
        type_text("That wasn't a valid option.")
        lorie_turner_day_two()

def victor_ashford_day_two():
    type_text("You find Victor Ashford in the library, reading the morning papers. He has a refined air of authority about him.")
    time.sleep(1)
    type_text("'Please, call me Victor,' he requests, as you ask him for a few minutes of his time.")
    time.sleep(1)
    type_text("'Of course I would be happy to assist you in your investigations.'")
    time.sleep(1)
    type_text("'I should mention,' he says carefully, 'that Lord Hugo had been making changes to his will.'")
    time.sleep(1)
    type_text("'He confided in me about his plans to leave the estate to Mr. Al-Jafar.'") 
    time.sleep(1)
    type_text("'It was to be announced at dinner tonight.'")
    time.sleep(1)
    type_text("You thank Victor for his time and leave him to his paper.")
    day_two_interviews()

def eleanor_day_two():
    type_text("You begin by asking Eleanor about her relationship with Lord Hugo.")
    time.sleep(1)
    type_text("She admits that she was never particularly close with him, but states that without a son, she had recently moved back in order to keep a close eye on him - and the house.")
    time.sleep(1)
    type_text("You try and slip a question in casually about what happens to the manor now Lord Hugo has passed away.")
    time.sleep(1)
    type_text("'The estate should remain in the family,' she says firmly.")
    time.sleep(1)
    type_text("'These outsiders, coming in with their research and their teaching... they don't understand the legacy of Hawkshead Manor.'")
    time.sleep(1)
    type_text(f"You ask her who she means, but she cuts you off. 'I'm a busy woman, {user_name}. I can't stand here nattering all day.")
    time.sleep(1)
    type_text("Lady Hawkshead pushes past you, and returns to the drawing room.")
    time.sleep(1)
    type_text("You sigh to yourself, and follow her into the adjoining room.")
    day_two_additional_interviews()

def oswald_turner_day_two():
    type_text("Your first impressions of Oswald have been distinctly negative.")
    time.sleep(1)
    type_text("Though he maintains a jovial external facade, this quickly comes crashing down as you ask him to join you next door.")
    time.sleep(1)
    type_text("He starts twitching nervously and glances at the door to the main lobby before joining you in the smaller anteroom.")
    time.sleep(1)
    type_text("'Mr Turner-' you begin, but he cuts you off")
    time.sleep(1)
    type_text("'I-I just do whatever Lorie thinks is best,' he stammers. 'She's the expert, after all. Though lately, she's been meeting with Eleanor quite frequently...'")
    time.sleep(1)
    type_text("You aren't getting much more out of this man. You thank him and tell him you have no questions after all.")
    day_two_additional_interviews()

def peter_smith_day_two():
    type_text("Out of everyone you've spoken to so far, Peter Smith gives away the least information through body language and social cues.")
    time.sleep(1)
    type_text("You decide a more direct approach might work best here.")
    time.sleep(1)
    type_text("'Mr. Smith, I'll cut to the chase. You have access to the manor's security system. Did you see or hear anything suspicious on the night of Lord Hawkshead's murder?'")
    time.sleep(1)
    type_text("'The security system was tampered with that night,' he reveals. 'Someone who knew the layout well. Someone who had been studying it...'")
    time.sleep(1)
    type_text("Unfortunately, I can't say who. I was up playing backgammon with Mohamed until late that evening.")
    time.sleep(1)
    type_text("You thank Mr. Smith and allow him to return to the drawing room, before following him through the door.")
    day_two_additional_interviews()
    
def day_two_interviews():
    type_text("Who would you like to speak with?")
    time.sleep(1)
    type_text("1. Lorie Turner")
    time.sleep(1)
    type_text("OR")
    time.sleep(1)
    type_text("2. Dr Victor Ashford")
    time.sleep(1)
    type_text("OR")
    time.sleep(1)
    type_text("3. Something else..")
    
    user_choice = input("Choose an option (1, 2, or 3): ").strip().lower()
    
    if user_choice in ["1", "one"]:
        lorie_turner_day_two()
    elif user_choice in ["2", "two"]:
        victor_ashford_day_two()
    elif user_choice in ["3", "three"]:
        type_text("There must be something else you can do...")
        day_two_actions()
    else:
        type_text("That wasn't an option.")
        day_two_interviews()

def day_two_additional_interviews():
    type_text("Who would you like to talk with next?")
    time.sleep(1)
    type_text("1. Eleanor")
    time.sleep(1)
    type_text("2. Oswald Turner")
    time.sleep(1)
    type_text("3. Peter Smith")
    time.sleep(1)
    type_text("4. You've talked to enough people. You're happy to move on.")
    
    user_choice = input("Choose an option (1, 2, 3, or 4): ").strip().lower()
    
    if user_choice in ["1", "one"]:
        eleanor_day_two()
    elif user_choice in ["2", "two"]:
        oswald_turner_day_two()
    elif user_choice in ["3", "three"]:
        peter_smith_day_two()
    elif user_choice in ["4", "four"]:
        type_text("You wouldn't exactly call it a satisfying day of work, but you've definitely learnt a lot about the dubious ensemble at Hawkshead Manor.")
    else:
        type_text("That wasn't an option. Try again.")
        day_two_additional_interviews()

# DAY TWO ACTION  FUNCTIONS

def study_search_day_two():
    global inventory
    type_text("Do you")
    time.sleep(1)
    type_text("1. Take the evidence immediately to Mr Al-Jafar?")
    time.sleep(1)
    type_text("OR")
    time.sleep(1)
    type_text("2. Continue searching the study")
    
    user_choice = input("One (1) or Two (2): ").strip().lower()
    
    if user_choice in ["1", "one"]:
        type_text("You find Mohamed Al-Jafar in his private quarters, next door to Hugo's study.")
        time.sleep(1)
        type_text("'Lord Hugo did speak of making me his heir,' he admits quietly.")
        time.sleep(1)
        type_text("'He said I reminded him of his son who passed away years ago.'")
        time.sleep(1)
        type_text("'But I never wanted his money - we shared an intimate friendship and I greatly enjoyed my time here.'")
        time.sleep(1)
        type_text("He seems trustworthy, and you thank him for his time.")
        time.sleep(1)
        type_text("That's enough time in the study. You need to talk to more people about this bizarre crime.")
        day_two_actions()
    elif user_choice in ["2", "two"]:
        type_text("Behind a loose panel, you find a notebook filled with Lorie's handwriting - detailed notes about each Egyptian artefact's value and authenticity.")
        type_text("You stow this notebook in your pocket, and return to the downstairs lobby.")
        inventory.append("Lorie's Notebook")
        day_two_actions()
    else:
        type_text("That wasn't an option.")
        study_search_day_two()

def day_two_actions():
    global inventory
    type_text("Do you:")
    time.sleep(1)
    type_text("1. Start conducting interviews immediately")
    time.sleep(1)
    type_text("OR")
    time.sleep(1)
    type_text("2. Search Lord Hugo's private study again in the daylight")
    time.sleep(1)
    type_text("OR")
    time.sleep(1)
    type_text("3. Head to the drawing room.")
    
    user_choice = input("One (1), Two (2) or Three (3): ").strip().lower()
    
    if user_choice in ["1", "one"]:
        day_two_interviews()
    elif user_choice in ["2", "two"]:
        type_text("In the morning light, you notice something you missed before - a partially burned letter in the fireplace.")
        time.sleep(1)
        type_text("It appears to be a draft of a new will, with Mohamed Al-Jafar's name visible.")
        inventory.append("Hugo's Will")
        time.sleep(1)
        study_search_day_two()
    elif user_choice in ["3", "three"]:
        type_text("Eleanor Hawkshead, Oswald Turner and Peter Smith are gathered in the drawing room.")
        time.sleep(1)
    else:
        type_text("Hmm. That wasn't an option. Try again.")
        day_two_actions()

# DAY TWO MAIN FUNC

def day_two():
    type_text("You stay up late thinking over your first impressions of the people you met over the course of the evening.")
    time.sleep(1)
    type_text("There must be more going on here than meets the eye.")
    time.sleep(1)
    type_text("No one seems particularly upset about Lord Hugo's death, with the possible exception of Mohamed Al-Jafar.")
    time.sleep(1)
    type_text("Eventually tiredness takes over, and you take your place in the plush, four-poster bed.")
    time.sleep(1)
    type_text("...")
    time.sleep(1)
    type_text("...")
    time.sleep(1)
    type_text("...")
    time.sleep(1)
    type_text("...")
    time.sleep(1)
    type_text("...")
    type_text("You wake to another gloomy morning at Hawkshead Manor.")
    time.sleep(1)
    type_text("The rain continues to drum against your window as you consider your first move of the day.")
    time.sleep(1)
    day_two_actions()
    type_text("They seem somewhat aggrieved by your continued presence, but agree that you can talk to each of them in private if you would like to.")
    day_two_additional_interviews()
    type_text("As you sit at the absurd stone hewn desk in your bedroom that evening, you mull over the day's discoveries.")
    time.sleep(1)
    type_text("There’s nothing more to do tonight other than to sleep on things. ")
    time.sleep(1)
    type_text("The next day you can advance your investigations.")

# DAY THREE MINI FUNCS

def pick_a_location():
    type_text("Do you: ")
    time.sleep(1)
    type_text("1. Search the kitchens.")
    time.sleep(1)
    type_text("2. Search the gardens.")
    time.sleep(1)
    type_text("3. Head to the dining room")
    time.sleep(1)
    type_text("4. That's enough for today.")

    user_choice = input("One (1), Two (2), Three (3) or Four (4): ").strip().lower()
    
    if user_choice in ["1", "one"]:
        type_text("You head to the kitchens.")
        time.sleep(1)
        type_text("The cook and a maid are clearly too busy to pay you much time, and anyway, neither were here on the eve of Lord Hugo's murder.")
        time.sleep(1)
        type_text("You decide to leave them to their work.")
        kitchens()
    elif user_choice in ["2", "two"]:
        type_text("You head to the gardens.")
        time.sleep(1)
        type_text("The extensive grounds are marked by pristine lawns and towering oak trees. ")
        time.sleep(1)
        type_text("Maintaining all of this must be a full-time job.")
        gardens()
    elif user_choice in ["3", "three"]:
        type_text("As you arrive in the dining room, Mr Filigree informs you that lunch is ready and you'd be very welcome to join the guests as they dine..")
        time.sleep()
        type_text("The meal is more basic than you imagined would be served at a place like Hawkshead Manor.")
        time.sleep()
        type_text("A cream of tomato soup alongside homemade bread.")
        time.sleep()
        type_text("You don't mind too much; you're hungry and a rich meal might upset your stomach anyhow.")
        time.sleep()
        type_text("You take a place at the table and are pleased to note that all the house's guests are present.")
        dining_room()

    elif user_choice in ["4", "four"]:
        type_text("That's enough investigating for today. Tomorrow you will make your final decisions.")
        
    else: 
        type_text("That's not a valid option. Try again.")
        pick_a_location()

def kitchens():
    global inventory
    type_text("Would you like to: ")
    time.sleep(1)
    type_text("1. Have something to eat.")
    time.sleep(1)
    type_text("OR")
    time.sleep(1)
    type_text("2. Search for evidence.")

    user_choice = input("One (1) or Two (2): ").strip().lower()

    if user_choice in ["1", "one"]:
        type_text("You make and eat a ham, egg, spam, jam, egg, spam, jam and spam sandwich.")
        time.sleep(1)
        type_text("Satisfied, you forget why you came into the kitchen, and return to the main hall.")
        pick_a_location()
    elif user_choice in ["2", "two"]:
        type_text("You discover a crumpled note in the kitchen waste bin - a message in Eleanor's handwriting.")
        time.sleep(1)
        type_text("It reads: 'The collection must be protected at all costs. He cannot give it away.'")
        time.sleep(1)
        type_text("You file this away for later and head back to the main hall.")
        inventory.append("Eleanor's Note")
        pick_a_location()
    else:
        type_text("That's not a valid option. Try again.")
        kitchens()

def gardens():
    global inventory
    type_text("Would you like to:")
    time.sleep(1)
    type_text("1. Search for evidence")
    time.sleep(1)
    type_text("OR")
    time.sleep(1)
    type_text("2. Look for the groundskeeper")

    user_choice = input("One (1) or Two (2): ").strip().lower()

    if user_choice in ["1", "one"]:
        type_text("Near the rose bushes, you find a hand-drawn map of the study's layout, with expert notes  about the location of each artefact and its potential value.")
        time.sleep(1)
        type_text("You stuff the note into your pocket.")
        inventory.append("Study Map")
        gardens()
    elif user_choice in ["2", "two"]:
        type_text("You find the groundskeeper, a Mary Pollard.")
        time.sleep(1)
        type_text("She claims to have been away with family for the last week, and she shares that though she was shocked to hear about Lord Hawkshead's death, she wonders whether his heir will take a greater interest in the manor's grounds and gardens.")
        time.sleep(1)
        type_text("Just then a distant bell sounds, informing you that dinner is ready.")
        time.sleep(1)
        type_text("You'd better head inside.")
        time.sleep(1)
        type_text("You take a place at the table and are pleased to note that all the house's guests are present.")
        time.sleep(1)
        type_text("The meal is more basic than you imagined would be served at a place like Hawkshead Manor.")
        time.sleep(1)
        type_text("A cream of tomato soup alongside homemade bread.")
        time.sleep(1)
        type_text("You don't mind too much; you're hungry and a rich meal might upset your stomach anyhow.")
        dining_room()
    else: 
        type_text("That's not a valid choice. Try again.")
        gardens()

def dining_room():
    type_text("Do you: ")
    time.sleep(1)
    type_text("1. Listen in on conversation")
    time.sleep(1)
    type_text("2. Watch the diners carefully")
    time.sleep(1)
    type_text("3. Finish your meal and leave the table. There's nothing for you here.")
    user_choice = input("One (1), Two (2) or Three (3): ").strip().lower()
    if user_choice in ["1", "one"]:
        type_text("You overhear Eleanor whispering to Lorie: 'Remember our agreement. The collection stays in the family, and you'll be its curator'")
        dining_room()
    elif user_choice in ["2", "two"]:
        type_text("The diners maintain a remarkable facade of calm and composure throughout the meal.")
        time.sleep(1)
        type_text("The only thing you notice is that Mohamed Al-Jafar does not contribute to the conversation any more than the slightest pieces of small talk, and he is the first to leave the table.")
        dining_room()
    elif user_choice in ["3", "three"]:
        type_text("You finish your soup and drain your glass.")
        time.sleep(1)
        type_text("As you leave the table, you can't help but notice that Eleanor Hawkshead has been watching you throughout the meal.")
    else:
        type_text("That wasn't a valid option. Try again.")
        dining_room()

#DAY THREE MAIN FUNC

def day_three():
    type_text("...")
    time.sleep(1)
    type_text("...")
    time.sleep(1)
    type_text("...")
    time.sleep(1)
    type_text("...")
    time.sleep(1)
    type_text("You wake up surprisingly well rested, but you're very aware you've been investigating for two days now and you still don't have a firm idea of who may have murdered Lord Hugo.")
    time.sleep(1)
    type_text("You decide to search key areas of the manor. Each location can provide a vital clue.")
    time.sleep(1)
    pick_a_location()
    type_text("You spend the evening alone in your bedroom.")
    time.sleep(1)
    type_text("You are more and more certain that you know who is at the bottom of this.")
    time.sleep(1)
    type_text("Before you head to bed, you call Mr. Filigree and ask him to ensure there is a police presence at the manor in the morning.")
    time.sleep(1)
    type_text("After breakfast, you will be revealing your suspicions.")

# DAY FOUR MINI FUNC

def final_interviews():
    type_text("You may only interview one guest! Choose carefully.")
    time.sleep(1)
    type_text("1. Lorie Turner")
    time.sleep(1)
    type_text("2. Oswald Turner")
    time.sleep(1)
    type_text("3. Peter Smith")
    time.sleep(1)
    type_text("4. Mohamed Al-Jafar")
    time.sleep(1)
    type_text("5. Dr. Victor Ashford")
    time.sleep(1)
    type_text("6. Eleanor Hawkshead")
    time.sleep(1)
    type_text("7. You know the answer. You don't need to talk to anyone again")
    
    user_choice = input("Please enter a number from 1-7: ").strip().lower()
    
    if user_choice in ["1", "one"]:
        type_text("'Before you make any... hasty decisions,' Lorie says, her usual composure slipping slightly, 'I want to emphasise the importance of Lord Hugo's collection.'")
        time.sleep(1)
        type_text("'Everything I did here - my research, my cataloguing - it was all to preserve these priceless artefacts. To protect them.'")
        time.sleep(1)
        type_text("Her eyes dart briefly to Eleanor. 'Some people understand the true value of preservation.'")
        time.sleep(1)
        type_text("'Others... well, they would have seen it all scattered to the winds.'")
    elif user_choice in ["2", "two"]:
        type_text("'I... I should say something,' Oswald stammers, standing abruptly from his chair beside Lorie.")
        time.sleep(1)
        type_text("'My wife has always been dedicated to her work. Perhaps... perhaps too dedicated sometimes.'")
        time.sleep(1)
        type_text("'But she would never...' He trails off, unable to finish the thought.")
        time.sleep(1)
        type_text("'I just want you to know that whatever you think happened, there must be an explanation.'")
        time.sleep(1)
        type_text("His wife gives him a filthy look as he retakes his seat.")
    elif user_choice in ["3", "three"]:
        type_text("'The s-security logs,' Peter interjects nervously, clutching his laptop.")
        time.sleep(1)
        type_text("'I've been analysing them further.'")
        time.sleep(1)
        type_text("'The killer knew exactly where the cameras were, how to avoid them.'")
        time.sleep(1)
        type_text("'But there's something else - someone accessed the security room at 9:47 PM, just before...'")
        time.sleep(1)
        type_text("He swallows hard. 'Just before everything happened.'")
        time.sleep(1)
        type_text("Mohamed Al-Jafar places a comforting hand on Peter's shoulder.")
        time.sleep(1)
    elif user_choice in ["4", "four"]:
        type_text("'Since you invite me to speak freely,'' Mohamed says quietly from his corner, 'I should confirm what Dr. Ashford has likely told you.'")
        time.sleep(1)
        type_text("'Lord Hugo did intend to make me his heir.'")
        time.sleep(1)
        type_text("'But more importantly, he planned to open the collection to the public, to share its historical significance with the world.'")
        time.sleep(1)
        type_text("'Some...' his eyes sweep the room, 'were not pleased with this decision.'")
        time.sleep(1)
        type_text("He lapses back into silence")
    elif user_choice in ["5", "five"]:
        type_text("'As his physician,' Dr. Ashford says carefully, 'I feel I should mention that Lord Hugo was of completely sound mind when he made his recent decisions.'")
        time.sleep(1)
        type_text("'He knew exactly what he was doing with his will, with the collection, with everything.'")
        time.sleep(1)
        type_text("And he knew...' he pauses significantly, 'he knew who might oppose those decisions.'")
        time.sleep(1)
        type_text("A crash of thunder punctuates the doctor's words.")
    elif user_choice in ["6", "six"]:
        type_text("'Oh, let's dispense with all this dramatic tension,' Eleanor cuts in, her voice sharp.")
        time.sleep(1)
        type_text("'Yes, I opposed Hugo's plan to give away our family's heritage. These artefacts belong to the Hawkshead name.'")
        time.sleep(1)
        type_text("'They should be preserved, protected, kept in proper hands.' Her gaze fixes meaningfully on Lorie.")
        time.sleep(1)
        type_text("'Some of us understand the importance of legacy.'")
    elif user_choice in ["Seven", "7"]:
        type_text("You don't need to talk to any of this lot. You're best off moving on.")
    else:
        type_text("That's not an option. Try again.")
        final_interviews()

def accusation():
    global suspect
    type_text("Pick a suspect - you are accusing them of murder!")
    time.sleep(1)
    type_text("1. Lorie Turner")
    time.sleep(1)
    type_text("2. Oswald Turner")
    time.sleep(1)
    type_text("3. Peter Smith")
    time.sleep(1)
    type_text("4. Mohamed Al-Jafar")
    time.sleep(1)
    type_text("5. Dr. Victor Ashford")
    time.sleep(1)
    type_text("6. Eleanor Hawkshead")
    time.sleep(1)
    user_choice = input("Please enter a number from 1-6").strip().lower()
    if user_choice in ["One", "1"]:
        suspect = "Lorie"
        type_text("'Mrs. Turner,' you state firmly, 'you killed Lord Hugo with the Egyptian dagger - a piece you knew intimately through your research.'")
        time.sleep(1)
        type_text("Lorie's sophisticated facade crumbles.")
        time.sleep(1)
        type_text("'Eleanor said it was the only way! The collection would have been lost, given to someone who couldn't possibly understand its value!'")
        time.sleep(1)
        type_text("Across the table, Eleanor's composure cracks slightly. 'You can't prove anything.'")
        time.sleep(1)
        if len(inventory) > 2:
            type_text("'Actually, I can.'")
            time.sleep(1)
            type_text("'The burned will draft, the notes about the collection, and most importantly, your agreement with Mrs. Turner to make her curator if she helped you 'protect' the collection.'")
            time.sleep(1)
            type_text("Eleanor rises to flee but finds the doors blocked by the police.")
            good_ending()
        else:
            type_text("Your voice falters.")
            time.sleep()
            type_text("You don't have much beyond a hunch. Nothing the police would consider definitive anyway.")
            time.sleep()
            failed_ending()
    elif user_choice in ["Two", "2"]:
        suspect = "Oswald"
        type_text("You accuse Oswald of having murdered Lord Hugo, though your reasoning is hard to follow and the guests eye you with some confusion. As you leave the room with the police and Oswald in handcuffs, you can't help but notice a smirk on Eleanor's face.")
        bad_ending()
    elif user_choice in ["Three", "3"]:
        suspect = "Peter"
        type_text("You accuse Peter of having murdered Lord Hugo, though your reasoning is hard to follow and the guests eye you with some confusion. As you leave the room with the police and Peter in handcuffs, you can't help but notice a smirk on Eleanor's face.")
        bad_ending()
    elif user_choice in ["Four", "4"]:
        suspect = "Mohamed"
        type_text("You accuse Mohamed of having murdered Lord Hugo, though your reasoning is hard to follow and the guests eye you with some confusion. As you leave the room with the police and Mohamed in handcuffs, you can't help but notice a smirk on Eleanor's face.")
        bad_ending()
    elif user_choice in ["Five", "5"]:
        suspect = "Victor"
        type_text("You accuse Victor of having murdered Lord Hugo, though your reasoning is hard to follow and the guests eye you with some confusion. As you leave the room with the police and Victor in handcuffs, you can't help but notice a smirk on Eleanor's face.")
        bad_ending()
    elif user_choice in ["Six", "6"]:
        suspect = "Eleanor"
        type_text("'Lady Eleanor,' you announce, 'you manipulated Mrs. Turner into committing murder to prevent Lord Hugo from giving his estate to Mr. Al-Jafar.'")
        time.sleep(1)
        type_text("Eleanor's composure cracks slightly. 'You can't prove anything.'")
        time.sleep(1)
        if len(inventory) > 2:
            type_text("'Actually, I can.'")
            time.sleep(1)
            type_text("'The burned will draft, the notes about the collection, and most importantly, your agreement with Mrs. Turner to make her curator if she helped you 'protect' the collection.'")
            time.sleep(1)
            type_text("Eleanor rises to flee but finds the doors blocked by the police.")
            good_ending()
        else:
            type_text("Your voice falters.")
            time.sleep(1)
            type_text("You don't have much beyond a hunch. Nothing the police would consider definitive anyway.")
            time.sleep(1)
            failed_ending()

def failed_ending():
    type_text("You know it was Eleanor and Lorie, but ultimately you didn't collect enough evidence during your time in Hawkshead Manor.")
    time.sleep(1)
    type_text("You can't go around accusing people based on a hunch!")
    time.sleep(1)
    type_text("After a few weeks, Eleanor is released from custody and your reputation takes a significant hit when Mohamed publishes an article about you.")
    time.sleep(1)
    type_text("You came so close!")
    time.sleep(1)
    type_text("GAME OVER")
    
def bad_ending():
    type_text("Uh oh...!")
    time.sleep(1)
    type_text(f"{suspect} spends several weeks in police custody at your direction, but ultimately the court finds no evidence that solidly links them to the crime.")
    time.sleep(1)
    type_text("Meanwhile, Hawkshead Manor passes into the hands of Lady Eleanor Hawkshead.")
    time.sleep(1)
    type_text("She appoints Lorie Turner as curator of the house's private collection.")
    time.sleep(1)
    type_text("This is very bad, for spurious reasons.")
    time.sleep(1)
    type_text("GAME OVER")

def good_ending():
    type_text("Well done!")
    time.sleep(1)
    type_text("The truth emerges: Eleanor Hawkshead, desperate to keep the estate in the family, manipulated Lorie Turner's academic passion into something darker. ")
    time.sleep(1)
    type_text("She convinced Lorie that Mohamed Al-Jafar would destroy the priceless collection's value, playing on her obsession with preserving the artefacts.")
    time.sleep(1)
    type_text("Lorie confesses to the murder, revealing how Eleanor had promised her unrestricted access to the collection as its curator.")
    time.sleep(1)
    type_text("Oswald, weak-willed and devoted to his wife, had suspected something but remained silent.")
    time.sleep(1)
    type_text("Both women are arrested - Lorie for the murder, Eleanor as an accessory.")
    time.sleep(1)
    type_text("Mohamed Al-Jafar, the intended heir, decides to turn Hawkshead Manor into a public museum, ensuring the collection will be preserved and shared with the world.")
    time.sleep(1)
    type_text("THE END")
    time.sleep(1)

# DAY FOUR MAIN 

def day_four():
    type_text("...")
    time.sleep(1)
    type_text("...")
    time.sleep(1)
    type_text("...")
    time.sleep(1)
    type_text("...")
    time.sleep(1)
    type_text("You wake up early and head to the kitchens for some early sustenance.")
    time.sleep(1)
    type_text("Investigating certainly puts a fire in your belly!")
    time.sleep(1)
    type_text("One by one, the other guests wake up, and you gather everyone in the drawing room.")
    time.sleep(1)
    type_text("The time has come to reveal the truth.")
    time.sleep(1)
    type_text("Tension is thick in the air.")
    time.sleep(1)
    type_text("Before you reveal anything, there is one final chance to ask guests questions.")
    time.sleep(1)
    type_text("The storm outside has grown fiercer, rain lashing against the windows of the drawing room.")
    time.sleep(1)
    type_text("All the suspects are gathered, the tension palpable. ")
    time.sleep(1)
    type_text("You know one of them is a killer, and soon you'll make your accusation.")
    time.sleep(1)
    type_text("But first, you'll give one person a final chance to speak.")
    final_interviews()
    type_text("The time has come for you to make your accusation.")
    time.sleep(1)
    type_text("Looking around the room, you see guilty knowledge, fear, and desperation in various faces.")
    time.sleep(1)
    type_text("But only one person actually plunged that Egyptian dagger into Lord Hugo's back.")
    time.sleep(1)
    type_text("Who is guilty and who is innocent?")
    time.sleep(1)
    type_text("...")
    time.sleep(1)
    type_text("...")
    time.sleep(1)
    type_text("...")
    time.sleep(1)
    type_text("...")
    time.sleep(1)
    type_text("It's time to decide.")
    accusation()
    exit()

# CALLING FUNCTIONS TO PLAY GAME
tutorial.day_zero()
start_game()
day_one()
day_two()
day_three()
day_four()
# end_game() - not currently being used
 
# End of the game (this is where you would call end_game to show the score)
# Python Project | MYSTERY AT HAWKSHEAD MANOR
# --------------
# Credits:
# Michael Leversha
# Omid Karimi
# Munir Saeed
# Tyler Hogan