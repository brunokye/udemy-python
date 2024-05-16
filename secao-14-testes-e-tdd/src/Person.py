import requests


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.get_data = False

    def get_all_data(self):
        answer = requests.get("https://www.example.com/")

        if answer.ok:
            self.get_data = True
            return "CONNECTED"
        else:
            self.get_data = False
            return "ERROR 404"
