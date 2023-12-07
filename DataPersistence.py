import json

class DataPersistence:
    def save_data(self, filename, data):
        with open(filename, 'w') as file:
            json.dump(data, file)

    def load_data(self, filename):
        try:
            with open(filename, 'r') as file:
                return [Book(**book_data) for book_data in json.load(file)]
        except FileNotFoundError:
            return []