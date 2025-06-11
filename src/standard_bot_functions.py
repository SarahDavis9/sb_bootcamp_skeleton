from standardbots import models, StandardBotsRobot

# Simon:
sdk = StandardBotsRobot(
    url='http://172.23.255.53:3000',
    token='xjis-b8j7nxag-2jk4rs-7i3g65g',
    robot_kind=StandardBotsRobot.RobotKind.Live
    )

#####################
# Get Joint Position
#####################
def get_joint_position():
    with sdk.connection():
        response = sdk.movement.position.get_arm_position()
        try:
            data = response.ok()
            j_1, j_2, j_3, j_4, j_5, j_6 = data.joint_rotations
            return j_1, j_2, j_3, j_4, j_5, j_6
        
        except Exception:
            print(response.data.message)


#########################
# Get Cartesian Position
#########################
def get_cartesian_position():
    with sdk.connection():
        response = sdk.movement.position.get_arm_position()
        try:
            data = response.ok()
            position = data.tooltip_position.position
            orientation = data.tooltip_position.orientation
            return position, orientation
        
        except Exception:
            print(response.data.message)

#####################
# Cartesian Movement
#####################
def move_cartesian(x, y, z, q_x=0.0, q_y=0.0, q_z=0.0, q_w=1.0):
    with sdk.connection():
        response = sdk.movement.position.move(
            position=models.Position(
                unit_kind=models.LinearUnitKind.Meters,
                x=x,
                y=y,
                z=z,
            ),
            orientation=models.Orientation(
                kind=models.OrientationKindEnum.Quaternion,
                quaternion=models.Quaternion(q_x, q_y, q_z, q_w),
            ),
        ).ok()

#####################
# Joint Movement
#####################
def move_joint(j1, j2, j3, j4, j5, j6):
    with sdk.connection():
        arm_rotations = models.ArmJointRotations( joints=(j1, j2, j3, j4, j5, j6)) # 6-tuple of float values  
        position_request = models.ArmPositionUpdateRequest( kind=models.ArmPositionUpdateRequestKindEnum.JointRotation, joint_rotation=arm_rotations) 
        sdk.movement.position.set_arm_position(position_request).ok()

#########################
# Gripper Sample - OPEN
#########################
def open_gripper(width=0.11, force=10.0):
    with sdk.connection():
        gripper_command = models.GripperCommandRequest(
            kind=models.GripperKindEnum.Onrobot2Fg14,
            onrobot_2fg14=models.OnRobot2FG14GripperCommandRequest(
                grip_direction=models.LinearGripDirectionEnum.Outward,
                target_grip_width=models.LinearUnit(
                    value=width, unit_kind=models.LinearUnitKind.Meters
                ),
                target_force=models.ForceUnit(
                    value=force,
                    unit_kind=models.ForceUnitKind.Newtons,
                ),
                control_kind=models.OnRobot2FG14ControlKindEnum.Move,
            ),
        )
        res = sdk.equipment.control_gripper(gripper_command).ok()


#########################
# Gripper Sample - CLOSE
#########################
def close_gripper(width=0.09, force=10.0):
    with sdk.connection():
        gripper_command = models.GripperCommandRequest(
            kind=models.GripperKindEnum.Onrobot2Fg14,
            onrobot_2fg14=models.OnRobot2FG14GripperCommandRequest(
                grip_direction=models.LinearGripDirectionEnum.Outward,
                target_grip_width=models.LinearUnit(
                    value=width, unit_kind=models.LinearUnitKind.Meters
                ),
                target_force=models.ForceUnit(
                    value=force,
                    unit_kind=models.ForceUnitKind.Newtons,
                ),
                control_kind=models.OnRobot2FG14ControlKindEnum.Move,
            ),
        )
        res = sdk.equipment.control_gripper(gripper_command).ok()