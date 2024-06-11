import time

import pytest

from Pages.Web_pages.Mixpanel_pages.MixpanelAnalyticsExecution import MixpanelAnalyticsExecution
from Tests.Mobile_Tests.Allow_Notify import Allow_Notify
from Tests.Mobile_Tests.AppRefresh import AppRefresh
from Tests.Mobile_Tests.Login_with_email import Login_with_email
from Tests.Mobile_Tests.Sign_up_with_email import Sign_up_with_email
from Tests.Mobile_Tests.Ewaste_flow import Ewaste_flow
import csv
from Tests.Mobile_Tests.TrackActions import TrackActions
from Tests.Mobile_Tests.compost_mvp_flow import compost_mvp_flow


class test_suite:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(test_suite, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        pass

    @pytest.mark.csv
    def test_login(self):
        exe_login = Login_with_email()
        if exe_login.test_login_with_email():
            Login_with_email_status = "Pass"
            log_test_result("Verify that user should be login successfully ",
                            Login_with_email_status)

        else:
            Login_with_email_status = "Fail"
            log_test_result("Verify that user should be login successfully",
                            Login_with_email_status)

    @pytest.mark.csv
    def test_signup_email(self):
        exe_signup = Sign_up_with_email()
        if exe_signup.test_signup_with_email():
            Signup_with_email_status = "Pass"
            log_test_result("Verify that user account should be created successfully ",
                            Signup_with_email_status)

        else:
            Signup_with_email_status = "Fail"
            log_test_result("Verify that user account should be created successfully",
                            Signup_with_email_status)

    @pytest.mark.csv
    def test_AllowNotify(self):
        exe_al = Allow_Notify()
        if exe_al.test_Allow_notify():
            test_allowNotification_status = "Pass"
            log_test_result("Verify that Allow Notif button should be tapped successfully ",
                            test_allowNotification_status)

        else:
            test_allowNotification_status = "Fail"
            log_test_result("Verify that Allow Notif button should be tapped successfully ",
                            test_allowNotification_status)

    @pytest.mark.csv
    def test_trackAction(self):
        exe_ta = TrackActions()
        if exe_ta.test_TrackAction():
            test_TrackAction_status = "Pass"
            log_test_result("Verify that tooltips and track action button should be performed successfully ",
                            test_TrackAction_status)

        else:
            test_TrackAction_status = "Fail"
            log_test_result("Verify that tooltips and track action button should be performed successfully",
                            test_TrackAction_status)

    @pytest.mark.csv
    def test_compost(self):
        exe_com = compost_mvp_flow()
        if exe_com.test_compost_mvp_screens():
            compost_mvp_status = "Pass"
            log_test_result("Verify that compost_mvp should be performed successfully",
                            compost_mvp_status)

        else:
            compost_mvp_status = "Fail"
            log_test_result("Verify that compost_mvp should be performed successfully",
                            compost_mvp_status)

    @pytest.mark.csv
    def test_ewaste(self):
        exe_ew = Ewaste_flow()
        if exe_ew.test_Ewaste():
            Execute_ewaste_events_verif_status = "Pass"
            log_test_result("Verify that Ewaste events should be verified successfully",
                            Execute_ewaste_events_verif_status)

        else:
            Execute_ewaste_events_verif_status = "Fail"
            log_test_result("Verify that Ewaste events should be verified successfully",
                            Execute_ewaste_events_verif_status)

    @pytest.mark.csv
    def mixpanel_export(self):
        mxp_ana = MixpanelAnalyticsExecution()
        if mxp_ana.export_events():
            Execute_mxp_events_verif_status = "Pass"
            log_test_result("Verify that Mixpanel Analytics Executed successfully",
                            Execute_mxp_events_verif_status)

        else:
            Execute_mxp_events_verif_status = "Fail"
            log_test_result("Verify that Mixpanel Analytics Executed successfully",
                            Execute_mxp_events_verif_status)

    @pytest.mark.csv
    def compost_verify(self):
        mxp_cmp = MixpanelAnalyticsExecution()
        if mxp_cmp.compost_result():
            Execute_mxp_events_verif_status = "Pass"
            log_test_result("Verify that Mixpanel Compost Analytics Executed successfully",
                            Execute_mxp_events_verif_status)

        else:
            Execute_mxp_events_verif_status = "Fail"
            log_test_result("Verify that Mixpanel Compost Analytics Executed successfully",
                            Execute_mxp_events_verif_status)

    @pytest.mark.csv
    def ewaste_verify(self):
        mxp_ew = MixpanelAnalyticsExecution()
        if mxp_ew.ewaste_result():
            Execute_mxp_events_verif_status = "Pass"
            log_test_result("Verify that Mixpanel Ewaste Analytics Executed successfully",
                            Execute_mxp_events_verif_status)

        else:
            Execute_mxp_events_verif_status = "Fail"
            log_test_result("Verify that Mixpanel Ewaste Analytics Executed successfully",
                            Execute_mxp_events_verif_status)

    @pytest.mark.csv
    def refresh_app(self):
        mxp_ew = AppRefresh()
        mxp_ew.app_refresh()

    @pytest.mark.csv
    def i_allow_app(self):
        i_all = Allow_Notify()
        i_all.test_i_Allow()

    @pytest.mark.csv
    def test_tooltips(self):
        exe_ta = TrackActions()
        exe_ta.test_tooltip()


def log_test_result(test_name, status):
    csv_file = "/Users/mac/Documents/Python_Projects/DBE_Project/Results/Test_suit_results.csv"
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
    run = test_suite()
    # run.test_signup_email()
    run.test_AllowNotify()
    run.test_trackAction()
    # run.test_compost()
    # run.test_ewaste()
    # run.mixpanel_export()
    # run.compost_verify()
    # run.ewaste_verify()
