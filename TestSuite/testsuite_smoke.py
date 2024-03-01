import pytest
from Mobile_Tests.Login_with_email import test_login_with_email
from Mobile_Tests.compost_mvp_flow import compost_mvp_screens
from Pages.Web_pages.Mixpanel_pages.mixpanel_analytics import test_mixpanel
import csv

Execute_Login_with_email = test_login_with_email()
Execute_Compost_mvp = compost_mvp_screens()
Execute_mixpanel = test_mixpanel()


@pytest.mark.csv
def test_suite():
    if Execute_Login_with_email is True:
        Execute_Login_with_email_status = "Pass"
        log_test_result("Verify that user account should be create successfully ",
                        Execute_Login_with_email_status)

        if Execute_Compost_mvp is True:
            Execute_Compost_mvp_status = "Pass"
            log_test_result("Verify tht should be logged in successfully ",
                            Execute_Compost_mvp_status)
            if Execute_mixpanel is True:
                Execute_mixpanel_status = "Pass"
                log_test_result("Verify that mixpanel should be executed successfully ",
                                Execute_mixpanel_status)

            else:
                Execute_mixpanel_status = "Fail"
                log_test_result("Verify that mixpanel should be executed successfully ",
                                Execute_mixpanel_status)

        else:
            Execute_Compost_mvp_status = "Fail"
            log_test_result("Verify tht should be logged in successfully",
                            Execute_Compost_mvp_status)
    else:
        Execute_SignUp_status = "Fail"
        log_test_result("Verify that user account should be create successfully",
                        Execute_SignUp_status)


def log_test_result(test_name, status):
    csv_file = "Results/Test_suit_results.csv"
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
