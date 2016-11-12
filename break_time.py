import time
import webbrowser

total_breaks = 3    #number of break cycles
break_count = 0
break_time = 2      #break time set in hours

print ('This program started on ' + time.ctime())
while (break_count < total_breaks):
    time.sleep(60 * 60 * break_time)
    webbrowser.open('https://www.youtube.com/watch?v=AjPau5QYtYs')
    break_count += 1