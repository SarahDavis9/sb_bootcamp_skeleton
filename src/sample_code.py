import standard_bot_functions as sb
from standardbots import models

def main():

    # Create positions and orientations
    position_1 = models.Position(unit_kind=models.LinearUnitKind.Meters, x=0.428, y=0.168, z=0.506)
    orientation_1 = models.Orientation(kind=models.OrientationKindEnum.Quaternion, quaternion=models.Quaternion(0.002, 0.713, 0.013, 0.701))
    position_2 = models.Position(unit_kind=models.LinearUnitKind.Meters, x=0.428, y=-0.110, z=0.265)
    orientation_2 = models.Orientation(kind=models.OrientationKindEnum.Quaternion, quaternion=models.Quaternion(0.003, 0.714, 0.013, 0.700))
    position_3 = models.Position(unit_kind=models.LinearUnitKind.Meters, x=0.428, y=-0.110, z=0.143)
    orientation_3 = models.Orientation(kind=models.OrientationKindEnum.Quaternion, quaternion=models.Quaternion(0.003, 0.714, 0.013, 0.700))
    position_4 = models.Position(unit_kind=models.LinearUnitKind.Meters, x=0.586, y=0.216, z=0.432)
    orientation_4 = models.Orientation(kind=models.OrientationKindEnum.Quaternion, quaternion=models.Quaternion(0.003, 0.714, 0.013, 0.700))
    position_5 = models.Position(unit_kind=models.LinearUnitKind.Meters, x=0.586, y=0.216, z=0.150)
    orientation_5 = models.Orientation(kind=models.OrientationKindEnum.Quaternion, quaternion=models.Quaternion(0.002, 0.713, 0.013, 0.701))
    position_6 = models.Position(unit_kind=models.LinearUnitKind.Meters, x=0.397, y=0.040, z=0.248)
    orientation_6 = models.Orientation(kind=models.OrientationKindEnum.Quaternion, quaternion=models.Quaternion(0.002, 0.713, 0.013, 0.701))
    position_7 = models.Position(unit_kind=models.LinearUnitKind.Meters, x=0.397, y=0.040, z=0.149)
    orientation_7 = models.Orientation(kind=models.OrientationKindEnum.Quaternion, quaternion=models.Quaternion(0.002, 0.713, 0.013, 0.701))
    position_8 = models.Position(unit_kind=models.LinearUnitKind.Meters, x=0.399, y=-0.127, z=0.307)
    orientation_8 = models.Orientation(kind=models.OrientationKindEnum.Quaternion, quaternion=models.Quaternion(0.002, 0.713, 0.013, 0.701))
    position_9 = models.Position(unit_kind=models.LinearUnitKind.Meters, x=0.399, y=-0.127, z=0.146)
    orientation_9 = models.Orientation(kind=models.OrientationKindEnum.Quaternion, quaternion=models.Quaternion(0.002, 0.713, 0.013, 0.701))

    # Move to home position (position 1)
    sb.move_cartesian(position_1.x, 
                      position_1.y, 
                      position_1.z, 
                      orientation_1.quaternion.x, 
                      orientation_1.quaternion.y, 
                      orientation_1.quaternion.z, 
                      orientation_1.quaternion.w)

    # Open the gripper
    sb.open_gripper()

    # Move to position above the dice (position 2)
    sb.move_cartesian(position_2.x, 
                      position_2.y, 
                      position_2.z, 
                      orientation_2.quaternion.x, 
                      orientation_2.quaternion.y, 
                      orientation_2.quaternion.z, 
                      orientation_2.quaternion.w)
    
    # Move down to pick up the dice (position 3)
    sb.move_cartesian(position_3.x, 
                      position_3.y, 
                      position_3.z, 
                      orientation_3.quaternion.x, 
                      orientation_3.quaternion.y, 
                      orientation_3.quaternion.z, 
                      orientation_3.quaternion.w)

    # Close the gripper - pick
    sb.close_gripper()

    # Move straight back up (position 2)
    sb.move_cartesian(position_2.x, 
                      position_2.y, 
                      position_2.z, 
                      orientation_2.quaternion.x, 
                      orientation_2.quaternion.y, 
                      orientation_2.quaternion.z, 
                      orientation_2.quaternion.w)
    
    # Move to new position (position 4)
    sb.move_cartesian(position_4.x, 
                      position_4.y, 
                      position_4.z, 
                      orientation_4.quaternion.x, 
                      orientation_4.quaternion.y, 
                      orientation_4.quaternion.z, 
                      orientation_4.quaternion.w)
    
    # Move straight down to set the dice down (position 5)
    sb.move_cartesian(position_5.x, 
                      position_5.y, 
                      position_5.z, 
                      orientation_5.quaternion.x, 
                      orientation_5.quaternion.y, 
                      orientation_5.quaternion.z, 
                      orientation_5.quaternion.w)
    
    # Open the gripper - place
    sb.open_gripper()

    # Move straight back up (position 4)
    sb.move_cartesian(position_4.x, 
                      position_4.y, 
                      position_4.z, 
                      orientation_4.quaternion.x, 
                      orientation_4.quaternion.y, 
                      orientation_4.quaternion.z, 
                      orientation_4.quaternion.w)
    
    # Move to new position to pick up second dice (position 6)
    sb.move_cartesian(position_6.x, 
                      position_6.y, 
                      position_6.z, 
                      orientation_6.quaternion.x, 
                      orientation_6.quaternion.y, 
                      orientation_6.quaternion.z, 
                      orientation_6.quaternion.w)
    
    # Move straight down (position 7)
    sb.move_cartesian(position_7.x, 
                      position_7.y, 
                      position_7.z, 
                      orientation_7.quaternion.x, 
                      orientation_7.quaternion.y, 
                      orientation_7.quaternion.z, 
                      orientation_7.quaternion.w)
    
    # Close the gripper - pick
    sb.close_gripper()

    # Move straight back up (position 6)
    sb.move_cartesian(position_6.x, 
                      position_6.y, 
                      position_6.z, 
                      orientation_6.quaternion.x, 
                      orientation_6.quaternion.y, 
                      orientation_6.quaternion.z, 
                      orientation_6.quaternion.w)
    
    # Move to new position (position 8)
    sb.move_cartesian(position_8.x, 
                      position_8.y, 
                      position_8.z, 
                      orientation_8.quaternion.x, 
                      orientation_8.quaternion.y, 
                      orientation_8.quaternion.z, 
                      orientation_8.quaternion.w)
    
    # Move straight down (position 9)
    sb.move_cartesian(position_9.x, 
                      position_9.y, 
                      position_9.z, 
                      orientation_9.quaternion.x, 
                      orientation_9.quaternion.y, 
                      orientation_9.quaternion.z, 
                      orientation_9.quaternion.w)
    
    # Open the gripper - place
    sb.open_gripper()

    # Move straight back up (position 8)
    sb.move_cartesian(position_8.x, 
                      position_8.y, 
                      position_8.z, 
                      orientation_8.quaternion.x, 
                      orientation_8.quaternion.y, 
                      orientation_8.quaternion.z, 
                      orientation_8.quaternion.w)
    
    # Move to home position (position 1)
    sb.move_cartesian(position_1.x, 
                      position_1.y, 
                      position_1.z, 
                      orientation_1.quaternion.x, 
                      orientation_1.quaternion.y, 
                      orientation_1.quaternion.z, 
                      orientation_1.quaternion.w)
    
    # PROGRAM END!! 


if __name__ == "__main__":
    main()

