class hamming:
    def distance (a, b):
        if type(a) != str or type(b) != str:
            raise ValueError('Wrong type.')
        if len(a) != len(b):
            raise ValueError('Wrong value.')    
        d = 0
        for i in range(0, len(a)):
            if b[i] != a[i]:
                d += 1
        return d
        