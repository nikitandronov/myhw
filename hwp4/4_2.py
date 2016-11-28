word = input ('Введите слово: ')
vocab = []
h = 0

for i in range (len(word) + 1):
    k = word[0:h]
    vocab.append(k)
    h = h + 1
    

for i in range (len(vocab)):
    print(vocab[i])
