import pandas as pd

col_names = ['Id',
             'Survived',
             'Passenger Class',
             'Full Name',
             'Gender',
             'Age',
             'SibSp',
             'Parch',
             'Ticket Number',
             'Price', 'Cabin',
             'Station']

titanic_data = pd.read_csv(r'E:\Datasets\titanic.csv', names=col_names, skiprows=[0])
print(titanic_data.head())