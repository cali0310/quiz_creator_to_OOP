import json
import os

class QuestionLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        
    def load(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                return json.load(file)
        return []