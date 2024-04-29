import time
import pytest
from Pages.Mobile_pages.eWest_page.EwastePage import EwastePage
import csv
from TestExecutionManager import TestExecutionManager, customize_test_step_results


class Ewaste_flow:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Ewaste_flow, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        pass

    @pytest.mark.csv
    def test_Ewaste(self):
        ew = EwastePage()
        if ew.ewaste_action_btn():
            ewaste_action_btn_status = 'Pass'
            # test_case_key = "DT-T255"  # Assuming test case key is constant for this example
            # custom_test_step_results = customize_test_step_results(test_case_key=test_case_key)
            # test_manager.make_post_request_with_results(test_case_key=test_case_key,
            #                                             status_name=ewaste_action_btn_status,
            #                                             test_step_results=custom_test_step_results
            #                                             )
            log_test_result("Verify that Ewaste action button should be tapped successfully",
                            ewaste_action_btn_status)
            time.sleep(5)
            if ew.ewaste_no_btn():
                ewaste_no_btn_status = 'Pass'
                # test_case_key = "DT-T255"  # Assuming test case key is constant for this example
                # custom_test_step_results = customize_test_step_results(test_case_key=test_case_key)
                # test_manager.make_post_request_with_results(test_case_key=test_case_key,
                #                                             status_name=ewaste_action_btn_status,
                #                                             test_step_results=custom_test_step_results
                #                                             )
                log_test_result("Verify that Ewaste NO button should be tapped successfully ", ewaste_no_btn_status)
                time.sleep(5)

                if ew.ewaste_no_arrow():
                    ewaste_no_arrow_status = 'Pass'
                    # test_case_key = "DT-T255"  # Assuming test case key is constant for this example
                    # custom_test_step_results = customize_test_step_results(test_case_key=test_case_key)
                    # test_manager.make_post_request_with_results(test_case_key=test_case_key,
                    #                                             status_name=ewaste_action_btn_status,
                    #                                             test_step_results=custom_test_step_results
                    #                                             )
                    log_test_result("Verify that Ewaste NO flow arrow  should be tapped successfully",
                                    ewaste_no_arrow_status)
                    time.sleep(5)

                    if ew.ewaste_action_btn_not_sure():
                        ewaste_action_btn_not_sure_status = 'Pass'
                        # test_case_key = "DT-T255"  # Assuming test case key is constant for this example
                        # custom_test_step_results = customize_test_step_results(test_case_key=test_case_key)
                        # test_manager.make_post_request_with_results(test_case_key=test_case_key,
                        #                                             status_name=ewaste_action_btn_status,
                        #                                             test_step_results=custom_test_step_results
                        #                                             )
                        log_test_result("Verify that Ewaste action button should be tapped again",
                                        ewaste_action_btn_not_sure_status)
                        time.sleep(5)

                        if ew.ewaste_yes_btn():
                            ewaste_yes_btn_status = 'Pass'
                            # test_case_key = "DT-T255"  # Assuming test case key is constant for this example
                            # custom_test_step_results = customize_test_step_results(test_case_key=test_case_key)
                            # test_manager.make_post_request_with_results(test_case_key=test_case_key,
                            #                                             status_name=ewaste_action_btn_status,
                            #                                             test_step_results=custom_test_step_results
                            #                                             )
                            log_test_result("Verify that ewaste_yes_btn should be tapped successful",
                                            ewaste_yes_btn_status)
                            time.sleep(5)

                            if ew.ewaste_yes_arrow():
                                ewaste_yes_arrow_status = 'Pass'
                                test_case_key = "DT-T384"  # Assuming test case key is constant for this example
                                custom_test_step_results = customize_test_step_results(test_case_key=test_case_key)
                                test_manager.make_post_request_with_results(test_case_key=test_case_key,
                                                                            status_name=ewaste_action_btn_status,
                                                                            test_step_results=custom_test_step_results
                                                                            )
                                log_test_result("Verify that ewaste_yes_arrow should be tapped successful",
                                                ewaste_yes_arrow_status)
                                time.sleep(5)

                                if ew.ewaste_map_link():
                                    ewaste_map_link_status = 'Pass'
                                    # test_case_key = "DT-T255"  # Assuming test case key is constant for this example
                                    # custom_test_step_results = customize_test_step_results(test_case_key=test_case_key)
                                    # test_manager.make_post_request_with_results(test_case_key=test_case_key,
                                    #                                             status_name=ewaste_action_btn_status,
                                    #                                             test_step_results=custom_test_step_results
                                    #                                             )
                                    log_test_result("Verify that ewaste_map_link should be tapped successful",
                                                    ewaste_map_link_status)
                                    time.sleep(5)

                                    if ew.ewaste_map_details_cross():
                                        ewaste_map_details_cross_status = 'Pass'
                                        # test_case_key = "DT-T255"  # Assuming test case key is constant for this example
                                        # custom_test_step_results = customize_test_step_results(
                                        #     test_case_key=test_case_key)
                                        # test_manager.make_post_request_with_results(test_case_key=test_case_key,
                                        #                                             status_name=ewaste_action_btn_status,
                                        #                                             test_step_results=custom_test_step_results
                                        #                                             )
                                        log_test_result(
                                            "Verify that ewaste_map_details_cross should be tapped successful",
                                            ewaste_map_details_cross_status)
                                        time.sleep(5)

                                        if ew.ewaste_photo_cap_btn():
                                            ewaste_photo_cap_btn_status = 'Pass'
                                            # test_case_key = "DT-T255"  # Assuming test case key is constant for this example
                                            # custom_test_step_results = customize_test_step_results(
                                            #     test_case_key=test_case_key)
                                            # test_manager.make_post_request_with_results(test_case_key=test_case_key,
                                            #                                             status_name=ewaste_action_btn_status,
                                            #                                             test_step_results=custom_test_step_results
                                            #                                             )
                                            log_test_result(
                                                "Verify that ewaste_photo_cap_btn should be tapped successful",
                                                ewaste_photo_cap_btn_status)
                                            time.sleep(5)
                                            time.sleep(5)
                                            if ew.ewaste_cam_plus_btn():
                                                ewaste_cam_plus_btn_status = 'Pass'
                                                # test_case_key = "DT-T255"  # Assuming test case key is constant for this example
                                                # custom_test_step_results = customize_test_step_results(
                                                #     test_case_key=test_case_key)
                                                # test_manager.make_post_request_with_results(test_case_key=test_case_key,
                                                #                                             status_name=ewaste_cam_plus_btn_status,
                                                #                                             test_step_results=custom_test_step_results
                                                #                                             )
                                                log_test_result(
                                                    "Verify that cam_plus_btn should be tapped successful",
                                                    ewaste_cam_plus_btn_status)
                                                time.sleep(5)
                                                if ew.ewaste_camera_btn():
                                                    ewaste_camera_btn_status = 'Pass'
                                                    # test_case_key = "DT-T255"  # Assuming test case key is constant for this example
                                                    # custom_test_step_results = customize_test_step_results(
                                                    #     test_case_key=test_case_key)
                                                    # test_manager.make_post_request_with_results(
                                                    #     test_case_key=test_case_key,
                                                    #     status_name=ewaste_action_btn_status,
                                                    #     test_step_results=custom_test_step_results
                                                    #     )
                                                    log_test_result(
                                                        "Verify that ewaste_camera_btn should be tapped successful",
                                                        ewaste_camera_btn_status)
                                                    time.sleep(5)

                                                    if ew.ewaste_camera_permission():
                                                        ewaste_camera_permission_status = 'Pass'
                                                        # test_case_key = "DT-T255"  # Assuming test case key is constant for this example
                                                        # custom_test_step_results = customize_test_step_results(
                                                        #     test_case_key=test_case_key)
                                                        # test_manager.make_post_request_with_results(
                                                        #     test_case_key=test_case_key,
                                                        #     status_name=ewaste_action_btn_status,
                                                        #     test_step_results=custom_test_step_results
                                                        # )
                                                        log_test_result(
                                                            "Verify that ewaste_camera_permission should be tapped successful",
                                                            ewaste_camera_permission_status)
                                                        time.sleep(5)

                                                        if ew.ewaste_camera_capture():
                                                            ewaste_camera_capture_status = 'Pass'
                                                            # test_case_key = "DT-T255"  # Assuming test case key is constant for this example
                                                            # custom_test_step_results = customize_test_step_results(
                                                            #     test_case_key=test_case_key)
                                                            # test_manager.make_post_request_with_results(
                                                            #     test_case_key=test_case_key,
                                                            #     status_name=ewaste_action_btn_status,
                                                            #     test_step_results=custom_test_step_results
                                                            # )
                                                            log_test_result(
                                                                "Verify that ewaste_camera_capture should be tapped successful",
                                                                ewaste_camera_capture_status)
                                                            time.sleep(5)

                                                            if ew.save_ok_photo():
                                                                save_ok_photo_status = 'Pass'
                                                                # test_case_key = "DT-T255"  # Assuming test case key is constant for this example
                                                                # custom_test_step_results = customize_test_step_results(
                                                                #     test_case_key=test_case_key)
                                                                # test_manager.make_post_request_with_results(
                                                                #     test_case_key=test_case_key,
                                                                #     status_name=ewaste_action_btn_status,
                                                                #     test_step_results=custom_test_step_results
                                                                # )
                                                                log_test_result(
                                                                    "Verify that save_ok_photo should be tapped successful",
                                                                    save_ok_photo_status)
                                                                time.sleep(5)

                                                                if ew.verify_complete_btn():
                                                                    verify_complete_btn_status = 'Pass'
                                                                    # test_case_key = "DT-T255"  # Assuming test case key is constant for this example
                                                                    # custom_test_step_results = customize_test_step_results(
                                                                    #     test_case_key=test_case_key)
                                                                    # test_manager.make_post_request_with_results(
                                                                    #     test_case_key=test_case_key,
                                                                    #     status_name=ewaste_action_btn_status,
                                                                    #     test_step_results=custom_test_step_results
                                                                    # )
                                                                    log_test_result(
                                                                        "Verify that verify_complete_btn should be tapped successful",
                                                                        verify_complete_btn_status)
                                                                    time.sleep(5)

                                                                    if ew.completed_action_btn():
                                                                        completed_action_btn_status = 'Pass'
                                                                        test_case_key = "DT-T381"  # Assuming test case key is constant for this example
                                                                        custom_test_step_results = customize_test_step_results(
                                                                            test_case_key=test_case_key)
                                                                        test_manager.make_post_request_with_results(
                                                                            test_case_key=test_case_key,
                                                                            status_name=ewaste_action_btn_status,
                                                                            test_step_results=custom_test_step_results
                                                                        )
                                                                        log_test_result(
                                                                            "Verify that completed_action_btn should be tapped successful",
                                                                            completed_action_btn_status)

                                                                    else:
                                                                        completed_action_btn_status = 'Fail'
                                                                        test_case_key = "DT-T381"  # Assuming test case key is constant for this example
                                                                        custom_test_step_results = customize_test_step_results(
                                                                            test_case_key=test_case_key)
                                                                        test_manager.make_post_request_with_results(
                                                                            test_case_key=test_case_key,
                                                                            status_name=ewaste_action_btn_status,
                                                                            test_step_results=custom_test_step_results
                                                                        )
                                                                        log_test_result(
                                                                            "Verify that completed_action_btn should be tapped successful",
                                                                            completed_action_btn_status)

                                                                else:
                                                                    verify_complete_btn_status = 'Fail'
                                                                    # test_case_key = "DT-T255"  # Assuming test case key is constant for this example
                                                                    # custom_test_step_results = customize_test_step_results(
                                                                    #     test_case_key=test_case_key)
                                                                    # test_manager.make_post_request_with_results(
                                                                    #     test_case_key=test_case_key,
                                                                    #     status_name=ewaste_action_btn_status,
                                                                    #     test_step_results=custom_test_step_results
                                                                    # )
                                                                    log_test_result(
                                                                        "Verify that verify_complete_btn should be tapped successful",
                                                                        verify_complete_btn_status)

                                                            else:
                                                                save_ok_photo_status = 'Fail'
                                                                # test_case_key = "DT-T255"  # Assuming test case key is constant for this example
                                                                # custom_test_step_results = customize_test_step_results(
                                                                #     test_case_key=test_case_key)
                                                                # test_manager.make_post_request_with_results(
                                                                #     test_case_key=test_case_key,
                                                                #     status_name=ewaste_action_btn_status,
                                                                #     test_step_results=custom_test_step_results
                                                                # )
                                                                log_test_result(
                                                                    "Verify that save_ok_photo should be tapped successful",
                                                                    save_ok_photo_status)

                                                        else:
                                                            ewaste_camera_capture_status = 'Fail'
                                                            # test_case_key = "DT-T255"  # Assuming test case key is constant for this example
                                                            # custom_test_step_results = customize_test_step_results(
                                                            #     test_case_key=test_case_key)
                                                            # test_manager.make_post_request_with_results(
                                                            #     test_case_key=test_case_key,
                                                            #     status_name=ewaste_action_btn_status,
                                                            #     test_step_results=custom_test_step_results
                                                            # )
                                                            log_test_result(
                                                                "Verify that ewaste_camera_capture should be tapped successful",
                                                                ewaste_camera_capture_status)

                                                    else:
                                                        ewaste_camera_permission_status = 'Fail'
                                                        # test_case_key = "DT-T255"  # Assuming test case key is constant for this example
                                                        # custom_test_step_results = customize_test_step_results(
                                                        #     test_case_key=test_case_key)
                                                        # test_manager.make_post_request_with_results(
                                                        #     test_case_key=test_case_key,
                                                        #     status_name=ewaste_action_btn_status,
                                                        #     test_step_results=custom_test_step_results
                                                        # )
                                                        log_test_result(
                                                            "Verify that ewaste_camera_permission should be tapped successful",
                                                            ewaste_camera_permission_status)

                                                else:
                                                    ewaste_camera_btn_status = 'Fail'
                                                    # test_case_key = "DT-T255"  # Assuming test case key is constant for this example
                                                    # custom_test_step_results = customize_test_step_results(
                                                    #     test_case_key=test_case_key)
                                                    # test_manager.make_post_request_with_results(
                                                    #     test_case_key=test_case_key,
                                                    #     status_name=ewaste_action_btn_status,
                                                    #     test_step_results=custom_test_step_results
                                                    #     )
                                                    log_test_result(
                                                        "Verify that ewaste_camera_btn should be tapped successful",
                                                        ewaste_camera_btn_status)

                                            else:
                                                ewaste_cam_plus_btn_status = 'Fail'
                                                # test_case_key = "DT-T255"  # Assuming test case key is constant for this example
                                                # custom_test_step_results = customize_test_step_results(
                                                #     test_case_key=test_case_key)
                                                # test_manager.make_post_request_with_results(test_case_key=test_case_key,
                                                #                                             status_name=ewaste_cam_plus_btn_status,
                                                #                                             test_step_results=custom_test_step_results
                                                #                                             )
                                                log_test_result(
                                                    "Verify that cam_plus_btn should be tapped successful",
                                                    ewaste_cam_plus_btn_status)

                                        else:
                                            ewaste_photo_cap_btn_status = 'Fail'
                                            # test_case_key = "DT-T255"  # Assuming test case key is constant for this example
                                            # custom_test_step_results = customize_test_step_results(
                                            #     test_case_key=test_case_key)
                                            # test_manager.make_post_request_with_results(test_case_key=test_case_key,
                                            #                                             status_name=ewaste_action_btn_status,
                                            #                                             test_step_results=custom_test_step_results
                                            #                                             )
                                            log_test_result(
                                                "Verify that ewaste_photo_cap_btn should be tapped successful",
                                                ewaste_photo_cap_btn_status)

                                    else:
                                        ewaste_map_details_cross_status = 'Fail'
                                        # test_case_key = "DT-T255"  # Assuming test case key is constant for this example
                                        # custom_test_step_results = customize_test_step_results(
                                        #     test_case_key=test_case_key)
                                        # test_manager.make_post_request_with_results(test_case_key=test_case_key,
                                        #                                             status_name=ewaste_action_btn_status,
                                        #                                             test_step_results=custom_test_step_results
                                        #                                             )
                                        log_test_result(
                                            "Verify that ewaste_map_details_cross should be tapped successful",
                                            ewaste_map_details_cross_status)

                                else:
                                    ewaste_map_link_status = 'Fail'
                                    # test_case_key = "DT-T255"  # Assuming test case key is constant for this example
                                    # custom_test_step_results = customize_test_step_results(test_case_key=test_case_key)
                                    # test_manager.make_post_request_with_results(test_case_key=test_case_key,
                                    #                                             status_name=ewaste_action_btn_status,
                                    #                                             test_step_results=custom_test_step_results
                                    #                                             )
                                    log_test_result("Verify that ewaste_map_link should be tapped successful",
                                                    ewaste_map_link_status)
                            else:
                                ewaste_yes_arrow_status = 'Fail'
                                test_case_key = "DT-T384"  # Assuming test case key is constant for this example
                                custom_test_step_results = customize_test_step_results(test_case_key=test_case_key)
                                test_manager.make_post_request_with_results(test_case_key=test_case_key,
                                                                            status_name=ewaste_action_btn_status,
                                                                            test_step_results=custom_test_step_results
                                                                            )
                                log_test_result("Verify that ewaste_yes_arrow should be tapped successful",
                                                ewaste_yes_arrow_status)

                        else:
                            ewaste_yes_btn_status = 'Fail'
                            # test_case_key = "DT-T255"  # Assuming test case key is constant for this example
                            # custom_test_step_results = customize_test_step_results(test_case_key=test_case_key)
                            # test_manager.make_post_request_with_results(test_case_key=test_case_key,
                            #                                             status_name=ewaste_action_btn_status,
                            #                                             test_step_results=custom_test_step_results
                            #                                             )
                            log_test_result("Verify that ewaste_yes_btn should be tapped successful",
                                            ewaste_yes_btn_status)

                    else:
                        ewaste_action_btn_not_sure_status = 'Fail'
                        # test_case_key = "DT-T255"  # Assuming test case key is constant for this example
                        # custom_test_step_results = customize_test_step_results(test_case_key=test_case_key)
                        # test_manager.make_post_request_with_results(test_case_key=test_case_key,
                        #                                             status_name=ewaste_action_btn_status,
                        #                                             test_step_results=custom_test_step_results
                        #                                             )
                        log_test_result("Verify that Ewaste action button should be tapped again",
                                        ewaste_action_btn_not_sure_status)
                else:
                    ewaste_no_arrow_status = 'Fail'
                    # test_case_key = "DT-T255"  # Assuming test case key is constant for this example
                    # custom_test_step_results = customize_test_step_results(test_case_key=test_case_key)
                    # test_manager.make_post_request_with_results(test_case_key=test_case_key,
                    #                                             status_name=ewaste_action_btn_status,
                    #                                             test_step_results=custom_test_step_results
                    #                                             )
                    log_test_result("Verify that Ewaste NO flow arrow  should be tapped successfully",
                                    ewaste_no_arrow_status)
            else:
                ewaste_no_btn_status = 'Fail'
                # test_case_key = "DT-T255"  # Assuming test case key is constant for this example
                # custom_test_step_results = customize_test_step_results(test_case_key=test_case_key)
                # test_manager.make_post_request_with_results(test_case_key=test_case_key,
                #                                             status_name=ewaste_action_btn_status,
                #                                             test_step_results=custom_test_step_results
                #                                             )
                log_test_result("Verify that Ewaste NO button should be tapped successfully", ewaste_no_btn_status)

        else:
            ewaste_action_btn_status = 'Fail'
            # test_case_key = "DT-T255"  # Assuming test case key is constant for this example
            # custom_test_step_results = customize_test_step_results(test_case_key=test_case_key)
            # test_manager.make_post_request_with_results(test_case_key=test_case_key,
            #                                             status_name=ewaste_action_btn_status,
            #                                             test_step_results=custom_test_step_results
            #                                             )
            log_test_result("Verify that Ewaste action button should be tapped successfully",
                            ewaste_action_btn_status)


test_manager = TestExecutionManager()


def log_test_result(test_name, status):
    csv_file = "/Users/mac/Documents/Python_Projects/DBE_Project/Results/Ewaste_results.csv"
    csv_headers = ["Tests Summary", "Status"]
    csv_rows = [{"Tests Summary": test_name, "Status": status}]  # Wrapping rows in a list of dictionaries

    with open(csv_file, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=csv_headers)

        # Check if the file is empty to write the header
        if file.tell() == 0:
            writer.writeheader()

        writer.writerows(csv_rows)

