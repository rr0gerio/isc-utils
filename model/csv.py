import csv


class CSVModel:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_rows_matching_column_value(self, column_name, value):
        matching_rows = []

        with open(self.file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row[column_name] == value:
                    matching_rows.append(row)
        return matching_rows

    def get_unique_values_for_column(self, column_name):
        unique_values = set()
        with open(self.file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                value = row[column_name]
                unique_values.add(value)
        return unique_values
