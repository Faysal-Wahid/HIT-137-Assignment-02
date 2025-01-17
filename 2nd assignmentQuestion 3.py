import turtle

def draw_tree(t, branch_length, depth, left_angle, right_angle, reduction_factor):
    """
    Draws a tree using recursion.

    Parameters:
    t (turtle.Turtle): The turtle object.
    branch_length (float): The starting length of the branch.
    depth (int): The depth of recursion.
    left_angle (float): Angle for the left branch.
    right_angle (float): Angle for the right branch.
    reduction_factor (float): Factor to reduce branch length.
    """
    if depth == 0:
        return  # Base case: stop recursion when depth is 0

    # Draw the main branch
    t.forward(branch_length)

    # Draw the right subtree
    t.right(right_angle)
    draw_tree(t, branch_length * reduction_factor, depth - 1, left_angle, right_angle, reduction_factor)

    # Return to the main branch
    t.left(left_angle + right_angle)

    # Draw the left subtree
    draw_tree(t, branch_length * reduction_factor, depth - 1, left_angle, right_angle, reduction_factor)

    # Return to the original angle and position
    t.right(left_angle)
    t.backward(branch_length)

def main():
    # Get user inputs
    left_angle = float(input("Enter the left branch angle (degrees): "))
    right_angle = float(input("Enter the right branch angle (degrees): "))
    starting_length = float(input("Enter the starting branch length: "))
    recursion_depth = int(input("Enter the recursion depth: "))
    reduction_factor = float(input("Enter the branch length reduction factor (e.g., 0.7): "))

    # Set up the screen and turtle
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Customizable Recursive Tree")

    tree_turtle = turtle.Turtle()
    tree_turtle.shape("classic")
    tree_turtle.color("green")
    tree_turtle.speed(0)

    # Move to the starting position
    tree_turtle.left(90)
    tree_turtle.up()
    tree_turtle.backward(starting_length / 2)
    tree_turtle.down()

    # Draw the tree
    draw_tree(tree_turtle, starting_length, recursion_depth, left_angle, right_angle, reduction_factor)

    # Keep the window open
    screen.mainloop()

if __name__ == "__main__":
    main()
