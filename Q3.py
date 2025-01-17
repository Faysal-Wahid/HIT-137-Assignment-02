import turtle
#Input from user. Left angle, right angle, lenght of branch, depth, reduction factor
left_ang = float(input("Enter an angle for the left branch: "))
right_ang = float(input("Enter an angle to draw the right branch: "))
branch_len = float(input("Enter the leght of the first branch: "))
depth = int(input("Type the depth of the recursion: "))
reduc_factor = float(input("Enter the branch length reduction factor: "))

#Function to draw a tree on turtle
def tree_drawing(branch_len, left_ang, right_ang, depth, reduc_factor):
    if depth == 0:
        return
    else:
        
        turtle.forward(branch_len)
        
        turtle.left(left_ang)
        tree_drawing(branch_len * reduc_factor, left_ang, right_ang, depth - 1, reduc_factor)
        
        turtle.right(left_ang + right_ang)  
        tree_drawing(branch_len * reduc_factor, left_ang, right_ang, depth - 1, reduc_factor)
        
        turtle.left(right_ang)
        turtle.backward(branch_len)


turtle.speed(0)
turtle.left(90)  
tree_drawing(branch_len, left_ang, right_ang, depth, reduc_factor)
turtle.drawn()
