#-*- coding: utf-8 -*-
#YJKResultProcess
# python 3.3 or 2.7 will be ok
# 处理YJK的结果
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt

#指定字体，注意系统路径
font = FontProperties(fname=r"F:\Fonts\SIMSUN.TTF", size=14) 

#第一个，层间位移角,中间结果用文本保存，有x,y,自定义方向，地震和风分开。

def collectEkDisp():
    '''收集地震作用下位移角'''
    f=open('wdisp.out', 'r')
    name=['ex', 'ey']
    dp=[]
    while True:
        line=f.readline()
        #若结尾则退出            
        if not line:
            break
        #若找到'方向地震作用下的楼层最大位移'，则开始读数，肯定是先x再y
        if line.find('方向地震作用下的楼层最大位移')>0:
            d=[]
            f.readline()
            f.readline()
            f.readline()
            f.readline()
            
            while True:
                line=f.readline()
                #若空行则退出            
                if not line.strip():
                    break    
                line=f.readline()
                t=line.split()
                if t[3].strip(u'1/'):
                    ta=t[3][2:]
                else:
                    ta=t[4]
                d.append(ta)
            
            dp.append(d)    
        #若找到'地震方向'，则是自定义地震力方向，开始读数
        if line.find('地震方【')>0 and line.find('节点位移')<0:
            #找方向名
            i=line.find('地震方向')
            ta=line[i+4:i+8]
            name.append(ta)           
            
            d=[]
            f.readline()
            f.readline()
            f.readline()
            f.readline()
            
            while True:
                line=f.readline()
                #若空行则退出            
                if not line.strip():
                    break    
                line=f.readline()
                t=line.split()
                if t[3].strip(u'1/'):
                    ta=t[3][2:]
                else:
                    ta=t[4]
                d.append(ta)
            
            dp.append(d)     
   
        #若找到'+X 方向风荷载作用下的楼层最大位移'，则是wind X，开始读数
        if line.find('+X 方向风荷载作用下的楼层最大位移')>0 :
            name.append('Wind X')           
            
            d=[]
            f.readline()
            f.readline()
            f.readline()
            f.readline()
            
            while True:
                line=f.readline()
                #若空行则退出            
                if not line.strip():
                    break    
                line=f.readline()
                t=line.split()
                if t[3].strip(u'1/'):
                    ta=t[3][2:]
                else:
                    ta=t[4]
                d.append(ta)
            
            dp.append(d)   
            
        #若找到'+X 方向风荷载作用下的楼层最大位移'，则是wind X，开始读数
        if line.find('+Y 方向风荷载作用下的楼层最大位移')>0 :
            name.append('Wind Y')           
            
            d=[]
            f.readline()
            f.readline()
            f.readline()
            f.readline()
            
            while True:
                line=f.readline()
                #若空行则退出            
                if not line.strip():
                    break    
                line=f.readline()
                t=line.split()
                if t[3].strip(u'1/'):
                    ta=t[3][2:]
                else:
                    ta=t[4]
                d.append(ta)
            
            dp.append(d)
            
        
    print(name)
    print(dp)
    return(name, dp)

def plotYJKstoreyDispAngle(name, dp, boundName, boundValue, storeyShift, shiftCut):
    
    '''绘图'''
    makstyle=['3', 'D', 's', 'p', '*', 'h', 'o', 'H', '+', '|', '_']
    
    storey=[]
    for i in range(len(dp[0]), 0, -1):
        storey.append(i-storeyShift)
  
    plt.figure(figsize=(9, 6))
    for i in range(0, len(name)):
        x=storey[shiftCut:]
        y=dp[i][shiftCut:]
        x.reverse()
        y.reverse()
        plt.plot(x, y, label=name[i], marker=makstyle[i],linewidth=1.5)
          
    plt.plot((x[0], x[-1]), (boundValue, boundValue), label=boundName, linewidth=4, color='red')
    plt.legend(loc='center', frameon=True, prop=font)
    
    plt.ylabel(u'层间位移角',  rotation=270,fontproperties=font)
    plt.xlabel(u'楼层', fontproperties=font)
    plt.title(u'最大层间位移角',fontproperties=font)    
    plt.grid(True)


#    plt.ylim(0, 1000)
    plt.xlim(x[0], x[-1])
    plt.xticks(x)        
    plt.show()
#    plt.savefig('dispAngle.png', dpi=120)
         

def collectWindReaction():
    '''wind reaction in wmass.out'''
    f=open('wmass.out', 'r')
    name=['Wind Vx', 'Wind Vy', 'Wind Mx', 'Wind My']
    VX=[]
    VY=[]
    MX=[]
    MY=[]    
    while True:
        line=f.readline()
        print(line)
        #若结尾则退出            
        if not line:
            break
        if line.find(u'风荷载信息')>0 and line.find(u'....')<=0:          
            storey=[]
            f.readline()
            f.readline()
            f.readline()
            f.readline()
            
            while True:
                line=f.readline()
                #若空行则退出            
                if not line.strip():
                    break    
                t=line.split()
                storey.append(t[0])
                VX.append(t[3])
                MX.append(t[4])
                VY.append(t[6])
                MY.append(t[7])                
    dp=(VX, VY, MX, MY)
    return(name, storey, dp)
    
            
def plotYJKstoreyResult(name, storey, dp, boundName, boundValue, storeyShift, shiftCut, xlabel, ylabel, title):
    
    '''绘图'''
    makstyle=['3', 'D', 's', 'p', '*', 'h', 'o', 'H', '+', '|', '_']
    
    plt.figure(figsize=(9, 6))
    for i in range(0, len(name)):
        x=storey[shiftCut:]
        y=dp[i][shiftCut:]
        for j in range(0, len(x)):
            x[j]=int(x[j])        
        x.reverse()
        y.reverse()
        plt.plot(x, y, label=name[i], marker=makstyle[i],linewidth=1.5)
    #多个限值
    for i in range(0, len(boundValue)):
        if boundValue[i]!=0:
            plt.plot((x[0], x[-1]), (boundValue[i], boundValue[i]), label=boundName[i], linewidth=3, color='red')    
   
    plt.legend(loc='center', frameon=True, prop=font)
    
    plt.ylabel(ylabel, rotation=270,fontproperties=font)
    plt.xlabel(xlabel, fontproperties=font)
    plt.title(title,fontproperties=font)    
    plt.grid(True)

#    plt.xlim(x[0], x[-1])
    plt.xticks(x)        
    plt.show()
#    plt.savefig('dispAngle.png', dpi=120)
         


#(name, dp)=collectEkDisp()    
#plotYJKstoreyDispAngle(name, dp, u'1/500', 500, 0, 0)

(name, storey, dp)=collectWindReaction()
#print(name, storey, dp)
plotYJKstoreyResult(name[0:2], storey, dp[0:2], [], [], 0, 0, '层号','层剪力(kN)', '层剪力-风')
