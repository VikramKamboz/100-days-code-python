import time

gettime = time.strftime('%H:%M:%S')
print(gettime)

get_current_hour = int(time.strftime('%H'))
print(type(get_current_hour))

if (get_current_hour < 12 and get_current_hour>6):
    print('Good morning')
elif (get_current_hour >= 12 and get_current_hour < 16):
    print('good afternoon')
else:
    print('Good evening')
