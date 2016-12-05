with open('text.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

    max = lines[0]

    for i in range(len(lines)):
        if len(lines[i]) > len(max):
            max = lines[i]

    min = lines[0]

    for i in range(len(lines)):
        if len(lines[i]) < len(min):
            min = lines[i]

    g = len(max)//len(min)

    print("Самая короткая строка текста короче самой длинной в", g , "раз")
  
        
    

