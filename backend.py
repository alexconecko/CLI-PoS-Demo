import sys

class admin_panel():
    def magic_methods(self):
        i = 0
        while i < len(backend_operations.foods_listed_by_name):
            sys.stdout.write(backend_operations.foods_listed_by_name[i].__str__() + "\n" + backend_operations.foods_listed_by_name[i].__repr__() + "\n")
            i += 1


class food_item():
    #double underscores are denoted before the member name in order to keep the data private
    __item_name = ""
    __item_servings = 0
    __item_price = 0.0
    
    #constructor ensures that objects initialise with values for these members
    def __init__(self, item_name, item_servings, item_price):
        self.__item_name = item_name
        self.__item_servings = item_servings
        self.__item_price = item_price
    
    #property tag is used for our getter methods, using this tag we can call the methods without the use of () at 
    #the end providing the illusion of an actual attribute/property.    
    @property
    def item_name(self):
        return self.__item_name
    
    @property
    def item_servings(self):
        return self.__item_servings
    
    @property
    def item_price(self):
        return self.__item_price
    
    #----------------------------RAISE ERROR IMPLEMENTATIONS-------------------------------
    #Just as an accessor/getter method allows the retrieval of a property of an object, 
    # a mutator/setter method allows the modification of a property, by creating a setter
    #method for each property above we fix attribute errors
    @item_name.setter
    def item_name(self, value):
        #if statement used to validate that the value is not an empty string
        if value != 0:
            self.__item_name = value
        else:
            raise ValueError("item name cannot be empty.")
            
    @item_servings.setter
    def item_servings(self, value):
        if value != 0:
            self.__item_servings = value
        else:
            raise ValueError("item servings cannot be empty.")
            
    @item_price.setter
    def item_price(self, value):
        if value != 0:
            self.__item_price = value
        else:
            raise ValueError("item price cannot be empty.")
                   

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
                value = int(user_input_handling.get_str(self, prompt))
            except:
                prompt = "That wasn't right. Re-enter: "
        return value

    def get_float(self, prompt):
        value = None
        while value == None:
            try:
                value = float(user_input_handling.get_str(self, prompt))
            except:
                prompt = "That wasn't right. Re-enter: "
        return value

    def get_positive_float(self, prompt):
        value = user_input_handling.get_float(self, prompt)
        while value < 0:
            value = user_input_handling.get_float(self, "Input must be positive. Re-enter: ")
        return value

    def get_menu_choice(self):
        menu = "\n=====================\n"
        menu += "BurgerJoint POS system\n"
        menu += "======================\n"
        menu += "[A]dd an item\n"
        menu += "[D]isplay saved data\n"
        menu += "[~]Admin Panel\n"
        menu += "E[x]it\n"
        
        sys.stdout.write(menu)
        
        menu = menu.lower()
        choice = user_input_handling.get_str(self, "Enter choice: ").lower()
        while not "[" + choice + "]" in menu:
            choice = user_input_handling.get_str(self, (choice + " was an invalid choice! Re-enter: ")).lower()
        
        return choice
    
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

class backend_operations():
    foods_listed_by_name = []
    
    #--------------RAISE ERROR IMPLEMENTATION-------------------------
    def load_data(self):
        try:
            file_object = open("data.csv", "r")
            for line in file_object:
                fields = line.split(",")
                item_name = fields[0].strip()
                item_serving = fields[1].strip()
                item_price = fields[2].strip()
                backend_operations.add_item(item_name, item_serving, item_price)
        except:
            raise OSError("Error loading data file.\n")

    @staticmethod
    def add_item(item_name, item_servings, item_price):
        food = food_item(item_name, item_servings, item_price)
        food.item_name = item_name
        food.item_servings = item_servings
        food.item_price = item_price
        backend_operations.foods_listed_by_name.append(food)
        
        
    def display_saved_data(self):
        i = 0
        for item in backend_operations.foods_listed_by_name:
            sys.stdout.write(backend_operations.foods_listed_by_name[i].item_name + " ")
            sys.stdout.write(str(backend_operations.foods_listed_by_name[i].item_servings) + " ")
            sys.stdout.write(str(backend_operations.foods_listed_by_name[i].item_price) + "\n")
            i += 1
    #---------------RAISE ERROR IMPLEMENTATION---------------------
    def save_data(self):
        try:
            file_object = open("data.csv", "w")
            i = 0
            while i < len(backend_operations.foods_listed_by_name):
                file_object.write(backend_operations.foods_listed_by_name[i].item_name + "," + str(backend_operations.foods_listed_by_name[i].item_servings) + "," + str(backend_operations.foods_listed_by_name[i].item_price) + "\n")
                i += 1
            file_object.close()
        except:
            raise OSError("Could not save data to file.")
            
