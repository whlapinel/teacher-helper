import json
from typing import Union, List



class User:
    def __init__(self):
        self.username = None
        self.password = None
        self.pin = None
        self.classrooms: List[{str[str]}] = []


    def save_to_config(self, filename='user_config.json'):
        user_data = {
            "username": self.username,
            "password": self.password,
            "pin": self.pin,
            "classrooms": self.classrooms
        }
        with open(filename, 'w') as file:
            json.dump(user_data, file, indent=4)

    def load_from_config(self, filename='user_config.json'):
        try:
            with open(filename, 'r') as file:
                user_data = json.load(file)
                self.username = user_data['username']
                self.password = user_data['password']
                self.pin = user_data['pin']
                for classroom in user_data['classrooms']:
                    self.classrooms.append({'name': classroom['name'], 'type':classroom['type']})
            return True
        except (FileNotFoundError, json.JSONDecodeError, Exception) as e:
            print(f"Failed to load user data: {e}")
            return False

    def construct_from_input(self):
        self.username = input("Enter your username: ")
        self.password = input("Enter your password: ")
        self.pin = input("Your credentials will be stored on your device and encrypted. Enter a pin (4-6 digits): ")
        classrooms = []
        for i in range(1, 4):
            classroom_name = input(f"Enter classroom name {i}: ")
            classroom_type = input(f"Enter classroom type for {classroom_name} (e.g. std, hon): ")
            classrooms.append({"name": classroom_name, "type": classroom_type})
        self.classrooms = classrooms



