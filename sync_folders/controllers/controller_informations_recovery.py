"""
Controller for the rsync folders verifications
"""

import sync_folders


class ControllerRsync:
    """
    Rsync folders verifications
    """

    def __init__(self):
        self.controller_utils = sync_folders.GetInfoForSync()
        self.user = str
        self.home_user_folder = str
        self.partitions_actives = []

    def user_session(self) -> str:
        """
        get user
        """

        self.user = self.controller_utils.get_user_session()

        return self.user

    def user_folder_session(self) -> str:
        """
        get folder user session
        """

        self.home_user_folder = self.controller_utils.get_user_folder()

        return self.home_user_folder

    def all_active_partitions(self) -> list:
        """
        get all_partitions active
        """

        self.partitions_actives = self.controller_utils.get_all_active_partitions() # noqa

        return self.partitions_actives
