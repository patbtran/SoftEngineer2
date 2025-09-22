import data
import cashier
import sandwich_maker


from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():


    ###  write the rest of the codes ###
    while True:

        option = input("What would you like? (small/ medium/ large/ off/ report): ")

        # User selects what size of sandwich they want, matches with recipe dictionary
        # If user input is found in recipe dictionary
        if option in recipes:
            # Sandwich that's current in the making is matched with its size & it's requirements
            current_sandwich = recipes[option]

            # Checks if there are enough resources before making sandwich
            if sandwich_maker_instance.check_resources(current_sandwich["ingredients"]):
                # If true, process if user amount inserted is enough for transaction
                coin_sum = cashier_instance.process_coins()

                if cashier_instance.transaction_result(coin_sum, current_sandwich["cost"]):
                    sandwich_maker_instance.make_sandwich(option, current_sandwich["ingredients"])


        # User selects to see what ingredients are remaining
        elif option == "report":
            print("Bread: " + str(resources["bread"]))
            print("Ham: " + str(resources["ham"]))
            print("Cheese: " + str(resources["cheese"]))

        # User decides they want to turn off machine
        elif option == "off":
            print("Turning off machine...")
            break

        else:
            print("Sorry, that is not a valid option. Try again.")
if __name__=="__main__":
    main()