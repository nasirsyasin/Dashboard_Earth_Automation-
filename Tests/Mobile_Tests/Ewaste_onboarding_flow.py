import pytest
from Pages.Mobile_pages.eWest_page.ewaste_locators import test_Ewaste_onboarding, test_ewaste_complete
import csv

(ewaste_action_btn, ewaste_no_btn, ewaste_no_arrow, ewaste_action_btn_not_sure,
 ewaste_not_sure_btn) = test_Ewaste_onboarding()
(ewaste_not_sure_back_arrow, ewaste_yes_btn, ewaste_yes_arrow) = test_ewaste_complete()


@pytest.mark.csv
def test_Ewaste():
    if ewaste_action_btn is True:
        ewaste_action_btn_status = 'Pass'
        log_test_result("Verify that upon tapping login link user should navigate to login screen",
                        ewaste_action_btn_status)
        if ewaste_no_btn is True:
            ewaste_no_btn_status = 'Pass'
            log_test_result("Verify that user should able to enter email successfully ", ewaste_no_btn_status)
            if ewaste_no_arrow is True:
                ewaste_no_arrow_status = 'Pass'
                log_test_result("Verify that user should able to enter password successfully",
                                ewaste_no_arrow_status)
                if ewaste_action_btn_not_sure is True:
                    ewaste_action_btn_not_sure_status = 'Pass'
                    log_test_result("Verify that the user is able to complete a successful login", ewaste_action_btn_not_sure_status)

                else:
                    ewaste_action_btn_not_sure_status = 'Fail'
                    log_test_result("Verify that the user is able to complete a successful login", ewaste_action_btn_not_sure_status)
            else:
                ewaste_no_arrow_status = 'Fail'
                log_test_result("Verify that user should able to enter password successfully",
                                ewaste_no_arrow_status)
        else:
            ewaste_no_btn_status = 'Fail'
            log_test_result("Verify that user should able to enter email successfully ", ewaste_no_btn_status)

    else:
        ewaste_action_btn_status = 'Fail'
        log_test_result("Verify that upon tapping login link user should navigate to login screen",
                        ewaste_action_btn_status)


def log_test_result(test_name, status):
    csv_file = "../../Results/Login_results.csv"
    csv_headers = ["Test Summary", "Status"]
    csv_rows = [{"Test Summary": test_name, "Status": status}]  # Wrapping rows in a list of dictionaries

    with open(csv_file, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=csv_headers)

        # Check if the file is empty to write the header
        if file.tell() == 0:
            writer.writeheader()

        writer.writerows(csv_rows)


if __name__ == "__main__":
    pytest.main()
