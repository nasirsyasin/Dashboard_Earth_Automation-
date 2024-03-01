import csv


def find_data(input_file, find_condition):
    found_rows = []

    with open(input_file, 'r', newline='') as infile:
        reader = csv.DictReader(infile)

        for row in reader:
            if eval(find_condition):
                found_rows.append(row)

    return found_rows


# Example: Finding data where City is 'New York'
# find_condition = "row['Event Name'] == 'session_started'"
# find_condition = "row['App Build Number'] == '528'"

find_condition = "row['Device ID'] == '59F82C4C-1050-44DD-97B0-D71AFE1B3387'"
input_file = "/csv/events-export-2313088-1705408575043.csv"

found_data = find_data(input_file, find_condition)

# Display the found data
for row in found_data:
    print(row)
