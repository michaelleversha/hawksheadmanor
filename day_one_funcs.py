import time
import config

type_text = config.type_text
user_name = config.user_name
study_visit = config.study_visit
drawing_room_visit = config.drawing_room_visit
suspects = config.suspects
game_score = config.game_score

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
            type_text("hmm we shouldn't be here and the game probably goes wrong...")
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
     global game_score
     game_score -= 5
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
     global game_score
     game_score -= 5
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
    global game_score
    game_score -= 5
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
    global game_score
    game_score -= 5
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
     global game_score
     game_score -= 5
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
