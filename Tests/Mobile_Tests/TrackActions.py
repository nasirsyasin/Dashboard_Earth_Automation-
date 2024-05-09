import time

import pytest
import csv

from Pages.Mobile_pages.TrackActions import TrackAction
from TestExecutionManager import TestExecutionManager, customize_test_step_results


class TrackActions:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(TrackActions, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        pass

    @pytest.mark.csv
    def test_TrackAction(self):
        ta = TrackAction()

        if ta.trackActions():
            trackActions_status = 'Pass'
            test_case_key = "DT-T779"  # Assuming test case key is constant for this example
            custom_test_step_results = customize_test_step_results(test_case_key=test_case_key)
            test_manager.make_post_request_with_results(test_case_key=test_case_key,
                                                        status_name=trackActions_status,
                                                        test_step_results=custom_test_step_results
                                                        )
            log_test_result("Verify that trackActions button should be tapped ",
                            trackActions_status)

        else:
            trackActions_status = 'Fail'
            test_case_key = "DT-T779"  # Assuming test case key is constant for this example
            custom_test_step_results = customize_test_step_results(test_case_key=test_case_key)
            test_manager.make_post_request_with_results(test_case_key=test_case_key,
                                                        status_name=trackActions_status,
                                                        test_step_results=custom_test_step_results
                                                        )
            log_test_result("Verify that  trackActions button should be tapped again",
                            trackActions_status)

    @pytest.mark.csv
    def test_tooltip(self):
        ta = TrackAction()
        if ta.tooltip_1_nxt():
            tooltip_1_nxt_status = 'Pass'
            # test_case_key = "DT-T255"  # Assuming test case key is constant for this example
            # custom_test_step_results = customize_test_step_results(test_case_key=test_case_key)
            # test_manager.make_post_request_with_results(test_case_key=test_case_key, status_name=tooltip_1_nxt_status,
            #                                             test_step_results=custom_test_step_results
            #                                             )
            log_test_result("Verify that tooltip_1_nxt button should be tapped",
                            tooltip_1_nxt_status)
            time.sleep(5)
            if ta.tooltip_2_done():
                tooltip_2_done_status = 'Pass'
                test_case_key = "DT-T272"  # Assuming test case key is constant for this example
                custom_test_step_results = customize_test_step_results(test_case_key=test_case_key)
                test_manager.make_post_request_with_results(test_case_key=test_case_key,
                                                            status_name=tooltip_2_done_status,
                                                            test_step_results=custom_test_step_results
                                                            )
                log_test_result("Verify that tooltip_2_done button should be tapped",
                                tooltip_2_done_status)
                time.sleep(5)

            else:
                tooltip_2_done_status = 'Fail'
                test_case_key = "DT-T272"  # Assuming test case key is constant for this example
                custom_test_step_results = customize_test_step_results(test_case_key=test_case_key)
                test_manager.make_post_request_with_results(test_case_key=test_case_key,
                                                            status_name=tooltip_2_done_status,
                                                            test_step_results=custom_test_step_results
                                                            )
                log_test_result("Verify that  tooltip_2_done button should be tapped again",
                                tooltip_2_done_status)
        else:
            tooltip_1_nxt_status = 'Fail'
            # test_case_key = "DT-T255"  # Assuming test case key is constant for this example
            # custom_test_step_results = customize_test_step_results(test_case_key=test_case_key)
            # test_manager.make_post_request_with_results(test_case_key=test_case_key, status_name=tooltip_1_nxt_status,
            #                                             test_step_results=custom_test_step_results
            #                                             )
            log_test_result("Verify that  tooltip_1_nxt button should be tapped again",
                            tooltip_1_nxt_status)


test_manager = TestExecutionManager()


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

# if __name__ == "__main__":
#     pytest.main()
#     run = TrackActions()
#     run.test_TrackAction()
