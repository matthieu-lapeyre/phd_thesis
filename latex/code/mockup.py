class MyDummyPrimitive(pypot.primitive.Primitive):
    def run(self, motors):
        fake_motors = [self.get_mockup_motor(m) for m in motors]

        while True:
            for m in fake_motors:
                ...
