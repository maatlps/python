m = int(input("Me dê uma distância em metros: "))
km = m / 1000
hm = m / 100
dc = m / 10
cm = m * 100
dcm = m * 10
mm = m * 1000
print('{} metros corresponde a {} kilometros\n{} hectômetros\n{} decâmetros'.format(m, km, hm, dc))
print('{} decímetros\n{} centímetros\ne {} decímetros'.format(dc, cm, mm))

