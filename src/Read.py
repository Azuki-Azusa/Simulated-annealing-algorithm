def Read():
    with open(r'../tc/eil101_629.txt', 'r') as f:
        data = f.read()
        data = data.split()
        length = len(data)
        x = []
        y = []
        length = length
        for i in range(length // 3):
            x.append(int(data[3 * i + 1]))
            y.append(int(data[3 * i + 2]))
            '''
            print(data[i * 3 + 1], data[i * 3 + 2])
        print(len(data))
        '''
        return x, y

Read()