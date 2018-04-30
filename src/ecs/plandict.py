
from quzao import Quzao
def plandict(huatu_flavor_dict, day_shunxu, day_call, last_flavor, jiu_flavor_need_dict):
    flavor_dict = eval(huatu_flavor_dict)
    #day_num = []
    i = 1
    huatu_dict = {}
    
    for items in day_shunxu:
        #day_num.append(i)
        
        for item in flavor_dict[items]:
            if (huatu_dict.has_key(item)):
                huatu_dict[item].append(flavor_dict[items][item])
            else:
                huatu_dict[item] = []
                huatu_dict[item].append(flavor_dict[items][item])
        for item in huatu_dict:
            if ( flavor_dict[items].has_key(item) == False ):
                huatu_dict[item].append(0)
    
    
    new_flavor_dict = {}
    for item in huatu_dict:
        
        lenth = len(huatu_dict[item])
        new_flavor_dict[item] = []
        if ((day_call - lenth) > 0):
            for i in range(day_call - lenth):
                new_flavor_dict[item].append(0)
        new_flavor_dict[item].extend(huatu_dict[item])
        
    last_flavor_need_data = {}
    for item in last_flavor:
        last_flavor_need_data[item] = new_flavor_dict[item]

    flavor_need_dict = {}
    for item in last_flavor:
        '''last_k_mean = 0
        last_2k_mean = 0
        last_other_mean = 0
        last_k = 0
        min_err = 1000
        last_flavor_need_data[item] = Quzao(last_flavor_need_data[item])
        length = len(last_flavor_need_data[item])
        for i in range(7, length/5 - 1):
            
            for u in range(i):
                last_k_mean += float(1.0 / i) * float(last_flavor_need_data[item][-1 *  (u + 1)])
                
                last_2k_mean += float(1.0 / i) * float(last_flavor_need_data[item][-1 *  (i + u + 1)])
            for y in range(length - 2 * i):
                last_other_mean += float(1.0 / (length - 2.0 * i)) * float(last_flavor_need_data[item][y])
            d_err = last_k_mean - (last_2k_mean * 2.0 - last_other_mean)
            d_err = absolu(d_err)
            
            if (d_err < min_err):
                min_err = d_err
                last_k = i
        print min_err
        print last_k
        last_2k_mean = 0
        last_other_mean = 0    
        for i in range(last_k):
            last_2k_mean += float(1.0 / last_k) * float(last_flavor_need_data[item][- (i + 1)])
        for i in range(length - last_k):
            last_other_mean += float(1.0 / (length - last_k)) * float(last_flavor_need_data[item][i])
        flavor_need_num  =  float(last_2k_mean * 1.5 - 0.75 * last_other_mean)

        if (flavor_need_num < 0):
            flavor_need_num = last_2k_mean + last_other_mean'''


        #one
        flavor_need_num = 0
        
        last_flavor_need_data[item] = Quzao(last_flavor_need_data[item])
        length = len(last_flavor_need_data[item])
        arf = 1.3
        day_eft = -1 * arf /(length * 1)#0.44
        for i in range (length):
            if i > (length * 0.42):
                day_eft =( 2 + arf ) / (length * 1)#1-0.44
            flavor_need_num += last_flavor_need_data[item][i] * day_eft
        '''if (flavor_need_num < 0):
            flavor_need_num = 0
        flavor_need_dict[item] = flavor_need_num'''

    #another one 

    #flavor_need_dict = jiu_flavor_need_dict.copy()
        if (flavor_need_num < 0):
            flavor_need_num = 0
        flavor_need_dict[item] = flavor_need_num
    return flavor_need_dict
def absolu(x):
    if (x >= 0):
        return x
    else:
        return -1 * x