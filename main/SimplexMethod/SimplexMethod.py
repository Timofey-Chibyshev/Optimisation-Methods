import numpy
import numpy as np


class SimplexException(Exception):
    def __init__(self, err_msg):
        self.err_msg = err_msg


def calc_global_minimum_point(c, A, b):
    try:
        if is_zero_vector(c):
            raise SimplexException("'c' is a zero vector.")
        if A.shape[0] > A.shape[1]:  # This check should  be located before the check is rank A == m
            raise SimplexException("Error: 'm' > 'n'.")
        print('\n', np.linalg.matrix_rank(A), '\n')
        if np.linalg.matrix_rank(A) != A.shape[0]:
            raise SimplexException("'A' is a degenerate matrix.")

        x1, N1, BN1 = artifical_basis_method(A, b)
        print("After abm:", x1)
        sumMa = 0
        for i in range(len(x1)):
            sumMa += x1[i] * c[i]
        print(sumMa)
        gmp, N_gmp, B_gmp = simplex_method(c, A, b, x1, N1, BN1)  # "gmp" means "global minimum point"
        return gmp
    except SimplexException as ex:
        raise SimplexException(ex.err_msg)
    except Exception as ex:
        print("Internal error.")


def artifical_basis_method(A, b):
    m, n = A.shape
    c_help = np.hstack((np.zeros(n), np.ones(m)))
    A_help = np.hstack((A, np.identity(m)))
    b_help = np.array(b)
    x1_help = np.hstack((np.zeros(n), b_help))
    N1_help = list(range(n, n + m))
    BN1_help = np.identity(m)
    for i in range(m):
        if b_help[i] < 0:
            b_help[i] *= -1
            x1_help[n+i] = b_help[i]
            for j in range(n):
                A_help[i, j] *= -1
    x1_help, N1_help, BN1_help = simplex_method(c_help, A_help, b_help, x1_help, N1_help, BN1_help)

    if not is_zero_vector(get_subvector(x1_help, list(range(n, n + m)))): # if x[Nk]!= zero_vector
        raise SimplexException("Constraint set is empty.")

    x1 = get_subvector(x1_help, list(range(0, n))) # x[N/Nk]
    N1 = N1_help
    BN1 = BN1_help
    counter = 0
    if set(N1_help) & set(range(n, n + m)) != set({}):
        N1, BN1 = change_basis_in_abm(A_help, BN1_help, N1_help)
        counter += 1
    for i in range(m):
        if b[i] < 0:
            for j in range(m):
                BN1[j, i] = -BN1[j, i]
    print('Counter of change_basis_in_abm:', counter, '\n')
    return x1, N1, BN1


# "abm" means "artifical basis method"
def change_basis_in_abm(A_help, BN1_help, N1_help):
    m = A_help.shape[0]
    n = A_help.shape[1] - m
    M = list(range(m))
    N = list(range(n))

    basis_ind = 0
    while N1_help[basis_ind] < n:
        basis_ind += 1

    while basis_ind < m:
        # change basis
        other_A_indices = sorted(list(set(N) - set(N1_help)))
        i = 0
        while True:
            N1_help[basis_ind] = other_A_indices[i]
            if np.linalg.det(get_submatrix(A_help, M, N1_help)) == 0:
                i += 1
            else:
                break
        # recalculate BN1
        N1_help, BN1_help = recalc_BN1_in_abm(basis_ind, N1_help, BN1_help, A_help)
        basis_ind += 1
    return N1_help, BN1_help


# "abm" means "artifical basis method"
def recalc_BN1_in_abm(basis_ind, N1_help, BN1_help, A):
    m, n = A.shape
    M = range(m)

    for i in M:
        BN1_help[basis_ind, i] = np.dot(get_submatrix(BN1_help, [i], M), get_submatrix(A, M, [basis_ind]))

    N1_help_element = N1_help[basis_ind]
    old_basis_ind = basis_ind
    N1_help.sort()
    new_basis_ind = N1_help.index(N1_help_element)
    if old_basis_ind < new_basis_ind:
        new_BN1_strings_order = list(range(0, old_basis_ind))
        new_BN1_strings_order.extend(list(range(old_basis_ind + 1, new_basis_ind + 1)))
        new_BN1_strings_order.extend([old_basis_ind])
        new_BN1_strings_order.extend(list(range(new_basis_ind + 1, m)))
        BN1_help = get_submatrix(BN1_help, new_BN1_strings_order, M)
    elif old_basis_ind > new_basis_ind:
        new_BN1_strings_order = list(range(0, new_basis_ind))
        new_BN1_strings_order.extend([old_basis_ind])
        new_BN1_strings_order.extend(list(range(new_basis_ind, old_basis_ind)))
        new_BN1_strings_order.extend(list(range(old_basis_ind + 1, m)))
        BN1_help = get_submatrix(BN1_help, new_BN1_strings_order, M)
    return N1_help, BN1_help


