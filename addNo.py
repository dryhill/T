#add no

f=open('a.lgw','r')
w=open('addno.lgw', 'w')

tag=0
noshift=10000
while not tag:
    t=f.readline()
    if(t!=''):
        if t.find('k,')>=0:
            ta=t.split(',')
            ta[1]=str(int(ta[1])+noshift)
            w.write(','.join(ta))
            continue
        if t.find('l,')>=0:
            ta=t.split(',')
            ta[1]=str(int(ta[1])+noshift)    
            ta[2]=str(int(ta[2])+noshift)              
            w.write(','.join(ta)+'\n')
            continue
        if t.find('k,')<0 or t.find('l,')<0: 
            w.write(t)
       
    else:
        tag=1
f.close()
w.close()

