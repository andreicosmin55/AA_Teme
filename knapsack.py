#Implementați o strategie de cumpărare (un algoritm) care să decidă ce

#saci achiziționăm din cei n și în ce cantități, astfel încât să maximi-
#zăm profitul pe care îl obținem când ne întoarcem în țară și vindem

#cantitățile de grâne achiziționate.

def citire(filename):
    ls = []
    f = open(filename)
    n = int(f.readline())
    for i in range (n):
        x,y = [int(x) for x in f.readline().split()]
        ls.append([x,y])
    m = int(f.readline())
    return n, ls, m

def compara(ls):
    return ls[2]

n,ls,m = citire("backpack.in")

copie_m = m
for i in ls:
    i.append(i[1]/i[0])

ls.sort(key=compara, reverse= True)

val_finala = 0
j = 0

def fractional_knapsack(capacitate_maxima):
    val_finala = 0
    m = capacitate_maxima
    j = 0
    while m>0 and j + 1 != len(ls):
        if(ls[j][0] <= m):
            val_finala += ls[j][1]
            m -= ls[j][0]
            print("Am luat valoarea intreaga", ls[j][1], "pentru cele", ls[j][0],"kg")
            j += 1
        else:
            procent = m/ls[j][0]
            val_finala += procent * ls[j][1]
            m -= procent * ls[j][0]
            print("Am luat", procent * ls[j][1],"din valoarea intreaga", ls[j][1], "pentru cele", ls[j][0], "kg, cu greutate de", procent * ls[j][0])
            j += 1
    print("Valoarea maxima este", val_finala, "pe care o putem lua in cele", copie_m, "kg")

fractional_knapsack(m)

#Nu mai merge aplicata metoda Greedy

#contra ex: Greutate        Valoare
#              10             11
#              7               7
#              6               6
#              4               3
# Pentru greutate maxima pe care o putem cara = 13, aplicand metoda Greedy am obtine 11, cand raspunsul corect ar fi 13.


