from textwrap import indent
from matplotlib.pyplot import axis
from numpy import positive
import pandas as pd
file = pd.read_csv('bollywood-1.csv')
end = "-"*100
print(end)   #differentiating line for my convineince 

# 1)How many records are present in the datasheet?
print(f"""1)Number of records present in the datasheet are {file.shape[0]}
{end}""")

# 2)How many movies were released in each Release Time? 
# Sort number of releases in Release Time in descending order.
file['Movies Released'] = 1
second = file.groupby('ReleaseTime').sum('Movies Released')
second =second.sort_values(['Movies Released'])['Movies Released']
print(f'''2)Number of movies released in each Release Time : {second} 
{end}''')

# 3)Which genre had highest number of releases during the Festive Season?
third = file.groupby('Genre').sum('Movies Released')
third = third.sort_values(['Movies Released'],ascending=False)
print(f'''3)Genre with highest number of releases during the Festive Season is {third.index[0]}
{end}''')

# 4)How many movies in each genre got released in different release times
# (Note: Do a cross tabulation between Genre and ReleaseTime.)
fourth = pd.crosstab(file['Genre'],file['ReleaseTime'])
print(f'''4)Number of movies of each genre released in different release times:
{fourth}
{end}''')

# 5)In which year were maximum number movie released? 
#(Note: Extract a new column called year from ReleaseDate column.) 
file['Year'] = file['Release Date'].apply(lambda x: x.split('-')[2])
fifth = file.groupby('Year').sum('Movies Released')
fifth = fifth.sort_values(['Movies Released'],ascending=False)['Movies Released']
print(f'''5)The year in which maximum movies were released is {fifth.index[0]}
{end}''')

# 6)Which month sees most releases of high budgeted movies(budget >= 30 crore)?
file['Month'] = file['Release Date'].apply(lambda x: x.split('-')[1])
file['High Budget'] = [1 if i >= 30 else 0 for i in file.Budget]
sixth = file.groupby('Month').sum('High Budget')
sixth = sixth.sort_values(['High Budget'],ascending=False)['High Budget']
print(f'''6)The month which sees most releases of high budgeted movies is {sixth.index[0]}
{end}''')

# 7)Which are the top 10 flop movies with minimum return on investment (ROI)?
#  Calculate return on investment (ROI) as (Box0fficeCollection - Budget) / Budget. 
#file['ROI'] = (file['BoxOfficeCollection'] / file['Budget'])-1
file['ROI'] = file['BoxOfficeCollection'] - file['Budget'] / file['Budget']
seventh = file.sort_values(['ROI'])
print(f'''The top 10 flop movies with minimum return on investment (ROI)
{seventh.reset_index(drop=True).iloc[:10,[2,14]]}
{end}''')

# 8)Do the movies have higher ROI if they get released on festive seasons or longweekend?
#Calculate the average ROI for different release times.
eighth = file.groupby('ReleaseTime').sum('ROI')
eighth['Average ROI'] = eighth['ROI']/eighth['Movies Released']
print(f'''8)The average ROI for different release times {eighth.iloc[:,9]}
Yes,movies have higher ROI if they get released on festive seasons or longweekend.
{end}''')

# 9)Is there a correlation between box office collection and YouTube likes?
# Is the correlation positive or negative?
ninth = file.corr()
ninth_corr = file.corr()
for i in range(ninth.shape[0]):
     for j in range(ninth.shape[1]):
        if ninth.iloc[i,j] > 0:
            ninth.iloc[i,j] = 'Positive'
        elif ninth.iloc[i,j] < 0:
            ninth.iloc[i,j] = 'Negative' 
        else :
            ninth.iloc[i,j] = 0
print(f'''9)Yes,there is a correlation between box office collection and YouTube likes which is {ninth.iloc['Box Office Collections','YouTube Likes']}
{end}''')       
print(ninth)







print()  #differentiating line for my convineince 