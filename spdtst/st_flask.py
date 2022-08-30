from flask import Flask,render_template, request
import sys, socket, json, time
from datetime import datetime
from multiprocessing import Process, Queue

app = Flask(__name__)
txtHostName = None
g_txtTarget = 'Red Pitaya'
g_fIsRedPitaya = True
g_fIsontainer = False

#------------------------------------------------------------------------------
@app.route("/")
def index():
    return render_template ("index.html")
   
#------------------------------------------------------------------------------
@app.route('/on_measure_speed')
def OnRedPitayaMessage():
    txtReply = 'Red Pitaya Reply'
    res = request.args['message']
    print(res)
    try:
        res = request.args['message'].lower()
        print('+++++++++++++++++++++++++++++++++++++++++++++')
        print('on_measure_speed')
        print(res)
        dictCommand = json.loads(res)
        txtReply = str(dictCommand)#message_server(dictCommand)
        #if 'setup' in dictCommand:
            #print('calling client_setup_command')
            #txtReply = client_setup_command (dictCommand)
        #else:
            #txtReply = client_read_signal (dictCommand)
    except Exception as e:
        txtReply = "Runtime error in OnRedPitayaMessage:\n{}".format(e)
        print(txtReply)
    print('----------------------------------------------')
    return (txtReply)

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
if (__name__ == '__main__'):
    #print('argc={}'.format(len(sys.argv)))
    #txtHostName = socket.gethostname() + ".local"
    #if (len(sys.argv) > 1):
        #if (sys.argv[1].lower() == 'docker'):
            #txtHostName = '0.0.0.0'
            #g_fIsontainer = True
    txtHostName = '0.0.0.0'
    print('Host Name {}'.format(txtHostName));
    app.run (host=txtHostName, port=5005, debug=True)
    #app.run (host='0.0.0.0', port=5005, debug=True)
    if (socket != None):
        if (hasattr(socket,'close')):
            socket.close()
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
