import urllib2
import json
import time

import pypot.robot
import pypot.server

robot = pypot.robot.from_config(...)
robot.start_sync()

server = pypot.server.HTTPServer(robot, host, port)
server.start()

time.sleep(1) # Make sure the server is really started

url = 'http://{}:{}/motor/list.json'.format(host, port)
print urllib2.urlopen(url).read()

url = 'http://{}:{}/motor/base_tilt_lower/goal_position'.format(host, port)
data = 20.0
r = urllib2.Request(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
print urllib2.urlopen(r).read()
