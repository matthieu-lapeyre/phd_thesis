import time

import pypot.primitive

class LoopDancePrimitive(pypot.primitive.LoopPrimitive):
    # The update function is automatically called at the frequency given on the constructor
    def update(self, amp=30, freq=0.5):
        x = amp * numpy.sin(2 * numpy.pi * freq * self.elapsed_time)

        self.robot.base_pan.goal_position = x
        self.robot.head_pan.goal_position = -x
