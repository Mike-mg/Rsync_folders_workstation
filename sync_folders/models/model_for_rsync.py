"""
Model to retrieve user and system information and generate synchronization
"""

import os


class ModelRsync():
    """
    Class for the sync folders
    """

    def __init__(self, source: str,
                 destination: str,
                 list_folders_selected: list):

        self.source = source
        self.destination = destination
        self.list_folders_selected = list_folders_selected
        self.model_recovery_data = ModelRecoveryData()
        self.user_session = self.model_recovery_data.get_user_session()
        self.user_folder_session = self.model_recovery_data.get_user_folder()

    def rsync_dry_run(self) -> None:
        """
        Execute Rsync --dry-run option
        """

        for folder in self.list_folders_selected:

            if self.source != self.user_folder_session and self.destination != self.user_folder_session: # noqa
                os.system(f"rsync -rtlongvh {self.source}/{folder}/ {self.destination}/{folder}/") # noqa

            elif self.source == self.user_folder_session:
                os.system(f"rsync -rtlongvh {self.source}/{folder}/ {self.destination}/{self.user_session}/{folder}/") # noqa

            elif self.destination == self.user_folder_session:
                os.system(f"rsync -rtlongvh {self.source}/{folder}/ {self.destination[:5]}/{folder}/") # noqa

    def rsync_folders(self):
        """
        Execute Rsync folders option synchronization
        """

        for folder in self.list_folders_selected:

            if not os.path.exists(f"{self.destination}/{folder}"): # noqa
                os.makedirs(f"{self.destination}/{folder}", exist_ok=False)

            if self.source != self.user_folder_session and self.destination != self.user_folder_session: # noqa
                os.system(f"rsync -rtlogvh {self.source}/{folder}/ {self.destination}/{folder}/") # noqa

            elif self.source == self.user_folder_session:
                os.system(f"rsync -rtlogvh {self.source}/{folder}/ {self.destination}/{self.user_session}/{folder}/") # noqa

            elif self.destination == self.user_folder_session:
                os.system(f"rsync -rtlogvh {self.source}/{folder}/ {self.destination[:5]}/{folder}/") # noqa


class ModelRecoveryData():
    """
    Get data for rsync
    """

    def __init__(self):
        self.user_session = self.get_user_session()
        self.user_folder = self.get_user_folder()
        self.active_partitions = self.get_all_active_partitions()
        self.folders_source_selected = []

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

        self.active_partitions = [
            partition.strip() for partition in os.popen(
                "lsblk -f | grep sd[b-z] | awk '{print $NF}'") if partition.startswith("/")] # noqa

        self.active_partitions.append(self.get_user_folder())

        return self.active_partitions

    def get_folders_partition_source(self, partition: str) -> list:
        """
        return a list of folder partition self.source
        """

        for folder in os.listdir(partition):
            if not folder.startswith("."):
                if " " in folder:
                    name_folder_modified = folder.replace(' ', '_')
                    name_actual = f"{partition}/{folder}"
                    new_name = f"{partition}/{name_folder_modified}"
                    os.rename(name_actual, new_name)

        self.folders_source_selected = [
            folder for folder in os.listdir(
                partition) if not folder.startswith(".")]

        return self.folders_source_selected


if __name__ == "__main__":
    pass
    model = ModelRecoveryData()
    model.get_folders_partition_source("/run/media/mike/wd_m.2_256Go")
