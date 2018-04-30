import math
def Quzao(flavor_need):
    list_mean = 0
    lenth = len(flavor_need)
    dao_lenth = float(1.0 / lenth)
    k_canshu = 5


    length = 0

    for i in flavor_need:
        if i != 0:
            length += 1
        list_mean += dao_lenth * i


    etf = float(length) / float(lenth)
    sigma_f = 0
    dao_1_lenth = float(1.0 / (lenth - 1))
    for i in flavor_need:
        sigma_f += dao_1_lenth * abs(float (i - list_mean)) ** 2
    sigma_f = math.sqrt(sigma_f)
    
    delete_list = []
    
    for i in range(lenth):
        if ((flavor_need[i] - list_mean) >0 and  (flavor_need[i] - list_mean) > k_canshu * sigma_f):
            flavor_need[i] = list_mean + k_canshu * sigma_f
        elif (flavor_need[i] == 0):
            flavor_need[i] = 0.5 * list_mean

    print flavor_need






    return flavor_need
