import time
import config
import day_one_funcs

type_text = config.type_text
user_name = config.user_name

def day_one():
    type_text("The motorcar pulls up to the grand, foreboding entrance of Hawkshead Manor, its Gothic architecture looming overhead. As you step out into the pouring rain, the heavy oak doors swing open and the butler, Mr. Filigree, greets you.")
    time.sleep(1)
    type_text(f"'Welcome to Hawkshead Manor, {user_name},' he says solemnly. 'We've been expecting you.'")
    time.sleep(1)
    day_one_funcs.arrival_choice()
    day_one_funcs.main_hall_choice()