def simplex_method(c, A, b, x1, N1, BN1):
    m, n = A.shape
    xk = x1
    Nk = N1
    is_basis_changed_by_hand = False
    BNk = BN1
    counterBasis = 0
    counterPoints = 0

    while True:
        print('Counter of change_basis_in_Simplex:', counterBasis, '\n')
        print('Counter of extreme points:', counterPoints, '\n')
        dk = calc_dk(c, BNk, A, Nk)
        print(xk)
        if is_xk_global_minimum_point(dk):
            print('Counter of change_basis_in_Simplex:', counterBasis, '\n')
            print('Counter of extreme points:', counterPoints, '\n')
            return xk, Nk, BNk
        jk = calc_jk(dk)
        uk = calc_uk(jk, Nk, BNk, A)
        if is_vector_non_positive(uk):
            raise SimplexException("The function is unbounded from below on the constraint set.")
        if can_go_to_next_extreme_point(xk, uk, Nk):
            counterPoints += 1
            tetak, ik = calc_tetak_and_ik(xk, uk, Nk)
            xk = xk - tetak * uk
            is_basis_changed_by_hand = False
            Nk[Nk.index(ik)] = jk
            Nk.sort()
            BNk = np.linalg.inv(get_submatrix(A, list(range(m)), Nk))
        else:
            counterBasis += 1
            Nk = get_new_basis(A, xk, Nk, is_basis_changed_by_hand)
            BNk = np.linalg.inv(get_submatrix(A, list(range(m)), Nk))
            is_basis_changed_by_hand = True


def calc_dk(c, BNk, A, Nk):
    n = A.shape[1]
    N = list(range(n))
    N_sub_Nk = list(set(N) - set(Nk))

    dk = np.zeros(n, float)
    for i in N_sub_Nk:
        dk[i] = c[i] - (np.dot(np.dot(get_subvector(c, Nk), BNk), A))[i]
    return dk


def is_xk_global_minimum_point(dk):
    n = dk.shape[0]
    for i in range(n):
        if dk[i] < -1e-5:
            return False
    return True


def calc_jk(dk):
    n = dk.shape[0]
    for i in range(n):
        if dk[i] < -1e-5:
            return i


def calc_uk(jk, Nk, BNk, A):
    m, n = A.shape
    M = list(range(m))

    uk = np.zeros(n)
    uk[jk] = -1
    for i in M:
        uk[Nk[i]] = (np.dot(BNk, get_submatrix(A, M, [jk])))[i]
    return uk


def can_go_to_next_extreme_point(xk, uk, Nk):
    Nkplus = [i for i in Nk if xk[i] > 0]
    if (Nk == Nkplus): # i. e. if xk is a nondegenerate vector
        return True
    elif is_vector_non_positive(get_subvector(uk, list(set(Nk) - set(Nkplus)))):
        return True
    else:
        return False


def calc_tetak_and_ik(xk, uk, Nk):
    indices = [i for i in Nk if xk[i] > 0 and uk[i] > 0]
    tetas = [(xk[i] / uk[i]) for i in indices]
    tetak = min(tetas)
    for i in range(len(tetas)):
        if tetas[i] == tetak:
            return tetak, indices[i]


def get_new_basis(A, xk, Nk, is_basis_changed_by_hand):
    m, n = A.shape
    M = list(range(m))
    N = list(range(n))
    Nkplus = sorted([i for i in N if xk[i] > 0])
    Nkzero = sorted([i for i in N if xk[i] == 0])
    choice = sorted(list(set(Nk) - set(Nkplus)))
    fillable_ind = 0
    i = 0
    if is_basis_changed_by_hand:
        fillable_ind = len(choice) - 1
        i = Nkzero.index(choice[fillable_ind])
        if i == (len(Nkzero) - 1):
            fillable_ind -= 1
            i = Nkzero.index(choice[fillable_ind]) + 1
        else:
            i += 1
    while True:
        choice[fillable_ind] = Nkzero[i]
        if np.linalg.matrix_rank(get_submatrix(A, M, list(set(Nkplus) | set(choice[0:fillable_ind + 1])))) == len(Nkplus) + (fillable_ind + 1):
            if len(Nkplus) + (fillable_ind + 1) == m:
                Nk = sorted(list(set(Nkplus) | set(choice)))
                return Nk
            else:
                fillable_ind += 1
                i += 1
        else:
            if (len(Nkplus) + (fillable_ind + 1) == m) and (i == len(Nkzero) - 1):
                fillable_ind = fillable_ind - 1
                i = Nkzero.index(choice[fillable_ind]) + 1
            else:
                i += 1


def get_subvector(vector, indices):
    subvector = []
    for i in indices:
        subvector.append(vector[i])
    return np.array(subvector, type(vector[0]))


def get_submatrix(matrix, str_indices, col_indices):
    submatrix = []
    for i in range(len(str_indices)):
        submatrix.append([])
        for j in range(len(col_indices)):
            submatrix[i].append(matrix[str_indices[i], col_indices[j]])
    submatrix = np.array(submatrix, type(matrix[0, 0]))
    if len(str_indices) == 1 or len(col_indices) == 1:
        submatrix = submatrix.flatten()
    return submatrix


def is_zero_vector(vector):
    for i in range(vector.shape[0]):
        if vector[i] < -1e-5 or vector[i] > 1e-5:
            return False
    return True


def is_vector_non_positive(vector):
    for i in range(vector.shape[0]):
        if vector[i] > 1e-5:
            return False
    return True
