import os
import shutil

if os.path.exists('A') :
    shutil.rmtree('A')
    os.mkdir('A')
else:    
    os.mkdir('A')

#inpfile
inpfile='a.inp'
insertLoadinLineNum=125005
#insertLoadinLineNum=124986
inpf=open(inpfile, 'r')

scale=1000
forceNum=1
forcePara=6
sets=['Set-8', 'Set-10','Set-12']
setPrefix=['A-', 'B-', 'C-']
precolNum=1
preRowNum=0
rows=forceNum*forcePara
cols=8

def outConFM(file,case,preFix,Set,f):

    Ftype='Concentrated force'
    casename=preFix+case+'-F' 
    file.write('**Name:'+casename+' Type:'+Ftype+'\n')
    file.write('*Cload'+'\n')
    file.write(Set+',1,'+str(round(f[0]*scale,2))+'\n')
    file.write(Set+',2,'+str(round(f[1]*scale,2))+'\n')
    file.write(Set+',3,'+str(round(f[2]*scale,2))+'\n') 
        
    Ftype='Moment'
    casename=preFix+case+'-M'   
    file.write('**Name:'+casename+' Type:'+Ftype+'\n')
    file.write('*Cload'+'\n')
    file.write(Set+',4,'+str(round(f[3]*scale,2))+'\n')
    file.write(Set+',5,'+str(round(f[4]*scale,2))+'\n')
    file.write(Set+',6,'+str(round(f[5]*scale,2))+'\n') 
            


f=open('load.txt','r')
t=f.readline()
caseCN=t.split()
del caseCN[0]
del caseCN[0]
#caseEN=  ['DEAD','Live','T+20','T-20','Wind30','Wind120','Wind150','Wind180','Wind210','Wind240','Wind330','EX','EY','EZ']
#caseTag=['D','L','T','T','W','W','W','W','W','W','W','EX','EY','EZ']

caseEN=  ['DEAD','Live','T+20','T-20','Wind330','EX','EY','EZ']
caseTag=['D','L','T','T','W','EX','EY','EZ']

Dindex=[]
Lindex=[]
Tindex=[]
Windex=[]
EXindex=[]
EYindex=[]
EZindex=[]
for i in range(0, len(caseTag)):
    t=caseTag[i]
    if t=='D':Dindex.append(i)
    if t=='L':Lindex.append(i)
    if t=='T':Tindex.append(i)
    if t=='W':Windex.append(i)
    if t=='EX':EXindex.append(i)
    if t=='EY':EYindex.append(i)
    if t=='EZ':EZindex.append(i)

forceLines=[]
for i in range(0, rows):
    t=f.readline().split()
    forceLines.append(t)

#to float
for i in range(0, rows):
    t=forceLines[i]
    for j in range(1, len(t)):
        t[j]=float(t[j])
#    print(t)

#to column force
forceColum=[]
for j in range(0, cols):
    t=[]
    for i in range(0, rows):
        t.append(forceLines[i][j+precolNum])
    forceColum.append(t)
    
#to subdir
os.chdir('A')

#print(forceColum)
#output case Keyword
for j in range(0,len(caseEN)):
    file=open(caseEN[j]+'.txt','w') 
    #
    for i in range(0,forceNum):
        F=forceColum[j][i*forcePara:(i+1)*forcePara]
        outConFM(file,caseEN[j],setPrefix[i],sets[i],F)
    file.close()

