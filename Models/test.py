import ax12 as x
import time

y = x.Ax12()

y.moveSpeed(x.Ax12(), 9, 300, 500)
time.sleep(2)
y.moveSpeed(x.Ax12(), 9,300, 0)
