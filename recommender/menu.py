class Menu:
    def __init__(self):
        self.options = {
            "1": "View all items",
            "2": "View item details",
            "3": "Add item to cart",
            "4": "Remove item from cart",
            "5": "Checkout",
            "6": "Exit"
        }

    def display(self):
        print('==================================')
        print("Welcome to the Recommender System!")
        print("Please choose an option:")
        for key, value in self.options.items():
            print(f"{key}: {value}")
