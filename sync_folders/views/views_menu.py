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

    def show_menu(self) -> None:
        """
        Show the menu program

        """

        banner = "Sync backup folders desktop"

        print(f"{'=' * len(banner)}\n{banner}\n{'=' * len(banner)}")

        type_rsync = ["Difference between the folders",
                      "Synchronization of folders"]

        self.sub_menu("Select the type of Rsync")

        for index, type_of_rsync in enumerate(type_rsync):

            print(f"{'[ '}{index}{' ]'} {type_of_rsync}")

    def choice_menu(self) -> int:

        choice_type_rsync = input("\nChoice type synchronisation : ")
        choice_type_rsync = int(choice_type_rsync)

        return choice_type_rsync

    def show_partitions_active(self) -> None:

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
