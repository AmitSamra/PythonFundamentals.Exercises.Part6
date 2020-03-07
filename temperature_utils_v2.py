def temperature_tuple(temperatures, input_unit_of_measurement):

    if input_unit_of_measurement == 'f':
        a = []
        for i in temperatures:
            a.append((i, round(((5/9) * (i - 32)), 2)))
        return tuple(a)

    elif input_unit_of_measurement == 'c':
        b = []
        for j in temperatures:
            b.append((j,round((9/5)*j + 32,2)))
        return tuple(b)

    elif input_unit_of_measurement == 'a':
        return ()

    elif input_unit_of_measurement == 'k':
        d = []
        for k in temperatures:
            d.append((k,round((k) + 373.15,2)))
        return tuple(d)

a = temperature_tuple((32, 68, 100, 104), 'f')
print(a)
b = temperature_tuple((-17.7778, 0, 100), 'c')
print(b)
c = temperature_tuple((1, 2, 3), 'a')
print(c)
d = temperature_tuple((-17.7778, 0, 100), 'k')
print(d)
