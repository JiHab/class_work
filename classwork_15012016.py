import math

#print(math.isfinite(3))

l = (56, -87, 456, 4885, -0, 1)


def func(_str, args, save):
    try:
        fun = getattr(math, _str)

        if save:
            file = open('sqrt.txt', 'w')
            #print(fun(*args))
            file.write(str(fun(*args)))
            file.write('asdasdasd')
            file.close()
            #fun(*args)
    except:
        print('invalid argument')

func('isfinite',(1, ), save=True)
func('afdfdsfsdfs',(1, ), save=True)



