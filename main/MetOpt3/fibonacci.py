def count_n_and_fibs(a, b, eps):
    N = (b - a) / eps
    fibs = [1, 1]
    i = 2
    while 1:
        fibs.append(fibs[i-2] + fibs[i-1])
        if fibs[i] > N:
            return fibs, i
        i += 1

def count_fibs(n):
    fibs = [1, 1]
    for i in range(2, n+1):
        fibs.append(fibs[i-1] + fibs[i-2])
    return fibs
#
# def calc_gmp_fibonacci(a, b, t, eps, f):
#     fibs = get_first_t_plus_2_fibonacci_numbers(t)
#     f_calls_number = 0
#
#     gmp_approx = 0
#     k = 1
#     ak, bk = a, b
#     lk, f_at_lk, lk_is_visited = 0, 0, False
#     mk, f_at_mk, mk_is_visited = 0, 0, False
#     while bk - ak > eps:
#         # full cycle with fibs?
#         if k == t:
#             k = 1
#             lk_is_visited, mk_is_visited = False, False
#
#         # calculate lk and (or) mk
#         alphak = fibs[t-k]/fibs[t-k+2]
#         if lk_is_visited:
#             mk = alphak*ak + (1-alphak)*bk
#             f_at_mk, f_calls_number = f(mk), f_calls_number + 1
#         elif mk_is_visited:
#             lk = (1-alphak)*ak + alphak*bk
#             f_at_lk, f_calls_number = f(lk), f_calls_number + 1
#         else:
#             lk, mk = (1-alphak)*ak + alphak*bk, alphak*ak + (1-alphak)*bk
#             f_at_lk, f_at_mk, f_calls_number = f(lk), f(mk), f_calls_number + 2
#
#         # choose next range
#         if f_at_lk <= f_at_mk:
#             gmp_approx = lk
#             bk = mk
#             mk, f_at_mk = lk, f_at_lk
#             lk_is_visited, mk_is_visited = False, True
#         else:
#             gmp_approx = mk
#             ak = lk
#             lk, f_at_lk = mk, f_at_mk
#             lk_is_visited, mk_is_visited = True, False
#
#         k += 1
#     return gmp_approx, f_calls_number
#

def get_first_n_fibs(n):
    fib_numbers = [1, 1]
    for i in range(2, n):
        fib_numbers.append(fib_numbers[i-2] + fib_numbers[i-1])
    return fib_numbers

def fibonacci(a, b, eps, f):
    f_calls = 2
    fibs, n = count_n_and_fibs(a, b, eps)
    # n = 4
    lambda_k = a + fibs[n-2] / fibs[n] * (b - a)
    mu_k = a + fibs[n-1] / fibs[n] * (b - a)
    f_lambda_k = f(lambda_k)
    f_mu_k = f(mu_k)
    k = 1
    a_k = a
    b_k = b
    while 1:
        if f_lambda_k > f_mu_k:
            a_k = lambda_k
            lambda_k = mu_k
            f_lambda_k = f_mu_k
            mu_k = a_k + fibs[n-k-1] / fibs[n-k] * (b_k - a_k)
            if k == n - 1:
                break
            else:
                k += 1
                f_mu_k = f(mu_k)
                f_calls += 1

        else:
            b_k = mu_k
            mu_k = lambda_k
            f_mu_k = f_lambda_k
            lambda_k = a_k + fibs[n-k-2] / fibs[n-k] * (b_k - a_k)
            if k == n - 1:
                break
            else:
                k += 1
                f_lambda_k = f(lambda_k)
                f_calls += 1

    return (a_k + b_k) / 2, f_calls
    # mu_k = lambda_k + dif
    # f_mu_k = f(mu_k)
    # f_calls += 1
    # if f_mu_k == f_lambda_k:
    #     return (lambda_k + b_k) / 2, f_calls
    # else:
    #     return (a_k + mu_k) / 2, f_calls


def fibonacci1(a, b, eps, f, n):
    f_calls = 2
    # n = 4
    fibs = count_fibs(n)
    lambda_k = a + fibs[n-2] / fibs[n] * (b - a)
    mu_k = a + fibs[n-1] / fibs[n] * (b - a)
    f_lambda_k = f(lambda_k)
    f_mu_k = f(mu_k)
    k = 1
    a_k = a
    b_k = b
    while 1:
        if f_lambda_k > f_mu_k:
            a_k = lambda_k
            lambda_k = mu_k
            f_lambda_k = f_mu_k
            mu_k = a_k + fibs[n-k-1] / fibs[n-k] * (b_k - a_k)
            if k == n - 1:
                break
            else:
                k += 1
                f_mu_k = f(mu_k)
                f_calls += 1

        else:
            b_k = mu_k
            mu_k = lambda_k
            f_mu_k = f_lambda_k
            lambda_k = a_k + fibs[n-k-2] / fibs[n-k] * (b_k - a_k)
            if k == n - 1:
                break
            else:
                k += 1
                f_lambda_k = f(lambda_k)
                f_calls += 1

    return a_k, b_k, f_calls