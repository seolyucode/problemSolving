# 4366. 정식이의 은행업무

t = int(input())

for tc in range(1, t+1):
    bin_n = list(input())
    ter_n = list(input())

    bin_lst = []
    for i in range(len(bin_n)):
        tmp = bin_n[:]
        if bin_n[i] == '1':
            tmp[i] == '0'
        else:
            tmp[i] == '1'
        bin_lst.append(tmp)


    print(bin_lst)