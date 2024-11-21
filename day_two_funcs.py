import time
import config

type_text = config.type_text
user_name = config.user_name
inventory = config.inventory
game_score = config.game_score

### DAY TWO  INTERVIEW FUNCTIONS

def lorie_turner_day_two():
    global game_score
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
        game_score -= 5
        day_two_interviews()
    elif user_choice in ["2", "two"]:
        type_text("'Eleanor? Oh yes, she's been very... interested in my work here.'")
        time.sleep(1)
        type_text("'Particularly regarding Lord Hugo's collection. She seemed quite concerned about its future.'")
        time.sleep(1)
        type_text("You make a note in your jotter. 'Thank you, Mrs Turner. That will be all for now.'")
        game_score -= 5
        day_two_interviews()
    else:
        type_text("That wasn't a valid option. Try again.")
        lorie_turner_day_two()

def victor_ashford_day_two():
    global game_score
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
    game_score -= 5
    day_two_interviews()

def eleanor_day_two():
    global game_score
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
    game_score -= 5
    day_two_additional_interviews()

def oswald_turner_day_two():
    global game_score
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
    game_score -= 5
    day_two_additional_interviews()

def peter_smith_day_two():
    global game_score
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
    game_score -= 5
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
        type_text("You find Lorie Turner in the library, methodically going through some papers.")
        time.sleep(1)
        type_text("She seems more composed than her husband.")
        time.sleep(1)
        type_text("'Mrs. Turner, might I have a word?'")
        time.sleep(1)
        type_text("She looks up, her sharp eyes meeting yours. 'Of course, detective. I suppose you'd like to know more about my research work with Lord Hugo?'")
        lorie_turner_day_two()
    elif user_choice in ["2", "two"]:
        victor_ashford_day_two()
    elif user_choice in ["3", "three"]:
        type_text("There must be something else you can do...")
        day_two_actions()
    else:
        type_text("That wasn't an option. Try again.")
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
        game_score += 10
        day_two_actions()
    else:
        type_text("That wasn't an option.")
        study_search_day_two()

def day_two_actions():
    global inventory
    global game_score
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
        game_score += 10
        time.sleep(1)
        study_search_day_two()
    elif user_choice in ["3", "three"]:
        type_text("Eleanor Hawkshead, Oswald Turner and Peter Smith are gathered in the drawing room.")
        time.sleep(1)
    else:
        type_text("Hmm. That wasn't an option. Try again.")
        day_two_actions()
