"""
Controller the menu
"""

import sync_folders


class ControllerMenu:
    """
    Verify the informations
    """

    def __init__(self):
        self.view = sync_folders.ViewMenu()
        self.controller_model_dry_run = sync_folders.Rsync_dry_run()

    def show_menu_banner(self):
        """
        show banner program
        """

        self.view.show_menu()

    def choice_menu(self):
        """
        Show select of type of sync
        """

        choice_menu = self.view.choice_menu()

        if choice_menu == 0:
            """
            Execute Rsync --dry-run
            """

            self.controller_model_dry_run.rsync_dry_run()

        elif choice_menu == 1:
            """
            Execute Rsync synchronization folders
            """

            self.controller_model_dry_run.rsync_synchronization_folders()
