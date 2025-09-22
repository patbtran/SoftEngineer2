class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        for item in ingredients:
            if ingredients[item] > self.machine_resources[item]:
                print("Sorry there is not enough " + item)
                return False
        #If there are enough of all ingredients, return true
            return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        for item in order_ingredients:
            #Update the current inventory after making sandwich
            self.machine_resources[item] -= order_ingredients[item]
        print(sandwich_size + " sandwich is ready. bon appetite!")