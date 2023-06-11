"""
Program entry point
"""

import os
import sync_folders


def start_main():
    """
    Entry the program
    """

    choice_menu = sync_folders.ControllerMenu()

    os.system("clear")

    choice_menu.choice_user_menu()


if __name__ == "__main__":
    start_main()
