
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
    for item in ecs_lines:
        day_num += 1
        values = item.split("\t")
        uuid = values[0]
        flavorName = values[1]
        if result_dict.has_key(flavorName):
            result_dict[flavorName] += 1
        else:
            result_dict[flavorName] = 1
        createTime = values[2]
        createTime_s = createTime.split(' ')
        if (flavor_dict.has_key(createTime_s[0])):
            if (flavor_dict[createTime_s[0]].has_key(flavorName)):
                flavor_dict[createTime_s[0]][flavorName] += 1
            else:
                flavor_dict[createTime_s[0]][flavorName] = 1
        else:
            flavor_dict[createTime_s[0]] = {}
    print result_dict

    train_day_len = len(flavor_dict)

    add_num = 0
    for items in result_dict:
        if (result_dict[items] > train_day_len / 2):
            add_num = 1
        result_dict[items] = float(result_dict[items]) / train_day_len

    # print result_dict
    '''for index, item in input_lines:
                    print "index of input data"'''

    # print input_lines
    pc = []
    flavor_need = []
    time_need = []

    flavor_num = 0

    for items in input_lines:

        if (items == '\r\n'):
            break
        items_s = items.split('\r\n')
        pc.append(items_s[0])
    while (input_lines[0] != '\r\n'):
        del input_lines[0]
    while (input_lines[0] == '\r\n'):
        del input_lines[0]
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
        del input_lines[0]
    while (input_lines[0] == '\r\n'):
        del input_lines[0]
    caple_class = input_lines[0]
    del input_lines[0]
    while (input_lines[0] == '\r\n'):
        del input_lines[0]
    for items in input_lines:
        items_s = items.split('\r\n')
        time_need.append(items_s[0])

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
    for items in pc:
        items_s = items.split(' ')
        cpu_num = int(items_s[0])
        mem_num = int(items_s[1])
    for items in flavor_need:
        items_s = items.split(' ')
        last_flavor.append(items_s[0])
        last_flavor_cpu.append(int(items_s[1]))
        last_flavor_mem.append(int(items_s[2]))
    for items in time_need:
        items_s = items.split(' ')
        items_s_s = items_s[0].split('-')
        last_time_need.append(int(items_s_s[0]))
        last_time_need.append(int(items_s_s[1]))
        last_time_need.append(int(items_s_s[2]))
    last_pc = []
    for items in pc:
        items_s = items.split(' ')
        last_pc.append(int(items_s[0]))
        last_pc.append(int(items_s[1]) * 1024)
        last_pc.append(int(items_s[2]))
    print "result_dict: ", result_dict
    print "last_pc: ", last_pc  # fu wu qi gui ge
    print "flavor_need: ", flavor_need  # xu qiu de xu ni ji
    print "time_need: ", time_need  # yu ce de shi jian

    print "caple_class: ", caple_class  # yu ce de zi yuan lei xing
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

    if (caple_class == 'cpu'):
        last_first = last_pc[0]
        last_second = last_pc[1]
        first_dict = last_cpu_dict
        second_dict = mem_dict
    else:
        last_second = last_pc[0]
        last_first = last_pc[1]
        second_dict = cpu_dict
        first_dict = last_mem_dict

    # qiu yu ce de tian shu
    last_day_need = 11.6






    for key in result_dict:
        result_dict[key] *= last_day_need
        result_dict[key] = int(result_dict[key]) + 1
    flavor_need_dict = {}

    all_flavor_num = 0
    for items in last_flavor:
        flavor_need_dict[items] = result_dict[items]
        all_flavor_num += result_dict[items]
    #print flavor_need_dict
    start_num = int(flavor_num) - 1
    end_num = 0
    flavor_result = []
    flavor_result.append('1')
    first_left = last_first
    second_left = last_second
    #print first_dict[-1][0]
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
                # zuo yi ge you xi
    
    result.append(all_flavor_num)
    for key in flavor_need_dict:
        result.append(key + ' ' + str(result_dict[key]))
    result.append('\r')
    num1 = len(flavor_result)
    result.append(num1)
    
    result = result + flavor_result
    return result
