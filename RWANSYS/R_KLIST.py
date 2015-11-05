# 读ANSYS的lis文件，形成一个列表，传递出去

def RKlist():
    ''' 读KLIST文件，生成节点列表'''
    Klist=[]
    f=open('KLIST.lis', 'r')
    tag=0

    while not tag:
        t=f.readline()
        if(t!=''):
            if not t.strip(): continue
            if t.find('LIST')>=0 or t.find('NO')>=0: continue
            ta=t.split()
            print(ta)
            Klist.append([str(float(ta[0])), str(float(ta[1])), str(float(ta[2])), str(float(ta[3]))])
        else:
            tag=1
    f.close()
    return(Klist)

#RKlist()

