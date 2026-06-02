import shelve

with shelve.open('shelve_test') as cars:
    cars['opel'] = 'Germany'
    cars['ford'] = 'USA'
    cars['mazda'] = 'Japan'

    print(cars['ford'])
    print(cars['mazda'])

    # del cars['ope']

    for key in cars:
        print(key)
