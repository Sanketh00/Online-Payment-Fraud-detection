import pandas as pd
import numpy as np
import seaborn as sns
import joblib
from matplotlib import pyplot as plt
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
root = Tk()
root.title("Online Payement Fraud Detection")
root.geometry("1400x850")

def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo #avoid garbage collection

image = Image.open("C:\\Users\\hp\\Desktop\\20630.jpg")
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand = YES)
#data = pd.read_csv("C:\\Users\\hp\\Desktop\\PS_20174392719_1491204439457_log.csv")
#data.dropna(inplace = True)
#data["type"] = data["type"].map({"CASH_OUT": 1, "PAYMENT": 2, 
 #                                "CASH_IN": 3, "TRANSFER": 4,
  #                               "DEBIT": 5})
#data["isFraud"] = data["isFraud"].map({0: "No Fraud", 1: "Fraud"})

def predict():
    typee=Entry_1.get()
    amount=Entry_2.get()
    oldbal=Entry_3.get()
    newbal=Entry_4.get()
    features = np.array([[int(typee), float(amount), float(oldbal), float(newbal)]])
    #out=model1.predict(features)
    model=joblib.load('fraud.sav')
    out=model.predict(features)
    if out[0]=="Fraud":
        out1="   Fraud    "
    else:
        out1="No Fraud"
    print(out)
    label_66 = ttk.Label(root, text =out1,font=("Helvetica", 20),background="#14161a",foreground="#ffffff")
    label_66.place(x = 500,y = 400)
'''from sklearn.model_selection import train_test_split
x = np.array(data[["type", "amount", "oldbalanceOrg", "newbalanceOrig"]])
y = np.array(data[["isFraud"]])
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.20, random_state=42)
from sklearn.tree import DecisionTreeClassifier
model1 = DecisionTreeClassifier()
model1.fit(xtrain, ytrain)'''
label_1 = ttk.Label(root, text ='Transcation Types\n\n1:Cash Out\n2:Payment\n3:Cash in\n4:Transfer\n5:Debit',font=("Helvetica", 16),background="white",foreground="black", borderwidth=1, relief="solid")
label_1.place(x = 700,y = 200)
label_1 = ttk.Label(root, text ='Online Payment Fraud Detection',font=("Bernard MT Condensed", 20),background="white",foreground="black")
label_1.place(x = 450,y = 50)

label_1 = ttk.Label(root, text ='Transcation Type',font=("Helvetica", 20),background="#14161a",foreground="#ffffff")
label_1.place(x = 150,y = 200)
    
Entry_1= Entry(root,borderwidth=3, relief="solid")
Entry_1.place(x = 500,y = 200)


label_2 = ttk.Label(root, text ='Transcation Amount',font=("Helvetica", 20),background="#14161a",foreground="#ffffff")
label_2.place(x = 150,y = 250)
Entry_2= Entry(root,borderwidth=3, relief="solid")
Entry_2.place(x = 500,y = 250)
label_3 = ttk.Label(root, text ='Old Balance',font=("Helvetica", 20),background="#14161a",foreground="#ffffff")
label_3.place(x = 150,y = 300)
    
Entry_3 = Entry(root,borderwidth=3, relief="solid")
Entry_3.place(x = 500,y = 300)
label_4 = ttk.Label(root, text ='New Balance',font=("Helvetica", 20),background="#14161a",foreground="#ffffff")
label_4.place(x = 150,y = 350)
    
Entry_4 = Entry(root,borderwidth=3, relief="solid")
Entry_4.place(x = 500,y = 350)

b1 = Button(root, text = 'PREDICT',font=("Helvetica", 16),background="white",command = predict,foreground="black",borderwidth=3, relief="solid")
b1.place(x = 150,y = 400)

root.mainloop()
