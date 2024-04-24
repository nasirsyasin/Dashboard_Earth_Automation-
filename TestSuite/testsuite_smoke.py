import pytest
import csv
from Tests.Mobile_Tests.Ewaste_flow import test_Ewaste
from Tests.Mobile_Tests.Login_with_email import test_login_with_email
from Tests.Mobile_Tests.TrackActions import test_TrackAction
from Tests.Mobile_Tests.compost_mvp_flow import test_compost_mvp_screens


class MobileTestSuite:
    def __init__(self):
        self.execute_login_with_email = test_login_with_email()
        self.execute_track_action = test_TrackAction()
        self.execute_compost = test_compost_mvp_screens()
        self.execute_ewaste = test_Ewaste()

    def run_tests(self):
        self.execute_login_with_email_status = self.execute_login_with_email()
        self.execute_track_action_status = self.execute_track_action()
        self.execute_compost_status = self.execute_compost()
        self.execute_ewaste_status = self.execute_ewaste()

    def log_test_result(self, test_name, status):
        csv_file = "/Users/mac/Documents/Python_Projects/DBE_Project/Results/Test_suit_results.csv"
        csv_headers = ["Tests Summary", "Status"]
        csv_rows = [{"Tests Summary": test_name, "Status": status}]

        with open(csv_file, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=csv_headers)

            if file.tell() == 0:
                writer.writeheader()

            writer.writerows(csv_rows)

    def execute_tests(self):
        self.run_tests()
        self.log_test_result("Verify that Execute_login_with_email successfully", self.execute_login_with_email_status)
        self.log_test_result("Verify tht Execute_track_action successfully", self.execute_track_action_status)
        self.log_test_result("Verify that Execute_compost successfully", self.execute_compost_status)
        self.log_test_result("Verify that Execute_ewaste successfully", self.execute_ewaste_status)


if __name__ == "__main__":
    test_suite = MobileTestSuite()
    test_suite.execute_tests()
    pytest.main()
