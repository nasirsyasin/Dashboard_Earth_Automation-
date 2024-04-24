import requests


def make_authenticated_request(api_url, bearer_token):
    headers = {
        'Authorization': f'Bearer {bearer_token}',
        'Content-Type': 'application/json',  # Adjust content type if needed
    }

    try:
        response = requests.get(api_url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print("Request successful. Response:")
            print(response.json())
        else:
            print(f"Error: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


folder_api_url = 'https://api.zephyrscale.smartbear.com/v2/folders/'
api_url = 'https://api.zephyrscale.smartbear.com/v2/testcycles/DT-R60'
api_url_teststatus = 'https://api.zephyrscale.smartbear.com/v2/statuses/5792475'
testcase_execution_api = 'https://api.zephyrscale.smartbear.com/v2/testexecutions'
file_path = '/Users/mac/Documents/Python_Projects/DBE_Project/token.txt'

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read the API token from the file
    bearer_token = file.read().strip()

# Call the function to make authenticated request
make_authenticated_request(api_url, bearer_token)

payload = {
    "projectKey": "DT",
    "testCaseKey": "DT-T71",
    "testCycleKey": "DT-R60",
    "statusName": "Fail",
    "testScriptResults": [
        {
            "statusName": "Un Executed",
            "actualEndDate": None,
            "actualResult": None
        }
    ],
    "environmentName": None,
    "actualEndDate": None,
    "executionTime": None,
    "executedById": "61cda917ce3652006a786500",
    "assignedToId": "61cda917ce3652006a786500",
    "comment": "Test executed successfully"
}

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {bearer_token}"  # Add authorization header for PUT request
}

response = requests.post(testcase_execution_api, json=payload, headers=headers)

print(response.status_code)
print(response.text)
