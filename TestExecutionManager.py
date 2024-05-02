from AuthenticatedRequester import AuthenticatedRequester


def get_number_of_steps_for_test_case(test_case_key):
    # Assume you have a dictionary or database table that maps test case keys to their respective number of steps
    test_case_steps_mapping = {
        "DT-T71": 1,
        "DT-T1": 5,
        "DT-T255": 4,
        "DT-T788": 3,
        "DT-T272": 4,
        "DT-T779": 1,
        "DT-T360": 3,
        "DT-T344": 10,
        "DT-T347": 18,
        "DT-T345": 13,
        "DT-T346": 18,
        "DT-T384": 8,
        "DT-T381": 4
        # Add more mappings as needed
    }

    # Return the number of steps for the specified test case key if it exists in the mapping
    return test_case_steps_mapping.get(test_case_key)


def customize_test_step_results(test_case_key=None):
    # Get the number of steps for the specified test case key
    num_steps = get_number_of_steps_for_test_case(test_case_key)

    if num_steps is None:
        print(f"Error: Failed to retrieve the number of steps for the test case {test_case_key}.")
        return []

    # Customize test step results for each step
    test_step_results = []
    for _ in range(num_steps):
        test_step_results.append({
            "statusName": "Not Executed",
            "actualEndDate": None,
            "actualResult": None
        })
    return test_step_results


class TestExecutionManager:
    def __init__(self):
        self.requester = AuthenticatedRequester()

    def make_post_request_with_results(self, test_case_key, status_name,
                                       test_step_results):
        # Call the method to make authenticated POST request with custom test results
        self.requester.make_post_request_with_results(project_key="DT",
                                                      test_case_key=test_case_key,
                                                      test_cycle_key="DT-R69",
                                                      status_name=status_name,
                                                      test_results=test_step_results)

# # Example usage
# if __name__ == "__main__":
#     # Create an instance of TestExecutionManager
#     test_manager = TestExecutionManager()
#
#     # Define custom test step results
#     custom_test_step_results = customize_test_step_results(test_case_key="DT-T1")
#
#     # Call the method to make authenticated POST request with custom test results
#     test_manager.make_post_request_with_results(test_case_key="DT-T1", status_name="Not Executed",
#                                                 test_step_results=custom_test_step_results
#                                                 )
