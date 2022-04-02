import statistics
from turtle import color
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

csv = pd.read_csv('StudentsPerformance.csv')

math_score = csv['math score'].tolist()
reading_score = csv['reading score'].tolist()
writing_score = csv['writing score'].tolist()

mean=[statistics.mean(math_score),statistics.mean(reading_score),statistics.mean(writing_score)]
median=[statistics.median(math_score),statistics.median(reading_score),statistics.median(writing_score)]
mode=[statistics.mode(math_score),statistics.mode(reading_score),statistics.mode(writing_score)]
stdev=[statistics.stdev(math_score),statistics.stdev(reading_score),statistics.stdev(writing_score)]

#1,2,3 = math score,reading score,writing score respectively
#in the second place 1,2,3 refers to the stdev multiplier

stdev11_start,stdev11_end = mean[0]-stdev[0],mean[0]+stdev[0]
stdev12_start,stdev12_end = mean[0]-(stdev[0]*2),mean[0]+(stdev[0]*2)
stdev13_start,stdev13_end = mean[0]-(stdev[0]*3),mean[0]+(stdev[0]*3)

stdev21_start,stdev21_end = mean[1]-stdev[1],mean[1]+stdev[1]
stdev22_start,stdev22_end = mean[1]-(stdev[1]*2),mean[1]+(stdev[1]*2)
stdev23_start,stdev23_end = mean[1]-(stdev[1]*3),mean[1]+(stdev[1]*3)

stdev31_start,stdev31_end = mean[2]-stdev[2],mean[2]+stdev[2]
stdev32_start,stdev32_end = mean[2]-(stdev[2]*2),mean[2]+(stdev[2]*2)
stdev33_start,stdev33_end = mean[2]-(stdev[2]*3),mean[2]+(stdev[2]*3)

items_inside11 = [items for items in math_score if items > stdev11_start and items < stdev11_end]
items_inside12 = [items for items in math_score if items > stdev12_start and items < stdev12_end]
items_inside13 = [items for items in math_score if items > stdev13_start and items < stdev13_end]

items_inside21 = [items for items in reading_score if items > stdev21_start and items < stdev21_end]
items_inside22 = [items for items in reading_score if items > stdev22_start and items < stdev22_end]
items_inside23 = [items for items in reading_score if items > stdev23_start and items < stdev23_end]

items_inside31 = [items for items in writing_score if items > stdev31_start and items < stdev31_end]
items_inside32 = [items for items in writing_score if items > stdev32_start and items < stdev32_end]
items_inside33 = [items for items in writing_score if items > stdev33_start and items < stdev33_end]

print('mean of math score is {}'.format(mean[0]))
print('mean of reading score is {}'.format(mean[1]))
print('mean of writing score is {}'.format(mean[2]))

print('median of math score is {}'.format(median[0]))
print('median of reading score is {}'.format(median[1]))
print('median of writing score is {}'.format(median[2]))

print('mode of math score is {}'.format(mode[0]))
print('mode of reading score is {}'.format(mode[1]))
print('mode of writing score is {}'.format(mode[2]))

print('stdev of math score is {}'.format(stdev[0]))
print('stdev of reading score is {}'.format(stdev[1]))
print('stdev of writing score is {}'.format(stdev[2]))

print('{}% of math score is inside stdev'.format((len(items_inside11)/len(math_score))*100))
print('{}% of math score is inside stdev2'.format((len(items_inside12)/len(math_score))*100))
print('{}% of math score is inside stdev3\n'.format((len(items_inside13)/len(math_score))*100))

print('{}% of reading score is inside stdev1'.format((len(items_inside21)/len(reading_score))*100))
print('{}% of reading score is inside stdev2'.format((len(items_inside22)/len(reading_score))*100))
print('{}% of reading score is inside stdev3 \n'.format((len(items_inside23)/len(reading_score))*100))

print('{}% of writing score is inside stdev1'.format((len(items_inside31)/len(writing_score))*100))
print('{}% of writing score is inside stdev2'.format((len(items_inside32)/len(writing_score))*100))
print('{}% of writing score is inside stdev3\n'.format((len(items_inside33)/len(writing_score))*100))

def visualization():
    dist=ff.create_distplot([math_score],['math score'],show_hist=False)
    
    #adding the traces
    dist.add_traces(data=[go.Scatter(x=[stdev11_start,stdev11_start],y=[0,0.03],name='stdev1',mode='lines'),go.Scatter(x=[stdev11_end,stdev11_end],y=[0,0.03],name='stdev1',mode='lines')])
    dist.add_traces(data=[go.Scatter(x=[stdev12_start,stdev12_start],y=[0,0.03],name='stdev2',mode='lines'),go.Scatter(x=[stdev12_end,stdev12_end],y=[0,0.03],name='stdev2',mode='lines')])
    dist.add_traces(data=[go.Scatter(x=[stdev13_start,stdev13_start],y=[0,0.03],name='stdev3',mode='lines'),go.Scatter(x=[stdev13_end,stdev13_end],y=[0,0.03],name='stdev3',mode='lines')])
    dist.add_trace(go.Scatter(x=[mean[0],mean[0]],y=[0,0.03],mode='lines',name='mean'))
    
    dist.show()

visualization()