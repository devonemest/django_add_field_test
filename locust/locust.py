import string

from locust import HttpUser, task, between, TaskSet
import random
import json


class Tasks(TaskSet):
    @task(1)
    def get_user(self):
        response = self.client.get(f"/users/{random.randint(1, 900000)}")
        if response.status_code == 200:
            print("Users fetched successfully")
        else:
            print(f"Failed to fetch users: {response.status_code}")


    @task(2)
    def create_new_dummie(self):
        new_dummie = {
          "name": ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)),
          "height": random.uniform(150.0, 190.0),
          "weight": random.uniform(150.0, 190.0)
        }
        headers = {'Content-Type': 'application/json'}
        response = self.client.post("/dummies/", data=json.dumps(new_dummie), headers=headers)

        if response.status_code == 201:
            print("new_dummie created successfully")
        else:
            print(f"Failed to create new_dummie: {response.status_code}")

    @task(3)
    def get_dummie(self):
        response = self.client.get(f"/dummies/{random.randint(1, 900000)}")
        if response.status_code == 200:
            print("dummie fetched successfully")
        else:
            print(f"Failed to fetch dummie: {response.status_code}")


class Tasks(HttpUser):
    tasks = [Tasks]
    wait_time = between(1, 5)

    host = "http://127.0.0.1:8000/"

