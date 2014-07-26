class FootIO(IO, StoppableThreadLoop):
    def __init__(self, port, baudrate):
        self.serial_com = serial.Serial(port, baudrate)
        self._measured_values = []

    def last_values(self):
        return self._measured_values

    def update(self):
        l = self.serial_com.readline()
        l = l.replace('\r\n', '')
        self._measured_values = map(float, l.split(','))


class FootPressure(SensorsController):
    def __init__(self, io):
        SensorsController.__init__(self, io)
        self._values = []

    def update(self):
        self._values = self.io.last_values()

    @property
    def pressure_values(self):
        return self._values
