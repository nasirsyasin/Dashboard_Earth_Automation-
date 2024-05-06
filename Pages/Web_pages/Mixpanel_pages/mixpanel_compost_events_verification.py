import pytest

from Pages.Web_pages.Analytics_zephyr_results import post_results_to_zephyr
from csv_comparison import compare_csv_by_column

predefine_ewaste_events = "/Users/mac/Documents/Python_Projects/DBE_Project/Mixpanel_Results/predefine_compost_events.csv"
mixpanel_events = "/Users/mac/Documents/Python_Projects/DBE_Project/Mixpanel_Results/mixpanel_events.csv"
mixpanel_compost_events_results = "/Users/mac/Documents/Python_Projects/DBE_Project/Mixpanel_Results/compost_events_results.csv"
column_1 = "Event Name"
column_2 = "test_case_key"


def test_compost_events_verification():
    compare_csv_by_column(predefine_ewaste_events, mixpanel_events, column_1, column_2, mixpanel_compost_events_results)
    post_results_to_zephyr(mixpanel_compost_events_results)

# if __name__ == "__main__":
#     pytest.main()
#     pytest.test_compost_events_verification()
