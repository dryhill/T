
dxfile='a.dxf'



def readDxfLine():
    
    #LINE example        
    #        LINE
    #          5
    #        DF
    #        330
    #        19
    #        100
    #        AcDbEntity
    #          8
    #        0
    #        100
    #        AcDbLine
    #         10
    #        111.0
    #         20
    #        222.0
    #         30
    #        0.0
    #         11
    #        444.0
    #         21
    #        666.0
    #         31
    #        0.0
    #          0
    
    t=f.readline()  #10 line
    t=f.readline() 
    t=f.readline() 
    t=f.readline() 
    t=f.readline() 
    t=f.readline() 
    t=f.readline() 
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

    t=f.readline()     
    return([(startX, startY, startZ), (endX, endY, endZ)])
    
def readDxfCircle():

    #circle example
    #CIRCLE
    #  5
    #2B1
    #330
    #29F
    #100
    #AcDbEntity
    #  8
    #0
    #100
    #AcDbCircle
    # 10
    #8888.0
    # 20
    #9999.0
    # 30
    #0.0
    # 40
    #556.0
    #  0
    t=f.readline()  #10 line
    t=f.readline() 
    t=f.readline() 
    t=f.readline() 
    t=f.readline() 
    t=f.readline() 
    t=f.readline() 
    t=f.readline() 
    t=f.readline() 
    t=f.readline()     
    t=f.readline() #10
    X=f.readline().strip()
    t=f.readline() #20
    Y=f.readline().strip()    
    t=f.readline() #30
    Z=f.readline().strip()   
    t=f.readline() #40
    R=f.readline().strip()
    return([X, Y, Z, R])

def readDxfPolyline(i):
    
    #example polyline
#    AcDbPolyline
#     90
#            6
#     70
#         1
#     43
#    0.0
#     10
#    11.0
#     20
#    22.0
#     10
#    333.0
#     20
#    444.0
#     10
#    -555.0
#     20
#    666.0
#     10
#    -777.0
#     20
#    -888.0
#     10
#    -211.0444175097509
#     20
#    -658.847285332602
#     10
#    -35.41183699168596
#     20
#    -103.3667682562161
#      0
    x=[]
    y=[]
    t=f.readline()  
    edgeNum=int(f.readline())
    t=f.readline()  #70
    t=f.readline()  #1
    t=f.readline()  #43
    t=f.readline()  #0.0
    i=i+7
    for j in range(0, edgeNum):
        t=f.readline()  #10
        x.append(f.readline().strip())
        t=f.readline()  #20
        y.append(f.readline().strip())   
        i=i+4
    vertexPoint=[]
    for j in range(0, edgeNum):
        vertexPoint.append((x[j], y[j]))
        
    return(vertexPoint)
    

    
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
        i=i+23
    if t=='CIRCLE': 
        print('find circle')
        circleEntity.append(readDxfCircle())
        i=i+23    
    if t=='AcDbPolyline':
        print('polyline', i)
        polylineEntity.append(readDxfPolyline(i))
        print(i)
        
    if i==fileRowNum: break

print(lineEntity)
print(polylineEntity)
print(circleEntity)
f.close()

    
    
