import time
CurrTime=time.strftime('%H:%M:%S')
h=int(time.strftime('%H'))
if(h>4 and h<12 ):
    print("good Morning")
elif(h<4 and h>12):
    print("good afternoon")
else:
    print("good eveining")
    