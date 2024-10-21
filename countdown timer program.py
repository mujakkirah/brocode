# time counter 

import time

my_time = int(input("Enter the time in second: "))
for x in range(my_time, 0, -1):  #( 0, my_time): 
    second = x % 60
    minutes = int(x /60) % 60
    hours = int( x / 3600) % 24
    print(f"{hours:02}:{minutes:02}:{second:02}")


time.sleep(1)
print("Time is up")