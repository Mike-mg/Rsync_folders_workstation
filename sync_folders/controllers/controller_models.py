"""
Controller models
"""

import sync_folders


class controllerRsync:
    """
    Execute Rsync --dry-run synchronisation
    """

    def __init__(self):
        self.view = sync_folders.ViewMenu()
        self.model_recovery_data = sync_folders.ModelRecoveryData()
        self.list_folders_source_selected = []
        self.partition_source = str
        self.partition_destination = str

    def rsync_dry_run(self):
        """
        Execute Rsync --dry-run between different folders
        """

        self.recovery_data_for_source()

        model = sync_folders.ModelRsync(
            self.partition_source,
            "/run/media/mike/wd_m.2_500Go_2",
            self.list_folders_source_selected
            )

        model.rsync_dry_run()

        # model = self.model_rsync(
        #     active_partitions[index_partition_source],
        #     "/run/media/mike/wd_m.2_500Go_2",
        #     self.folders_source_selected)

    # def rsync_synchronization_folders(self):
    #     """
    #     Execute Rsync synchronization folders
    #     """

    #     partition_source = self.view.select_partition_source()
    #     partition_destination = self.view.select_partition_destination()

    #     model = sync_folders.ModelRsync(
    #         self.partition_source,
    #         "/run/media/mike/wd_m.2_500Go_2",
    #         self.list_folders_source_selected
    #         )

    def recovery_data_for_source(self):
        """
        Controller recovery data
        """

        index_partition_source = self.view.\
            get_index_partition_source(
                self.model_recovery_data.get_all_active_partitions())

        self.partition_source = self.model_recovery_data.\
            get_all_active_partitions()[index_partition_source]

        list_folders_partition_source = self.model_recovery_data.\
            get_folders_partition_source(self.partition_source)

        index_folders_source_selected = self.view.\
            get_index_folders_partition_source(list_folders_partition_source)

        for folder in index_folders_source_selected:
            self.list_folders_source_selected.append(
                list_folders_partition_source[folder])

        self.partition_destination = self.view.select_partition_destination(
            self.model_recovery_data.get_all_active_partitions())
