# imported libraries
import pandas as pd
import numpy as np

df = pd.read_csv("Points.csv") # reads .csv file using pandas
time = df["t"].to_numpy() #turns the "time" column into a numpy array
theta = df["O"].to_numpy() #turns the "theta" column into a numpy array
periods = []
last = 0 #the last maximum
lastmin = 0
angle = []
ticker = 0

for i, x in enumerate(theta): #iterating through the theta list

    try: #try case for iterating over the length of the list
        if x > theta[i+1] and x > theta[i-1] and x > 0: #checks if the theta is a local maximum
            periods.append(((time[i] - last)/4)) #adds the differnce between current local maximum and last to find PERIOD
            angle.append(x*(np.pi/180)) #also adds angle to same index in different list
            last = time[i]  # changes last maximum to current for next loop

        elif x < theta[i+1] and x < theta[i-1]:
            periods.append((time[i] - last) / 4)  # adds the differnce between current local min and last to find PERIOD
            lastmin = time[i]  # changes last maximum to current for next loop
            angle.append(x*(np.pi/180))  # also adds angle to same index in different list


    except:
        continue

X  = open("PeriodVAngle.txt", "w") #writing new data into a text doc

#dropping first and last accounting for half measuremnts
periods.pop(0)
angle.pop(0)
periods.pop()
angle.pop()


#text edititng
for i in range(len(periods)):
    #writes new txt with angle, period, angle_error, period_error
    X.write(str(angle[i]) + " " + str(periods[i]) + " "+"0.00175" + " " + "0.00834" +"\n")
