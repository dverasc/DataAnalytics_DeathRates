##this is just grabbing the libraries I need and a print message just to confirm that it was succesful
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
print("Success")

##here I am bringing in the csv file and getting a quick peek at the first 25 rows just to get a sense of the data
df = pd.read_csv(r"C:\Users\dveras\Downloads\DeathRatesandCause_ByAllDrugs_By_Race_Ethnicity.csv")
df.head(25)

##this is where I drill down and create dataframes to reflect the categories I want to focus on (Hispanic origin, in the state of Florida)
Spanish = df[df['Hispanic Origin'] == 'Hispanic or Latino']
Spanish.head(25)
Spanish1 = Spanish[Spanish.State == 'Florida']

##the rows are categorized as either male or spanish so I am creating two separate data frames for each gender
MaleSpanish = Spanish1[Spanish1.Gender == 'Male']
FemaleSpanish = Spanish1[Spanish1.Gender == 'Female']
##Alabama = df[df.State == 'Alabama']

##visualizing the male rows
percent = MaleSpanish['Crude Rate']
year = MaleSpanish['Year']
plt.pie(percent,labels=year,autopct='%1.1f%%')
plt.axis('equal')
plt.title("Florida Male Latino Drug Death by Year")
plt.show()

##visualizing the female rows
percent = FemaleSpanish['Crude Rate']
year = FemaleSpanish['Year']
plt.pie(percent,labels=year, autopct='%1.1f%%')
plt.axis('equal')
plt.title("Florida Feale Latino Drug Death by Year")
plt.show()
