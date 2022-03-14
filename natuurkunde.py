import matplotlib.pyplot as plt

a = 0
t = 0
dt = 0.01
dx = 0
v = 0
c = 0
gc = 0.0000000000667384                 # Nm²kg⁻²
mearth = 5972000000000000000000000          # mass of earth - kg
rearth = 6371000                            # radius of earth - m
mmoon = 73500000000000000000000            # mass of moon - kg 
rmoon = 1738000                            # radius of moon - m
mmercury = 330000000000000000000000  # mass of mercury - kg
rmercury = 2440000                   # radius of mercury - m

print("Choose: 1 Earth | 2 Moon | 3 Mercurius") 
chp = int(input())
if chp == 1:
    mp = mearth
    rp = rearth
elif chp == 2:
    mp = mmoon
    rp = rmoon
elif chp == 3:
    mp = mmercury
    rp = rmercury
else:
    exit()

x = int(input("Input height (meters):"))
m = int(input("Input weight (kg):"))
o = int(input("Input the frontal area (m²):"))

print("Choose cw waarde: 1 cube | 2 bol | 3 droplet | 4 cone")
ch = int(input(("Input cw:")))
if ch == 1:
    cw = 1.05
elif ch == 2:
    cw = 0.47
elif ch == 3:
    cw = 0.04
elif ch == 4:
    cw = 0.5

pv = []
pt = []
px = []
pflw = []
pa = []

while(x > 0):
    print(x)

    if x < 10000000:
        dt = 0.01
    else:
        dt = 15

    fg = gc * ((mp * m)/((rp + x)**2))      #gravitational force
    
    if chp == 1:
        r = 1.293 * (0.5**(x / 5500))           #rho, air density
        flw = 0.5 * r * cw * o * v * v          #air resistance
    else:
        flw = 0
    
    fres = fg - flw
    a = fres / m 
    dv = a * dt
    v = v + dv
    dx = v * dt
    x = x - dx
    t = t + dt
    c = c + 1                               #counter
    pt.append(t)
    px.append(x)
    pv.append(v)
    pflw.append(flw)
    pa.append(a)

print("0")
print("Elapsed time is:", t)
print("Used samples in calculation:", c)

plot1 = plt.figure(1)
plt.plot(pt, px)
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.title('Height')

plot2 = plt.figure(2)
plt.plot(pt, pv)
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.title('Velocity')

plot3 = plt.figure(3)
plt.plot(pt, pa)
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s²)')
plt.title('Acceleration')

if chp == 1:
    plot4 = plt.figure(4)
    plt.plot(pt, pflw)
    plt.xlabel('Time (s)')
    plt.ylabel('Air resistance (N)')
    plt.title('Air resistance')

plt.show()




# https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
# https://matplotlib.org/stable/gallery/subplots_axes_and_figures/two_scales.html
# https://www.kite.com/python/answers/how-to-show-two-figures-at-once-in-matplotlib-in-python 
