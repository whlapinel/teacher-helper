import json
from typing import Union, List


class Classroom:
    def __init__(self, name, type):
        if type not in ['standard', 'honors']:
            raise ValueError("Classroom type must be 'standard' or 'honors'")
        self.name = name
        self.type: str = type
    
class User:
    def __init__(self):
        self.username = None
        self.password = None
        self.pin = None
        self.classrooms: List[Classroom] = []

    def __repr__(self):
        return f"User(username: {self.username} password: {self.password} classes: {self.classroom_names})"


    def save_to_config(self, filename='user_config.json'):
        user_data = {
            "username": self.username,
            "password": self.password,
            "classrooms": self.classroom_names
        }
        with open(filename, 'w') as file:
            json.dump(user_data, file, indent=4)

    def load_from_config(self, filename='user_config.json'):
        try:
            with open(filename, 'r') as file:
                user_data = json.load(file)
            self.username = user_data['username']
            self.password = user_data['password']
            self.classroom_names = user_data['classrooms']
            print(f"Username: {user_data['username']}")
            print(f"Password: {user_data['password']}")
            print(f"Classrooms: {','.join(user_data['classrooms'])}")
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
            classroom = input(f"Enter classroom {i}: ")
            classrooms.append(classroom)
        self.classroom_names = classrooms



