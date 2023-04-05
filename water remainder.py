import time
from plyer import notification
if __name__=="__main__":
    while True:
        title="PLease DRink Water!!"
        message="A man should drink 4 litre water a Day"
        notification.notify(title,message,timeout=8)
        time.sleep(60*60)