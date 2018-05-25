import os
import flask
import time, datetime

app = flask.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  if flask.request.method == 'POST':
    pass
  return flask.render_template('pepper.html', text="Hello")

@app.route('/' + '<action>')
def act(action):
  return flask.render_template('pepper.html', text=action)

if __name__ == '__main__':
  app.run(host='0.0.0.0')
