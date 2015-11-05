# ANSYS to DXF V12
import sys
sys.path.append("..")
from RWANSYS.R_KLIST import *
from RWANSYS.R_LLIST import *

from RWDxfV12.R_HeadEnd import *
from RWDxfV12.W_line import *

#Klist的格式, no,x,y,z
#Llist的格式，no，点1no，点2no
#这里假设导出前都进行了编号压缩，所以能按序取
Noshift=10000  #对线第一个编号加个初始值，防止以前的被其他图元使用
Klist=RKlist()
Llist=RLlist()

[head, end]=RDxfV12HeadEnd()
f=open('line.dxf', 'w')
for t in head:
    f.write(t)

for t in Llist:
    Lno=int(t[0])+Noshift
    pt1No=int(t[1])-1
    pt2No=int(t[2])-1
    x1=Klist[pt1No][1]
    y1=Klist[pt1No][2]    
    z1=Klist[pt1No][3]    

    x2=Klist[pt2No][1]
    y2=Klist[pt2No][2]    
    z2=Klist[pt2No][3] 
    
    l=[Lno, x1, y1, z1, x2, y2, z2]
    WDxfV12line(f, l)

for t in end:
    f.write(t)
f.write('EOF') # end tag 
f.close()
