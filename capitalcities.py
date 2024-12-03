def data_maker(capitals):
    city = []
    country = []
    for i in range(len(capital)):
        if i % 2 == 0:
            city.append(capital[i])
        else:
            country.append(capital[i])
    return city, country