import pandas as pd

class DataFrameChecker:
    def __init__(self, data):
        self.data = data

    def check_errors(self):
        has_errors = False
        print("Errors in DataFrame:")
        for column in self.data.columns:
            try:
                # Check for missing values in the column
                if self.data[column].isnull().any():
                    has_errors = True
                    print("Error: Missing values found in column:", column)
                    print(self.data[self.data[column].isnull()])

                # Check for out-of-range errors
                errors = self.data[(self.data[column] < self.data[column].min()) | (self.data[column] > self.data[column].max())]
                if not errors.empty:
                    has_errors = True
                    print("Errors found in column:", column)
                    print(errors)

            except TypeError:
                print("Error: Non-numeric values found in column:", column)
                has_errors = True

        if not has_errors:
            print("No errors found in DataFrame")

    def check_duplicates(self):
        duplicates = self.data[self.data.duplicated()]
        if not duplicates.empty:
            print("Duplicates found in DataFrame:")
            print(duplicates)
        else:
            print("No duplicates found in DataFrame")

    def check_missing_values(self):
        missing_values = self.data.isnull().sum()
        if missing_values.sum() > 0:
            print("Missing values found in DataFrame:")
            print(missing_values[missing_values > 0])
        else:
            print("No missing values found in DataFrame")



