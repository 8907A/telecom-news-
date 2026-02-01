# generate_html.py - 生成静态HTML页面
from datetime import datetime
import sqlite3

def generate_html():
    # 从数据库获取文章信息
    conn = sqlite3.connect('info.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM articles ORDER BY date DESC LIMIT 50")
    articles = c.fetchall()
    conn.close()
    
    # 生成HTML内容
    html_content = f"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>通讯行业信息整合平台</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Microsoft YaHei', Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f5f5f5;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        header {
            background-color: #3498db;
            color: white;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 30px;
            text-align: center;
        }
        
        h1 {
            font-size: 28px;
            margin-bottom: 10px;
        }
        
        .subtitle {
            font-size: 16px;
            opacity: 0.9;
        }
        
        .article-list {
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            padding: 20px;
        }
        
        .article-item {
            border-bottom: 1px solid #eee;
            padding: 20px 0;
        }
        
        .article-item:last-child {
            border-bottom: none;
        }
        
        .article-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 10px;
        }
        
        .article-title {
            font-size: 18px;
            font-weight: bold;
            margin-right: 20px;
            flex: 1;
        }
        
        .article-title a {
            color: #3498db;
            text-decoration: none;
            transition: color 0.3s;
        }
        
        .article-title a:hover {
            color: #2980b9;
            text-decoration: underline;
        }
        
        .article-meta {
            font-size: 12px;
            color: #999;
            white-space: nowrap;
        }
        
        .article-source {
            background-color: #f0f0f0;
            padding: 2px 8px;
            border-radius: 10px;
            margin-right: 10px;
        }
        
        .article-summary {
            font-size: 14px;
            color: #666;
            margin-bottom: 10px;
            line-height: 1.5;
        }
        
        .article-footer {
            font-size: 12px;
            color: #999;
        }
        
        .article-date {
            margin-right: 20px;
        }
        
        .article-category {
            background-color: #e8f4f8;
            padding: 2px 8px;
            border-radius: 10px;
        }
        
        .refresh-info {
            text-align: center;
            margin-top: 20px;
            font-size: 12px;
            color: #999;
        }
        
        @media (max-width: 768px) {
            .article-header {
                flex-direction: column;
                align-items: flex-start;
            }
            
            .article-meta {
                margin-top: 10px;
                white-space: normal;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>通讯行业信息整合平台</h1>
            <p class="subtitle">整合IT之家、通讯行业微信公众号和官网的最新资讯</p>
        </header>
        
        <div class="article-list">
            {''.join([f'''            <div class="article-item">
                <div class="article-header">
                    <h2 class="article-title">
                        <a href="{article['url']}" target="_blank">{article['title']}</a>
                    </h2>
                    <div class="article-meta">
                        <span class="article-source">{article['source']}</span>
                    </div>
                </div>
                <p class="article-summary">{article['summary']}</p>
                <div class="article-footer">
                    <span class="article-date">{article['date']}</span>
                    <span class="article-category">{article['category']}</span>
                </div>
            </div>''' for article in articles])}
        </div>
        
        <div class="refresh-info">
            <p>信息更新时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            <p>手动更新：运行 python app.py update 后运行 python generate_html.py</p>
        </div>
    </div>
</body>
</html>
"""
    
    # 写入HTML文件
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("静态HTML页面生成完成！")
    print("请打开 index.html 文件查看通讯行业资讯。")

if __name__ == '__main__':
    generate_html()
