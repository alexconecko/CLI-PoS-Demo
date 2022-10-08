import sys

item_names = []
item_servings = []
item_prices = []

def get_str(prompt):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    value = sys.stdin.readline().strip()
    while len(value) == 0:
        sys.stdout.write("Input cannot be blank. Re-enter: ")
        sys.stdout.flush()
        value = sys.stdin.readline().strip()
    
    return value

def get_int(prompt):
    value = None
    while value == None:
        try:
            value = int(get_str(prompt))
        except:
            prompt = "That wasn't right. Re-enter: "
    return value

def get_float(prompt):
    value = None
    while value == None:
        try:
            value = float(get_str(prompt))
        except:
            prompt = "That wasn't right. Re-enter: "
    return value

def get_positive_float(prompt):
    value = get_float(prompt)
    while value < 0:
        value = get_float("Input must be positive. Re-enter: ")
    return value

def get_menu_choice():
    menu = "\n=====================\n"
    menu += "BurgerJoint POS system\n"
    menu += "======================\n"
    menu += "[A]dd an item\n"
    menu += "[D]isplay saved data\n"
    menu += "E[x]it\n"
    
    sys.stdout.write(menu)
    
    menu = menu.lower()
    choice = get_str("Enter choice: ").lower()
    while not "[" + choice + "]" in menu:
        choice = get_str(choice + " was an invalid choice! Re-enter: ").lower()
    
    return choice

def load_data():
    try:
        file_object = open("test_case_02.txt", "r")
        for line in file_object:
            fields = line.split(",")
            item_name = fields[0].strip()
            item_serving = fields[1].strip()
            item_price = fields[2].strip()
            add_item(item_name, item_serving, item_price)
    except OSError:
        sys.stdout.write("Error loading data file.\n")
    except IndexError:
        sys.stdout.write("Data file could not be read properly. Check csv structure.\n")

def add_item(item_name, item_serving, item_price):
    item_names.append(item_name)
    item_servings.append(item_serving)
    item_prices.append(item_price)

def add_item_via_menu():
    sys.stdout.write("-----------\n")
    sys.stdout.write("Add an item\n")
    sys.stdout.write("-----------\n")

    item_name = get_str("Enter item name: ")
    sys.stdout.write("\n")
    item_serving = get_int("Enter item servings amount: ")
    sys.stdout.write("\n")
    item_price = get_positive_float("Enter item price: $")
    sys.stdout.write("\n")
    add_item(item_name, item_serving, item_price)
    
def display_saved_data():
    i = 0
    for item in item_names:
        sys.stdout.write(item_names[i] + " ")
        sys.stdout.write(str(item_servings[i]) + " ")
        sys.stdout.write(str(item_prices[i]) + "\n")
        i += 1

def save_data():
    try:
        file_object = open("test_case_02.txt", "w")
        i = 0
        while i < len(item_names):
            file_object.write(item_names[i] + "," + str(item_servings[i]) + "," + str(item_prices[i]) + "\n")
            i += 1
        file_object.close()
    except OSError:
        sys.stdout.write("Could not save data to file.")