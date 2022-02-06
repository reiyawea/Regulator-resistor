# Regulator-resistor calculator

Calculate the best combination of voltage divider resistors for feedback of voltage regulator, such as MC34063, AMS1117-ADJ, MT3608, etc.
Output voltage of such regulators Vout = Vref * (1 + R1/R2), where Vout and Vref are given, and each of R1 and R2 is one single resistor, two in series or two in parallel.
Useful when you have a limited collection of resistors but want a more precise voltage output.


sample output (best result last):
```
R1=22K, R2=(1K//4.7K), Vout=34.601V, err=-0.399V, rel=-1.140%
R1=(220K+1M), R2=(47K//1M), Vout=35.222V, err=0.222V, rel=0.634%
R1=(680K//1M), R2=(22K//47K), Vout=35.013V, err=0.013V, rel=0.037%
R1=(47K//1M), R2=(2.2K//6.8K), Vout=35.008V, err=0.008V, rel=0.022%
R1=(68K//470K), R2=2.2K, Vout=35.003V, err=0.003V, rel=0.008%
```
