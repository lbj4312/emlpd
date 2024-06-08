import random
def emlpd():
    em=0
    you=0
    for i in range(1,4):
        em_xie=2
        you_xie=2
        print("------------第{}局------------".format(i))
        zd=[True,False]*5
        print("有5个实弹，5个空弹，每人有3滴血")
        for j in range(3):
            x=random.choice(zd)
            dj=random.choice(["放大镜","锯子"])
            print("你有道具",dj)
            b=input("是否使用道具")
            if b=="是" or b=="Y" or b=="y" or b=="yes":
                if dj=="放大镜":
                    print("子弹是",x)
                else:
                    x=int(x)*2
            a=input("打谁?")
            if a=="自己":
                you_xie=you_xie-int(x)
                if int(x)==1 or int(x)==0:
                    zd.remove(x)
                else:
                    zd.remove(True)
                if x:
                    print("是实弹,你减了血")
                else:
                    print("恭喜你，是空弹")
            else:
                em_xie=em_xie-int(x)
                if int(x)==1 or int(x)==0:
                    zd.remove(x)
                else:
                    zd.remove(True)
                if x:
                    print("是实弹,他减了血")
                else:
                    print("很可惜，是空弹")
            x=random.choice(zd)
            if random.choice([1,2])==1:
                print("他选择打你")
                you_xie=you_xie-int(x)
                zd.remove(x)
                if x:
                    print("是实弹,你减了一滴血")
                else:
                    print("恭喜你，是空弹")
            else:
                print("他选择打自己")
                em_xie=em_xie-int(x)
                zd.remove(x)
                if x:
                    print("是实弹,他减了一滴血")
                else:
                    print("很可惜，是空弹")
            if you_xie<=0:
                em=em+1
                print("你输了这一局")
                break
            elif em_xie<=0:
                print("你赢了这一局")
                you=you+1
                break
    if em>you:
        print("你亖了")
    else:
        print("你赢了")
