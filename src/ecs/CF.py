def Cf(str_flavor_need_dict, flavor_num, last_first, last_second, first_dict, second_dict, range_num):
    flavor_need_dict = eval(str_flavor_need_dict)
    start_num = int(flavor_num) - 1
    end_num = 0
    flavor_result = []
    flavor_result.append('General-1')
    first_left = last_first
    second_left = last_second
    total = 0
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
                    total += first_left
                    tt = flavor_result[-1].split(" ")
                    tt_t = tt[0].split('-')
                    ttt = int(tt_t[1]) + 1
                    flavor_result.append("General-" + str(ttt))
                    first_left = last_first
                    second_left = last_second
                    break
            continue
        for i in range(range_num):
            
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
                total += first_left
                tt = flavor_result[-1].split(" ")
                tt_t = tt[0].split('-')
                ttt = int(tt_t[1]) + 1
                flavor_result.append("General-" + str(ttt))
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
                total += first_left
                tt = flavor_result[-1].split(" ")
                tt_t = tt[0].split('-')

                ttt = int(tt_t[1]) + 1
                flavor_result.append("General-" + str(ttt))
                first_left = last_first
                second_left = last_second

        tt = flavor_result[-1].split(" ")
        tt_t = tt[0].split('-')
        ttt = int(tt_t[1])
    return flavor_result, total, ttt