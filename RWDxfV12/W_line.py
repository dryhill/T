# 写dxf V12的line，进来的列表:[线编号，x1.y1,z1,x2,y2,z2]

def WDxfV12line(f, l):
    ''' 写line，典型的格式,l=[no,x1,y1,z1,x2,y2,z2]：
  0
LINE
  5
FE      #每个线的唯一编号，十六进制
 8
0
 10
111.0   #x1
 20
222.0   #y1
 30
0.0     #z1
 11
333.0   #x2
 21
444.0   #y2
 31 
0.0     #z2   
    '''
    [no,x1,y1,z1,x2,y2,z2]=l
    f.write('  0'+'\n')
    f.write('LINE'+'\n')
    f.write('  5'+'\n')
    f.write(hex(no)[2:]+'\n')  #十进制转换为十六进制，去掉0x的前缀
    f.write('  8'+'\n')
    f.write('0'+'\n')
    f.write(' 10'+'\n')
    f.write(str(x1)+'\n')
    f.write(' 20'+'\n')
    f.write(str(y1)+'\n')   
    f.write(' 30'+'\n')
    f.write(str(z1)+'\n')    
    f.write(' 11'+'\n')
    f.write(str(x2)+'\n')  
    f.write(' 21'+'\n')
    f.write(str(y2)+'\n')    
    f.write(' 31'+'\n')
    f.write(str(z2)+'\n')    
    return()

#f=open('aa.txt', 'w')
#WDxfV12line(f, [12, 111, 222, 0, 333, 444, 0])
#f.close()
