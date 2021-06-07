from math import gcd


def phi(n):
    amount = 0
    for k in range(1, n):
        if gcd(n, k) == 1:
            amount += 1
    return amount


def check_ord(el: int, osn: int):
    if gcd(osn, el) != 1 or el == 0:
        return -1
    elif osn == 1:
        return 1
    el = el % osn
    curr = el   # (el * el) % osn
    ord_el = 1  # 2
    while curr != 1:
        curr = (curr * el) % osn
        ord_el += 1
    return ord_el


def print_ord(init, osn):
    l = set()
    tmp = init % osn
    while tmp not in l:
        l.add(tmp)
        tmp = (tmp * init) % osn
    # print('len is', len(l))
    return len(l)


# n = p^p_d * q * 2^r + 1
# r = 5   # 5     3     6     3     2     4  6    12  4   4   5 (3875873-prime)
q = 3       # 109   337   3001  757   757   101   17    457   109|    # 1     1     1     1     1     5   11   1   5   1   91
p = 5       # 5     7     7     7     5     5     5     233   5  |    # 17    11    97    11    97    11  17   11  11  11  11
p_d = 1     # 9     5     4     3     3     3     3     1     3  |
n = (p ** p_d) * q  # ((p ** p_d) * q * (2 ** r)) + 1
osnovanie = p ** p_d
# detect r
r = 0
t = n - 1
while t % 2 == 0:
    r += 1
    t /= 2
t = int(t)
print(f'n = {n} = {p}^{p_d} * {q}\nn - 1 = t*2^r\tt = {t}\tr = {r}')
# print('ord 2', check_ord(2))

s_count = 0
a_count = 0
supa_count = 0
o_count = 0

vzaim = list()
vzaimw = list()
vzaima = list()

print(160 * '=')
for i in range(n):
    curr = list()
    curr.append(i)
    a_t = pow(i, t, n)
    curr.append(-1 if a_t == n - 1 else a_t)
    for j in range(r):
        a = pow(curr[-1], 2, n)
        a = -1 if a == n - 1 else a
        curr.append(a)

    if curr[1] == 1 or -1 in curr:
        print(f'witness' + 34 * '\t' + f'{curr}')
        s_count += 1
    elif curr[1] != 1 and curr[-1] == 1 and -1 not in curr:
        curr_group_size = print_ord(curr[0], osnovanie * q)
        curr_ord_p = check_ord(curr[0], p)
        curr_group_pd_size = print_ord(curr[0], osnovanie)
        curr_ord_q = print_ord(curr[0], q)

        if curr_ord_p >= phi(p):# curr_group_pd_size >= phi(osnovanie):    # curr_group_size >= phi(osnovanie * q):   # i % 2 == 1 and  // curr_group_size >= phi(osnovanie - 1)
            supa_count += 1
            print('prim', end='')
        else:
            a_count += 1
            print('Nprim', end='')
        print(f'anti\tord in Z{p} = {curr_ord_p}  \
        \tord in Z{q} = {curr_ord_q}  \
        \tsubGroup Size in Z{p}^{p_d} = {curr_group_pd_size}  \
        \tsubGroup Size in Z{p}^{p_d}*{q} = {curr_group_size}\
        \t{curr}')
    elif curr[-1] != 1:
        o_count += 1
print(160 * '=')
print('\nNumber of witnesses is ' + str(s_count))
print('Number of anti witnesses a^(n-1) != 1 is ' + str(o_count))
print('Number of not prim anti witnesses is ' + str(a_count))
print('Number of prim anti witnesses is ' + str(supa_count))
print('\nn\t\t\t\t=', n)
print('phi(n)\t\t\t=', phi(n))
print('phi(n - 1)\t\t=', phi(n - 1))
print('phi(t)\t\t\t=', phi(osnovanie * q))
print('phi(t - 1)\t\t=', phi((osnovanie * q) - 1))
for i in range(p_d):
    currp = p ** (p_d - i)
    curr = phi(currp)
    print(f'{p}^{p_d - i}\t\t\t=', currp)
    print(f'phi({p}^{p_d - i})\t\t=', curr)
    print(f'phi(phi{p}^{p_d - i})\t=', phi(curr))

# EXAMPLE
# s = [44, 44, -1, 1, 1]    # 11^2
# a = [597, 597, 1, 1, 1]
a = [23765, 23765, 1, 1, 1]     # 5*11^3
s = [24787, 81694, -1, 1, 1]
sa = [(s[0] * a[0]) % ((11 ** 3) * 5 * (2 ** 4) + 1)]
for j in range(4):
    tmp = pow(sa[0], (11 ** 3) * (2 ** j), (11 ** 3) * 5 * (2 ** 4) + 1)  # n = (11 ** 3) * 5 * (2 ** 4) + 1
    tmp = -1 if tmp == (11 ** 3) * 5 * (2 ** 4) else tmp
    sa.append(tmp)
print('\n' + 40 * '=')
print('Example for n - 1 = 11^3 * 5 * 2^4')
print('s:\t\t', s)
print('a:\t\t', a)
print('s * a:\t', sa)
print('ord', a[0], 'is', check_ord(a[0], 11), 'in Z11')
print(40 * '=')
# END EXAMPLE
