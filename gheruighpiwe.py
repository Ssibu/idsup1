from matplotlib import pyplot
from collections import Counter
'''years=[1950,1960,1970,1980,1990,2000,2010]
gdp=[300.2,543.2,1075.9,2862.5,5979.6,10289.7,14958.3]
pyplot.plot(years,gdp,color='red',marker='o',linestyle='--')
pyplot.title("Year and GDP")
pyplot.xlabel("years")
pyplot.show()'''
'''movies=['RRR','Bahubali','3 idiots','12th fail','Drishyam']
num_awards=[5,11,3,8,10]
pyplot.bar(movies,num_awards,color='green',edgecolor='magenta',width=0.8)
pyplot.yticks(range(20))'''
'''grades=[83,95,91,87,78,8,85,82,100,67,73,77,0]
list=[min(grade//10*10,90)for grade in grades]
print(list)
histogram=Counter(list)
print(histogram)
pyplot.bar([x+5 for x in histogram.keys()],histogram.values(),width=10)
pyplot.xticks([10*i for i in range(11)])'''
'''variance=[1,2,4,8,16,32,64,128,256]
bias_squared =[256,128,64,32,16,8,4,2,1]
total_error =[x+y for x,y in zip(variance,bias_squared)]
xs=[i for i,_ in enumerate(variance)]
pyplot.plot(xs,variance,'g-',label='variance')
pyplot.plot(xs,bias_squared,'r-',label='bias_squared')
pyplot.plot(xs,total_error,'b-',label='total_error')'''
user=[70,65,72,63,71,64,60,64,67]
minutes=[175,170,205,128,220,130,105,145,190]
website=['a','b','c','d','e','f','g','h','i']
pyplot.scatter(user,minutes)
for label,friend_count,minute_count in zip(website,user,minutes):
    pyplot.annutate(label,xy=(friend_count,minute_count),xytext=(10,-10),textcoords='offset points')

