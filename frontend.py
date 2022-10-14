import sys
from backend import *

class point_of_sale_user_interface():
    def point_of_sale_UI(self):
        backend_operations.load_data(self)
        choice = user_input_handling.get_menu_choice(self)
        while choice != "x":
            sys.stdout.write("\n")
            if choice == "a":
                user_input_handling.add_item_via_menu(self)
            elif choice == "d":
                backend_operations.display_saved_data(self)
            choice = user_input_handling.get_menu_choice(self)
        backend_operations.save_data(self)

run = point_of_sale_user_interface()
run.point_of_sale_UI()
