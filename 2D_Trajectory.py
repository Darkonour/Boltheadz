import math
import matplotlib.pyplot as plt

v=float(input("Enter the initial velocity : "))
theta=float(input("Enter projection angle : "))
print()

if (v>0) and (theta >= 0 and theta <= 90):
    g=9.81
    rad=math.radians(theta)

    total_time=(2*v*math.sin(rad))/g
    steps=100
    dt=total_time/steps

    x=[]
    y=[]
    t=0.0

    for i in range(steps + 1):
        x_coordinate = v*math.cos(rad)*t
        y_coordinate = (v*math.sin(rad)*t)-(0.5*g*t*t)

        x.append(x_coordinate)
        y.append(y_coordinate)

        t=t+dt

    plt.plot(x,y)
    plt.title("Rocket Trajectory")
    plt.xlabel("Distance (m)")
    plt.ylabel("Height (m)")
    plt.grid(True)
    plt.show()

else:
    print("Invalid Input")
