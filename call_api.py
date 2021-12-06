from time import sleep
from urllib.parse import urljoin

import requests

BASE_URL = "http://localhost:8004/tasks/"


def main() -> None:
    # Schedule task
    resp = requests.post(BASE_URL, json={"x": 15.5})

    # Fail if task wasn't scheduled successfuly
    if not resp.ok:
        print(f"Request failed: [{resp.status_code}] {resp.text}")
        exit(1)

    # Extract id of the created task and show it to the user
    task_id = resp.json()["task_id"]
    print(f"Id of created task: {task_id}")

    # Task status (and result, if available) is obtained from GET /tasks/{task_id}
    result_url = urljoin(BASE_URL, task_id)

    # Periodically poll server for the result, untill status is different from "PENDING".
    while (resp := requests.get(result_url).json())["status"] == "PENDING":
        print("Task not ready, waiting for 5 seconds...")
        sleep(5)

    # Print result
    print(f"Task status: {resp['status']}")
    print(f"Task result: {resp['result']}")


if __name__ == "__main__":
    main()
