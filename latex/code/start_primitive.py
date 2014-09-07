my_robot = pypot.robot.from_config(...)
my_robot.start_sync()

dance = LoopDancePrimitive(my_robot, 50)
# The robot will dance until you call dance.stop()
dance.start()
