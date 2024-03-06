import pytest
from Pages.Mobile_pages.LoginPage import LoginPage
import csv


# login_link_clicked, login_email_input, login_password_input, login_btn, Notification_popup = Login_Screen()

@pytest.mark.csv
def test_login_with_email():
    ls = LoginPage()
    if ls.login_link():
        login_link_status = 'Pass'
        log_test_result("Verify that upon tapping login link user should navigate to login screen",
                        login_link_status)
        if ls.email_input():
            login_email_input_status = 'Pass'
            log_test_result("Verify that user should able to enter email successfully ", login_email_input_status)
            if ls.password_input():
                login_password_input_status = 'Pass'
                log_test_result("Verify that user should able to enter password successfully",
                                login_password_input_status)
                if ls.login_btn():
                    login_btn_status = 'Pass'
                    log_test_result("Verify that the user is able to complete a successful login", login_btn_status)

                else:
                    login_btn_status = 'Fail'
                    log_test_result("Verify that the user is able to complete a successful login", login_btn_status)
            else:
                login_password_input_status = 'Fail'
                log_test_result("Verify that user should able to enter password successfully",
                                login_password_input_status)
        else:
            login_email_input_status = 'Fail'
            log_test_result("Verify that user should able to enter email successfully ", login_email_input_status)

    else:
        entry_login_link_status = 'Fail'
        log_test_result("Verify that upon tapping login link user should navigate to login screen",
                        entry_login_link_status)


def log_test_result(test_name, status):
    csv_file = "/Users/mac/Documents/Python_Projects/DBE_Project/Results/Login_results.csv"
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
    pytest.Login_with_email()