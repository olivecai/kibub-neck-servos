import argparse
from const import *
from st3215 import ST3215



def main():
    s = ST3215(NECK_SERVO_DEVICE)
    parser=argparse.ArgumentParser()
    #moveto
    parser.add_argument('--moveto', dest='moveto', type=str, help='Step of the servo, range -2048 to 2048')
    #nudge
    parser.add_argument('--nudge', dest='nudge', type=str, help='Correct position of the servo, range -2048 to 2048')
    # yaw or pitch
    parser.add_argument('--axis', dest='axis', type=str, help='Axis of the servo, yaw or pitch')


    args=parser.parse_args()
    if args.axis == 'yaw':
        id = YAW_ID
    elif args.axis == 'pitch':
        id = PITCH_ID
    else:
        print('Invalid axis')
    if args.nudge:
        current_pos= s.ReadPosition(id)
        s.MoveTo(id, current_pos + int(args.nudge))
    if args.moveto: 
        s.MoveTo(id, int(args.moveto))

if __name__ == '__main__':
    main()