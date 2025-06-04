import string
import random

from openpyxl import workbook, load_workbook


class Utils:
    def read_data_from_excel(file, sheet):
        wb = load_workbook(file)
        ws = wb[sheet]
        data_list = []

        T_rows = ws.max_row
        T_columns = ws.max_column

        for r in range(2, T_rows + 1):
            row = []
            for c in range(1, T_columns + 1):
                row.append(ws.cell(r, c).value)
            data_list.append(row)
        return data_list

    @staticmethod
    def random_email():
        domains = ["gmail.com", "yahoo.com", "outlook.com"]
        return f"emailtest{random.randint(1, 1000)}@{random.choice(domains)}"
