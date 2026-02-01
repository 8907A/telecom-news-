# 最简单的Flask测试应用
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World! 通讯行业信息整合平台测试成功！'

if __name__ == '__main__':
    print("启动最简单的Flask应用...")
    print("访问地址: http://127.0.0.1:8080")
    app.run(debug=True, host='127.0.0.1', port=8080, use_reloader=False)
