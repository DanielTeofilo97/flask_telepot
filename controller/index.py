import os
ltable = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
cont = 0
idxT = 0


class Index:
    def __init__(self): 
        Index =  0 

    def MontaHtml(self):
        idx = Index()
        indexPage=idx.MontaLinhaTable()
        return indexPage

    def MontaLinhaTable(self):
        indexPage = ''' 
        <meta http-equiv="refresh" content="30">  
        <table style="HEIGHT:100%;WIDTH:100%;" border=1>
        <tr align="center" bottom="middle"><td>
        <table border=2>
        <tr>
        <th>ID</th>
        <th>ID SEND</th>
        <th>ID RECIEVE</th>
        <th>HORA</th>
        <th>STATUS</th>
        <th>MENSAGEM</th>
        </tr>'''
        linhas=''
        i=0
        for i in range(len(ltable)):
            j=0
            if not ltable[i]:
                pass
            else:
                for j in range(1,6):
                    if j==1:
                        linhas +="<tr><td>"+str(ltable[i][0])+"</td>"
                        linhas +="<td>"+str(ltable[i][j])+"</td>"
                    elif j==5:
                        linhas +="<td>"+str(ltable[i][j])+"</td></tr>"
                    else:
                        linhas +="<td>"+str(ltable[i][j])+"</td>"       
        indexPage += linhas+"</table>"                
        return indexPage
    
    def PopulaIndex(self,ids,idr,hr,stf,msg):
        global cont,idxT,ltable
        if cont==30:
            cont=0
        ltable[cont]=[idxT,ids,idr,hr,stf,msg]
        lista_tupla_ordenada = sorted(ltable, reverse=True)
        x = 0
        for x in range(len(lista_tupla_ordenada)):
           ltable[x]=lista_tupla_ordenada[x]  
        cont+=1
        idxT+=1
         

pass


