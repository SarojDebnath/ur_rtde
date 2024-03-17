import gripper
import time
i=0
while (i<3):
    gripper.Open()
    time.sleep(3)
    gripper.Close()
    time.sleep(3)
    i+=1
gripper.Open()