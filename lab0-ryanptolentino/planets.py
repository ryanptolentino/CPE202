def weight_on_planets():
    weight = float(input('What do you weigh on earth? '))
    mars = weight * .38
    jupiter = weight * 2.34
    print('\nOn Mars you would weigh %s pounds.' % mars + '\nOn Jupiter you would weigh %s pounds.' % jupiter)


if __name__ == '__main__':
    weight_on_planets()
