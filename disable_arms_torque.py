FOLLOWER_RIGHT = '/dev/follower_right'
FOLLOWER_LEFT = '/dev/follower_left'

from st3215 import ST3215
r = ST3215(FOLLOWER_RIGHT)
l = ST3215(FOLLOWER_LEFT)
print("disabling torque on right and left follower arms....")
print([r.StopServo(i) for i in range(1,7)])
print([l.StopServo(i) for i in range(1,7)])

print("disabled torques on right and left follower arms.")

