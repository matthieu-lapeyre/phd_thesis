# Working with the real robot
import pypot.robot

poppy = pypot.robot.from_config(config)
poppy.start_sync()

poppy.walk.start()

# Working with the simulated version
import pypot.vrep

poppy = pypot.vrep.from_vrep(config, vrep_host, vrep_port, vrep_scene)
poppy.start_sync()

poppy.walk.start()

