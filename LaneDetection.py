from serial_test import Send, Read
import time

Send('M')
print('Sent... M')
left = 0
right = 0
while True:
    d = Read()
    print(d)
    if d == 'a':
        left += 1
        print('Left lane counter ', left)
        
    if d == 'b':
        right += 1
        print('Right lane counter ', right)

    time.sleep(1)
