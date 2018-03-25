
def Bfd(str_flavor_need_dict, flavor_num, last_first, last_second, first_dict, second_dict):
    flavor_need_dict = eval(str_flavor_need_dict)
    start_num = int(flavor_num) - 1
    flavor_result = []
    flavor_result.append('1')
    first_left = last_first
    second_left = last_second
    pre_name = first_dict[start_num][0]
    while (start_num != 0 or flavor_need_dict[pre_name] != 0):
        while (1):
            pre_name = first_dict[start_num][0]
            while (flavor_need_dict[pre_name] == 0 and start_num > 0):
                start_num -= 1
                pre_name = first_dict[start_num][0]
            if (start_num == 0 and flavor_need_dict[pre_name] == 0):
                break
            pre_first_need = first_dict[start_num][1]
            pre_second_need = second_dict[pre_name]
            if (pre_first_need <= first_left and pre_second_need <= second_left):
                flavor_result[-1] = flavor_result[-1] + " " + pre_name + " " + '1'
                first_left -= pre_first_need
                second_left -= pre_second_need
                flavor_need_dict[pre_name] -= 1
            else:
                break
        if (start_num == 0 and flavor_need_dict[pre_name] == 0):
            break
        end_num = start_num
        while (1):
            
            
            bac_name = first_dict[end_num][0]
            while (flavor_need_dict[bac_name] == 0 and 0 < end_num):
                end_num -= 1
                bac_name = first_dict[end_num][0]
            if (end_num == 0 and flavor_need_dict[bac_name] == 0 and start_num != 0):
                tt = flavor_result[-1].split(" ")
                ttt = int(tt[0]) + 1
                flavor_result.append(str(ttt))
                first_left = last_first
                                                    
                second_left = last_second
                break
            elif (end_num == 0 and flavor_need_dict[bac_name] == 0):
                break
            else:
                bac_first_need = first_dict[end_num][1]
                bac_second_need = second_dict[bac_name]
                if (end_num == 0 and (bac_first_need > first_left or bac_second_need > second_left)):
                    tt = flavor_result[-1].split(" ")
                    ttt = int(tt[0]) + 1
                    flavor_result.append(str(ttt))
                    first_left = last_first
                    second_left = last_second
                    break

            
            
            while (bac_first_need <= first_left and bac_second_need <= second_left and flavor_need_dict[bac_name] > 0):
                #match_num = end_num
                flavor_result[-1] = flavor_result[-1] + " " + first_dict[end_num][0] + " " + '1'
                first_left -= first_dict[end_num][1]
                second_left -= second_dict[bac_name]
                flavor_need_dict[bac_name] -= 1
            end_num -= 1
            
                
                
    return flavor_result