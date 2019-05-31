"""
Demo the Bebop indoors (sets small speeds and then flies just a small amount)
Note, the bebop will hurt your furniture if it hits it.  Even though this is a very small
amount of flying, be sure you are doing this in an open area and are prepared to catch!

Author: Amy McGovern
"""

from pyparrot.pyparrot.Bebop import Bebop


bebop = Bebop(drone_type="Bebop2")

def simpleflight():

    print("connecting")
    success = bebop.connect(10)
    print(success)

    print("sleeping")
    bebop.smart_sleep(5)

    bebop.ask_for_state_update()

    bebop.safe_takeoff(10)

    print("flip back")
    print("flying state is %s" % bebop.sensors.flying_state)
    success = bebop.flip(direction="back")
    print("mambo flip result %s" % success)
    bebop.smart_sleep(5)

    bebop.smart_sleep(5)
    bebop.safe_land(10)

    print("DONE - disconnecting")
    bebop.disconnect()


def startmission():
    bebop = Bebop(drone_type="Bebop2")

    print("connecting")
    success = bebop.connect(10)
    print(success)

    if (success):
        print("turning on the video")
        bebop.start_video_stream()

        print("sleeping")
        bebop.smart_sleep(2)

        bebop.ask_for_state_update()

        bebop.safe_takeoff(10)

        bebop.set_max_tilt(5)
        bebop.set_max_vertical_speed(1)

        print("Flying direct: Slow move for indoors")
        bebop.fly_direct(roll=0, pitch=20, yaw=0, vertical_movement=0, duration=2)

        bebop.smart_sleep(5)


        bebop.safe_land(10)

        print("DONE - disconnecting")
        bebop.stop_video_stream()
        bebop.smart_sleep(5)
        print(bebop.sensors.battery)
        bebop.disconnect()


def takeoff():

    print("connecting")
    success = bebop.connect(10)
    print(success)

    if (success):
        print("sleeping")
        bebop.smart_sleep(2)

        bebop.ask_for_state_update()

        bebop.safe_takeoff(10)

        bebop.flat_trim(duration=10)


def land():
    bebop.smart_sleep(2)

    bebop.safe_land(10)

    print("DONE - disconnecting")
    bebop.smart_sleep(2)
    print(bebop.sensors.battery)
    bebop.disconnect()


def rotate():
    print("Flying direct: Slow move for indoors")
    bebop.fly_direct(roll=0, pitch=0, yaw=100, vertical_movement=0, duration=5)

    bebop.smart_sleep(1)
    bebop.flat_trim(duration=10)


def flip():
    print("flip front")
    print("flying state is %s" % bebop.sensors.flying_state)
    success = bebop.flip(direction="front")
    print("mambo flip result %s" % success)
    bebop.smart_sleep(1)

    bebop.flat_trim(duration=10)


def battery_status():
    response = "77%"
    return response

