import standard_bot_functions as sb
from standardbots import models

def main():
    # Create positions
    position_1 = models.Position(unit_kind=models.LinearUnitKind.Meters, x=0.1, y=0.2, z=1.0)
    position_2 = models.Position(unit_kind=models.LinearUnitKind.Meters, x=0.1, y=0.2, z=1.0)
    position_3 = models.Position(unit_kind=models.LinearUnitKind.Meters, x=0.1, y=0.2, z=1.0)
    position_4 = models.Position(unit_kind=models.LinearUnitKind.Meters, x=0.1, y=0.2, z=1.0)
    position_5 = models.Position(unit_kind=models.LinearUnitKind.Meters, x=0.1, y=0.2, z=1.0)
    position_6 = models.Position(unit_kind=models.LinearUnitKind.Meters, x=0.1, y=0.2, z=1.0)
    position_7 = models.Position(unit_kind=models.LinearUnitKind.Meters, x=0.1, y=0.2, z=1.0)
    position_8 = models.Position(unit_kind=models.LinearUnitKind.Meters, x=0.1, y=0.2, z=1.0)
    position_9 = models.Position(unit_kind=models.LinearUnitKind.Meters, x=0.1, y=0.2, z=1.0)

    # Move to home position (position 1)
    sb.move_cartesian(position_1.x, position_1.y, position_1.z)

    # Open the gripper
    sb.open_gripper()

    # Move to position above the dice (position 2)
    sb.move_cartesian(position_2.x, position_2.y, position_2.z)

    # Move down to pick up the dice (position 3)
    sb.move_cartesian(position_3.x, position_3.y, position_3.z)

    # Close the gripper - pick
    sb.close_gripper()

    # Move straight back up (position 2)
    sb.move_cartesian(position_2.x, position_2.y, position_2.z)

    # Move to new position (position 4)
    sb.move_cartesian(position_4.x, position_4.y, position_4.z)

    # Move straight down to set the dice down (position 5)
    sb.move_cartesian(position_5.x, position_5.y, position_5.z)

    # Open the gripper - place
    sb.open_gripper()

    # Move straight back up (position 4)
    sb.move_cartesian(position_4.x, position_4.y, position_4.z)

    # Move to new position to pick up second dice (position 6)
    sb.move_cartesian(position_6.x, position_6.y, position_6.z)

    # Move straight down (position 7)
    sb.move_cartesian(position_7.x, position_7.y, position_7.z)

    # Close the gripper - pick
    sb.close_gripper()

    # Move straight back up (position 6)
    sb.move_cartesian(position_6.x, position_6.y, position_6.z)

    # Move to new position (position 8)
    sb.move_cartesian(position_8.x, position_8.y, position_8.z)

    # Move straight down (position 9)
    sb.move_cartesian(position_9.x, position_9.y, position_9.z)

    # Open the gripper - place
    sb.open_gripper()

    # Move straight back up (position 8)
    sb.move_cartesian(position_8.x, position_8.y, position_8.z)

    # Move to home position (position 1)
    sb.move_cartesian(position_1.x, position_1.y, position_1.z)

    # PROGRAM END!! 


if __name__ == "__main__":
    main()

