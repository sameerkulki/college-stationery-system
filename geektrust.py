"""Submitted by : shreyank H
    Date : 25/12/2022
    Problem Statement : Geektrust Problem (Shopping Cart)
    Description : This program is to calculate the total cost of the items in the cart after applying the discounts.
    Phone : 9731417723 """
from sys import argv
from utils import add_item_to_cart, get_discounted_cost
def main():
    # Sample code to read inputs from the file
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    lines = f.readlines()
    cart = {}
    cart['items'] = {}
    for line in lines:
        # Add your code here to process input commands.
        line = line.split(" ")
        command = line[0]

        if command == 'ADD_ITEM':
            item = line[1]
            quantity = line[2]
            cart,output = add_item_to_cart(cart, item, quantity)
            print(output)
        elif command == 'PRINT_BILL':
            total_cost,total_discount  = get_discounted_cost(cart)
            print('TOTAL_DISCOUNT',total_discount)
            print('TOTAL_AMOUNT_TO_PAY',total_cost)

        #process the input command and get the output
        # Once it is processed print the output using the command System.out.println()
    
if __name__ == "__main__":
    main()