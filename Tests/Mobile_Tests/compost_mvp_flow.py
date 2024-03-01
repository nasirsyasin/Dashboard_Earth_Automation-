import pytest
import csv
from Pages.Mobile_pages.compost_page.MVPCompostPage import test_compost_mvp_flow, test_compost_mvp_no_flow, test_compost_complete

mvp_get_started_btn, fork_1_yes_btn, fork_2_yes_arrow, fork_back_arrow_1, fork_back_arrow_2 = test_compost_mvp_flow()
(fork_1_no_btn, fork_2_no_arrow, fork_3_no_arrow, fork_4_no_open_dropdown,
 fork_4_no_closed_dropdown, fork_4_no_arrow) = test_compost_mvp_no_flow()
compost_done_tooltip, complete_compost_action = test_compost_complete()


@pytest.mark.csv
def compost_mvp_screens():
    if mvp_get_started_btn is True:
        mvp_get_started_btn_status = 'Pass'
        log_test_result("Verify that mvp_get_started_btn is tapped ", mvp_get_started_btn_status)

        if fork_1_yes_btn is True:
            fork_1_yes_btn_status = 'Pass'
            log_test_result("Verify that fork_1_yes_btn is tapped ", fork_1_yes_btn_status)
            if fork_2_yes_arrow is True:
                fork_2_yes_arrow_status = 'Pass'
                log_test_result("Verify that fork_2_yes_arrow is tapped ", fork_2_yes_arrow_status)

                if fork_back_arrow_1 is True:
                    fork_back_arrow_1_status = 'Pass'
                    log_test_result("Verify that fork_back_arrow_1 is tapped ",
                                    fork_back_arrow_1_status)
                    if fork_back_arrow_2 is True:
                        fork_back_arrow_2_status = 'Pass'
                        log_test_result("Verify that fork_back_arrow_2 is tapped ", fork_back_arrow_2_status)

                        if fork_1_no_btn is True:
                            fork_1_no_btn_status = 'Pass'
                            log_test_result("Verify that fork_1_no_btn is tapped ",
                                            fork_1_no_btn_status)
                            if fork_2_no_arrow is True:
                                fork_2_no_arrow_status = 'Pass'
                                log_test_result("Verify that fork_2_no_arrow is tapped ", fork_2_no_arrow_status)
                                if fork_3_no_arrow is True:
                                    fork_3_no_arrow_status = 'Pass'
                                    log_test_result("Verify that fork_3_no_arrow is tapped ", fork_3_no_arrow_status)
                                    if fork_4_no_open_dropdown is True:
                                        fork_4_no_open_dropdown_status = 'Pass'
                                        log_test_result("Verify that fork_4_no_open_dropdown is tapped ",
                                                        fork_4_no_open_dropdown_status)
                                        if fork_4_no_closed_dropdown is True:
                                            fork_4_no_closed_dropdown_status = 'Pass'
                                            log_test_result("Verify that fork_4_no_closed_dropdown is tapped ",
                                                            fork_4_no_closed_dropdown_status)
                                            if fork_4_no_arrow is True:
                                                fork_4_no_arrow_status = 'Pass'
                                                log_test_result("Verify that fork_4_no_arrow is tapped ",
                                                                fork_4_no_arrow_status)
                                                if compost_done_tooltip is True:
                                                    compost_done_tooltip_status = 'Pass'
                                                    log_test_result("Verify that compost_done_tooltip is tapped ",
                                                                    compost_done_tooltip_status)
                                                    if complete_compost_action is True:
                                                        complete_compost_action_status = 'Pass'
                                                        log_test_result(
                                                            "Verify that complete_compost_action is tapped ",
                                                            complete_compost_action_status)
                                                    else:
                                                        complete_compost_action_status = 'Fail'
                                                        log_test_result(
                                                            "Verify that complete_compost_action is tapped ",
                                                            complete_compost_action_status)
                                                else:
                                                    compost_done_tooltip_status = 'Fail'
                                                    log_test_result("Verify that compost_done_tooltip is tapped ",
                                                                    compost_done_tooltip_status)
                                            else:
                                                fork_4_no_arrow_status = 'Fail'
                                                log_test_result("Verify that fork_4_no_arrow is tapped ",
                                                                fork_4_no_arrow_status)
                                        else:
                                            fork_4_no_closed_dropdown_status = 'Fail'
                                            log_test_result("Verify that fork_4_no_closed_dropdown is tapped ",
                                                            fork_4_no_closed_dropdown_status)
                                    else:
                                        fork_4_no_open_dropdown_status = 'Fail'
                                        log_test_result("Verify that fork_4_no_open_dropdown is tapped ",
                                                        fork_4_no_open_dropdown_status)
                                else:
                                    fork_3_no_arrow_status = 'Fail'
                                    log_test_result("Verify that fork_3_no_arrow is tapped  ", fork_3_no_arrow_status)
                            else:
                                fork_2_no_arrow_status = 'Fail'
                                log_test_result("Verify that fork_2_no_arrow is tapped  ",
                                                fork_2_no_arrow_status)

                        else:
                            fork_1_no_btn_status = 'Fail'
                            log_test_result("Verify that fork_1_no_btn is tapped ",
                                            fork_1_no_btn_status)

                    else:
                        fork_back_arrow_2_status = 'Fail'
                        log_test_result("Verify that fork_back_arrow_2_status is tapped  ",
                                        fork_back_arrow_2_status)

                else:
                    fork_back_arrow_1_status = 'Fail'
                    log_test_result("Verify that fork_back_arrow_1_status is tapped ",
                                    fork_back_arrow_1_status)
            else:
                fork_2_yes_arrow_status = 'Fail'
                log_test_result("Verify that fork_2_yes_arrow is tapped  ", fork_2_yes_arrow_status)
        else:
            fork_1_yes_btn_status = 'Fail'
            log_test_result("Verify that fork_1_yes_btn is tapped  ",
                            fork_1_yes_btn_status)

    else:
        mvp_get_started_btn_status = 'Fail'
        log_test_result("Verify that mvp_get_started_btn is tapped  ",
                        mvp_get_started_btn_status)


def log_test_result(test_name, status):
    csv_file = "Results/Compost_MVP_Screens.csv"
    csv_headers = ["Compost MVP Test Steps", "Status"]
    csv_rows = [{"Compost MVP Test Steps": test_name, "Status": status}]  # Wrapping rows in a list of dictionaries

    with open(csv_file, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=csv_headers)

        # Check if the file is empty to write the header
        if file.tell() == 0:
            writer.writeheader()

        writer.writerows(csv_rows)


if __name__ == "__main__":
    pytest.main()
