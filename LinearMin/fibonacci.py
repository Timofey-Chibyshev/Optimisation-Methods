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


def fibonacci_with_given_n(a, b, f, n):  # another variant of Fibonacci method
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