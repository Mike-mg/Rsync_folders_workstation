"""
Views menu program
"""

import sync_folders


class ViewMenu:
    """
    Show the views of program
    """

    def __init__(self):
        self.controller_rsync = sync_folders.ControllerRsync()

    def sub_menu(self, sub_menu) -> None:
        """
        Format sub menu
        """

        print(f"\n\n{'-' * 50}\n{sub_menu}\n{'-' * len(sub_menu)}") # noqa

    def menu_list(self):
        """
        Show menu list
        """

        type_rsync = ["Difference between the folders",
                      "Synchronization of folders",
                      "Quit"]

        self.sub_menu("Menu - SyncFolders")

        for index, type_of_rsync in enumerate(type_rsync):

            print(f"{'[ '}{index}{' ]'} {type_of_rsync}")

    def choice_user_menu(self) -> int:
        """
        Choice user menu
        """

        choice_menu_option = input("\nSelect a menu option : ")
        choice_menu_option = int(choice_menu_option)

        return choice_menu_option

    def show_partitions_active(self) -> None:
        """
        show active partitions
        """

        for index, partition in enumerate(
                self.controller_rsync.all_active_partitions()):

            print(f"{'[ '}{index}{' ]'} {partition}")

    def select_partition_source(self) -> None:
        """
        Select partition source
        """

        self.sub_menu("Select the partition source")
        self.show_partitions_active()
        choice_partition_source = input("\nSelect a partition : ")
        choice_partition_source = int(choice_partition_source)

        return choice_partition_source

    def select_partition_destination(self) -> None:
        """
        Select partition destination
        """

        self.sub_menu("Select the partition destination")
        self.show_partitions_active()
        choice_partition_destination = input("\nSelect a partition : ")
        choice_partition_destination = int(choice_partition_destination)

        return choice_partition_destination
