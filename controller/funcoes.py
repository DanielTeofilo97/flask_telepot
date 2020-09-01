import telepot
import os
import json
from datetime import datetime
#list1 = ['TEN','VOL','CAV']
#list2 = ['-439019312','-437201495','-446151491']
name_groups = ['TEN','VOL','CAV']
groups_id = ['-439019312','-437201495','-446151491']

class Funcoes:
    def __init__(self): 
        Funcoes =  0 

    def GetGroupsAndIds(self):
        # Armazena name groups
        #for items in list1:
            #name_groups = items.split(',')
        # Armazena id groups
        #for items in list2:
            #groups_id = items.split(',')
        return groups_id,name_groups

    def retornaIdGroupSendMsg(self,text):
        group = text[0:3]
        texto = text.replace(group,'')
        txt = '🤖💲 TOC MILIONÁRIO BOT 💲🤖'
        txt +='\n'+ texto
        func =  Funcoes()
        ids,groups = func.GetGroupsAndIds()
        cont=0
        for name_group in groups:
            if name_group == group:
                id_gp = ids[cont]
            cont +=1
        return id_gp,txt,group  
        
    def RetornaFileId(self,fileId):
        d = str(fileId)
        json1 = d.replace("'",'"')
        json2 = json.loads(json1)
        try:
            json3 = json2[2]
        except:
            json3 = json2[1]
        else:
            json3 = json2[0]
        json4 = json3['file_id']
        return json4

    def Now(self):
        now = datetime.now()
        now = now.strftime("%d/%m/%Y %H:%M:%S")
        return now    

pass




   


