"""
Model to retrieve user and system information and generate synchronization
"""

import os


class ModelRsync():
    """
    Class for the sync folders
    """

    def __init__(self, source, destination, list_folders_selected):
        self.source = source
        self.destination = destination
        self.list_folders_selected = list_folders_selected
        self.recovery_data = ModelRecoveryData()
        self.user_session = self.recovery_data.get_user_session()
        self.user_folder_session = self.recovery_data.get_user_folder()

    def rsync_dry_run(self) -> None:
        """
        Execute Rsync --dry-run option
        """

        for folder in self.list_folders_selected:

            if self.source != self.user_folder_session and self.destination != self.user_folder_session: # noqa
                # os.system(f"rsync -rtlongvh {self.source}/{self.user_session}/{folder}/ {self.destination}/{self.user_session}/{folder}/") # noqa
                print(f"rsync -rtlongvh {self.source}/{self.user_session}/{folder}/ {self.destination}/{self.user_session}/{folder}/") # noqa

            elif self.source == self.user_folder_session:
                os.system(f"rsync -rtlongvh {self.source}/{folder}/ {self.destination}/{self.user_session}/{folder}/") # noqa

            elif self.destination == self.user_folder_session:
                os.system(f"rsync -rtlongvh {self.source}/{self.user_session}/{folder}/ {self.destination}/{folder}/") # noqa

    def rsync_folders(self):
        """
        Execute Rsync folders option synchronization
        """

        for folder in self.list_folders_selected:

            if not os.path.exists(f"{self.destination}/{self.user_session}/{folder}"): # noqa
                os.makedirs(f"{self.destination}/{self.user_session}/{folder}", exist_ok=False) # noqa

            if self.source != self.user_folder_session and self.destination != self.user_folder_session: # noqa
                os.system(f"rsync -rtlogvh --progress {self.source}/{self.user_session}/{folder}/ {self.destination}/{self.user_session}/{folder}/") # noqa

            elif self.source == self.user_folder_session:
                os.system(f"rsync -rtlogvh --progress {self.source}/{folder}/ {self.destination}/{self.user_session}/{folder}/") # noqa

            elif self.destination == self.user_folder_session:
                os.system(f"rsync -rtlogvh --progress {self.source}/{self.user_session}/{folder}/ {self.destination}/{folder}/") # noqa


class ModelRecoveryData():
    """
    Get data for rsync
    """

    def __init__(self):
        self.user_session = self.get_user_session()
        self.user_folder = self.get_user_folder()
        self.active_partitions = self.get_all_active_partitions()

    def get_user_session(self) -> str:
        """
        return user name
        """

        self.user_session = os.popen("whoami").read().strip()

        return self.user_session

    def get_user_folder(self) -> str:
        """
        return folder user
        """

        self.user_folder_session = os.popen('cd ~ && pwd').read().strip()

        return self.user_folder_session

    def get_all_active_partitions(self) -> list:
        """
        return a list of active partition
        """

        self.active_partitions = [partition.strip() for partition in os.popen(
            "lsblk -f | grep sd[b-z] | awk '{print $NF}'") if partition.startswith("/")] # noqa

        self.active_partitions.append(self.get_user_folder())

        return self.active_partitions

    def get_folders_partition_source(self, partition: str) -> list:
        """
        return a list of folder partition self.source
        """

        folders_partition_source = [folders for folders in os.listdir(
            partition) if not folders.startswith(".")]

        return folders_partition_source


if __name__ == "__main__":
    pass
    # model = ModelRsync()
    # print(model.get_user_session())
    # print(model.get_user_folder())
    # print(model.get_all_active_partitions())
    # print(model.get_folders_partition_selected())
