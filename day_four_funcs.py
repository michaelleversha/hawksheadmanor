import time
import config

type_text = config.type_text
user_name = config.user_name
inventory = config.inventory
suspect = config.suspect

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
