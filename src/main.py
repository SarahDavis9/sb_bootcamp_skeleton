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

    ######################################
    #
    #   Fill in each comment below with 
    #   the correct function calls!
    #
    ######################################

    # Move to home position (position 1)

    # Open the gripper

    # Move to position above the dice (position 2)
    
    # Move down to pick up the dice (position 3)

    # Close the gripper - pick

    # Move straight back up (position 2)
    
    # Move to new position (position 4)
    
    # Move straight down to set the dice down (position 5)
    
    # Open the gripper - place

    # Move straight back up (position 4)
    
    # Move to new position to pick up second dice (position 6)
    
    # Move straight down (position 7)
    
    # Close the gripper - pick

    # Move straight back up (position 6)
    
    # Move to new position (position 8)
    
    # Move straight down (position 9)
    
    # Open the gripper - place

    # Move straight back up (position 8)
    
    # Move to home position (position 1)
    
    # PROGRAM END!! 


if __name__ == "__main__":
    main()

