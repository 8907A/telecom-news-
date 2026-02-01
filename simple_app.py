# 最简单的Flask应用
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    print("启动最简单的Flask应用...")
    app.run(debug=True, host='127.0.0.1', port=5000)
