from datetime import datetime
from flask import Flask, render_template, jsonify
import sqlite3
import logging
from apscheduler.schedulers.background import BackgroundScheduler
import threading

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)

# 初始化数据库
def init_db():
    try:
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
        logger.info("数据库初始化成功")
    except Exception as e:
        logger.error(f"数据库初始化失败: {e}")

# 导入信息获取模块
try:
    from crawlers import wechat_crawler, website_crawler
    from utils.content_processor import filter_content, generate_summary
    logger.info("模块导入成功")
except Exception as e:
    logger.error(f"模块导入失败: {e}")

# 更新信息
def update_info():
    logger.info("开始更新信息...")
    try:
        # 获取通讯行业相关文章
        wechat_crawler.crawl_wechat_articles()
        # 获取通讯行业官网信息
        website_crawler.crawl_website_articles()
        logger.info("信息更新完成！")
    except Exception as e:
        logger.error(f"更新信息时出错: {e}")

# 手动触发更新信息
@app.route('/update')
def manual_update():
    try:
        update_info()
        return "信息更新完成！"
    except Exception as e:
        return f"更新失败: {e}"

# 首页展示信息
@app.route('/')
def index():
    try:
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
    except Exception as e:
        logger.error(f"首页加载失败: {e}")
        return "首页加载失败，请稍后重试"

# API获取文章
@app.route('/api/articles')
def get_articles():
    try:
        conn = sqlite3.connect('info.db')
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute("SELECT * FROM articles ORDER BY date DESC LIMIT 50")
        articles = c.fetchall()
        conn.close()
        return jsonify([dict(row) for row in articles])
    except Exception as e:
        logger.error(f"API获取文章失败: {e}")
        return jsonify([])

if __name__ == '__main__':
    init_db()
    
    # 初始化定时任务
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=update_info, trigger="cron", hour=8, minute=0)  # 每天早上8点更新
    scheduler.start()
    
    # 启动后台线程执行首次信息更新
    def update_info_background():
        try:
            update_info()
        except Exception as e:
            logger.error(f"首次更新信息时出错: {e}")
    
    update_thread = threading.Thread(target=update_info_background)
    update_thread.daemon = True
    update_thread.start()
    
    logger.info("通讯行业信息整合平台启动中...")
    # 启动Flask应用
    app.run(debug=True, host='127.0.0.1', port=5000)
