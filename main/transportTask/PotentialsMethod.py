import numpy as np


class PotentialsException(Exception):
    def __init__(self, err_msg):
        self.err_msg = err_msg


empty_val = 0


def calc_global_minimum_point(C, a, b):
    sum_a = sum(a)
    sum_b = sum(b)
    if sum_a < sum_b:
        n, m = C.shape
        C, a, b = add_fictitious_producer(C, a, b)
        x = potentials_method(C, a, b)

        exclude_indices = range(n*m, (n+1)*m)
        i = len(exclude_indices) - 1
        while i >= 0:
            x = np.delete(x, exclude_indices[i])
            i -= 1
        return x
    elif sum_a > sum_b:
        n, m = C.shape
        C, a, b = add_fictitious_consumer(C, a, b)
        x = potentials_method(C, a, b)

        exclude_indices = [((i+1)*(m+1) - 1) for i in range(n)]
        i = len(exclude_indices) - 1
        while i >= 0:
            x = np.delete(x, exclude_indices[i])
            i -= 1
        return x
    else:
        return potentials_method(C, a, b)


def add_fictitious_producer(C, a, b):
    n, m = C.shape
    new_C = []
    for i in range(n+1):
        new_C.append([])
        if i < n:
            for j in range(m):
                new_C[i].append(C[i, j])
        else:
            for j in range(m):
                new_C[i].append(0)
    a = np.append(a, sum(b)-sum(a))
    return np.array(new_C, float), a, b


def add_fictitious_consumer(C, a, b):
    n, m = C.shape
    new_C = []
    for i in range(n):
        new_C.append([])
        for j in range(m):
            new_C[i].append(C[i, j])
        new_C[i].append(0)
    b = np.append(b, sum(a) - sum(b))
    return np.array(new_C, float), a, b


def potentials_method(C, a, b):
    xk, xk_basis_cells = nwa_method(a, b)
    print('After nwa_method: ', xk, '\n')
    while True:
        u, v = calc_potentials(C, xk_basis_cells)
        print('U: ', u)
        print('V: ', v)
        # diff for [i, j] cell equals (v[j]-u[i])-C[i, j]
        max_diff, max_diff_cell = calc_differences(C, u, v)
        print('max_diff: ', max_diff)
        print('max_deff_cell: ', max_diff_cell)
        print()
        if max_diff > 0:
            xk, xk_basis_cells = get_next_point(C, xk, xk_basis_cells, max_diff_cell)
            print("Координаты нового решения:", xk_basis_cells)
            print("Значения нового решения  :", xk)
        else:
            break
    for i in range(len(xk)):
        if xk[i] == empty_val:
            xk[i] = 0
    return np.array(xk)


# "nwa" means "northwest angle"
def nwa_method(a, b):
    n, m = a.shape[0], b.shape[0]
    prod_ind = 0
    cons_ind = 0
    x = [empty_val for i in range(n * m)]
    x_basis_cells = []
    while (prod_ind < n) and (cons_ind < m):
        x[prod_ind * m + cons_ind] = min(a[prod_ind], b[cons_ind])
        x_basis_cells.append([prod_ind, cons_ind])
        a[prod_ind] -= x[prod_ind * m + cons_ind]
        b[cons_ind] -= x[prod_ind * m + cons_ind]
        if a[prod_ind] == 0:
            if b[cons_ind] == 0:
                if not (cons_ind == m-1 and prod_ind == n-1):  # "extend" basis
                    x[prod_ind * m + cons_ind + 1] = 0
                    x_basis_cells.append([prod_ind, cons_ind])
                prod_ind += 1
                cons_ind += 1
            else:
                prod_ind += 1
        else:
            cons_ind += 1
    return x, x_basis_cells


def calc_potentials(C, xk_basis_cells):
    n, m = C.shape
    u = np.zeros(n)
    u_filled_elems = [False for i in range(u.shape[0])]
    u_filled_elems_number = 0
    v = np.zeros(m)
    v_filled_elems = [False for i in range(v.shape[0])]
    v_filled_elems_number = 0
    xk_basis_cells = sorted(xk_basis_cells)

    # we can assign any value for one potential
    u[0] = 0
    u_filled_elems[0] = True
    u_filled_elems_number += 1
    # calculate other n + m - 1 potentials
    while u_filled_elems_number < len(u) or v_filled_elems_number < len(v):
        for basis_cell in xk_basis_cells:
            i = basis_cell[0]
            j = basis_cell[1]
            if u_filled_elems[i] == True and v_filled_elems[j] == False:
                v[j] = C[i, j] + u[i]
                v_filled_elems[j] = True
                v_filled_elems_number += 1
            elif u_filled_elems[i] == False and v_filled_elems[j] == True:
                u[i] = v[j] - C[i, j]
                u_filled_elems[i] = True
                u_filled_elems_number += 1
    return u, v


