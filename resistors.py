import itertools


def val2exp(r):
    '''convert a resistor value to a human readable string'''
    if r < 1000:
        v = str(r)
        u = ''
    elif 1e3 <= r < 1e6:
        v = r/1e3
        if abs(v - int(v)) < 1e-9:
            v = int(v)
        v = str(v)
        u = 'K'
    else:
        v = r/1e6
        if abs(v - int(v)) < 1e-9:
            v = int(v)
        v = str(v)
        u = 'M'
    return v + u


class Resistor:
    def __init__(self, value):
        assert(isinstance(value, (int, float)))
        self.value = float(value)
        self.text = val2exp(value)

    def __add__(self, r):
        '''return an equivalent resistor of two in series'''
        assert(isinstance(r, Resistor))
        res = Resistor(self.value+r.value)
        res.text = F'({self.text}+{r.text})'
        return res

    def __floordiv__(self, r):
        '''return an equivalent resistor of two in parallel'''
        assert(isinstance(r, Resistor))
        res = Resistor(1./(1./self.value+1./r.value))
        res.text = F'({self.text}//{r.text})'
        return res

    def __str__(self):
        return self.text

    def __truediv__(self, r):
        if isinstance(r, Resistor):
            return self.value/r.value
        elif isinstance(r, (int, float)):
            return self.value/r
        else:
            raise TypeError

    def __eq__(self, r):
        if isinstance(r, Resistor):
            return abs(self.value - r.value) < 1e-9
        elif isinstance(r, (int, float)):
            return abs(self.value - r) < 1e-9
        else:
            raise TypeError

    def __hash__(self):
        return int(self.value*1e9)


Rval = [1, 2.2, 4.7, 6.8, 10, 22, 47, 68, 100, 220, 470, 680, 1000]  # value of resistors in stock, in Kohm
R = [Resistor(r*1000) for r in Rval]  # value of single resistor
Rser = [r1+r2 for r1, r2 in itertools.product(R, repeat=2)]  # value of two in series
Rpara = [r1//r2 for r1, r2 in itertools.product(R, repeat=2)] # value of two in parallel
Res = set(R+Rser+Rpara)  # generate all possible values of resistor combination

v_set = 35  # expected output voltage of regulator
v_ref = 1.25  # reference voltage of regulator
v_err = 1.0  # initial voltage error

for r1, r2 in itertools.product(Res, repeat=2):
    v = (1+r1/r2)*v_ref
    if abs(v-v_set) < abs(v_err):
        v_err = v-v_set
        print('R1=%s, R2=%s, Vout=%.3fV, err=%.3fV, rel=%.3f%%' %
              (r1, r2, v, v_err, v_err/v_set*100.))

'''
output (best result last):
R1=22K, R2=(1K//4.7K), Vout=34.601V, err=-0.399V, rel=-1.140%
R1=(220K+1M), R2=(47K//1M), Vout=35.222V, err=0.222V, rel=0.634%
R1=(680K//1M), R2=(22K//47K), Vout=35.013V, err=0.013V, rel=0.037%
R1=(47K//1M), R2=(2.2K//6.8K), Vout=35.008V, err=0.008V, rel=0.022%
R1=(68K//470K), R2=2.2K, Vout=35.003V, err=0.003V, rel=0.008%
'''
