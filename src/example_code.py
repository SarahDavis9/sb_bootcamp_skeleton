import standard_bot_functions as sb

def main():
    # This is where you will write your code to move the robot!
    
    # Move the robot using cartesian coordinates
    position, orientation = sb.get_cartesian_position()
    print(f"Cartesian Position: {position}, Orientation: {orientation}")

    # Move the Z position 80mm up
    sb.move_cartesian(position.x, position.y, position.z + 0.08)

    # Move the robot using joint rotations
    j1, j2, j3, j4, j5, j6 = sb.get_joint_position()
    print(f"Joint Positions: {j1}, {j2}, {j3}, {j4}, {j5}, {j6}")
    
    # Rotate the last joint 90 degrees
    sb.move_joint(j1, j2, j3, j4, j5, j6 + 1.57)
    
    #Open the gripper
    sb.open_gripper()

    # Close the gripper
    sb.close_gripper()

if __name__ == "__main__":
    main()

