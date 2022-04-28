#importing graphic interface modules
from tkinter import *
from tkinter import messagebox #messagebox has to be imported seperately 

#importing ML model which was trained in Jupyter Notebook
import joblib
model = joblib.load('BCP_Model.joblib')

#import module which will be used for data pre-processing
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd

#the features for the model
features = [
    'radius_mean',
    'texture_mean',
    'perimeter_mean',
    'area_mean',
    'smoothness_mean',
    'compactness_mean',
    'concavity_mean',
    'concave points_mean',
    'symmetry_mean'
]

'''
Using Model to Predict Breast Cancer
'''
def predict():
    #get features from user
    details = []
    for entry in entries:
        details.append(float(entry.get()))

    
    #pre-processing data
    X = np.array([details], dtype=float)

    #predicting the result
    result = model.predict(X)
    result = result[0]

    return result


'''
GRAPHICAL INTERFACE
'''
def displayResult():

    #get the result
    result = predict()

    #displaying result
    if result == 0:
        messagebox.showinfo("Result", "The patient does not have breast cancer")
    else:
        messagebox.showinfo("Result", "The patient has breast cancer")


def predictScreen():

    #removing previous window
    home.destroy()

    #initializing window
    predict = Tk()
    predict.title("Breast Cancer Prediction")
    predict.configure(background='black')
    predict.geometry("600x600")

    #display main text
    mainText = Label(predict, text="Enter the following details", font=("Arial", 20), bg='black', fg='white',pady=30)
    mainText.grid(row=0, column=0, columnspan=2)

    #store the entries globally so they can be accessed by predict function
    global entries
    entries = []

    for i,feature in enumerate(features): #require both index and feature name for each label and entry
        
        #display feature text
        label = Label(predict, text=feature, font=("Arial", 15), bg='black', fg='white')
        label.grid(row=i+1,column=0,pady=5)

        #creating entry
        entry = Entry(predict, font=("Arial", 15), bg='black', fg='white')
        entry.grid(row=i+1,column=1)
        entries.append(entry)

    #Submit button
    button = Button(predict, text="Submit", font=("Arial", 20), bg='black', fg='lime green',command=displayResult)
    button.grid(row=12,column=1,columnspan=2,pady=20)

def homeScreen():

    #initializing window
    global home
    home = Tk()
    home.title("Breast Cancer Prediction")
    home.configure(background='black')
    home.geometry("400x400")

    #display Title
    Label(home, text="Breast Cancer Prediction", font=("Arial", 20), bg='black', fg='white').pack(pady=20)

    #creating button
    Button(home, text="Predict", font=("Arial", 20), bg='black', fg='white', command=predictScreen).pack(pady=20)

    #running the main window
    home.mainloop()
    

'''
MAIN PROGRAM
'''
if __name__ == '__main__':
    homeScreen()
 
