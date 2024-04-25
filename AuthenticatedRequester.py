import requests


class AuthenticatedRequester:
    # File path for token
    file_path = '/Users/mac/Documents/Python_Projects/DBE_Project/token.txt'

    # API URL for execution
    api_url = 'https://api.zephyrscale.smartbear.com/v2/testexecutions'

    def __init__(self):
        with open(self.file_path, 'r') as file:
            # Read the API token from the file
            self.bearer_token = file.read().strip()

        self.headers = {
            'Authorization': f'Bearer {self.bearer_token}',
            'Content-Type': 'application/json',  # Adjust content type if needed
        }

    def make_post_request_with_results(self, project_key, test_case_key, test_cycle_key, status_name, test_results):
        payload = self.generate_payload(project_key, test_case_key, test_cycle_key, status_name, test_results)
        try:
            response = requests.post(self.api_url, json=payload, headers=self.headers)
            print(response.status_code)
            print(response.text)
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    @staticmethod
    def generate_payload(project_key, test_case_key, test_cycle_key, status_name, test_results):
        # Define default parameters
        payload = {
            "projectKey": project_key,
            "testCaseKey": test_case_key,
            "testCycleKey": test_cycle_key,
            "statusName": status_name,
            "testScriptResults": test_results,
            "environmentName": None,
            "actualEndDate": None,
            "executionTime": None,
            "executedById": "61cda917ce3652006a786500",
            "assignedToId": "61cda917ce3652006a786500",
            "comment": "Testing"
        }
        return payload
