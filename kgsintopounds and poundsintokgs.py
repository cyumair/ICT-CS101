pds = 20
print('KILOGRAMS  POUNDS  |  POUNDS  KILOGRAMS')
for kgs in range(1, 200, 2):
    kgstpds = round((kgs * 2.2), 2)
    while pds < 516:
        pdstkgs = round((pds / 2.2), 2)
        print(kgs,'          ', kgstpds, '  |          ', pds, '   ', pdstkgs)
        pds += 5
        break
        
        
       
       
