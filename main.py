# Python code to assign different 1000 corp members to 10 platoons


number_of_corps = 100

for corp in range(1, number_of_corps):
    if corp % 10 == 0:
        print('corp member {}, platoon {}'.format(corp, 10))
        continue
    print('corp member {}, platoon {}'.format(corp, corp % 10))

