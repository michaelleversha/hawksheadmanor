import time
import config

type_text = config.type_text
user_name = config.user_name
inventory = config.inventory
game_score = config.game_score

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
    global game_score
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
        if "Eleanor's Note" in inventory:
            type_text("You've searched the kitchen from top to bottom. All that's here now are hints about what might be for lunch...")
            pick_a_location()
        else:
            type_text("You discover a crumpled note in the kitchen waste bin - a message in Eleanor's handwriting.")
            time.sleep(1)
            type_text("It reads: 'The collection must be protected at all costs. He cannot give it away.'")
            time.sleep(1)
            type_text("You file this away for later and head back to the main hall.")
            inventory.append("Eleanor's Note")
            game_score += 10
            pick_a_location()
    else:
        type_text("That's not a valid option. Try again.")
        kitchens()

def gardens():
    global inventory
    global game_score
    type_text("Would you like to:")
    time.sleep(1)
    type_text("1. Search for evidence")
    time.sleep(1)
    type_text("OR")
    time.sleep(1)
    type_text("2. Look for the groundskeeper")

    user_choice = input("One (1) or Two (2): ").strip().lower()

    if user_choice in ["1", "one"]:
        if "Study Map" in inventory:
            type_text("You've searched the grounds thoroughly. You can't find anything else.")
            gardens()
        else:
            type_text("Near the rose bushes, you find a hand-drawn map of the study's layout, with expert notes  about the location of each artefact and its potential value.")
            time.sleep(1)
            type_text("You stuff the note into your pocket.")
            inventory.append("Study Map")
            game_score += 10
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
