class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins")
        dollars_amount = int(input("How many dollars?: "))
        half_dollars_amount = int(input("How many half dollars?: "))
        quarters_amount = int(input("How many quarters?: "))
        nickels_amount = int(input("How many nickels?: "))
        return dollars_amount + half_dollars_amount*.5 + quarters_amount*.25 + nickels_amount*.05

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