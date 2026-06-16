import argparse
from const import *
from st3215 import ST3215



def main():
    s = ST3215(NECK_SERVO_DEVICE)
    parser=argparse.ArgumentParser()
    parser.add_argument('--axis', dest='axis', type=str, help='Axis of the servo, yaw or pitch')

    args=parser.parse_args()
    if args.axis == 'yaw':
        id = YAW_ID
    elif args.axis == 'pitch':
        id = PITCH_ID
    else:
        print('Invalid axis')

    current_pos= s.ReadPosition(id)
    print(f"Current position of {args.axis} servo: {current_pos}")

if __name__ == '__main__':
    main()