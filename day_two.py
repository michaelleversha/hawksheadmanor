import time
import config
import day_two_funcs

type_text = config.type_text

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
    day_two_funcs.day_two_actions()
    type_text("They seem somewhat aggrieved by your continued presence, but agree that you can talk to each of them in private if you would like to.")
    day_two_funcs.day_two_additional_interviews()
    type_text("As you sit at the absurd stone hewn desk in your bedroom that evening, you mull over the day's discoveries.")
    time.sleep(1)
    type_text("There’s nothing more to do tonight other than to sleep on things. ")
    time.sleep(1)
    type_text("The next day you can advance your investigations.")
