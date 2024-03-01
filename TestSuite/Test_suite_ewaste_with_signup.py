import pytest
from Tests.Mobile_Tests.Login_with_email import test_login_with_email
from Tests.Mobile_Tests.Ewaste_flow import test_Ewaste
import csv

from Pages.Web_pages.Mixpanel_pages.mixpanel_export_events import test_mixpanel
from Pages.Web_pages.Mixpanel_pages.mixpanel_ewaste_events_verification import test_ewaste_events_verification

Execute_signup_with_email = test_login_with_email()
Execute_Ewaste_onboarding = test_Ewaste()
Execute_mixpanel = test_mixpanel()
Execute_ewaste_events_verif = test_ewaste_events_verification()


@pytest.mark.csv
def test_suite_ewaste():
    if Execute_signup_with_email is True:
        Execute_signup_with_email_status = "Pass"
        log_test_result("Verify that user account should be create successfully ",
                        Execute_signup_with_email_status)

        if Execute_Ewaste_onboarding is True:
            Execute_Ewaste_onboarding_status = "Pass"
            log_test_result("Verify tht ewaste should be performed successfully ",
                            Execute_Ewaste_onboarding_status)
            if Execute_mixpanel is True:
                Execute_mixpanel_status = "Pass"
                log_test_result("Verify that mixpanel events should be exported successfully",
                                Execute_mixpanel_status)
                if Execute_ewaste_events_verif is True:
                    Execute_ewaste_events_verif_status = "Pass"
                    log_test_result("Verify that Ewaste events should be verified successfully",
                                    Execute_ewaste_events_verif_status)

                else:
                    Execute_ewaste_events_verif_status = "Fail"
                    log_test_result("Verify that Ewaste events should be verified successfully",
                                    Execute_ewaste_events_verif_status)

            else:
                Execute_mixpanel_status = "Fail"
                log_test_result("Verify that mixpanel events should be exported successfully",
                                Execute_mixpanel_status)

        else:
            Execute_Ewaste_onboarding_status = "Fail"
            log_test_result("Verify tht should performed successfully",
                            Execute_Ewaste_onboarding_status)
    else:
        Execute_SignUp_status = "Fail"
        log_test_result("Verify that user account should be create successfully",
                        Execute_SignUp_status)


def log_test_result(test_name, status):
    csv_file = "Results/Test_suit_ewaste_results.csv"
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
    pytest.test_suite_ewaste()
