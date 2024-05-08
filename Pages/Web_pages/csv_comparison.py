import csv


def read_csv(file_path):
    data = []
    with open(file_path, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile, fieldnames=["Event Name", "test_case_key", "Operating System"],
                                   skipinitialspace=True)
        next(csvreader)  # Skip the header row
        for row in csvreader:
            if row:  # Check if row is not empty
                data.append(dict(row))  # Convert each row to a dictionary
    return data


def compare_csv_by_column(file1, file2, column_name, column_test_key, result_file):
    csv1_data = read_csv(file1)
    csv2_data = read_csv(file2)

    # Create a set of event names from csv2_data
    matching_events = set(row[column_name] for row in csv2_data)
    # Write the matching rows to the result CSV file with status and test_case_key
    with open(result_file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Event Name', 'Status', 'test_case_key'])  # Write the header

        for row1 in csv1_data:
            event_name = row1[column_name]
            status = 'Pass' if event_name in matching_events else 'Fail'
            test_case_key = row1.get(column_test_key, column_test_key)
            csvwriter.writerow([event_name, status, test_case_key])
    print(f"Matching rows with status and test_case_key written to {result_file}")
