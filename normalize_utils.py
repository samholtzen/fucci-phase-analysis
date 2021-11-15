
def find_max_value(flo_list):
    max_value = -1
    for flo_value in flo_list:
        if flo_value > max_value:
            max_value = flo_value
    return max_value


def create_flo_ratio_values(flo_list, max_value):
    flo_ratio_values = []
    for flo_value in flo_list:
        flo_ratio_values.append(flo_value / max_value)
    return flo_ratio_values


def create_flo_ratio_list(flo_expression):
    flo_ratio_list = []
    for flo_list in flo_expression:
        max_value = find_max_value(flo_list)
        flo_ratio_list.append(create_flo_ratio_values(flo_list, max_value))
    return flo_ratio_list


def find_mitosis_event(flo_expression_red, flo_expression_green):
    flo_ratio_red_list = create_flo_ratio_list(flo_expression_red)
    flo_ratio_green_list = create_flo_ratio_list(flo_expression_green)
    position_mitosis_list = []
    max_len = 0
    if len(flo_ratio_red_list) < len(flo_ratio_green_list):
        max_len = len(flo_ratio_red_list)
    else:
        max_len = len(flo_ratio_green_list)

    for i in range(max_len):
        for j in range(len(flo_ratio_red_list[i])):
            if flo_ratio_red_list[i][j] > 0.05 \
                    and flo_ratio_green_list[i][j] <= 0.05:
                position_mitosis_list.append([i, j])
                #print("position: " + str(i) + " , " + str(j))
                #print("red_ratio_value: " + str(flo_ratio_red_list[i][j]))
                #print("green_ratio_value: " + str(flo_ratio_green_list[i][j]))
                break
    return modify_final_list(flo_ratio_green_list, position_mitosis_list)


def modify_final_list(flo_ratio_green_list, position_mitosis_list):
    for element in range(len(position_mitosis_list)):
        i = position_mitosis_list[element][0]
        j = position_mitosis_list[element][1]
        updated_val = str(flo_ratio_green_list[i][j]) + "M"
        flo_ratio_green_list[i][j] = updated_val
        #print("updated_val_in_flo_green_list" + updated_val)
        #print("\n\n")
    return flo_ratio_green_list



