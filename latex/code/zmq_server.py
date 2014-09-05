import zmq

#As an example of what you can do, here is the code of getting the load of a motor and changing its position:

robot = pypot.robot.from_config(...)
robot.start_sync()

server = pypot.server.ZMQServer(robot, host, port)
server.start()

c = zmq.Context()
s = c.socket(zmq.REQ)
s.connect('tcp://{}:{}'.format(host, port))

req = {
    'get': {motor_name: ('present_load', )},
    'set': {motor_name: {'goal_position': 20.0}}
}

s.send_json(req)
answer = s.recv_json()
