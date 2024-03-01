import pytest
from csv_comparison import compare_csv_by_column

predefine_ewaste_events = "/Users/mac/Documents/Python_Projects/DBE_Project/Mixpanel_Results/predefine_ewaste_events.csv"
mixpanel_events = "/Users/mac/Documents/Python_Projects/DBE_Project/Mixpanel_Results/mixpanel_events.csv"
mixpanel_ewaste_events_results = "/Users/mac/Documents/Python_Projects/DBE_Project/Mixpanel_Results/ewaste_events_results.csv"
column_1 = "Event Name"


def test_ewaste_events_verification():
    compare_csv_by_column(predefine_ewaste_events, mixpanel_events, column_1, mixpanel_ewaste_events_results)


# if __name__ == "__main__":
#     pytest.main()
#     pytest.test_ewaste_events_verification()
