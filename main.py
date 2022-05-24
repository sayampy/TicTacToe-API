from flask import *
from flask_session import Session
from game import check_game,print_game
app = Flask(__name__,static_url_path='')
app.config["SESSION_PERMANENT"] = False

app.config["SESSION_TYPE"] = "filesystem"
Session(app)
@app.route('/',methods=['GET'])
def index():
    if request.args.get('place'):
        place = int(request.args.get('place'))-1
        if not session.get('board'):
            session['board']=[None]*9
        if session['board'][place]==None:
            session['board'][place]='X'
            print_game(session['board'])
        game=check_game(session.get('board'))
    return return #'<script>window.close();</script>'
        

@app.route('/img',methods=['GET'])
def image():
    file='empty.png'
    if session.get('board'):
        if request.args.get('place'):
            place = int(request.args.get('place'))-1
            move = session['board'][place]
            if move=='X':
                file='X.png'
            if move=='O':
                file='O.png'
    return send_file(f'./static/{file}', mimetype='image/png')
@app.route('/restart')
def restart():
    session['board']=None
    return '<script>close();</script>'
@app.route('/test')
def test():
    return rendertemplate('test.html')

if __name__=='__main__':
    __import__('os').system('clear')
    app.run(host='0.0.0.0', port=81)