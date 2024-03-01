import csv


def read_csv(file_path):
    data = []
    with open(file_path, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile, fieldnames=["Event Name", "Operating System"], skipinitialspace=True)
        next(csvreader)  # Skip the header row
        for row in csvreader:
            if row:  # Check if row is not empty
                data.append(dict(row))  # Convert each row to a dictionary
    return data


def compare_csv_by_column(file1, file2, column_name, result_file):
    csv1_data = read_csv(file1)
    csv2_data = read_csv(file2)

    # Find matching rows based on the specified column
    matching_events = set(row[column_name] for row in csv2_data)

    # Write the matching rows to the result CSV file with status
    with open(result_file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Event Name', 'Status'])  # Write the header

        for row1 in csv1_data:
            event_name = row1[column_name]
            status = 'Passed' if event_name in matching_events else 'Failed'
            csvwriter.writerow([event_name, status])  # Write the Event Name and Status columns only

    print(f"Matching rows with status written to {result_file}")

