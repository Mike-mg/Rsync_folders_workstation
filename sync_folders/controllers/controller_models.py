"""
Controller models
"""

import sync_folders


class Rsync_dry_run:
    """
    Execute Rsync --dry-run synchronisation
    """

    def __init__(self):
        self.model_rsync = sync_folders.RsyncFolders()
        self.view = sync_folders.ViewMenu()

    def rsync_dry_run(self):
        """
        Execute Rsync --dry-run between different folders
        """

        partition_source = self.view.select_partition_source()
        partition_destination = self.view.select_partition_destination()

        self.model_rsync.rsync_dry_run(
            self.model_rsync.active_partitions[partition_source],
            self.model_rsync.active_partitions[partition_destination])

    def rsync_synchronization_folders(self):
        """
        Execute Rsync synchronization folders
        """

        partition_source = self.view.select_partition_source()
        partition_destination = self.view.select_partition_destination()

        self.model_rsync.rsync_folders(
            self.model_rsync.active_partitions[partition_source],
            self.model_rsync.active_partitions[partition_destination])
