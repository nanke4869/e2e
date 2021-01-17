
dic = {"0": "NAME", "1": "EAT", "2": "FOOD", "3": "PRC", "4": "RAT", "5": "AREA",
       "6": "FAM", "7": "NEAR"}


path = 'e2e_dataset/'
file_name = ["0-200.txt", "200-400.txt", "400-600.txt", "600-800.txt", "1000-1200.txt"]
ans = open(path+"train.txt", "a+", encoding='utf-8')
for name in file_name:
    file = open(path+name, "r", encoding='utf-8')

    lines = file.readlines()
    for line in lines:
        part = line.split("<eos>")
        words = part[0].split(" ")
        indexs = part[1].split(" ")
        labels = ["O"]*len(words)

        for index in indexs:
            print(id)
            index = index.replace("\n", "")
            id = index.split(",")
            for k in range(int(id[0]), int(id[1])):
                if k == int(id[0]):
                    labels[k] = "B-" + dic[id[2]]
                else:
                    labels[k] = "I-" + dic[id[2]]

        for i in range(len(words)):
            ans.write(words[i] + " " + labels[i] + "\n")
        ans.write("\n")