import time
import config
import day_three_funcs

type_text = config.type_text

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
    day_three_funcs.pick_a_location()
    type_text("You spend the evening alone in your bedroom.")
    time.sleep(1)
    type_text("You are more and more certain that you know who is at the bottom of this.")
    time.sleep(1)
    type_text("Before you head to bed, you call Mr. Filigree and ask him to ensure there is a police presence at the manor in the morning.")
    time.sleep(1)
    type_text("After breakfast, you will be revealing your suspicions.")
