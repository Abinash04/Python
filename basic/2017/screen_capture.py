
"""
A simple screen grabbing utility

@author Abinash Behera - 
@date 2017-07-28
"""


from PIL import ImageGrab
import time

time.sleep(5)
ImageGrab.grab().save("screen_capture.jpg", "JPEG")
