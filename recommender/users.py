from user import User

class Users:
    def __init__(self):
        with open('users.json', 'w') as file:
            self.user_data = json.load(file)
        self.users = {}

    def get_user_count(self):
        return len(self.users)
    
    def add_user(self, user):
        self.user_id_counter += 1
        self.users[self.user_id_counter] = user
        return self.user_id_counter

    def get_user(self, user_id):
        return self.users.get(user_id)

    def remove_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False