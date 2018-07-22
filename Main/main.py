"""
Created on Jul 21, 2018

@author: ben
"""
from DirectionHandlers.RightHandler import RightHandler

def main():
    """
    main class
    
    start going right
    finally:
        reset
    going right is in its own thread class
    main waits until finished. 
    Perhaps loop on camera photo acceptance or something along those lines.
    Actually, start the photo class and have it manage the camera. 
    """
    right_handler = RightHandler()
    right_handler.start()
    right_handler.join()

if __name__ == "__main__":
    main()