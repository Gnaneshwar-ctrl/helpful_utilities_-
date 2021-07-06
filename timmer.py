import time 
import webbrowser

total_breaks = 7
break_count = 0

while(break_count < total_breaks):
    print("current time:" + time.ctime())
    time.sleep(60*60*2)
    webbrowser.open("www.google.com")
    break_count += 1

