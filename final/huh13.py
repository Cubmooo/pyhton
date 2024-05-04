import random
while True:
    number1hour=str(random.randint(0,20)).zfill(2)
    number1min=str(random.randint(0,59)).zfill(2)
    number2hour=str(int(number1hour)+random.randint(0,3)).zfill(2)
    number2min=str(random.randint(0,59)).zfill(2)
    answer=(60-int(number1min)+int(number2min))+60*(int(number2hour)-int(number1hour)-1)
    if answer<0:
        continue
    break

print(number1hour,number1min,number2hour,number2min)
print(answer)