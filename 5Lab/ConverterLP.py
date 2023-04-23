import numpy as np

'''
    The file was created to translate the LP task from the standard form to the canonical 
        one and vice versa
'''

'''
    M = M1 + M2, if a[i]x >= b, then i in M1, also if a[i]x = b, then i in M2
    N = N1 + N2, if x[i] >= 0, then i in N1, also if x[i] = 0, then i in N2
'''


def manager(c, A, b, A_signs, min_max, x_signs):
    M1, M2, N1, N2 = [], [], [], []

    for i in range(len(A_signs)):
        if A_signs[i] == '<=':
            A_signs[i] = '>='
            for j in range(len(A[i])):
                A[i][j] *= -1
            for k in range(len(b)):
                if k == i:
                    b[k] *= -1
        if A_signs[i] == '>=':
            M1.append(i)
        if A_signs[i] == '=':
            M2.append(i)
    for i in range(len(c) - 1):
        if i in x_signs:
            N1.append(i)
        else:
            N2.append(i)

    if min_max == 'max':
        min_max_new = 'min'
        for i in range(len(c)):
            c[i] *= -1
    else:
        min_max_new = 'min'

    return M1, M2, N1, N2, min_max_new


def common_to_canonical(c, A, b, M1, M2, N1, N2, A_signs):
    c_new = common_to_canonical_calc_c(c, M1, N1, N2)
    A_new = common_to_canonical_calc_A(A, M1, M2, N1, N2)
    b_new = common_to_canonical_calc_b(b, M1, M2)
    return c_new, A_new, b_new, ['=' for i in range(len(A_signs))], [i for i in range(len(A_new[0]))]


def common_to_canonical_calc_c(c, M1, N1, N2):
    c_new = []
    for i in N1:
        c_new.append(c[i])
    for i in N2:
        c_new.append(c[i])
    for i in N2:
        c_new.append(-c[i])
    for i in M1:
        c_new.append(0)
    return np.array(c_new, float)


def common_to_canonical_calc_A(A, M1, M2, N1, N2):
    A_new = []
    for i in range(len(M1)):
        A_new.append([])
        for j in range(len(N1)):
            A_new[i].append(A[M1[i]][N1[j]])
        for j in range(len(N2)):
            A_new[i].append(A[M1[i]][N2[j]])
        for j in range(len(N2)):
            A_new[i].append(-A[M1[i]][N2[j]])
        for j in range(len(M1)):
            if i == j:
                A_new[i].append(-1)
            else:
                A_new[i].append(0)
    for i in range(len(M2)):
        A_new.append([])
        for j in range(len(N1)):
            A_new[i + len(M1)].append(A[M2[i]][N1[j]])
        for j in range(len(N2)):
            A_new[i + len(M1)].append(A[M2[i]][N2[j]])
        for j in range(len(N2)):
            A_new[i + len(M1)].append(-A[M2[i]][N2[j]])
        for j in range(len(M1)):
            A_new[i + len(M1)].append(0)
    return np.array(A_new, float)


def common_to_canonical_calc_b(b, M1, M2):
    b_new = []
    for i in M1:
        b_new.append(b[i])
    for i in M2:
        b_new.append(b[i])
    return np.array(b_new, float)


def get_common_gmp_by_canonical_gmp(canonical_gmp, N1, N2):
    common_gmp = np.zeros(len(N1) + len(N2), float)
    for i in range(len(N1)):
        common_gmp[N1[i]] = canonical_gmp[i]
    for i in range(len(N2)):
        u = canonical_gmp[len(N1) + i]
        v = canonical_gmp[len(N1) + len(N2) + i]
        common_gmp[N2[i]] = u - v
    return common_gmp


def printing(c_p, A_p, b_p, A_signs_p, min_max, x_signs):
    print('\n \n', 'A', '=', len(A_p), 'x', len(A_p[0]), ':')
    for i in range(len(A_p)):
        for j in range(len(A_p[i])):
            print(' ', A_p[i][j], 'x', [j + 1], sep='', end=' ')
        print(A_signs_p[i], ' ', b_p[i], '\n')
    print('F(x):', end=' ')
    for i in range(len(c_p)):
        print(c_p[i], end=' ')
    print('->', min_max)

    for i in range(len(A_p[0])):
        if i in x_signs:
            print('x', [i + 1], sep='', end=' ')
            print('>=', '0', end=' ')
