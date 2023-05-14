"""
Models for get informations
"""

import os


class GetInfoForSync:
    """
    Class that gets the necessary information
    for the synchronization of the folders
    """

    def __init__(self):
        self.user_session = str
        self.user_folder_session = str
        self.active_partitions = []

    def get_user_session(self) -> str:
        """
        return user name
        """

        get_user = os.popen("whoami")
        self.user_session = str(get_user.read()).strip()

        return self.user_session

    def get_user_folder(self) -> str:
        """
        return folder user
        """

        get_folder_user_session = os.popen(
            "cat /etc/passwd | grep mike | cut -d : -f6")

        self.user_folder_session = str(f"{get_folder_user_session.read().strip()}/")[:-1]

        return self.user_folder_session

    def get_all_active_partitions(self) -> list:
        """
        returns a list of active partition
        """

        actives_partitions = []

        actives_partitions.append(self.get_user_folder())

        all_partition = os.popen("lsblk -f | grep sd[bc] | awk '{print $NF}'")

        for partition in all_partition:
            if partition.startswith("/"):
                actives_partitions.append(partition.strip())

        self.active_partitions = actives_partitions

        return self.active_partitions
