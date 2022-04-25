from configuration import Configuration

configuration = Configuration()


class FinancialData:
    def __init__(self):
        self.location_current_csv = configuration.location_current_csv
        self.location_current_master = configuration.location_current_master
        self.location_old_csv = configuration.location_old_csv
        self.location_old_master = configuration.location_old_csv



