import numpy as np
import math
from collections import Counter
from scipy import stats

def listify(data):
    data_list = data.split(',') #Split string by commas
    for a in data_list: #Convwert all values to floats
        a = float(a)
    data_list = np.array(data_list, dtype = 'float_') #Turn list into an array
    return data_list
    
def single_data(data):
    data_list = listify(data)
    total = math.fsum(data_list)
    average = total/len(data_list)
    mode = stats.mode(data_list)
    if (len(data_list) % 2) != 0:
        median = data_list[(len(data_list) - 1) / 2]
    else:
        median = (data_list[len(data_list)/2] + data_list[len(data_list) - 1]) / 2
    stdev = np.std(data_list)
    var = np.var(data_list)
    n = len(data)
    mini = min(data_list)
    maxi = max(data_list)
    return 'Mean: '+str(average)+ '\n'+'Median: '+str(median)+'\n'+'Mode: '+str(mode[1])+'\n'+'Minimum: '+str(mini)+'\n'+'Maximum: '+str(maxi)+'\n'+'n: '+str(n)+'\n'+'Standard Deviation: '+str(stdev)+'\n'+'Variance: '+str(var)
    
def data_a(data1, data2, dependent, tails):
    data1_list = listify(data1)
    data2_list = listify(data2)
    data1_a = single_data(data1)
    data2_a = []
    if len(data2_list) == 1:
        results = stats.ttest_1samp(data1_list, data2_list[0])
    elif len(data2_list) == 0:
        p_value = 'None'
    else:
        data2_a = single_data(data2)
        if dependent == 'independ':
            results = stats.ttest_ind(data1_list, data2_list)
        else: 
            results = stats.ttest_rel(data1_list, data2_list)
    if tails == 2:
        p_value = results[0]
    else:
        p_value = results[0] / 2
    return ['p-value: '+str(p_value)+ '\n', 'Data Set 1: '+ data1_a, 'Data Set 2: '+data2_a]