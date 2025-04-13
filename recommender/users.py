class Users:
    def __init__(self):
        self.users = {}
        self.user_id_counter = 0

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