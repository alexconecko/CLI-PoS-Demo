import sys
from backend import *

def run_point_of_sale():
    load_data()
    choice = get_menu_choice()
    while choice != "x":
        sys.stdout.write("\n")
        if choice == "a":
            add_item_via_menu()
        elif choice == "d":
            display_saved_data()
        choice = get_menu_choice()
    save_data()

run_point_of_sale()
