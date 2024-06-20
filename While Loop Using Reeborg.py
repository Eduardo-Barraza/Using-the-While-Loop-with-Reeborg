# Define the main function
def main():
    # Keep moving forward until Reeborg encounters a wall
    while front_is_clear():
        # If there is a beeper on the current cell, pick it up
        if beeper_present():
            pick_beeper()
        
        # Move forward to the next cell
        move()
    
    # Check for a beeper on the last cell and pick it up if present
    if beeper_present():
        pick_beeper()

# Call the main function to execute the program
main()
