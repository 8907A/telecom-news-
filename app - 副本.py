from datetime import datetime
from flask import Flask, render_template, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
import os
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

# 导入爬虫模块
from crawlers import wechat_crawler, website_crawler
from utils.content_processor import filter_content, generate_summary

# 定时任务：每天更新信息
def update_info():
    print("开始更新信息...")
    # 抓取微信公众号文章
    wechat_crawler.crawl_wechat_articles()
    # 抓取通讯行业官网信息
    website_crawler.crawl_website_articles()
    print("信息更新完成！")

# 初始化定时任务
scheduler = BackgroundScheduler()
scheduler.add_job(func=update_info, trigger="cron", hour=8, minute=0)  # 每天早上8点更新
scheduler.start()

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

@app.route('/api/articles')
def get_articles():
    conn = sqlite3.connect('info.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM articles ORDER BY date DESC LIMIT 50")
    articles = c.fetchall()
    conn.close()
    return jsonify([dict(row) for row in articles])

if __name__ == '__main__':
    init_db()
    # 首次运行时立即更新信息
    update_info()
    app.run(debug=True)
