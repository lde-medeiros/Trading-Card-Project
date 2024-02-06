import time

while True:
    # Collect the user's input
    print("\n\nMAIN MENU: \n\nDo you want to enter new card data (n), Search for an existing card (e), or remove a card (r)?\n\n")
    user_input = input()

    if user_input == "n":
        # Collect the card data
        print("\n\nPlease enter the card's real market value $:")
        market_value = float(input())

        print("\n\nPlease enter the card's name:")
        name = input()

        print("\n\nPlease enter the card's manufacturer:")
        manufacturer = input()

        print("\n\nPlease enter the card's condition:")
        condition = input()

        print("\n\nSUCCESSFULLY ADDED CARD")
        # Get the current time in the GMT-5 time zone
        current_time = time.strftime("%Y-%m-%d %H:%M:", time.gmtime())

        # Write the card data to a file
        with open("card_data.txt", "a") as file:
            file.write("{}\t{}\t{}\t{}\t{}\n".format(current_time, market_value, name, manufacturer, condition))
 
    elif user_input == "e":
        # Collect the search data
        print("\n\nPlease enter the card's name:")
        name = input()

        print("\n\nPlease enter the card's manufacturer:")
        manufacturer = input()

        # Search the file for the card data
        with open("card_data.txt", "r") as file:
            for line in file:
                # Split the line into columns
                columns = line.split("\t")

                # Check if the name and manufacturer match
                if columns[2] == name and columns[3] == manufacturer:
                    # Print the card data
                    print("\n\nCARD FOUND! DISPLAYING DATA...\n\n")
                    print("\nReal market value: {}".format(columns[1]))
                    print("\nName: {}".format(columns[2]))
                    print("\nManufacturer: {}".format(columns[3]))
                    print("\nCondition: {}".format(columns[4]))
                elif columns[2] != name and columns[3] != manufacturer:
                  print("\nCARD NOT FOUND")
                  

    elif user_input == "r":
        # Collect the search data
        print("\n\nPlease enter the card's name to remove:")
        name = input()

        print("\n\nPlease enter the card's manufacturer to remove:")
        manufacturer = input()

        # Read the lines from the file
        with open("card_data.txt", "r") as file:
            lines = file.readlines()

        # Write the lines back to the file, skipping the matching line
        with open("card_data.txt", "w") as file:
            for line in lines:
                # Split the line into columns
                columns = line.split("\t")

                # Check if the name and manufacturer match
                if not (columns[2] == name and columns[3] == manufacturer):
                    file.write(line)
        print("\n\nSUCCESSFULLY REMOVED CARD")
        