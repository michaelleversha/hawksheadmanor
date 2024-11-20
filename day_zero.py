import time
import config
import day_zero_funcs

user_name = config.user_name

type_text = config.type_text

def day_zero():
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
    day_zero_funcs.bed_choice()
    day_zero_funcs.car_choice()