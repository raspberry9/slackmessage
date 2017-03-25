import os
from flask import Flask
from flask import jsonify, request

app = Flask(__name__)

@app.route('/test', methods=['GET', 'POST'])
def test():
    content = request.get_json(silent=True)
    print(content)
    return 'success'

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    data = {
        "text": "Would you like to play a game?",
        "attachments": [
            {
                "text": "Choose a game to play",
                "fallback": "You are unable to choose a game",
                "callback_id": "wopr_game",
                "color": "#3AA3E3",
                "attachment_type": "default",
                "actions": [
                    {
                        "name": "game",
                        "text": "Chess",
                        "type": "button",
                        "value": "chess"
                    },
                    {
                        "name": "game",
                        "text": "Falken's Maze",
                        "type": "button",
                        "value": "maze"
                    },
                    {
                        "name": "game",
                        "text": "Thermonuclear War",
                        "style": "danger",
                        "type": "button",
                        "value": "war",
                        "confirm": {
                            "title": "Are you sure?",
                            "text": "Wouldn't you prefer a good game of chess?",
                            "ok_text": "Yes",
                            "dismiss_text": "No"
                        }
                    }
                ]
            }
        ]
    }
    return jsonify(data)      

if __name__ == '__main__':
    host = os.environ.get('SERVER_HOST', '0.0.0.0')
    try:
        port = int(os.environ.get('SERVER_PORT', '5000'))
    except:
        port = 5000

    app.run(host=host, port=port)
