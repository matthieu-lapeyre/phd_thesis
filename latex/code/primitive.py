import time

import pypot.primitive

class DancePrimitive(pypot.primitive.Primitive):
    def run(self, amp=30, freq=0.5):
        # self.elapsed_time gives you the time (in s) since the primitive has been running
        while self.elapsed_time < 30:
            x = amp * numpy.sin(2 * numpy.pi * freq * self.elapsed_time)

            self.robot.base_pan.goal_position = x
            self.robot.head_pan.goal_position = -x

            time.sleep(0.02)
