#!/usr/bin/python3

import requests

def get_employee_todo_progress(employee_id):
    # Replace with the actual API endpoint
    api_url = f"https://jsonplaceholder.typicode.com/{employee_id}/todos"

    try:
        response = requests.get(api_url)
        response_data = response.json()

        if response.status_code == 200:
            employee_name = response_data.get("employee_name")
            total_tasks = len(response_data.get("todos"))
            done_tasks = sum(1 for todo in response_data.get("todos") if todo.get("status") == "Done")

            print(f"Employee {employee_name} is done with tasks ({done_tasks}/{total_tasks}):")
            for todo in response_data.get("todos"):
                if todo.get("status") == "Done":
                    print(f"\t{todo.get('title')}")

        else:
            print(f"Error: Unable to retrieve data for employee ID {employee_id}")

    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    employee_id = int(input("Enter the employee ID: "))
    get_employee_todo_progress(employee_id)
