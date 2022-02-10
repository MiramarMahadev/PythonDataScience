import pandas as pd
import matplotlib.pyplot as mt
file = pd.read_csv('bollywood-1.csv')
end = ('\n\n'+"-"*100)   #for creating a dash line for differentiating solutions
print(end)      #differentiating line for my convineince 

# 1)How many records are present in the datasheet?
print(f"\n1)Number of records present in the datasheet are {file.shape[0]}{end}")

# 2)How many movies were released in each Release Time? Sort number of releases in Release Time in descending order.
file['Movies Released'] = 1
second = file.groupby('ReleaseTime').sum('Movies Released')
second =second.sort_values(['Movies Released'])['Movies Released']
print(f'\n2)Number of movies released in each Release Time : {second}{end}')

# 3)Which genre had highest number of releases during the Festive Season?
third = file.groupby('Genre').sum('Movies Released')
third = third.sort_values(['Movies Released'],ascending=False)
print(f'\n3)Genre with highest number of releases during the Festive Season is {third.index[0]}{end}')

# 4)How many movies in each genre got released in different release times
fourth = pd.crosstab(file['Genre'],file['ReleaseTime'])
print(f'\n4)Number of movies of each genre released in different release times:\n\n{fourth}{end}')

# 5)In which year were maximum number movie released? 
file['Year'] = '20' + file['Release Date'].apply(lambda x: x.split('-')[2])
fifth = file.groupby('Year').sum('Movies Released')
fifth1 = fifth.sort_values(['Movies Released'],ascending=False)['Movies Released']
print(f'\n5)The year in which maximum movies were released is {fifth1.index[0]}{end}')

# 6)Which month sees most releases of high budgeted movies(budget >= 30 crore)?
file['Month'] = file['Release Date'].apply(lambda x: x.split('-')[1])
file['High Budget'] = [1 if i >= 30 else 0 for i in file.Budget]
sixth = file.groupby('Month').sum('High Budget')
sixth = sixth.sort_values(['High Budget'],ascending=False)['High Budget']
print(f'\n6)The month which sees most releases of high budgeted movies is {sixth.index[0]}{end}')

# 7)Which are the top 10 flop movies with minimum return on investment (ROI)?alculate return on investment (ROI) as (Box0fficeCollection - Budget) / Budget. 
file['ROI'] = file['BoxOfficeCollection'] - file['Budget'] / file['Budget']
seventh = file.sort_values(['ROI'])
print(f'\n7)The top 10 flop movies with minimum return on investment (ROI)\n\n{seventh.reset_index(drop=True).iloc[:10,[2,14]]}{end}')

# 8)Do the movies have higher ROI if they get released on festive seasons or longweekend? Calculate the average ROI for different release times.
eighth = file.groupby('ReleaseTime').sum('ROI')
eighth['Average ROI'] = eighth['ROI']/eighth['Movies Released']
print(f'\n8)The average ROI for different release times {eighth.iloc[:,9]}\n\nYes,movies have higher ROI if they get released on festive seasons or longweekend.\n{end}')

# 9)Is there a correlation between box office collection and YouTube likes? Is the correlation positive or negative?
ninth = file.drop(file.columns[[0,1,2,3,4,10,11,12,13,14]],axis=1)
ninth = ninth.corr()
x = ninth.iloc[1,3]
if x > 0: sign = 'Positive' 
elif x < 0: sign = 'Negative' 
else : sign = 0
print(f'\n{ninth}\n\n9)Yes,there is a correlation between box office collection and YouTube likes which is {x}. Hence, {sign}{end}')      
 
# 10)Which genre of movies typically sees more YouTube views? Draw boxplots for each genre of movies to compare.
print(f'\n10)Action,Thriller,Romance typically see more YouTube views{end}')
lab10 = list(set(file['Genre']))
g = ['sa','c','d','r','a','st','t']
for i in range(len(lab10)):
    g[i] = [ ]
    g[i] += list(file[file['Genre'] == lab10[i]]['YoutubeViews'])
mt.boxplot([g[i] for i in range(len(lab10))],labels=lab10)
mt.title("10) Genre vs Youtube Views")
mt.xlabel("Genre")
mt.ylabel("Youtube Views(x10⁷)")
mt.show()

# 11)Which of the variables among Budget, BoxOfficeCollection, YoutubeView, YoutubeLikes, YoutubeDislikes are highly correlated? Draw pair plot or heatmap.
lab11 = ninth.columns[[0,1,2,3,4]]
mt.imshow(ninth, cmap = 'autumn', interpolation = 'nearest',)
mt.title("11)Variable's correlation Heat Map")
mt.yticks(range(len(lab11)),lab11)
mt.xticks(range(len(lab11)),lab11,rotation=90)
mt.show()
print(f'\n11)YoutubeViews, YoutubeLikes are highly correlated{end}')

# 12)During 2013-2015 period, highlight the genre of movies and their box office collection? Visualize with best fit graph.
twelfth = file.groupby('Genre').sum('Box Office Collection')
t = twelfth['BoxOfficeCollection']
lab12 = list(twelfth.index[:])
print(f'\n12)The genre of movies and their box office collection\n{t}{end}')
mt.bar(lab12,list(t))
mt.title("12) Genre vs Box Office Collection")
mt.xlabel("Genre")
mt.ylabel("Box Office Collection")
mt.show()

# 13)During 2013-2015, find the number of movies released in every year. Also, visualize with best fit graph. 
thirteen = fifth['Movies Released']
lab13 = list(fifth.index[:])
print(f'\n13)Number of movies released in every year\n{thirteen}{end}')
mt.bar(lab13,thirteen)
mt.yticks(range(70)[::5])
mt.title("13) Year vs Movies Released")
mt.xlabel("Year")
mt.ylabel("Movies Released")
mt.show()

# 14)Find the distribution of movie budget for every Genre. 
fourteenth = file.groupby('Genre').sum('Budget')['Budget']
lab12 = list(fourteenth.index[:])
mt.pie(fourteenth,explode=(0,0,0.1,0,0,0,0.1),labels=lab12,autopct='%.2f %%')
mt.title("14) Distribution of movie budget for every Genre")
mt.show()
print(f'\n14)Distribution of movie budget for every Genre\n{fourteenth}{end}')

# 15)During 2013-2015, Visualize the number of YouTube likes and YouTube dislikes every year. Also, visualize with best fit graph.
fifteenth = file.groupby('Year').sum('Youtube Likes')
lab15 = list(fifteenth.index[:])
print(f'\n15)The number of YouTube likes and YouTube dislikes every year\n{fifteenth.iloc[:,[4,5]]}{end}')
mt.plot(lab15,fifteenth.iloc[:,4],'b*-')
mt.plot(lab15,fifteenth.iloc[:,5],'r*-')
mt.legend(['Youtube Likes','Youtube dislikes'])
mt.title("15) Youtube Likes vs Youtube dislikes every year")
mt.xlabel("Year")
mt.ylabel("count")
mt.show()
print()  #differentiating line for my convineince 