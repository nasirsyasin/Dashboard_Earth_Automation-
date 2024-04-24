import time

import pytest
from Pages.Mobile_pages.TrackActions import TrackAction
import csv


@pytest.mark.csv
def test_TrackAction():
    ta = TrackAction()
    if ta.trackActions():
        trackActions_status = 'Pass'
        log_test_result("Verify that trackActions button should be tapped again",
                        trackActions_status)

    else:
        trackActions_status = 'Fail'
        log_test_result("Verify that  trackActions button should be tapped again",
                        trackActions_status)


def log_test_result(test_name, status):
    csv_file = "/Users/mac/Documents/Python_Projects/DBE_Project/Results/TrackAction_results.csv"
    csv_headers = ["Tests Summary", "Status"]
    csv_rows = [{"Tests Summary": test_name, "Status": status}]  # Wrapping rows in a list of dictionaries

    with open(csv_file, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=csv_headers)

        # Check if the file is empty to write the header
        if file.tell() == 0:
            writer.writeheader()

        writer.writerows(csv_rows)


if __name__ == "__main__":
    pytest.main()
