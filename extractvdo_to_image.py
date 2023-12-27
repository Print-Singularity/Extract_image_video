# Importing all necessary libraries
import cv2
  
# Read the video from specified path
cam = cv2.VideoCapture("trainvdo.mp4")  

  
# frame
currentframe = 0
  
while(True):
      
    # reading from frame
    ret,frame = cam.read()
  
    if ret:
        # if video is still left continue creating images

        name = "C:/Users/AI/Desktop/extract_video/" + str(currentframe) + '.jpg'     #test
        print ('Creating...' + name)
        
        #How many fream did you want?  or you need all frame you can comment this Func.
        if currentframe == 20:
            break
            
  
        # writing the extracted images
        cv2.imwrite(name, frame)
  
        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
    else:
        break
  
# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()