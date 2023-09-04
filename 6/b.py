try:
    f = open('6/a.txt', 'r')
    for line in f.readlines():
        print( line.replace('\n', '') )
except Exception as e:
    print(e, type(e), sep='\n')
else:
    ...
finally:
    f.close()
