import re
from math import *
#输入类
class inputPara:
    '''把输入参数定义成类，好调用'''
    
    def __init__(self):
        f=open('input_para.txt', 'r')
        paraName=[]
        para=[]
        while True:
            line=f.readline()
            print(line)
            if line.strip():
#                ta=re.split(' ', line)
                ta=line.split('\t')
                paraName.append(ta[0])
                para.append(ta[1].strip('\n'))
            else:
                break
        
        for i in range(len(para)):
            para[i]=float(para[i])
            
        print(paraName)
        print(para)

        
        #指定给变量
        self.a1=para[paraName.index('a1')]
        self.a2=para[paraName.index('a2')]
        self.a3=para[paraName.index('a3')]   
        self.es=para[paraName.index('es')]   
        self.ds=para[paraName.index('ds')]  
        self.rou=para[paraName.index('rou')]     
        self.sas=para[paraName.index('sas')] 
        self.r=para[paraName.index('r')]     
        self.ae=para[paraName.index('ae')]   
        self.rs=para[paraName.index('rs')]   
        self.N=para[paraName.index('N')]     
        self.M=para[paraName.index('M')]    

def main(pa):
    '''主程序，根据N、M调用子程序'''
    if abs(pa.N)<1 : Bend(pa)
    if pa.N<-1 and abs(pa.M)>1 :DPY(pa)
    
def calcw(pa, sigmaS):
    
    a=pa.a1*pa.a2*pa.a3*sigmaS/pa.es
    cw=a*(30+pa.ds)/(0.28+10*pa.rou)
    return(cw)

def Bend(pa):
    '''受弯裂缝计算'''
    
    phi=(48.2+614*pa.ae*pa.rou)/(50+390*pa.ae*pa.rou)
    a=130*pa.ae*(pa.rs/pa.r+cos(phi))
    b=27.3*phi+203.6*((pa.rs/pa.r)**2)*pa.ae*pa.rou-24.4
    sigmaS=a/b*pa.M/(pa.r**3)
    
    cw=calcw(pa, sigmaS)
    
    print('Bend ','phi=',phi,' a=', a, 'b=', b, 'sigmaS=', sigmaS, 'cw=', cw)
    return(cw)

def DPY(pa):
    '''大偏压裂缝计算，轴力是负值'''
    N=abs(pa.N)
    e0=pa.M/N
    
    phi_a=(48.2+614*pa.ae*pa.rou)*(e0/pa.r)+203.6*(pa.rs/pa.r)**2*pa.ae*pa.rou-24.4
    phi_b=(50+390*pa.ae*pa.rou)*(e0/pa.r)-27.3
    phi=phi_a/phi_b
    
    a=130*pa.ae*(pa.rs/pa.r+cos(phi))
    b=27.3*phi+203.6*((pa.rs/pa.r)**2)*pa.ae*pa.rou-24.4
    sigmaS=a/b*N/pa.r**2*e0/pa.r
    
    cw=calcw(pa, sigmaS)
    
    print('DPY ','phi_a=',phi_a,'phi_b=',phi_b,'phi=',phi,' a=', a, 'b=', b, 'sigmaS=', sigmaS, 'cw=', cw)
    return(cw)

pa=inputPara()
main(pa)

        
                
           
