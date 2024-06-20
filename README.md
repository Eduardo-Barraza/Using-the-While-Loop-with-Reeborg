### Reeborg's World Example: Collecting Beepers

In this example, Reeborg will move forward until it encounters a wall. If there is a beeper on the current cell, Reeborg will pick it up. The goal is to demonstrate how a `while` loop can be used to repeat actions until a condition is met.

### Program Code

```python
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
```

### Explanation and Lessons

1. **While Loop**:
   - **Lesson**: Learn how to use the `while` loop to repeat actions until a condition is met.
   - **Details**: The `while front_is_clear():` loop keeps Reeborg moving forward as long as there is no wall in front.

2. **Conditionals**:
   - **Lesson**: Understand how to use `if` statements to perform actions based on conditions.
   - **Details**: The `if beeper_present():` checks if there is a beeper on the current cell and picks it up if true.

3. **Functions**:
   - **Lesson**: Organize code into functions to make it modular and reusable.
   - **Details**: The `main()` function encapsulates the main logic, making the code cleaner and easier to understand.

4. **Reeborg's World Functions**:
   - **Lesson**: Use predefined functions in Reeborg's World to control Reeborg's actions.
   - **Details**:
     - `move()`: Moves Reeborg forward by one cell.
     - `front_is_clear()`: Checks if there is no wall in front of Reeborg.
     - `beeper_present()`: Checks if there is a beeper on the current cell.
     - `pick_beeper()`: Picks up a beeper from the current cell.

### Main Lessons in This Program

1. **While Loop for Repetition**:
   - The `while` loop is used to repeat actions until a condition (`front_is_clear()`) is no longer met. This demonstrates how to use loops for repetitive tasks.

2. **Conditional Statements**:
   - The use of `if` statements inside the loop shows how to perform different actions based on certain conditions (`beeper_present()`).

3. **Breaking Down Problems**:
   - Encapsulating the logic in a `main()` function illustrates the importance of breaking down a problem into smaller, manageable parts.

4. **Understanding the Environment**:
   - Working with predefined functions in Reeborg's World helps understand how to interact with an environment using simple commands and sensors.

This simple program is a great way to introduce beginners to the concept of loops, conditionals, and modular programming in a fun and interactive way.
