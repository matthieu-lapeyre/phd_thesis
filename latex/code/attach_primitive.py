my_robot = pypot.robot.from_config(...)
my_robot.start_sync()

my_robot.attach_primitive(DancePrimitive(my_robot), 'dance')
my_robot.dance.start()
