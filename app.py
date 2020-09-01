from flask import Flask
from flask_cors import CORS
import sys,os
import time
import telepot
from telepot.loop import MessageLoop
from controller import core
from controller import index
business = core.Core()
idx = index.Index()
bot = telepot.Bot(os.getenv('ID_BOT'))


app = Flask(__name__)

cors = CORS(app,resource={r"/*":{ "origins" : "*" }})

@app.route("/",methods=['GET'])
def index():
    return idx.MontaHtml()

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'photo'and chat_id == int(os.getenv('ID_LISTEN')):
        business.EnviaFoto(msg)
    if content_type == 'text' and chat_id == int(os.getenv('ID_LISTEN')):
        business.EnviaMsg(msg)    

def main():
    MessageLoop(bot, handle).run_as_thread()
    print ('Escutando ...')
    port = int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0",port=port) 

if __name__ == "__main__":
    main()

