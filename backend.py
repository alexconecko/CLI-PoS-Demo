import sys

class food_item():
    item_names = []
    item_servings = []
    item_prices = []

class user_input_handling():
    def get_str(self, prompt):
        sys.stdout.write(prompt)
        sys.stdout.flush()
        value = sys.stdin.readline().strip()
        while len(value) == 0:
            sys.stdout.write("Input cannot be blank. Re-enter: ")
            sys.stdout.flush()
            value = sys.stdin.readline().strip()
        
        return value

    def get_int(self, prompt):
        value = None
        while value == None:
            try:
                value = int(self.get_str(prompt))
            except:
                prompt = "That wasn't right. Re-enter: "
        return value

    def get_float(self, prompt):
        value = None
        while value == None:
            try:
                value = float(self.get_str(prompt))
            except:
                prompt = "That wasn't right. Re-enter: "
        return value

    def get_positive_float(self, prompt):
        value = self.get_float(prompt)
        while value < 0:
            value = self.get_float("Input must be positive. Re-enter: ")
        return value

    def get_menu_choice(self):
        menu = "\n=====================\n"
        menu += "BurgerJoint POS system\n"
        menu += "======================\n"
        menu += "[A]dd an item\n"
        menu += "[D]isplay saved data\n"
        menu += "E[x]it\n"
        
        sys.stdout.write(menu)
        
        menu = menu.lower()
        choice = user_input_handling.get_str(self, "Enter choice: ").lower()
        while not "[" + choice + "]" in menu:
            choice = user_input_handling.get_str(self, (choice + " was an invalid choice! Re-enter: ")).lower()
        
        return choice

class backend_operations():
    def load_data(self):
        try:
            file_object = open("data.csv", "r")
            for line in file_object:
                fields = line.split(",")
                item_name = fields[0].strip()
                item_serving = fields[1].strip()
                item_price = fields[2].strip()
                backend_operations.add_item(self, item_name, item_serving, item_price)
        except OSError:
            sys.stdout.write("Error loading data file.\n")
        except IndexError:
            sys.stdout.write("Data file could not be read properly. Check csv structure.\n")

    def add_item(self, item_name, item_serving, item_price):
        food_item.item_names.append(item_name)
        food_item.item_servings.append(item_serving)
        food_item.item_prices.append(item_price)

    def add_item_via_menu(self):
        sys.stdout.write("-----------\n")
        sys.stdout.write("Add an item\n")
        sys.stdout.write("-----------\n")

        item_name = user_input_handling.get_str(self, "Enter item name: ")
        sys.stdout.write("\n")
        item_serving = user_input_handling.get_int(self, "Enter item servings amount: ")
        sys.stdout.write("\n")
        item_price = user_input_handling.get_positive_float(self, "Enter item price: $")
        sys.stdout.write("\n")
        backend_operations.add_item(item_name, item_serving, item_price)
        
    def display_saved_data(self):
        i = 0
        for item in food_item.item_names:
            sys.stdout.write(food_item.item_names[i] + " ")
            sys.stdout.write(str(food_item.item_servings[i]) + " ")
            sys.stdout.write(str(food_item.item_prices[i]) + "\n")
            i += 1

    def save_data(self):
        try:
            file_object = open("data.csv", "w")
            i = 0
            while i < len(food_item.item_names):
                file_object.write(food_item.item_names[i] + "," + str(food_item.item_servings[i]) + "," + str(food_item.item_prices[i]) + "\n")
                i += 1
            file_object.close()
        except OSError:
            sys.stdout.write("Could not save data to file.")