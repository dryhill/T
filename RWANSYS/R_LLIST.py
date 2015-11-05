# 读ANSYS的lis文件中直线（ANSYS中list-line-Attribute format列表，SPACE字段是1表示直线，0表示弧线），形成一个列表，传递出去

def RLlist():
    ''' 读LLIST文件，生成线列表'''
    Llist=[]
    f=open('LLIST.lis', 'r')
    tag=0

    while not tag:
        t=f.readline()
        if(t!=''):
            if not t.strip(): continue
            if t.find('LIST')>=0 or t.find('NUMBER')>=0: continue
            ta=t.split()
#            if ta[5]>0:
#                print(ta)
#                Llist.append([ta[0], ta[1], ta[2], ta[3]], ta[5])
            Llist.append([ta[0], ta[1], ta[2], ta[3], ta[5]])                
        else:
            tag=1
    f.close()
    print(Llist)
    return(Llist)

# 读ANSYS的lis文件中直线（ANSYS中list-line-radius format列表，RADIUS字段是直径，非0时是弧线），形成一个列表，传递出去
def Rarclist():
    ''' 读RLLIST文件，生成线列表'''
    arclist=[]
    f=open('RLLIST.lis', 'r')
    tag=0

    while not tag:
        t=f.readline()
        if(t!=''):
            if not t.strip(): continue
            if t.find('LIST')>=0 or t.find('NO')>=0: continue
            ta=t.split()
            if ta[3]>0:
                print(ta)
                arclist.append([ta[0], ta[1], ta[2], ta[3]]) #编号，点1，点2，半径
        else:
            tag=1
    f.close()
    print(arclist)
    return(arclist)


#RLlist()
#Rarclist()

