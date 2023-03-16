import time
from KUKA_youbot import KUKA

robot = KUKA('192.168.88.21', ros=False, offline=False, camera_enable=True, advanced=False)
robot.move_base(1, 0, 0)
time.sleep(1)
robot.move_base(0, 0, 0)
time.sleep(1)

