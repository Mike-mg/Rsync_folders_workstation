"""
Views menu program
"""


class ViewMenu:
    """
    Show the views of program
    """

    def __init__(self):
        pass

    def sub_menu(self, sub_menu: str) -> None:
        """
        Format sub menu
        """

        print(f"\n\n{'=' * 50}\n{sub_menu}\n{'=' * len(sub_menu)}\n")

    def menu_list(self) -> None:
        """
        Show menu list
        """

        type_rsync = ["Difference between the folders",
                      "Synchronization of folders",
                      "Quit"]

        self.sub_menu("Menu - SyncFolders ( For Gnu/Linux )")

        for index, type_of_rsync in enumerate(type_rsync):

            print(f"{'[ '}{index}{' ]'} {type_of_rsync}")

    def choice_user_menu(self) -> int:
        """
        Choice user menu
        """

        choice_menu_option = input("\nSelect a menu option : ")
        choice_menu_option = int(choice_menu_option)

        return choice_menu_option

    def select_partition_destination(self, active_partitions: list) -> None:
        """
        show active partitions
        """

        self.sub_menu("Select partition destination")

        for index, partition in enumerate(active_partitions):

            print(f"{'[ '}{index}{' ]'} {partition}")

        index_partition = input("\nSelect a partition : ")
        index_partition = int(index_partition)

        return index_partition

    def get_index_partition_source(self, active_partitions: list) -> int:
        """
        show active partitions
        """

        self.sub_menu("Select partition source")

        for index, partition in enumerate(active_partitions):

            print(f"[ {index} ] {partition}")

        index_partition_source = input("\nSelect a partition : ")
        index_partition_source = int(index_partition_source)

        return index_partition_source

    def get_index_folders_partition_source(
            self, folers_partitions_source: list) -> list:
        """
        show active partitions
        """

        self.sub_menu("Select folders partition source")

        for index, partition in enumerate(folers_partitions_source):

            print(f"{'[ '}{index}{' ]'} {partition}")

        list_index_folders_partition_source = input("\nSelect folders ( separate folder by ',') : ") # noqa
        list_index_folders_partition_source = [int(folder) for folder in list_index_folders_partition_source.split(",") if folder != ","] # noqa

        return list_index_folders_partition_source
