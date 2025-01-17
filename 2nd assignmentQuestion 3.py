import turtle

def draw_branch(t, branch_length, left_angle, right_angle, depth, reduction_factor, is_main_branch):
    if depth == 0:
        return

    # Set the color of the branch
    if is_main_branch:
        t.color("red")
    else:
        t.color("green")

    # Draw the main branch
    t.forward(branch_length)

    # Draw the left branch
    t.left(left_angle)
    draw_branch(t, branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor, False)
    t.right(left_angle)  # Return to the main branch

    # Draw the right branch
    t.right(right_angle)
    draw_branch(t, branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor, False)
    t.left(right_angle)  # Return to the main branch

    # Move back to the previous position
    t.backward(branch_length)

def main():
    # Get user input for the parameters
    left_angle = int(input("Enter the left branch angle (e.g., 20): "))
    right_angle = int(input("Enter the right branch angle (e.g., 25): "))
    starting_length = int(input("Enter the starting branch length (e.g., 100): "))
    depth = int(input("Enter the recursion depth (e.g., 5): "))
    reduction_factor = float(input("Enter the branch length reduction factor (e.g., 0.7): "))

    # Setup the turtle screen and turtle object
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed("fastest")
    t.left(90)  # Point the turtle upwards

    # Draw the tree
    draw_branch(t, starting_length, left_angle, right_angle, depth, reduction_factor, True)

    # Wait for the user to close the window
    screen.mainloop()

if __name__ == "__main__":
    main()

