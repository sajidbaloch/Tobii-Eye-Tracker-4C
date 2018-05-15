import tobii_research as tr
import time

found_eyetrackers = tr.find_all_eyetrackers()

my_eyetracker = found_eyetrackers[0]
print("Address: " + my_eyetracker.address)
print("Model: " + my_eyetracker.model)
print("Name (It's OK if this is empty): " + my_eyetracker.device_name)
print("Serial number: " + my_eyetracker.serial_number)


def gaze_data_callback(gaze_data):
    # Print gaze points of left and right eye
    while 1:
        print("Left eye: ({gaze_left_eye}) \t Right eye: ({gaze_right_eye})".format(
            gaze_left_eye=gaze_data['left_gaze_point_on_display_area'],
            gaze_right_eye=gaze_data['right_gaze_point_on_display_area']))


my_eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)

time.sleep(5)

my_eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_data_callback)
