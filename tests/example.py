
from KUKA import YouBot


robot = YouBot("192.168.88.22")


robot.move_arm(0,0,0,0,0)
time.sleep(5)