#combo
combo=['C1.2D+1.4L','C1.35D+0.98L',
       'C1.2G+1.3EX+0.5EZ','C1.2G+1.3EX-0.5EZ',
       'C1.2G-1.3EX+0.5EZ','C1.2G-1.3EX-0.5EZ',
       'C1.2G+1.3EY+0.5EZ','C1.2G+1.3EY-0.5EZ',
       'C1.2G-1.3EY+0.5EZ','C1.2G-1.3EY-0.5EZ',       
       'C1.2G+0.5EX+1.3EZ','C1.2G+0.5EX-1.3EZ',
       'C1.2G-0.5EX+1.3EZ','C1.2G-0.5EX-1.3EZ',       
       'C1.2G+0.5EY+1.3EZ','C1.2G+0.5EY-1.3EZ',
       'C1.2G-0.5EY+1.3EZ','C1.2G-0.5EY-1.3EZ',       
       'C1.2D+1.4W','C1.0D+1.4W',
       'C1.2D+1.4L+0.84W','C1.0D+1.4L+084W',
       'C1.2D+0.98L+1.4W','C1.0D+0.98L+1.4W',
       'C1.35D+0.98L+0.84W','C1.35D+0.84W',
       'C1.2G+1.35EX+0.28W','C1.2G-1.35EX+0.28W',
       'C1.2G+1.35EY+0.28W','C1.2G-1.35EY+0.28W',
       'C1.2G+1.35EZ+0.28W','C1.2G-1.35EZ+0.28W',       
       'C1.0G+1.35EX+0.28W','C1.0G-1.35EX+0.28W',
       'C1.0G+1.35EY+0.28W','C1.0G-1.35EY+0.28W',
       'C1.0G+1.35EZ+0.28W','C1.0G-1.35EZ+0.28W',
       'C1.0D+T',
       'C1.2D+1.4L+T'        
       ]

fa=[
[1.2,   1.4,    0,  0,  0,  0,0], 
[1.35,  0.98,   0,  0,  0,  0,0], 
[1.2,   0.6,    1.3,0,  0.5,0,0], 
[1.2,   0.6,    1.3,0, -0.5,0,0], 
[1.2,   0.6,   -1.3,0,  0.5,0,0], 
[1.2,   0.6,   -1.3,0, -0.5,0,0], 
[1.2,   0.6,   0, 1.3,  0.5,0,0], 
[1.2,   0.6,   0, 1.3, -0.5,0,0], 
[1.2,   0.6,   0,-1.3,  0.5,0,0], 
[1.2,   0.6,   0,-1.3, -0.5,0,0], 
[1.2,   0.6,    0.5,0,  1.3,0,0], 
[1.2,   0.6,    0.5,0, -1.3,0,0], 
[1.2,   0.6,   -0.5,0,  1.3,0,0], 
[1.2,   0.6,   -0.5,0, -1.3,0,0], 
[1.2,   0.6,   0, 0.5,  1.3,0,0], 
[1.2,   0.6,   0, 0.5, -1.3,0,0], 
[1.2,   0.6,   0,-0.5,  1.3,0,0], 
[1.2,   0.6,   0,-0.5, -1.3,0,0], 
[1.2,  0,    0,  0,  0,  1.4,0], 
[1.0,  0,    0,  0,  0,  1.4,0], 
[1.2,  1.4,    0,  0,  0,  0.84,0], 
[1.0,  1.4,    0,  0,  0,  0.84,0], 
[1.2,  0.98,    0,  0,  0,  0.84,0], 
[1.0,  0.98,    0,  0,  0,  0.84,0], 
[1.35,  0.98,    0,  0,  0,  0.84,0], 
[1.35,  0,       0,  0,  0,  0.84,0], 
[1.2,  0.6,   1.35,  0,  0,  0.28,0], 
[1.2,  0.6,  -1.35,  0,  0,  0.28,0], 
[1.2,  0.6,   0,   1.35,    0,  0.28,0], 
[1.2,  0.6,   0,  -1.35,    0,  0.28,0], 
[1.2,  0.6,   0,   0,  1.35,    0.28,0], 
[1.2,  0.6,   0,   0, -1.35,    0.28,0], 
[1.0,  0.6,   1.35,  0,  0,  0.28,0], 
[1.0,  0.6,  -1.35,  0,  0,  0.28,0], 
[1.0,  0.6,   0,   1.35,    0,  0.28,0], 
[1.0,  0.6,   0,  -1.35,    0,  0.28,0], 
[1.0,  0.6,   0,   0,  1.35,    0.28,0], 
[1.0,  0.6,   0,   0, -1.35,    0.28,0], 
[1.0,   0,    0,  0,  0,  0,1], 
[1.2, 1.4,    0,  0,  0,  0,1], 
[1.0, 0,    0,  0,  0,  0,0], 
[0, 1.0,    0,  0,  0,  0,0], 
[0, 0,    1.0,  0,  0,  0,0], 
[0, 0,      0,  1,  0,  0,0], 
[0, 0,      0,  0,  1,  0,0], 
[0, 0,      0,  0,  0,  1,0], 
[0, 0,      0,  0,  0,  0,1]
]

