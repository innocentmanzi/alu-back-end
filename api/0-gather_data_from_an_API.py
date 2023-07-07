#!/usr/bin/python3

import requests

def get_employee_todo_progress(employee_id):
    # Make a GET request to the API endpoint
    response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        todos = response.json()
        
        # Filter completed tasks
        completed_tasks = [todo for todo in todos if todo['completed']]
        total_tasks = len(todos)

        # Get the employee name from the first task
        if todos:
            employee_name = todos[0]['name']
        else:
            employee_name = 'Unknown'

        # Print employee's TODO list progress
        print(f"Employee {employee_name} is done with tasks ({len(completed_tasks)}/{total_tasks}):")

        # Print titles of completed tasks
        for task in completed_tasks:
            print(f"\t{task['title']}")
    else:
        print(f"Error: {response.status_code} - {response.text}")
