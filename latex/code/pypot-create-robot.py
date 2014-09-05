import pypot.robot

robot = pypot.robot.from_config('ergo_robot.json')
robot = start_sync()

robot.base_tilt_lower.goal_position = 120
