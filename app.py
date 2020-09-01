from flask import Flask
from flask_cors import CORS
import sys,os
import time
import telepot
from telepot.loop import MessageLoop
from telepot.aio.delegate import pave_event_space, per_chat_id, create_open
from controller import core
from controller import index
business = core.Core()
idx = index.Index()



app = Flask(__name__)

cors = CORS(app,resource={r"/*":{ "origins" : "*" }})

@app.route("/",methods=['GET'])
def index():
    return idx.MontaHtml()

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    chatid = int("-459839545")
    if content_type == 'photo'and chat_id == chatid:
        business.EnviaFoto(msg)
    if content_type == 'text' and chat_id == chatid:
        business.EnviaMsg(msg)    

def main():
    bot = telepot.Bot("1302528698:AAGV4qG8IkcWjt7ODYv8b8Id7Uf6JrnD4ok")
    MessageLoop(bot, handle).run_as_thread()
    print ('Escutando ...')
    port = int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0",port=port) 

if __name__ == "__main__":
    main()

