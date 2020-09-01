import os
ltable = [[],[],[],[],[],[],[],[],[],[]]
cont = 0


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
                for j in range(5):
                    if j==0:
                        linhas +="<tr><td>"+str(i)+"</td>"
                        linhas +="<td>"+str(ltable[i][j])+"</td>"
                    elif j==4:
                        linhas +="<td>"+str(ltable[i][j])+"</td></tr>"
                    else:
                        linhas +="<td>"+str(ltable[i][j])+"</td>"
        indexPage += linhas+"</table>"                
        return indexPage
    
    def PopulaIndex(self,ids,idr,hr,stf,msg):
        global cont
        if cont==10:
            cont=0
        ltable[cont]=[ids,idr,hr,stf,msg] 
        cont+=1   

pass


