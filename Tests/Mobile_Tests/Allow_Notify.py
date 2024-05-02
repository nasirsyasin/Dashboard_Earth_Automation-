import pytest
from Pages.Mobile_pages.AllowNotify import AllowNotify
import csv


class Allow_Notify:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Allow_Notify, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        pass

    @pytest.mark.csv
    def test_Allow_notify(self):
        ta = AllowNotify()
        if ta.allow_notif():
            allow_notif_status = 'Pass'
            # test_case_key = "DT-T255"  # Assuming test case key is constant for this example custom_test_step_results =
            # customize_test_step_results(test_case_key=test_case_key) test_manager.make_post_request_with_results(
            # test_case_key=test_case_key, status_name=allow_notif_status, test_step_results=custom_test_step_results
            # )
            log_test_result("Verify that allow_notif button should be tapped",
                            allow_notif_status)
            ta.app_refresh()
        else:
            allow_notif_status = 'Fail'
            # test_case_key = "DT-T255"  # Assuming test case key is constant for this example
            # custom_test_step_results = customize_test_step_results(test_case_key=test_case_key)
            # test_manager.make_post_request_with_results(test_case_key=test_case_key, status_name=allow_notif_status,
            #                                             test_step_results=custom_test_step_results
            #                                             )
            log_test_result("Verify that  allow_notif button should be tapped again",
                            allow_notif_status)


# test_manager = TestExecutionManager()


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
