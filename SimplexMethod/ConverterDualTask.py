def copyMatr(A):
    A_copy = list()
    for i in range(len(A)):
        A_copy.append([A[i][j] for j in range(len(A[i]))])
    return A_copy


def copyVec(A: list):
    A_copy = list()
    for i in range(len(A)):
        A_copy.append(float(A[i]))
    return A_copy


def correct_A(A_d, A_tmp):
    for i in range(len(A_tmp[0])):
        A_d.append([matrix_line[i] for matrix_line in A_tmp])


def correct_limits(A_tmp: list, b: list, limSigns: list, min_max: str):
    limitsCnt = len(limSigns)

    for i in range(limitsCnt):
        if (limSigns[i] == ">=" and min_max == "max") or (limSigns[i] == "<=" and min_max == "min"):
            if limSigns[i] == ">=":
                limSigns[i] = "<="
            else:
                limSigns[i] = ">="

            for j in range(len(A_tmp[i])):
                A_tmp[i][j] = -1 * A_tmp[i][j]
            b[i] = b[i] * -1


def correct_extr(min_max: str, valuesLimits: list, limSigns_d: list, c: list):
    if min_max == "min":
        min_max_d = "max"
        expr_d_sign = "<="
    else:
        min_max_d = "min"
        expr_d_sign = ">="

    for i in range(len(c) - 1):
        if i in valuesLimits:
            limSigns_d.append(expr_d_sign)
        else:
            limSigns_d.append("=")
    return min_max_d


def correct_valueSigns(limitsCnt, limSigns, valuesLimits_d):
    for i in range(limitsCnt):
        if limSigns[i] != '=':
            valuesLimits_d.append(i)


def manager_d(A: list, b: list, c: list, A_signs: list, min_max: str, x_signs: list):
    A_d = list()
    A_signs_d = list()
    x_signs_d = list()

    A_tmp = copyMatr(A)

    correct_limits(A_tmp, b, A_signs, min_max)
    min_max_d = correct_extr(min_max, x_signs, A_signs_d, c)
    correct_A(A_d, A_tmp)
    c_d = b
    b_d = c[:len(c) - 1]
    correct_valueSigns(len(A_signs), A_signs, x_signs_d)

    return A_d, b_d, c_d, A_signs_d, min_max_d, x_signs_d
