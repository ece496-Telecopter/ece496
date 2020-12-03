import airsim
import keyboard
import win32gui
import time
import sys
from threading import Thread

xlength = 1920
ylength = 1080

# margin
m = 0.2 

leftbound = m * xlength
rightbound = (1 - m) * xlength
upbound = m * ylength
downbound = (1 - m) * ylength

direction = "NULL"
start = False
       
# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

client.takeoffAsync().join()
#pos = client.simGetObjectPose("Waypoint_1").position

x_start = 0
y_start = 0
z_start = 0
spd = 50.0

#client.moveToPositionAsync(x_start, y_start, z_start, 5).join()

def printit():
    global direction
    global pos, x_start, y_start, z_start 
    
    while(1):
        time.sleep(1)
        gaze_pos = win32gui.GetCursorPos()
        x = gaze_pos[0]
        y = gaze_pos[1]
        
        print("running thread")
        if (x > rightbound and (upbound <= y <= downbound)):
          print("RIGHT")
          y_start = y_start+spd
          client.moveToPositionAsync(x_start, y_start, z_start, spd).join()
          
          
        elif (x < leftbound and (upbound <= y <= downbound)):
          print("LEFT")
          y_start = y_start-spd
          client.moveToPositionAsync(x_start, y_start, z_start, spd).join()
          
        elif (y > downbound and (leftbound <= x <= rightbound)):
          print("DOWN")
          x_start = x_start-spd
          client.moveToPositionAsync(x_start, y_start, z_start, spd).join()
          
        elif (y < upbound and (leftbound <= x <= rightbound)):
          print("UP")
          x_start = x_start+spd
          client.moveToPositionAsync(x_start, y_start, z_start, spd).join()
          
        else:
          print("NOT CARDINAL DIRECTION")


class GazeThread(Thread):

    def __init__(self):
        Thread.__init__(self)
    
    def run(self):
        printit()
        


#while True:
#    try:  # used try so that if user pressed other than the given key error will not be shown
'''
if keyboard.is_pressed('l'):  # if key 'l' is then move to next waypoint 
    start = True
    print(f"Starting Move to Waypoint_{i}")
    pos = client.simGetObjectPose(f"Waypoint_{i}").position
    client.moveToPositionAsync(pos.x_val, pos.y_val, pos.z_val, 5).join()
    print(f"Finished Move to Waypoint_{i}")
    i += 1
    continue # finishing the loop
    
elif keyboard.is_pressed('h'):  # if key 'l' is then move to next waypoint 
    print(f"Starting Move to Waypoint_{i}")
    i -= 1
    pos = client.simGetObjectPose(f"Waypoint_{i}").position
    client.moveToPositionAsync(pos.x_val, pos.y_val, pos.z_val, 5).join()
    print(f"Finished Move to Waypoint_{i}")
    continue # finishing the loop
 
elif keyboard.is_pressed('r'):
    print(f"Reseting to position")
    client.reset()
    continue

elif keyboard.is_pressed('q'):
    break

else:
'''
    
if __name__ == '__main__':

    
    print("Take off complete")
   
    gazethread = GazeThread()
    gazethread.start()
    print("1st thread started")
    

    
    
                
#    except:
#        break  # if user pressed a key other than the given key the loop will break

#print("All complete")