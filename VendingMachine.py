def vending_machine(payment, beverage):
    """
    The vending_machine function takes in two input arguments. The first input argument is the payment
    variable, the payment variable represents the amount of money given to the vending machine. The
    second input argument is the name of the selected beverage. 
    
    The function calculates how much change needs to be given by subtracting the price of the beverage from the payment. Then initialize two
    memos. The first memo will store the minimum number of notes needed for each amount of change
    from 0 to change value. memo_notes will store the last note used for each amount of change. After
    building up the memo and memo_notes, for each amount of change from the smallest note to change,
    it finds the minimum number of notes needed and the last note used. Now, calculate which notes to
    return as change. It starts with the total change and subtracts each note used from it until no change
    is left. The notes used are stored in change_notes. Finally, the code returns two things, the minimum
    number of notes needed for the total change and a list of notes to be given as change.
    
    Calculates the minimum number of notes needed for change in a vending machine transaction.

    Parameters:
        payment (int): The amount of money given to the vending machine.
        beverage (str): The name of the selected beverage.

    Returns:
        min_notes (int): The minimum number of notes needed for the total change.
        change_notes (List[int]): A list of notes to be given as change.
    """
    # All the available MYR notes
    rm_notes = [1, 5, 10, 20, 50, 100]

    # Prices of the beverages
    beverages = {"Beverage1": 33, "Beverage2": 12, "Beverage3": 5, "Beverage4": 24, "Beverage5": 50}

    # Price of the selected beverage
    price = beverages[beverage]

    # Calculate the change
    change = payment - price

    # Initialize the memo & memo_notes arrays
    memo = [0] + [float('inf')] * change    # store min number of notes needed for each amount of change from 0 to change
    memo_notes = [0] + [None] * change      # store the last note used for each amount of change
    
    # Build the memo & memo_notes arrays
    for i in range(min(rm_notes), change + 1):
        min_notes = float('inf'), None
        for note in rm_notes:
            if i - note >= 0 and memo[i - note] < min_notes[0]:
                    min_notes = memo[i - note], note
        memo[i], memo_notes[i] = min_notes[0] + 1, min_notes[1]

    # Build the list to keep track notes for the change
    change_notes = []
    while change > 0:
        note = memo_notes[change]
        change_notes.append(note)
        change -= note
    # Return the min number of notes & the list of notes
    return memo[payment - price], change_notes

# Test the function
payment = 78
beverage = "Beverage5"
min_notes, change_notes = vending_machine(payment, beverage)
print(f"Payment: {payment} \nBeverage: {beverage}")
print(f"Min number of notes for change is: {min_notes}")
print(f"Min notes for change are: {change_notes}")



        
