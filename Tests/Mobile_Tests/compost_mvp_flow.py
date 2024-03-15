import pytest
import csv
from Pages.Mobile_pages.compost_page.MVPCompostPage import MVPCompostPage


@pytest.mark.csv
def compost_mvp_screens():
    mvp_c = MVPCompostPage()
    if mvp_c.mvp_compost_btn():
        mvp_get_started_btn_status = 'Pass'
        log_test_result("Verify that mvp_get_started_btn is tapped ", mvp_get_started_btn_status)

        if mvp_c.fork_1_yes_btn():
            fork_1_yes_btn_status = 'Pass'
            log_test_result("Verify that fork_1_yes_btn is tapped ", fork_1_yes_btn_status)
            if mvp_c.fork_2_yes_arrow():
                fork_2_yes_arrow_status = 'Pass'
                log_test_result("Verify that fork_2_yes_arrow is tapped ", fork_2_yes_arrow_status)

                if mvp_c.fork_back_arrow_1():
                    fork_back_arrow_1_status = 'Pass'
                    log_test_result("Verify that fork_back_arrow_1 is tapped ",
                                    fork_back_arrow_1_status)
                    if mvp_c.fork_back_arrow_2():
                        fork_back_arrow_2_status = 'Pass'
                        log_test_result("Verify that fork_back_arrow_2 is tapped ", fork_back_arrow_2_status)

                        if mvp_c.fork_1_no_btn():
                            fork_1_no_btn_status = 'Pass'
                            log_test_result("Verify that fork_1_no_btn is tapped ",
                                            fork_1_no_btn_status)
                            if mvp_c.fork_2_no_arrow():
                                fork_2_no_arrow_status = 'Pass'
                                log_test_result("Verify that fork_2_no_arrow is tapped ", fork_2_no_arrow_status)
                                if mvp_c.fork_3_no_arrow():
                                    fork_3_no_arrow_status = 'Pass'
                                    log_test_result("Verify that fork_3_no_arrow is tapped ", fork_3_no_arrow_status)
                                    if mvp_c.fork_4_no_open_dropdown():
                                        fork_4_no_open_dropdown_status = 'Pass'
                                        log_test_result("Verify that fork_4_no_open_dropdown is tapped ",
                                                        fork_4_no_open_dropdown_status)
                                        if mvp_c.fork_4_no_closed_dropdown():
                                            fork_4_no_closed_dropdown_status = 'Pass'
                                            log_test_result("Verify that fork_4_no_closed_dropdown is tapped ",
                                                            fork_4_no_closed_dropdown_status)
                                            if mvp_c.fork_4_no_arrow():
                                                fork_4_no_arrow_status = 'Pass'
                                                log_test_result("Verify that fork_4_no_arrow is tapped ",
                                                                fork_4_no_arrow_status)
                                                if mvp_c.compost_done_tooltip():
                                                    compost_done_tooltip_status = 'Pass'
                                                    log_test_result("Verify that compost_done_tooltip is tapped ",
                                                                    compost_done_tooltip_status)
                                                    if mvp_c.complete_compost_action():
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
