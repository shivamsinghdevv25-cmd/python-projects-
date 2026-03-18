import time
t=time.strftime("%H:%M:%S")
print(t)
t=int(time.strftime('%H'))
print(t)
if t<12:
    print('Good morning Sir')
elif t<18:
    print('Good afternoon Sir')     
else:
    print('Good evening Sir')
print('Have a nice day')
