#2. un caracter are subsecventa comuna cu altul daca si numai daca sunt egale
# complexitate timp si spatiu O(1)
def subsecv_lungime_1(a, b):
    if a == b:
        return True
    return False

#3. un caracter are subsecventa comuna intr-un sir daca se afla in acesta
#complexitate timp O(len(sir)) si spatiu O(1)
def subsecv_caracter_sir(c, s):
    if c in s:
        return True
    return False


#4. pentru a afla dimensiunea celei mai lungi subsecvente => programare dinamica
#complexitate timp: O(n*m) unde n si m sunt lungimile celor 2 siruri
#complexitate spatiu: O(n*m) unde n si m sunt lungimile celor 2 siruri
def subsec_max(str1, str2):
    l1 = len(str1)
    l2 = len(str2)
    matr_sir = [[0 for i in range(l2+1)] for i in range(l1+1)]
    for i in range(1, l1+1):
        for j in range(1, l2+1):
            if str1[i-1] == str2[j-1]:
                matr_sir[i][j] = 1 + matr_sir[i-1][j-1]
            else:
                matr_sir[i][j] = max(matr_sir[i-1][j], matr_sir[i][j-1])
    index = matr_sir[l1][l2]
    res = [""] * index
    i = l1
    j = l2
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            res[index-1] = str1[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif matr_sir[i-1][j] > matr_sir[i][j-1]:
            i -= 1
        else:
            j -= 1
    return res


