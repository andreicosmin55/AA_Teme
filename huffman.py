def inputfile(filename):
    f = open(filename)
    string = f.read()
    f.close()
    return string

#Eficienta timp: O(n) - trebuie parcurs tot fisierul
#Eficienta spatiu: O(nr. de caractere diferite)
def v_frecventa(string):
    d = {}
    for c in string:
        if c not in d.keys():
            d.update({c: 1})
        else:
            d[c] += 1
    return d


class node:
    def __init__(self, freq, symbol, left=None, right=None):
        # frequency of symbol
        self.freq = freq

        # symbol name (character)
        self.symbol = symbol

        # node left of current node
        self.left = left

        # node right of current node
        self.right = right

        # tree direction (0/1)
        self.huff = ''

# O(n), n = numarul de simboluri distincte
def getCodes(node, huffDict, val=''): #se retin la finalul functiei in huffDict perechi astfel formate:
                                      #cheia este simbolul iar valoarea asociata este codificarea obtinuta pentru simbolul respectiv.
    newVal = val + str(node.huff)

    if (node.left):
        getCodes(node.left, huffDict, newVal)
    if (node.right):
        getCodes(node.right, huffDict, newVal)

    if not node.left and not node.right:
        huffDict[node.symbol] = newVal

# eficienta timp: O(n), n = lungimea textului primit ca input + o parcurgere a arborelui prin functia de mai sus
# eficienta memorie: O(n), n = lungimea sirului codat in 0 si 1
def encodeString(text, root):
    huffDict = {}
    getCodes(root, huffDict)

    encodedString = ''
    for letter in text:
        encodedString += huffDict[letter] #in loc de fiecare simbol punem codificarea obtinua prin arborele Huffman pentru acesta
    return encodedString

# eficienta timp: O(n*h), n = lungimea textului initial, h = inaltimea arborelui
def decodeString(encodedtext, root):

    decodedtext = ''
    node = root

    for i in range(len(encodedtext)):#parcurgem arborele pentru a decodifica astfel:
        if encodedtext[i] == '0': #valoarea asignata pentru partea stanga este 0
            node = node.left
        else:
            node = node.right # iar pentru partea dreapta este 1

        if not node.left and not node.right: #daca am ajuns la o frunza
            decodedtext += node.symbol
            node = root

    return decodedtext

# eficienta timp: O(n^2*logn) reprezentand sortarea (n = numarul de noduri din coada de prioritati)
def createHuffmanTree(d):
    nodes = [node(value, key) for key, value in d.items()]
    while len(nodes) > 1:
        # sortam nodurile descrescator dupa frecventa
        nodes.sort(key=lambda x: x.freq, reverse=True)

        # alegem cele mai mici 2 noduri
        left = nodes[-1]
        right = nodes[-2]

        # dam valori pentru a putea calcula sirurile de biti pentru codificare
        left.huff = 0
        right.huff = 1

        # pentru cele mai mici doua noduri alese anterior, contruim un nod "parinte" pentru cele 2 care va avea suma celor doua frecvente
        newNode = node(left.freq + right.freq, left.symbol + right.symbol, left, right)

        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)
    return nodes

string = inputfile('ex2.txt')
d = v_frecventa(string)
nodes = createHuffmanTree(d)

print('Received:',len(string), 'bytes')

output = 0
huffDict = {} #in huffDict vom retine pe post de cheie simbolul valoarea aferenta acestuia va fi codificarea rezultatului.
getCodes(nodes[0], huffDict)

for key, value in d.items():
    output += value * len(huffDict[key]) #luam din dictionarul principal de cate ori apare fiecare simbol si inmultim cu lungimea sirului de "biti"

print('Compressed to:',output//8, 'bytes')