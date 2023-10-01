import pandas as pd
import numpy as np
file = " " #csv file with data from tracker

df = pd.read_csv(file) # reads .csv file using pandas
time = df["t"].to_numpy() #turns the "time" column into a numpy array
theta = df["O"].to_numpy() #turns the "theta" column into a numpy array

X  = open("THETAvsTIME", "w") #writing new data into a text doc

#text edititng
for i in range(len(time)):
    X.write(str(time[i]/4) + " " + str(theta[i]*(np.pi/180)+0.05) + " "+"0.0087" + " " + "0.00417" +"\n")
