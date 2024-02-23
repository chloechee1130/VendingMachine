# All the available MYR notes
rm_notes = [1, 5, 10, 20, 50, 100]

# Number of each note available in the vending machine
note_counts = {1: 20, 5: 1, 10: 1, 20: 1, 50: 2, 100: 2}
# beverage 1 with 50

# Prices of the beverages
beverages = {"Beverage1": 2, "Beverage2": 5, "Beverage3": 10, "Beverage4": 13, "Beverage5": 20}

def vending_machine(inserted_notes, beverage):
    """
    The vending_machine function calculates the minimum number of notes needed for change in a vending machine transaction.

    Parameters:
        payment (int): The amount of money given to the vending machine.
        beverage (str): The name of the selected beverage.

    Returns:
        min_notes (int): The minimum number of notes needed for the total change.
        change_notes (List[int]): A list of notes to be given as change.
    """
    # Calculate the total payment
    payment = sum(inserted_notes)

    # Check if the payment is enough to buy the beverage
    price = beverages[beverage]
    if payment < price:
        return "Insufficient payment. Please insert more notes."
    
    # Calculate the change
    change = payment - price

    # Initialize the memo & memo_notes arrays
    memo = [0] + [float('inf')] * change    # store min number of notes needed for each amount of change from 0 to change
    memo_notes = [0] + [None] * change      # store the last note used for each amount of change
    

    # Build the memo & memo_notes arrays
    for i in range(min(rm_notes), change + 1):
        min_notes = float('inf'), None
        for note in rm_notes:
            if i - note >= 0 and memo[i - note] < min_notes[0] and note_counts[note] > 0:
                    min_notes = memo[i - note], note
        memo[i], memo_notes[i] = min_notes[0] + 1, min_notes[1]
    print(f"memo = {memo}\nmemo_notes = {memo_notes}")
    # Build the list to keep track notes for the change
    change_notes = []
    while change > 0:
        note = memo_notes[change]
        if note_counts[note] == 0:
            return "Insufficient notes in the vending machine. Please try again later."
        change_notes.append(note)
        change -= note
    # Return the min number of notes & the list of notes
    return memo[payment - price], change_notes

def main():
    """
    The main function handles the interaction with the user. 
    It prints out a menu of beverages, asks the user to select a beverage and insert notes, 
    and then calls the vending_machine function to calculate the change.
    """
    # Print the menu
    print("Available beverages:")
    for i, beverage in enumerate(beverages, start=1):
        print(f"{i}. {beverage} - MYR {beverages[beverage]}")
    
    # Prompt the user to insert notes and select a beverage
    beverage_number = int(input("Please select a beverage by typing its number: "))
    beverages_list = list(beverages.items())
    beverage = beverages_list[beverage_number - 1][0] 

    inserted_notes = []
    while True:
        note = input("Please insert a note (or type 'done' when finished): ")
        if note.lower() == 'done':
            break
        inserted_notes.append(int(note))

    min_notes, change_notes = vending_machine(inserted_notes, beverage)
    if isinstance(min_notes, str):
        print(min_notes)
    else:
        print(f"Min number of notes for change is: {min_notes}")
        print(f"Min notes for change are: {change_notes}")

if __name__ == "__main__":
    main()

        
# Test the function
# insert note = 10, 10
# beverage = "Beverage4"