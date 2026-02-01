import sqlite3

def add_sample_articles():
    """向数据库添加示例文章"""
    conn = sqlite3.connect('info.db')
    c = conn.cursor()
    
    # 示例文章数据
    sample_articles = [
        {
            'title': '5G技术在通讯行业的应用与发展',
            'summary': '本文详细介绍了5G技术在通讯行业的最新应用，包括工业互联网、车联网、智慧医疗等领域，并分析了未来发展趋势。',
            'url': 'https://example.com/5g-application',
            'source': 'T之家',
            'date': '2026-01-31',
            'category': '微信公众号',
            'content': '5G技术作为新一代移动通信技术，正在深刻改变着通讯行业的发展格局...'
        },
        {
            'title': '中国移动发布2026年5G网络建设计划',
            'summary': '中国移动今日发布了2026年5G网络建设计划，计划新增5G基站100万个，实现全国乡镇以上区域5G网络全覆盖。',
            'url': 'https://example.com/china-mobile-5g-plan',
            'source': '中国移动官网',
            'date': '2026-01-30',
            'category': '官网',
            'content': '1月30日，中国移动在2026年工作会议上发布了本年度5G网络建设计划...'
        },
        {
            'title': '华为发布全新5G芯片，性能提升50%',
            'summary': '华为今日发布了新一代5G芯片，采用7nm工艺，性能相比上一代提升50%，功耗降低30%。',
            'url': 'https://example.com/huawei-5g-chip',
            'source': '华为官网',
            'date': '2026-01-29',
            'category': '官网',
            'content': '1月29日，华为在深圳总部举行发布会，正式发布新一代5G芯片...'
        },
        {
            'title': '通讯行业2026年发展趋势分析',
            'summary': '本文分析了2026年通讯行业的发展趋势，包括5G普及、物联网增长、人工智能应用等方面。',
            'url': 'https://example.com/telecom-trends-2026',
            'source': '通讯世界',
            'date': '2026-01-28',
            'category': '微信公众号',
            'content': '随着技术的不断进步，通讯行业在2026年将迎来新的发展机遇...'
        },
        {
            'title': '中国联通与腾讯达成5G战略合作',
            'summary': '中国联通今日宣布与腾讯达成5G战略合作，双方将在云游戏、直播等领域开展深度合作。',
            'url': 'https://example.com/china-unicom-tencent-partnership',
            'source': '中国联通官网',
            'date': '2026-01-27',
            'category': '官网',
            'content': '1月27日，中国联通与腾讯在深圳签署5G战略合作协议...'
        }
    ]
    
    # 插入示例文章
    for article in sample_articles:
        # 检查是否已存在
        c.execute("SELECT id FROM articles WHERE url = ?", (article['url'],))
        if not c.fetchone():
            c.execute('''INSERT INTO articles (title, summary, url, source, date, category, content)
                         VALUES (?, ?, ?, ?, ?, ?, ?)''',
                      (article['title'], article['summary'], article['url'], 
                       article['source'], article['date'], article['category'], article['content']))
            print(f"添加文章: {article['title']}")
    
    conn.commit()
    conn.close()
    print("示例文章添加完成！")

if __name__ == '__main__':
    add_sample_articles()