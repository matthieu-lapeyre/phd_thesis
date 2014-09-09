# PID gains of legs' actuators
poppy.r_ankle_y.pid = (50, 50, 0)
poppy.l_ankle_y.pid = (50, 50, 0)

poppy.r_hip_x.pid = (50, 50, 0)
poppy.l_hip_x.pid = (50, 50, 0)

poppy.r_hip_y.pid = (30, 30, 0)
poppy.l_hip_y.pid = (30, 30, 0)

poppy.abs_y.pid = (20, 20, 0)
poppy.abs_x.pid = (20, 20, 0)


# Mouvement parameters
up_duration = 0.15 #duration of leg lift up in s
down_duration = 0.15 #duration of leg put down in s
up = 0.03 #height of leg lift up in m

#we create a 1D minimum jerk trajectory from 0 to up (m) with a duration of up_duration (s) with initial and final null velocities.
mj1 = min_jerk.MJTraj(0, up, up_duration)
mj2 = min_jerk.MJTraj(up, 0, down_duration)


#attache a primitive to "mjleftup" to lift the left leg according to inverse kinematics following the minimum jerk trajectory.
poppy.attach_primitive(min_jerk.MJLegs1D(poppy, mj1), 'mjleftup')
poppy.attach_primitive(min_jerk.MJLegs1D(poppy, mj2), 'mjleftdown')


# lift the left foot
poppy.mjleftup.start()
poppy.mjleftup.wait_to_stop()

# move the left leg to the left
poppy.l_hip_x.goal_position=15

#land the left foot
poppy.mjleftdown.start()
poppy.mjleftdown.wait_to_stop()
