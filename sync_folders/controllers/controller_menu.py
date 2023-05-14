"""
Controller the menu
"""

import sync_folders


class ControllerMenu:
    """
    Controls the menu options selected by the user
    """

    def __init__(self):
        self.view = sync_folders.ViewMenu()
        self.controller_model_dry_run = sync_folders.RsyncDryRun()

    def choice_user_menu(self) -> bool:
        """
        Show select of type of sync
        """

        while True:
            # Show the menu while var choice_user_menu is True
            # If choice_user_menu = 2 then quit the program

            self.view.menu_list()
            choice_menu = self.view.choice_user_menu()

            if choice_menu == 0:
                # Execute Rsync --dry-run

                self.controller_model_dry_run.rsync_dry_run()

            elif choice_menu == 1:
                # Execute Rsync synchronization folders

                self.controller_model_dry_run.rsync_synchronization_folders()

            elif choice_menu == 2:
                # Exit program

                break
