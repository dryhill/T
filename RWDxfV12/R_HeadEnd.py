# 读dxf V12版本的头尾

def RDxfV12HeadEnd():
    ''' 读头尾，总共962行'''
    
    f=open('blank-1lineV12.dxf', 'r')
    t=f.readlines()
    head=t[0:940]
    oneline=t[940:958]
    end=t[958:-1]

    f.close()
    return([head, end])

#[head, end]=RDxfV12HeadEnd()
print('')

