class _PosSpeedLoadDxlController(_DxlController):
    def __init__(self, io, motors, sync_freq=50.):
        _DxlController.__init__(self, io, motors, sync_freq)

        self.ids = [m.id for m in motors]

    def setup(self):
        torques = self.io.is_torque_enabled(self.ids)
        for m, c in zip(self.motors, torques):
            m.compliant = not c
        self._old_torques = torques

        values = self.io.get_goal_position_speed_load(self.ids)
        positions, speeds, loads = zip(*values)
        for m, p, s, l in zip(self.motors, positions, speeds, loads):
            m._values['goal_position'] = p
            m._values['moving_speed'] = s
            m._values['torque_limit'] = l

    def update(self):
        self.knee_compliance_rule()

    def knee_compliance_rule(self):

        # Right Knee
            # Extension
        if ((self.robot.r_knee_y.present_position < 21)
            and self.r_knee_extend[self.cycle_iter]):

            self.robot.r_knee_y.compliant = True

            # Flexion
        elif ((self.robot.r_knee_y.present_position > 29)
             and (self.robot.r_knee_y.present_position < 70)
             and self.r_knee_flex[self.cycle_iter]):

            self.robot.r_knee_y.compliant = True

        else :
            self.robot.r_knee_y.compliant = False

        # Left Knee
           # Flexion
        if ((self.robot.l_knee_y.present_position < 21) and
            self.l_knee_extend[self.cycle_iter]):

            self.robot.l_knee_y.compliant = True

            # Extension
        elif ((self.robot.l_knee_y.present_position > 29)
            and (self.robot.l_knee_y.present_position < 70)
            and self.l_knee_flex[self.cycle_iter]):

            self.robot.l_knee_y.compliant = True

        else :
            self.robot.l_knee_y.compliant = False

