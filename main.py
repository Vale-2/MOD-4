

def str_counter(s):

    for i in s:
        counter = 0
        for io in s:
            if i == io:
                counter +=1
        print(i, counter)

str_counter('asddssddf')