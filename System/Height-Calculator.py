import os
import time

print('Height Calculator')
print('If you want to exit the programm during calculation, please press Crlt+C.')
time.sleep(2) 
print('Ready!')

while True:
    os.system('color 7')
    t = float(input('Please enter the free fall time of the object in seconds: '))
    v_0 = 331.4
    k = float(input('Please enter the temperature in degrees Celsius: '))
    v = k*0.6+v_0
    g = 9.80665
    os.system('color 2')
    t_1 = (((v*(2*g*t+v))**0.5)-v)/g
    h = (g*t_1**2)/2
    print('\n', 'The height is about ' + str(h) + '  meters')
    print('\n', 'Preparing for the second calculation...  *The preparation time will vary depending on the performance of your computer.', '\n')
    time.sleep(2) 