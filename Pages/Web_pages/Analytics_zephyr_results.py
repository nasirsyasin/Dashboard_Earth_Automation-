import csv
from TestExecutionManager import TestExecutionManager, customize_test_step_results


def read_csv_file(file_path):
    """
    Read data from a CSV file and return as a list of dictionaries.
    Assumes the first row contains headers.
    """
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


def post_results_to_zephyr(csv_file):
    # Assuming test_case_key, status_name, and test_step_results are columns in the CSV file
    csv_file_path = csv_file
    test_results = read_csv_file(csv_file_path)

    # Assuming self is an instance of the class where make_post_request_with_results is defined
    for result in test_results:
        custom_test_step_results = customize_test_step_results(test_case_key=result['test_case_key'])
        test_manager.make_post_request_with_results(
            test_case_key=result['test_case_key'],
            status_name=result['Status'],
            test_step_results=custom_test_step_results
        )


test_manager = TestExecutionManager()
