import os
import telepot
from controller import funcoes
from controller import index
bot = telepot.Bot("1302528698:AAGV4qG8IkcWjt7ODYv8b8Id7Uf6JrnD4ok")
func = funcoes.Funcoes()
idx = index.Index()
id_send = "-459839545"


class Core:
    def __init__(self): 
        Core =  0 

    def EnviaFoto(self,msg):
        fileid=''
        try:
            fileid = func.RetornaFileId(msg['photo'])
            id_group,texto,cod= func.retornaIdGroupSendMsg(msg['caption']) 
            bot.sendPhoto(id_group,fileid,texto)
            texto = '😉👍✅ Foto encaminhada com êxito para o group de id('+str(id_group)+')\n Código grupo = ('+str(cod)+')'
            bot.sendMessage(-437185665,texto)
            print('Foto enviada com sucesso para o grupo de id('+str(id_group)+')')
            data = func.Now()
            texto ='😉👍✅ Foto encaminhada com êxito'
            idx.PopulaIndex(id_send,id_group,data,"GOOD",texto)
        except :
            texto ='❌❌Erro ao enviar Foto❌❌\n  Não foi possivel encaminhar'
            texto += ' a foto pois não consegui achar o id do grupo 😥 : \n SEGUE ABAIXO o FILE_ID >>>>>\n ' +fileid
            bot.sendMessage(-437185665, texto)
            print('Erro ao enviar foto...')
            data = func.Now()
            texto ='❌❌Erro ao enviar Foto❌❌'
            idx.PopulaIndex(id_send,"-437185665",data,"BAD",texto)
            
    
    def EnviaMsg(self,msg):
        try:
            id_group,texto,cod= func.retornaIdGroupSendMsg(msg['text'])
            bot.sendMessage(id_group,texto)
            texto = '😉👍✅Mensagem encaminhada com êxito para o group de id('+str(id_group)+')\n Código grupo = ('+str(cod)+')'
            bot.sendMessage("-437185665",texto)
            print('Mensagem enviada com sucesso para o grupo de id('+str(id_group)+')')
            data = func.Now()
            texto = '😉👍✅Mensagem encaminhada com êxito'
            idx.PopulaIndex(id_send,id_group,data,"GOOD",texto)
        except:
            texto ='❌❌Erro ao enviar mensagem❌❌\n  Não foi possivel encaminhar'
            texto += ' a mensagem pois não consegui achar o id do grupo 😥 : \n SEGUE ABAIXO A MENSAGEM >>>>>\n ' +msg['text'] 
            bot.sendMessage("-437185665", texto)
            print('Erro ao enviar mensagem...')
            data = func.Now()
            texto ='❌❌Erro ao enviar mensagem❌❌'
            idx.PopulaIndex(id_send,"-437185665",data,"BAD",texto)
pass     