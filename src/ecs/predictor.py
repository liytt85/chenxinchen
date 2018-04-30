from CF import Cf
from NEW_CF import new_Cf
from plandict import plandict


def predict_vm(ecs_lines, input_lines):
    # Do your work from here#
    result = []
    if ecs_lines is None:
        print 'ecs information is none'
        return result
    if input_lines is None:
        print 'input file information is none'
        return result
    day_num = 0
    
    
    result_dict = {}
    flavor_dict = {}
    
    day_shunxu = []
    add_num = 0
    time_call_dict = {}
    day_call = 0
    # ji suan zong gong tian shu
    for item in ecs_lines:
        values = item.split("\t")
        #uuid = values[0]
        createTime_1 = values[2]
        createTime_s_1 = createTime_1.split(' ')
        if (createTime_s_1[0] == '2012-01-22' or createTime_s_1[0] == '2013-02-09' or createTime_s_1[0] == '2014-01-30' or createTime_s_1[0] == '2015-02-18' or createTime_s_1[0] == '2016-02-07' or createTime_s_1[0] == '2017-01-27'):
            add_num = -1
            continue
        if (time_call_dict.has_key(createTime_s_1[0])):
            pass
        else:
            day_call += 1
            time_call_dict[createTime_s_1[0]] = 0
    second_exp = {}
    day_eft = float(6) / float(day_call)
    arf = float(25.95) / float(day_call)

    for item in ecs_lines:
        
        values = item.split("\t")
        createTime = values[2]
        createTime_s = createTime.split(' ')
        if (createTime_s[0] == '2012-01-22' or createTime_s[0] == '2013-02-09' or createTime_s[0] == '2014-01-30' or createTime_s[0] == '2015-02-18' or createTime_s[0] == '2016-02-07' or createTime_s[0] == '2017-01-27'):
            add_num = -1
            continue

        uuid = values[0]
        flavorName = values[1]
        if (day_num == day_call - 2):
            result_dict_str = str(result_dict)
        if result_dict.has_key(flavorName):
            result_dict[flavorName] += 1 * day_eft * (1 - day_eft) ** (day_call - day_num - 1)
        else:
            result_dict[flavorName] = 1 * day_eft * (1 - day_eft) ** (day_call - day_num - 1) +  (1 - day_eft) ** (day_call - day_num - 1)
        
        if (flavor_dict.has_key(createTime_s[0])):
            if (flavor_dict[createTime_s[0]].has_key(flavorName)):
                flavor_dict[createTime_s[0]][flavorName] += 1
            else:
                flavor_dict[createTime_s[0]][flavorName] = 1
        else:
            day_shunxu.append(createTime_s[0])
            day_num += 1
            second_exp = result_dict
            '''if (day_num > int(day_call * 0.39)):
                day_eft = 2 + 2 * arf'''
            flavor_dict[createTime_s[0]] = {}
    print result_dict
    new_result_dict_str = str(result_dict)


    train_day_len = len(flavor_dict)

    #hua tu



    huatu_flavor_dict = str(flavor_dict)

    

    add_num = 0
    for items in result_dict:
        if (result_dict[items] < 0):
            result_dict[items] = 0
        
        result_dict[items] = (float(result_dict[items]))



    # print input_lines
    pc = []
    flavor_need = []
    time_need = []

    flavor_num = 0

    for items in input_lines:
        fuwuqi_num = items
        del input_lines[0]
        break
    for items in input_lines:
        if (items == '\r\n'):
            break
        items_s = items.split('\r\n')
        pc.append(items_s[0])
    while (input_lines[0] != '\r\n'):
        del input_lines[0]
    while (input_lines[0] == '\r\n'):
        del input_lines[0]
    print "pc fjskjfkjsdkjf",pc
    for items in input_lines:
        flavor_num = items
        del input_lines[0]
        break
    for items in input_lines:
        if (items == '\r\n'):
            break
        items_s = items.split('\r\n')
        flavor_need.append(items_s[0])
    while (input_lines[0] != '\r\n'):
        print input_lines[0]
        del input_lines[0]
    while (input_lines[0] == '\r\n'):
        print input_lines[0]
        del input_lines[0]
    
    
    while (input_lines[0] == '\r\n'):
        del input_lines[0]
    print flavor_need
    time_min_need = []
    for items in input_lines:
        if (items != '\r\n'):
            items_s = items.split('\r\n')
            time_need.append(items_s[0])
            #time_min_need.append(items_s[1])
    print time_need
    '''print pc  # fu wu qi gui ge
                print flavor_need  # xu qiu de xu ni ji
                print time_need  # yu ce de shi jian

                print caple_class  # yu ce de zi yuan lei xing
                print flavor_num  # zong gong xu ni ji xu qiu'''

    # split our need data
    last_flavor = []
    last_flavor_cpu = []
    last_flavor_mem = []
    last_time_need = []
    print "dfsfdsf", pc
    pc_data = {}
    for items in pc:
        items_s = items.split(' ')
        pc_data[items_s[0]] = []
        pc_data[items_s[0]].append(int(items_s[1]))
        pc_data[items_s[0]].append(int(items_s[2]) * 1024)
    print "pc_data", pc_data
    for items in flavor_need:
        items_s = items.split(' ')
        last_flavor.append(items_s[0])
        last_flavor_cpu.append(int(items_s[1]))
        last_flavor_mem.append(int(items_s[2]))
    for items in time_need:
        items_s = items.split(' ')
        time_min_need.append(items_s[1])
        items_s_s = items_s[0].split('-')
        last_time_need.append(int(items_s_s[0]))
        last_time_need.append(int(items_s_s[1]))
        last_time_need.append(int(items_s_s[2]))
    last_pc = pc_data
    print "time_min_need", time_min_need
    
    print "result_dict: ", result_dict
    print "last_pc: ", last_pc  # fu wu qi gui ge
    str_last_pc = str(last_pc)
    print "flavor_need: ", flavor_need  # xu qiu de xu ni ji
    print "time_need: ", time_need  # yu ce de shi jian

    
    print "flavor_num: ", flavor_num  # zong gong xu ni ji xu qiu
    print "train_day_len: ", train_day_len
    print "flavor_dict: ", flavor_dict
    print "last_flavor: ", last_flavor
    print "last_flavor_cpu: ", last_flavor_cpu
    print "last_flavor_mem: ", last_flavor_mem
    print "last_time_need: ", last_time_need

    # fen pei wu li fu wu qi

    # she zhi liang ge dict , zuo  zi yuan pai xu
    cpu_dict = {}
    mem_dict = {}
    for i in range(int(flavor_num)):
        cpu_dict[last_flavor[i]] = last_flavor_cpu[i]
        mem_dict[last_flavor[i]] = last_flavor_mem[i]
    #print cpu_dict, mem_dict
    last_cpu_dict = sorted(cpu_dict.items(), key=lambda item: item[1])
    last_mem_dict = sorted(mem_dict.items(), key=lambda item: item[1])
    #print last_cpu_dict, last_mem_dict

    '''if (caple_class == 'CPU'):
        last_first = last_pc[0]
        last_second = last_pc[1]
        first_dict = last_cpu_dict
        second_dict = mem_dict
    else:'''
    print "cpu_dict", cpu_dict
    print "mem_dict", mem_dict

    # qiu yu ce de tian shu
    last_day_need = 11.6
    #last_time_need = [2013, 12,12,2014,1,23]
    year_gap = last_time_need[3] - last_time_need[0]
    month_gap = last_time_need[4] - last_time_need[1]
    day_gap = last_time_need[5] - last_time_need[2]
    if (year_gap == 1):
        last_day_need = 31 - last_time_need[2] + 1 + last_time_need[5]
    elif (month_gap == 0):
        last_day_need = day_gap + 1
    else:
        if (last_time_need[1] == 2):
            if (last_time_need[0] == 2016 or last_time_need[0] == 2012):
                last_day_need = 29 - last_time_need[2] + 1 + last_time_need[5]
            else:
                last_day_need = 28 - last_time_need[2] + 1 + last_time_need[5]
        elif (last_time_need[1] == 2 or last_time_need[1] ==4 or last_time_need[1] == 6 or last_time_need[1] == 9 or last_time_need[1] == 11):
            last_day_need = 30 - last_time_need[2] + 1 + last_time_need[5]
        else:
            last_day_need = 31 - last_time_need[2] + 1 + last_time_need[5]
    print last_day_need



    result_dict_part = eval(result_dict_str)
    add_num = 0
    
    for key in result_dict:
        #result_dict[key] *= last_day_need / day_call
        if (result_dict_part.has_key(key)):
            add_num = result_dict[key] - result_dict_part[key]
        else:
            add_num = result_dict[key]
        
        result_dict[key] *= float(last_day_need + 13) / day_call
        
        result_dict[key] = int(result_dict[key] - add_num)
    for items in result_dict:
        if (result_dict[items] < 0):
            result_dict[items] = 0
        
        #result_dict[items] = (float(result_dict[items]))
    flavor_need_dict = {}
    new_result_dict = eval(new_result_dict_str)
    all_flavor_num = 0
    for items in last_flavor:
        flavor_need_dict[items] = int(arf * (2 * new_result_dict[items] - second_exp[items]) * last_day_need + day_eft / (1 - day_eft) * (new_result_dict[items] - second_exp[items]) * (last_day_need + 1) / 2)
        all_flavor_num += flavor_need_dict[items]
    #xin de yu ce jie guo
    flavor_need_dict = plandict(huatu_flavor_dict, day_shunxu, day_call, last_flavor, flavor_need_dict)
            
            
            
    all_flavor_num = 0        
    for item in flavor_need_dict:
        flavor_need_dict[item] = int(flavor_need_dict[item] * last_day_need)
        all_flavor_num += flavor_need_dict[item]





    #print "flavor need dict", flavor_need_dict
    new_flavor_need_dict = str(flavor_need_dict)
    #new way


    str_flavor_need_dict = str(flavor_need_dict)
    #new_flavor_result = Bfd(str_flavor_need_dict, flavor_num, last_first, last_second, first_dict, second_dict)

    print "str_flavor", str_flavor_need_dict
    #result_store = []
    print "last_cpu", last_cpu_dict
    last_first = last_pc['General'][1]
    last_second = last_pc['General'][0]
    first_dict = last_mem_dict
    second_dict = cpu_dict
    result_i_len = 0
    min_bin = 10000
    total_left = 0
    pc_num = 0
    for i in range(30):

        result_i, total, pc_num_f= Cf(str_flavor_need_dict, flavor_num, last_first, last_second, first_dict, second_dict, i)
        result_i_len = len(result_i)
        if (result_i_len < min_bin):
            result_store = result_i
            min_bin = result_i_len
            total_left = total
            pc_num = pc_num_f
    first_result = result_store
        #print 'result_store', result_store
    '''new_flavor_result, total_left_1 = new_Bfd(str_flavor_need_dict, flavor_num, last_first, last_second, first_dict, second_dict)'''

    '''num1 = len(new_flavor_result)
    num2 = len(result_store)
    if (num1 <= num2):
        #result.append(num1)
        first_result = new_flavor_result
    else:
        #result.append(num2)
        first_result = result_store'''

    last_first = last_pc['General'][0]
    last_second = last_pc['General'][1]
    first_dict = last_cpu_dict
    second_dict = mem_dict
    result_i_len = 0
    min_bin = 10000
    total_left = 0
    pc_num_1 = 0
    for i in range(30):

        result_i, total, pc_num_f= Cf(str_flavor_need_dict, flavor_num, last_first, last_second, first_dict, second_dict, i)
        result_i_len = len(result_i)
        if (result_i_len < min_bin):
            result_store = result_i
            min_bin = result_i_len
            total_left = total
            pc_num_1 = pc_num_f
    second_result = result_store
    '''new_flavor_result, total_left_1 = new_Bfd(str_flavor_need_dict, flavor_num, last_first, last_second, first_dict, second_dict)
    num1 = len(new_flavor_result)
    num2 = len(result_store)
    if (num1 <= num2):
        #result.append(num1)
        second_result = new_flavor_result
    else:
        #result.append(num2)
        second_result = result_store'''
   #---------------------------
    '''start_num = int(flavor_num) - 1
    end_num = 0
    flavor_result = []
    flavor_result.append('1')
    first_left = last_first
    second_left = last_second
    
    while (end_num < start_num):

        
        pre_name = first_dict[start_num][0]
        while (flavor_need_dict[pre_name] == 0 and end_num < start_num):
            start_num -= 1
            pre_name = first_dict[start_num][0]
        if (end_num == start_num):
            break
        pre_first_need = first_dict[start_num][1]
        pre_second_need = second_dict[pre_name]
        if (pre_first_need <= first_left and pre_second_need <= second_left):
            flavor_result[-1] = flavor_result[-1] + " " + pre_name + " " + '1'
            first_left -= pre_first_need
            second_left -= pre_second_need
            flavor_need_dict[pre_name] -= 1
        else:
            while (1):
                pred_name = first_dict[end_num][0]
                while (flavor_need_dict[pred_name] == 0 and end_num < start_num):
                    end_num += 1
                    pred_name = first_dict[end_num][0]
                if (end_num == start_num):
                    break
                pred_first_need = first_dict[end_num][1]
                pred_second_need = second_dict[pred_name]
                if (pred_first_need <= first_left and pred_second_need <= second_left):
                    flavor_result[-1] = flavor_result[-1] + \
                        " " + pred_name + " " + "1"
                    first_left -= pred_first_need
                    second_left -= pred_second_need
                    flavor_need_dict[pred_name] -= 1
                else:
                    tt = flavor_result[-1].split(" ")
                    ttt = int(tt[0]) + 1
                    flavor_result.append(str(ttt))
                    first_left = last_first
                    second_left = last_second
                    break
            continue
        for i in range(6):
            
            bac_name = first_dict[end_num][0]
            while (flavor_need_dict[bac_name] == 0 and end_num < start_num):
                end_num += 1
                bac_name = first_dict[end_num][0]
            if (end_num == start_num):
                break
            bac_first_need = first_dict[end_num][1]
            bac_second_need = second_dict[bac_name]
            if (bac_first_need <= first_left and bac_second_need <= second_left):
                flavor_result[-1] = flavor_result[-1] + \
                    " " + bac_name + " " + "1"
                first_left -= bac_first_need
                second_left -= bac_second_need
                flavor_need_dict[bac_name] -= 1
            else:
                tt = flavor_result[-1].split(" ")
                ttt = int(tt[0]) + 1
                flavor_result.append(str(ttt))
                first_left = last_first
                second_left = last_second
                break

    
    if (end_num == start_num):
        last_name = first_dict[start_num][0]
        while (flavor_need_dict[last_name] != 0):
            last_first_need = first_dict[start_num][1]
            last_second_need = second_dict[last_name]
            if (last_first_need <= first_left and last_second_need <= second_left):
                flavor_result[-1] = flavor_result[-1] + \
                    " " + last_name + " " + "1"
                first_left -= last_first_need
                second_left -= last_second_need
                flavor_need_dict[last_name] -= 1
            else:
                tt = flavor_result[-1].split(" ")
                ttt = int(tt[0]) + 1
                flavor_result.append(str(ttt))
                first_left = last_first
                second_left = last_second
                # zuo yi ge you xi'''
    
    #flavor_result = result_store


    new_result = new_Cf(str_flavor_need_dict, cpu_dict, mem_dict, flavor_num, str_last_pc)
    #-------------------------
    result.append(all_flavor_num)
    for key in flavor_need_dict:
        result.append(key + ' ' + str(flavor_need_dict[key]))
    result.append('\r')
    
    num1 = len(first_result)
    num2 = len(second_result)
    if (num1 <= num2):
        result.append("General" + " " + str(pc_num))
    
        
        result = result + first_result
    else:
        result.append("General" + " " + str(pc_num_1))
    
        
        result = result + second_result
    
    #print new_flavor_result
    #print flavor_result
    #ce shi ke gai jin lv
    #print float(total_left) / (num2 * last_first)
    #result.append(num2)
    #result = result + flavor_result
    return result
