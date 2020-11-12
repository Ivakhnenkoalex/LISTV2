def ft_len_mass(mass):
    a = 0
    for i in mass:
        a += 1
    return a


def ft_join(lst,sep =' '):
    d = ft_len_mass(lst)
    i = 0
    r = ''
    while d > i:
        if lst[i] == 0:
            r = r + '0'
        if lst[i] == 1:
            r = r + '1'
        if lst[i] == 2:
            r = r + '2'
        if lst[i] == 3:
            r = r + '3'
        if lst[i] == 4:
            r = r + '4'
        if lst[i] == 5:
            r = r + '5'
        if lst[i] == 6:
            r = r + '6'
        if lst[i] == 7:
            r = r + '7'
        if lst[i] == 8:
            r = r + '8'
        if lst[i] == 9:
            r = r + '9'
        if i != d - 1:
            r = r + sep
        i = i + 1
    return r
