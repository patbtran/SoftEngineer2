### Data ###
#from Assignment2.main import sandwich_maker_instance

#Nested dictionary
recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },

        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        #Loop through dictionary values to check if there is enough needed ingredients
        for item in ingredients:
            if ingredients[item] > resources[item]:
                print("Sorry there is not enough " + item)
                return False
        #If there are enough of all ingredients, return true
            return True
        """Returns True when order can be made, False if ingredients are insufficient."""

    #Retrieve total amount user inserted
    def process_coins(self):
        #Returns the total calculated from coins inserted.
        #   Hint: include input() function here, e.g. input(how many quarters?: )
        print("Please insert coins")
        dollars_amount = int(input("How many dollars?: "))
        half_dollars_amount = int(input("How many half dollars?: "))
        quarters_amount = int(input("How many quarters?: "))
        nickels_amount = int(input("How many nickels?: "))
        return dollars_amount + half_dollars_amount*.5 + quarters_amount*.25 + nickels_amount*.05

    #Coins represents how much money the user inserted
    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            print("Sorry that is not enough money. Money refunded.")
            return False
        else:
            change = coins - cost
            print("Here is your change: " + str(change))
            return True

    #order_ingredients is from recipes dictionary
    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item in order_ingredients:
            #Update the current inventory after making sandwich
            self.machine_resources[item] -= order_ingredients[item]
        print(sandwich_size + " sandwich is ready. Bon appetite!")

### Make an instance of SandwichMachine class and write the rest of the codes ###
machine = SandwichMachine(resources)

#Make an infinite loop to keep user for input until they choose to exit
while True:
    option = input("What would you like? (small/ medium/ large/ off/ report): ")

#User selects what size of sandwich they want, matches with recipe dictionary
    #If user input is found in recipe dictionary
    if option in recipes:
        #Sandwich that's current in the making is matched with its size & it's requirements
        current_sandwich = recipes[option]

        #Checks if there are enough resources before making sandwich
        if machine.check_resources(current_sandwich["ingredients"]):
            #If true, process if user amount inserted is enough for transaction
            coin_sum = machine.process_coins()

            if machine.transaction_result(coin_sum, current_sandwich["cost"]):
                machine.make_sandwich(option, current_sandwich["ingredients"])

#User selects to see what ingredients are remaining
    elif option == "report":
        print("Bread: " + str(resources["bread"]))
        print("Ham: " + str(resources["ham"]))
        print("Cheese: " + str(resources["cheese"]))
#User decides that they want to turn off machine
    elif option == "off":
        print("Turning off machine haha....")
        break

    else:
        print("Sorry, that is not a valid option! Try again!")