def calc_differences(C, u, v):
    max_diff = (v[0] - u[0]) - C[0, 0]
    max_diff_cell = [0, 0]
    n, m = C.shape
    print('matrix of diffs:')
    for i in range(n):
        for j in range(m):
            diff = (v[j]-u[i])-C[i, j]
            print('(', i, ',', j, ')', diff)
            if diff > max_diff:
                max_diff = diff
                max_diff_cell = [i, j]
    return max_diff, max_diff_cell


def get_next_point(C, xk, xk_basis_cells, max_diff_cell):
    n, m = C.shape
    cell_cycle = get_cell_cycle(n, m, xk_basis_cells, max_diff_cell)
    print("Координаты цикла пересчета:", cell_cycle)
    min_amount_of_transported_cargo = calc_min_amount_of_transported_cargo(xk, m, cell_cycle)
    recalculate_xk_components(xk, min_amount_of_transported_cargo, m, cell_cycle, max_diff_cell)
    update_xk_basis_cells(max_diff_cell, xk_basis_cells, cell_cycle, C, xk)
    return xk, xk_basis_cells


def get_cell_cycle(n, m, xk_basis_cells, max_diff_cell):
    start_cell = max_diff_cell
    cell_cycle = begin_cycle_search_up(start_cell, n, m, xk_basis_cells)
    if cell_cycle != []:
        return cell_cycle
    cell_cycle = begin_cycle_search_down(start_cell, n, m, xk_basis_cells)
    if cell_cycle != []:
        return cell_cycle
    cell_cycle = begin_cycle_search_left(start_cell, n, m, xk_basis_cells)
    if cell_cycle != []:
        return cell_cycle
    cell_cycle = begin_cycle_search_right(start_cell, n, m, xk_basis_cells)
    return cell_cycle


direction_vertical = 0
direction_horizontal = 1


def begin_cycle_search_up(start_cell, n, m, xk_basis_cells):
    cell_cycle = []
    start_i, start_j = start_cell[0], start_cell[1]
    i, j = start_i - 1, start_j  # координата точки над нашей
    while i >= 0:  # пока можем идти вверх
        if [i, j] in xk_basis_cells: # если базисная, то запишем ее второй предположительно
            next_cell = [i, j]  # от нее будем дальше пробовать строить цикл пересчета
            visit_cell(cell_cycle, next_cell, direction_vertical, n, m, xk_basis_cells, start_cell)  # рекурсивно обходим
            # до возвращения в начало, при этом меняя направление на 90 градусов
            if cell_cycle != []:
                break
        i -= 1
    return cell_cycle


def begin_cycle_search_down(start_cell, n, m, xk_basis_cells):
    cell_cycle = []
    start_i, start_j = start_cell[0], start_cell[1]
    i, j = start_i + 1, start_j
    while i < n:
        if [i, j] in xk_basis_cells:
            next_cell = [i, j]
            visit_cell(cell_cycle, next_cell, direction_vertical, n, m, xk_basis_cells, start_cell)
            if cell_cycle != []:
                break
        i += 1
    return cell_cycle


def begin_cycle_search_left(start_cell, n, m, xk_basis_cells):
    cell_cycle = []
    start_i, start_j = start_cell[0], start_cell[1]
    i, j = start_i, start_j - 1
    while j >= 0:
        if [i, j] in xk_basis_cells:
            next_cell = [i, j]
            visit_cell(cell_cycle, next_cell, direction_horizontal, n, m, xk_basis_cells, start_cell)
            if cell_cycle != []:
                break
        j -= 1
    return cell_cycle


def begin_cycle_search_right(start_cell, n, m, xk_basis_cells):
    cell_cycle = []
    start_i, start_j = start_cell[0], start_cell[1]
    i, j = start_i, start_j + 1
    while j < m:
        if [i, j] in xk_basis_cells:
            next_cell = [i, j]
            visit_cell(cell_cycle, next_cell, direction_horizontal, n, m, xk_basis_cells, start_cell)
            if cell_cycle != []:
                break
        j += 1
    return cell_cycle


