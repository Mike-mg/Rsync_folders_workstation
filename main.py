import sync_folders
import os

os.system("clear")

menu = sync_folders.ControllerMenu()
menu.show_menu_banner()
menu.choice_menu()
menu
