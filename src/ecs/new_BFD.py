def new_Bfd(str_flavor_need_dict, flavor_num, last_first, last_second, first_dict, second_dict):
    flavor_need_dict = eval(str_flavor_need_dict)
    start_num = int (flavor_num) - 1
    flavor_left_dict = {'1':[last_first, last_second]}
    first_name = first_dict[start_num][0]
    first_need = first_dict[start_num][1]
    second_need = second_dict[first_name]
    flavor_result = ['1']
    total = 0
    while (start_num >= 0):
        caple_dict = {}
        while (start_num > 0 and flavor_need_dict[first_name] == 0):
            start_num -= 1
            first_name = first_dict[start_num][0]
            first_need = first_dict[start_num][1]
            second_need = second_dict[first_name]
        if (start_num == 0 and flavor_need_dict[first_name] == 0):
            break
        for items in flavor_left_dict:
            if (first_need <= flavor_left_dict[items][0] and second_need <= flavor_left_dict[items][1]):
                caple_dict[items] = flavor_left_dict[items][0]
        if (len(caple_dict) == 0):
            #print flavor_left_dict
            add_key = len(flavor_left_dict) + 1
            flavor_left_dict[str(add_key)] = []
            flavor_left_dict[str(add_key)].append(last_first)
            flavor_left_dict[str(add_key)].append(last_second)
            tt = flavor_result[-1].split(" ")
            ttt = int(tt[0]) + 1
            flavor_result.append(str(ttt))
            flavor_left_dict[str(ttt)][0] -= first_need
            flavor_left_dict[str(ttt)][1] -= second_need
            flavor_need_dict[first_name] -= 1
            flavor_result[-1] = flavor_result[-1] + " " + first_name + " " + '1'
            continue
        sort_tuple = sorted(caple_dict.items(), key=lambda item: item[1])
        #print sort_tuple
        change_key = sort_tuple[0][0]
        flavor_left_dict[change_key][0] -= first_need
        #print flavor_left_dict[change_key][0]
        flavor_left_dict[change_key][1] -= second_need
        flavor_need_dict[first_name] -= 1
        flavor_result[int(change_key) - 1] = flavor_result[int(change_key) - 1] + " " + first_name + " " + '1'
        #print flavor_result
    for items in flavor_left_dict:
        total += flavor_left_dict[items][0]
    return flavor_result, total