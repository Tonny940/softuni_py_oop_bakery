from project.table.table import Table


class InsideTable(Table):

    def __init__(self, table_number, capacity):
        super().__init__(table_number, capacity)

    @property
    def min_table_num(self):
        return 1

    @property
    def max_table_num(self):
        return 50

    @property
    def error_message(self):
        return f"Inside table's number must be between " \
               f"1 and 50 inclusive!"