#print(fa)
#cases
comboname=[]
comboforce=[]
for i in range(0, len(fa)):
    for id in range(0, len(Dindex)):
        for il in range(0, len(Lindex)):
            for it in range(0, len(Tindex)):
                for iw in range(0, len(Windex)):
                    for iex in range(0, len(EXindex)):
                        for iey in range(0, len(EYindex)):
                            for iez in range(0, len(EZindex)):
                                dc=forceColum[Dindex[id]]
                                lc=forceColum[Lindex[il]]
                                tc=forceColum[Tindex[it]]
                                wc=forceColum[Windex[iw]]
                                exc=forceColum[EXindex[iex]]
                                eyc=forceColum[EYindex[iey]]
                                ezc=forceColum[EZindex[iez]]
                                
                                factor=fa[i]
                                ca=[caseEN[Dindex[id]], caseEN[Lindex[il]], caseEN[EXindex[iex]], caseEN[EYindex[iey]], caseEN[EZindex[iez]],caseEN[Windex[iw]],  caseEN[Tindex[it]]]
                                caf=[]
                                #combo faorce
                                for j in range(0, rows):
                                    caf.append(dc[j]*factor[0]+lc[j]*factor[1]+exc[j]*factor[2]+eyc[j]*factor[3]+ezc[j]*factor[4]+wc[j]*factor[5]+tc[j]*factor[6])
                                
                                for j in range(0, len(caf)):
                                    caf[j]=round(caf[j], 2)
                                    
                                caname='C'                                
                                for j in range(0, len(factor)):                                    
                                    if factor[j]!=0:
                                        caname=caname+str(factor[j])+ca[j]+'+'
                                if caname not in comboname: 
                                    comboname.append(caname)
                                    comboforce.append(caf)
                                    
for i in range(len(comboname)):
    print(i, comboname[i])
    print(i, comboforce[i])

#output combo Keyword
for j in range(0,len(comboname)):
    file=open(str(j)+comboname[j]+'.txt','w') 
    #
    for i in range(0,forceNum):
        F=comboforce[j][i*forcePara:(i+1)*forcePara]
        outConFM(file,comboname[j],setPrefix[i],sets[i],F)
    file.close()

#output combo force to txt
file=open('comboForce.txt', 'w')
for j in range(0, len(comboforce)):
    file.write('%40s'%(str(j)+comboname[j]))
file.write('\n')    
    
for i in range(0, rows):
    for j in range(0, len(comboforce)):
        file.write('%10.2f'%comboforce[j][i])
    file.write('\n')
file.close() 

#read inp file
doc=[]
while True:
    line=inpf.readline()
    if line: doc.append(line)
    if not line.strip(): break

for j in range(0,len(comboname)):
    file=open(str(j)+comboname[j]+'.inp','w') 
    #
    #first 
    file.write(doc[0])
    file.write(doc[1].replace('LOADCASE', comboname[j]))
    
    #2
    for i in range(2, insertLoadinLineNum):
        file.write(doc[i])
    #3    
    for i in range(0,forceNum):
        F=comboforce[j][i*forcePara:(i+1)*forcePara]
        outConFM(file,comboname[j],setPrefix[i],sets[i],F)
    
    #4
    for i in range(insertLoadinLineNum, len(doc)):
        file.write(doc[i])    
    
    file.close()
                                
