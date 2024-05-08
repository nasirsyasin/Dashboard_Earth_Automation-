from Pages.Web_pages.Analytics_zephyr_results import post_results_to_zephyr
from Pages.Web_pages.csv_comparison import compare_csv_by_column


class CompostEventsVerification:
    def __init__(self):
        self.predefine_ewaste_events = "/Users/mac/Documents/Python_Projects/DBE_Project/Mixpanel_Results/predefine_compost_events.csv"
        self.mixpanel_events = "/Users/mac/Documents/Python_Projects/DBE_Project/Mixpanel_Results/mixpanel_events.csv"
        self.mixpanel_compost_events_results = "/Users/mac/Documents/Python_Projects/DBE_Project/Mixpanel_Results/compost_events_results.csv"
        self.column_1 = "Event Name"
        self.column_2 = "test_case_key"

    def verify_compost_events(self):
        compare_csv_by_column(self.predefine_ewaste_events, self.mixpanel_events, self.column_1, self.column_2,
                              self.mixpanel_compost_events_results)
        post_results_to_zephyr(self.mixpanel_compost_events_results)

# if __name__ == "__main__":
#     compost_verification = CompostEventsVerification()
#     compost_verification.verify_compost_events()
#     pytest.main()
