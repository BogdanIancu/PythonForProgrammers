import requests
import json
import random


class Employee:
    def __init__(self):
        self.name = ""
        self.salary = 0

    def net_salary(self) -> float:
        if self.salary > 0:
            return self.salary * 0.55
        else:
            raise ValueError()

    def get_placeholder(self):
        json_response_text = requests.get("https://randomuser.me/api/").text
        json_response = json.loads(json_response_text)
        self.name = json_response["results"][0]["name"]["first"] + " " + json_response["results"][0]["name"]["last"]
        self.salary = random.randint(1000, 10_000)


employee = Employee()
employee.get_placeholder()
print(employee.name, employee.salary)
