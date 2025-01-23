import os
import platform
import time


def simulate_usb_payload():
    """A simulated eductional USB paylode for authorized use only."""
    print("This is a demonstration of a bad USb payload")
#simulate performing an action (eg open a file)
if platform.system() == "windows":
    os.system('msg * test paylod of a Bad USb')
elif platform.system() == "Linux" or platform.system() == "Darwin":
    os.system('this is a test paylode of a bad usb')
else:
    print("unsupported operting system")


if __name__== "__main__":
    print("simulating USB payload ... plugging in the usb..")
time.sleep(2)
simulate_usb_payload()