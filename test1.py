from datetime import datetime
import pandas as pd
import csv
import numpy as np
import os

PATH = './student.csv'
labels = ['Rollno', 'Name', 'Date', 'Time', 'Marks']
ADMIN_PASSWORD = 'pass'

def add_data(data):
    df = pd.DataFrame(data)
    if os.path.exists(PATH):        #if path exists firstly
        df.to_csv(PATH, index=False, mode='a', header=0)
    else:
        df.to_csv(PATH, index=False, mode='w')

def read_data():
    try:
        df = pd.read_csv(PATH)
        return df
    except pd.errors.EmptyDataError:   #search exception pandas.errors.EmptyDataError[source]
        print("No data is present!")
        return None
    except FileNotFoundError:
        print('No CSV file exists!')
        return None

def update_data():
    df = read_data()
    if df is None: return
    print('Do you want to update name(1) or rollno(2) ?')
    c=int(input())
    if(c==1):                        #with name
        print("Type the name which is to be changed:")
        sname=input()
        print("Type the new name:")
        rname=input()
        df.to_csv(PATH, index=False, mode='a')
        col='Name'
        #df.loc[df['Name']==sname]=rname
        df[col].replace(sname, rname ,inplace=True)
        df.to_csv('student.csv', index=False) 
        print(df)
    elif(c==2):                                 #with rollno
        print("Type the roll no which is to be changed:")
        srollno=int(input())
        print("Type the new roll no:")
        rrollno=int(input())
        df.to_csv(PATH, index=False, mode='a')
        col='Rollno'
        df[col].replace(srollno, rrollno ,inplace=True)
        df.to_csv('student.csv', index=False) 
        print(df) 

def delete_data():
    df = read_data()
    if df is None: return
    print("Enter the roll no whose data you want to be deleted:")
    newDf = df[~df.Rollno.isin([input()])]
    os.remove(PATH)
    newDf.to_csv(PATH, index=False)


#Yeh main function hai
print("Welcome to Student Management System")
print('ENTER PASSWORD')
adminPass = input()
if(adminPass == ADMIN_PASSWORD):
    print('WELCOME ADMIN')
    roll_no = []
    stud = []
    dates = []     #D.O.admission
    times = []
    mark = []
    while(True):
        print("1)Add Data\n2)Read Data\n3)Update Data\n4)Delete Data\n5)Exit!!")
        x = int(input("Enter your choice:"))
        if(x==1):
            num = int(input("How many students you want to add?: "))
            for i in range(num):
                number = input("Input roll no. of the student: ")
                roll_no.append(number)
                name = input("Input name of student: ")
                stud.append(name)
                date = datetime.now().strftime('%d/%m/%y')
                dates.append(date)
                time = datetime.now().strftime('%H:%M')
                times.append(time)
                marks = input("Enter marks: ")
                mark.append(marks)
            dict = {
            labels[0]: roll_no, 
            labels[1]: stud,
            labels[2]: dates,
            labels[3]: times,
            labels[4]: mark
            }
            add_data(dict)
        elif(x==2):
            print(read_data())
        
        elif(x==3):
            update_data() 

        elif(x==4):
            delete_data()

        elif(x==5):
            break
        
        else:
            print("Invalid input!")
        

else:
    print('enter a valid password!')








