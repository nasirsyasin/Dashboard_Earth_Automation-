import csv
import time
import pytest
from Pages.Mobile_pages.LoginPage import LoginPage
from TestExecutionManager import TestExecutionManager, customize_test_step_results


class Login_with_email:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Login_with_email, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        pass

    @pytest.mark.csv
    def test_login_with_email(self):
        ls = LoginPage()
        if ls.login_link():
            login_link_status = 'Pass'
            test_case_key = "DT-T255"  # Assuming test case key is constant for this example
            custom_test_step_results = customize_test_step_results(test_case_key=test_case_key)
            test_manager.make_post_request_with_results(test_case_key=test_case_key, status_name=login_link_status,
                                                        test_step_results=custom_test_step_results
                                                        )
            log_test_result("Verify that upon tapping login link user should navigate to login screen",
                            login_link_status)

            time.sleep(3)
            if ls.email_input():
                login_email_input_status = 'Pass'
                # test_case_key = "DT-T255"  # Assuming test case key is constant for this example
                # custom_test_step_results = customize_test_step_results(test_case_key=test_case_key)
                # test_manager.make_post_request_with_results(test_case_key=test_case_key, status_name=login_link_status,
                #                                             test_step_results=custom_test_step_results
                #                                             )
                log_test_result("Verify that user should able to enter email successfully ", login_email_input_status)

                if ls.password_input():
                    login_password_input_status = 'Pass'
                    # test_case_key = "DT-T255"  # Assuming test case key is constant for this example
                    # custom_test_step_results = customize_test_step_results(test_case_key=test_case_key)
                    # test_manager.make_post_request_with_results(test_case_key=test_case_key,
                    #                                             status_name=login_password_input_status,
                    #                                             test_step_results=custom_test_step_results
                    #                                             )
                    log_test_result("Verify that user should able to enter password successfully",
                                    login_password_input_status)
                    time.sleep(3)
                    if ls.login_btn():
                        login_btn_status = 'Pass'
                        test_case_key = "DT-T788"  # Assuming test case key is constant for this example
                        custom_test_step_results = customize_test_step_results(test_case_key=test_case_key)
                        test_manager.make_post_request_with_results(test_case_key=test_case_key,
                                                                    status_name=login_btn_status,
                                                                    test_step_results=custom_test_step_results
                                                                    )
                        log_test_result("Verify that the user is able to complete a successful login", login_btn_status)

                    else:
                        login_btn_status = 'Fail'
                        test_case_key = "DT-T788"  # Assuming test case key is constant for this example
                        custom_test_step_results = customize_test_step_results(test_case_key=test_case_key)
                        test_manager.make_post_request_with_results(test_case_key=test_case_key,
                                                                    status_name=login_btn_status,
                                                                    test_step_results=custom_test_step_results
                                                                    )
                        log_test_result("Verify that the user is able to complete a successful login", login_btn_status)

                else:
                    login_password_input_status = 'Fail'
                    # test_case_key = "DT-T255"  # Assuming test case key is constant for this example
                    # custom_test_step_results = customize_test_step_results(test_case_key=test_case_key)
                    # test_manager.make_post_request_with_results(test_case_key=test_case_key,
                    #                                             status_name=login_password_input_status,
                    #                                             test_step_results=custom_test_step_results
                    #                                             )
                    log_test_result("Verify that user should able to enter password successfully",
                                    login_password_input_status)
            else:
                login_email_input_status = 'Fail'
                # test_case_key = "DT-T255"  # Assuming test case key is constant for this example
                # custom_test_step_results = customize_test_step_results(test_case_key=test_case_key)
                # test_manager.make_post_request_with_results(test_case_key=test_case_key,
                #                                             status_name=login_email_input_status,
                #                                             test_step_results=custom_test_step_results
                #                                             )
                log_test_result("Verify that user should able to enter email successfully ", login_email_input_status)

        else:
            login_link_status = 'Fail'
            test_case_key = "DT-T255"  # Assuming test case key is constant for this example
            custom_test_step_results = customize_test_step_results(test_case_key=test_case_key)
            test_manager.make_post_request_with_results(test_case_key=test_case_key, status_name=login_link_status,
                                                        test_step_results=custom_test_step_results
                                                        )
            log_test_result("Verify that upon tapping login link user should navigate to login screen",
                            login_link_status)


test_manager = TestExecutionManager()


def log_test_result(test_name, status):
    csv_file = "/Users/mac/Documents/Python_Projects/DBE_Project/Results/Login_results.csv"
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
    run = Login_with_email()
    run.test_login_with_email()
