# 测试Flask应用
import sys
print(f"Python版本: {sys.version}")

# 测试Flask是否能正常导入和使用
try:
    from flask import Flask
    print("Flask导入成功")
    
    app = Flask(__name__)
    
    @app.route('/')
    def hello():
        return 'Hello, World!'
    
    print("Flask应用创建成功")
    print("尝试启动Flask应用...")
    
    # 使用不同的端口
    app.run(debug=True, host='127.0.0.1', port=8080, use_reloader=False)
    
except Exception as e:
    print(f"错误: {e}")
    import traceback
    traceback.print_exc()
