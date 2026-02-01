from datetime import datetime
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# 初始化数据库
def init_db():
    conn = sqlite3.connect('info.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS articles
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT NOT NULL,
                  summary TEXT,
                  url TEXT NOT NULL,
                  source TEXT NOT NULL,
                  date TEXT NOT NULL,
                  category TEXT,
                  content TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    # 从数据库获取文章信息
    conn = sqlite3.connect('info.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM articles ORDER BY date DESC LIMIT 50")
    articles = c.fetchall()
    conn.close()
    # 添加当前时间
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', articles=articles, current_time=current_time)

if __name__ == '__main__':
    init_db()
    print("通讯行业信息整合平台启动中...")
    print("访问地址: http://127.0.0.1:5000")
    app.run(debug=True, host='127.0.0.1', port=5000)
