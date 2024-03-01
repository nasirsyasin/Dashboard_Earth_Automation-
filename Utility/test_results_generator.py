import csv


def log_test_result(test_name, status, csv_file, csv_headers):
    csv_rows = [{"Test Summary": test_name, "Status": status}]

    with open(csv_file, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=csv_headers)

        # Check if the file is empty to write the header
        if file.tell() == 0:
            writer.writeheader()

        writer.writerows(csv_rows)

