dic={}
l=[]

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in dic:
            dic[score].append(name)
        else:
            dic[score]=[name]
        if score not in l:
            l.append(score)
m=min(l)
l.remove(m)
m=min(l)
dic[m].sort()
for i in dic[m]:
    print(i)
