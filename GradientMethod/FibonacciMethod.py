def count_n_and_fibs(a, b, eps):
    N = (b - a) / eps
    fibs = [1, 1]
    i = 2
    while 1:
        fibs.append(fibs[i-2] + fibs[i-1])
        if fibs[i] > N:
            return fibs, i
        i += 1


def multiple_vec(a, vec):
    return [vec[0] * a, vec[1] * a]


def summ_vec(vec1, vec2):
    return [vec1[0] + vec2[0], vec1[1] + vec2[1]]


def fibonacci(a, b, eps, f, x, grad_x):
    fibs, n = count_n_and_fibs(a, b, eps)
    lambda_k = a + fibs[n-2] / fibs[n] * (b - a)
    mu_k = a + fibs[n-1] / fibs[n] * (b - a)
    f_lambda_k = f(summ_vec(x, multiple_vec(-lambda_k, grad_x)))
    f_mu_k = f(summ_vec(x, multiple_vec(-mu_k, grad_x)))
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
                f_mu_k = f(summ_vec(x, multiple_vec(-mu_k, grad_x)))
        else:
            b_k = mu_k
            mu_k = lambda_k
            f_mu_k = f_lambda_k
            lambda_k = a_k + fibs[n-k-2] / fibs[n-k] * (b_k - a_k)
            if k == n - 1:
                break
            else:
                k += 1
                f_lambda_k = f(summ_vec(x, multiple_vec(-lambda_k, grad_x)))
    return (a_k + b_k) / 2
