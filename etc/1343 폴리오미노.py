Pol=input()

Pol = Pol.replace('XXXX','AAAA')
Pol = Pol.replace('XX','BB')

if 'X' in Pol:
    print(-1)
else:
    print(Pol)