'''import random
name = ['赵', '钱', '孙', '李', '郑', '吴']
i = 0
while i < 10:
    i += 1
    chose=input("请输入您的业务（1、点名2、分发棒棒糖）")
    if chose == '1':
        a=len(name)
        lindex=random.randint(0,a-1)
        print(name[lindex])
    elif chose == '2':
        num=random.randint(0,10)
        print('获得了',num,'个棒棒糖')
    else:
        print('你快去一边去吧')
'''
import random
print('-------------开始游戏-------------')
list1=['普通','稀有','传奇']
name=list1[random.randint(0,len(list1)-1)]
print(name)
chushi=10
if name == '普通':
    while True:
        c=0
        list2 = []
        while c<3:
            c+=1
            fenshu=random.randint(5,20)
            list2.append(fenshu)
        print(list2)
        quzhi=list2[random.randint(0,len(list2)-1)]
        print(quzhi)
        list3=[1,2]
        yunsuan=list3[random.randint(0,len(list3)-1)]
        if yunsuan == 1:
            chushi = chushi + quzhi
            print(chushi)
        elif yunsuan == 2:
            chushi = chushi - quzhi
            print(chushi)
        if chushi > 100:
            print('恭喜你,分数为',chushi)
            break
        elif chushi <= 0:
            print('你输了,分数为',chushi)
            break
if name == '稀有':
    chushi = 30
    while True:
        c = 0
        list2 = []
        while c < 3:
            c += 1
            fenshu = random.randint(5, 20)
            list2.append(fenshu)
        print(list2)
        quzhi = list2[random.randint(0, len(list2) - 1)]
        print(quzhi)
        list3 = [1, 2]
        yunsuan = list3[random.randint(0, len(list3) - 1)]
        if yunsuan == 1:
            chushi = chushi + quzhi
            print(chushi)
        elif yunsuan == 2:
            chushi = chushi - quzhi
            print(chushi)
        if chushi > 100:
            print('恭喜你,分数为', chushi)
            break
        elif chushi <= 0:
            print('你输了,分数为', chushi)
            break
if name == '传奇':
    while True:
        c = 0
        list2 = []
        while c < 3:
            c += 1
            fenshu = random.randint(5, 20)
            list2.append(fenshu)
        print(list2)
        quzhi = list2[random.randint(0, len(list2) - 1)]
        print(quzhi)
        list3 = [1, 2]
        yunsuan = list3[random.randint(0, len(list3) - 1)]
        if yunsuan == 1:
            chushi = chushi + quzhi
            print(chushi)
        elif yunsuan == 2:
            chushi = chushi + quzhi
            print(chushi)
        if chushi > 100:
            print('恭喜你,分数为', chushi)
            break
        elif chushi <= 0:
            print('你输了,分数为', chushi)
            break