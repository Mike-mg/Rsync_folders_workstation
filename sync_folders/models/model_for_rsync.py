"""
Model to retrieve user and system information and generate synchronization
"""

import os
import sync_folders


class RsyncFolders:
    """
    Class for the sync folders
    """

    def __init__(self):
        self.controller_informations = sync_folders.ControllerRsync()
        self.folders_sync = [
            "Documents",
            "GitHub",
            "Images",
            "OC_DA_Python",
            "Projects_python",
        ]
        self.user_session = self.controller_informations.user_session()
        self.user_folder_session = self.controller_informations.user_folder_session() # noqa
        self.active_partitions = self.controller_informations.all_active_partitions() # noqa

    def rsync_dry_run(self,
                      source: str,
                      destination: str,
                      ) -> None:
        """
        Execute Rsync --dry-run option
        """

        for folder in self.folders_sync:
            os.system(f"rsync -navh {source}/{self.user_session}/{folder}/\
                      {destination}{self.user_folder_session}") # noqa

    def rsync_folders(self,
                      source: str,
                      destination: str,
                      ) -> None:
        """
        Execute Rsync folders option synchronization
        """

        for folder in self.folders_sync:
            os.system(f"rsync -avh {source}/{self.user_session}/{folder}/\
                      {destination}{self.user_folder_session}") # noqa