def visit_cell(cell_cycle, current_cell, previous_direction, n, m, xk_basis_cells, start_cell):
    cell_cycle.append(current_cell)
    current_cell_i, current_cell_j = current_cell[0], current_cell[1]

    if previous_direction == direction_vertical:
        # in this case we cannot go up or down

        # try to go left
        i, j = current_cell_i, current_cell_j - 1
        while j >= 0:
            if [i, j] == start_cell:  # the cycle had found
                return

            if [i, j] in xk_basis_cells:
                if [i, j] not in cell_cycle:  # we don't want have self-intersection
                    next_cell = [i, j]
                    old_cycle = cell_cycle.copy()
                    visit_cell(cell_cycle, next_cell, direction_horizontal, n, m, xk_basis_cells, start_cell)
                    if cell_cycle != old_cycle:  # it is possible only when we have found the cycle
                        return
            j -= 1

        # try to go right
        i, j = current_cell_i, current_cell_j + 1
        while j < m:
            if [i, j] == start_cell:  # the cycle had found
                return

            if [i, j] in xk_basis_cells:
                if [i, j] not in cell_cycle:  # we don't want have self-intersection
                    next_cell = [i, j]
                    old_cycle = cell_cycle.copy()
                    visit_cell(cell_cycle, next_cell, direction_horizontal, n, m, xk_basis_cells, start_cell)
                    if cell_cycle != old_cycle:  # it is possible only when we have found the cycle
                        return
            j += 1
    elif previous_direction == direction_horizontal:
        # in this case we cannot go left or right
        # try to go up
        i, j = current_cell_i - 1, current_cell_j
        while i >= 0:
            if [i, j] == start_cell:  # the cycle had found
                return

            if [i, j] in xk_basis_cells:
                if [i, j] not in cell_cycle:  # we don't want have self-intersection
                    next_cell = [i, j]
                    old_cycle = cell_cycle.copy()
                    visit_cell(cell_cycle, next_cell, direction_vertical, n, m, xk_basis_cells, start_cell)
                    if cell_cycle != old_cycle:  # it is possible only when we have found the cycle
                        return
            i -= 1
        # try to go down
        i, j = current_cell_i + 1, current_cell_j
        while i < n:
            if [i, j] == start_cell:  # the cycle had found
                return

            if [i, j] in xk_basis_cells:
                if [i, j] not in cell_cycle:  # we don't want have self-intersection
                    next_cell = [i, j]
                    old_cycle = cell_cycle.copy()
                    visit_cell(cell_cycle, next_cell, direction_vertical, n, m, xk_basis_cells, start_cell)
                    if cell_cycle != old_cycle: # it is possible only when we have found the cycle
                        return
            i += 1

    # we have not build the cycle using 'current_cell'
    # print('Printing cell cycle: \n', cell_cycle)
    cell_cycle_last_ind = len(cell_cycle) - 1
    del cell_cycle[cell_cycle_last_ind]


def calc_min_amount_of_transported_cargo(xk, m, cell_cycle):
    cell_ind_in_cycle = 0
    min_amount_of_transported_cargo = xk[(cell_cycle[cell_ind_in_cycle])[0] * m + (cell_cycle[cell_ind_in_cycle])[1]]
    while cell_ind_in_cycle < len(cell_cycle):
        cell = cell_cycle[cell_ind_in_cycle]
        i, j = cell[0], cell[1]
        amount_of_transported_cargo = xk[i * m + j]
        if amount_of_transported_cargo < min_amount_of_transported_cargo:
            min_amount_of_transported_cargo = amount_of_transported_cargo
        cell_ind_in_cycle += 2
    return min_amount_of_transported_cargo


def recalculate_xk_components(xk, min_amount_of_transported_cargo, m, cell_cycle, max_diff_cell):
    i, j = max_diff_cell[0], max_diff_cell[1]
    xk[i * m + j] = min_amount_of_transported_cargo  # don't forget that this component is empty_val
    for cell_ind_in_cycle in range(len(cell_cycle)):
        cell = cell_cycle[cell_ind_in_cycle]
        i, j = cell[0], cell[1]
        if cell_ind_in_cycle % 2 == 0:
            xk[i * m + j] -= min_amount_of_transported_cargo
        else:
            xk[i * m + j] += min_amount_of_transported_cargo


def update_xk_basis_cells(max_diff_cell, xk_basis_cells, cell_cycle, C, xk):
    delete_cell = [-1, -1]
    max_price = -1
    m = C.shape[1]
    for cell in cell_cycle:
        i, j = cell[0], cell[1]
        if xk[i * m + j] == 0 and C[i, j] > max_price:
            max_price = C[i, j]
            delete_cell = cell
    xk_basis_cells.remove(delete_cell)
    xk_basis_cells.append(max_diff_cell)
    xk[delete_cell[0] * m + delete_cell[1]] = empty_val
