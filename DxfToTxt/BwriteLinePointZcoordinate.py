
dxfile='lt.dxf'
dzShift=-0.28


def readDxfLine():
    
    '''
      0
    LINE
      5
    67
      8
    0
     10
    155100.61945788231
     20
    8800.0002783924792
     30
    23120.635092187811
     11
    154500.61945788091
     21
    8799.9992418844322
     31
    23106.240409144099
    '''
    
    t=f.readline()  #4 lines
    t=f.readline() 
    t=f.readline() 
    t=f.readline() 

    t=f.readline() #10
    startX=f.readline().strip()
    t=f.readline() #20
    startY=f.readline().strip()
    t=f.readline() #30
    startZ=f.readline().strip()  
  
    t=f.readline() #11  
    endX=f.readline().strip()
    t=f.readline() #21
    endY=f.readline().strip()
    t=f.readline() #31
    endZ=f.readline().strip()   

    return([(startX, startY, startZ), (endX, endY, endZ)])
    
def writeDxfText(x, y, z, text, height, id):
    ''' write text at (x,y,z) position, dxf format CAD12:
  0
TEXT
  5
150   (id)
  8
0
 10
66.0  (x)
 20   (y)
77.0
 30   (z)
88.0
 40
300.0  (height)
  1
casa   (text)
    '''       
    
    #begin write
    f.write(
    '''0
TEXT
  5
''')
    f.write(str(id)+'\n')

    f.write(
''' 8
0
 10
 ''')
 
    f.write(str(x)+'\n')
    f.write(' 20'+'\n')
    f.write(str(y)+'\n')  
    f.write(' 30'+'\n')  
    f.write(str(z)+'\n') 
    f.write('40'+'\n')
    f.write(str(height)+'\n')
    f.write(' 1\n')
    f.write(str(text)+'\n')   
    return()
        

f=open(dxfile, 'r')
fileRowNum=len(f.readlines())
f.seek(0)
i=1

lineEntity=[]
circleEntity=[]
polylineEntity=[]
while True:
    t=f.readline().strip()
#    print(i, t)
    i=i+1
    if t=='LINE': 
        print('find Line')
        lineEntity.append(readDxfLine())
        i=i+16
         
    if i>fileRowNum: break

print(lineEntity)
f.close()

f=open('textfile.dxf', 'w')
f1=open('blanK-only1text-Dxf.dxf', 'r')
ta=f1.readlines()
f1.seek(0)
for i in range(0, 946):
    f.write(ta[i])  

#collect points
pointEntity=[]
for t in lineEntity:
    pti=t[0]
    ptj=t[1]
    if pti not in pointEntity: pointEntity.append(pti)
    if ptj not in pointEntity: pointEntity.append(ptj)   

#write z coordinate, float 2
for i in range(0, len(pointEntity)):
    t=pointEntity[i]
    x=round(float(t[0]), 2)
    y=round(float(t[1]), 2)
    z=round(float(t[2]), 2)   
    text=round(float(t[2])/1000+dzShift, 3) 
    writeDxfText(x, y, z, text, 150, '1E'+str(i))

#writeDxfText(55, 66, 77, 'AABB', 300, 100)
#writeDxfText(10, 11, 12, 'BBCC', 300, 101)
# 
for i in range(962, len(ta)):
    f.write(ta[i])
f.close()
f1.close()

    
    
