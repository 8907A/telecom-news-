# 简单的测试脚本
print("Hello, World!")

# 测试Flask是否能正常导入
try:
    from flask import Flask
    print("Flask导入成功")
except Exception as e:
    print(f"Flask导入失败: {e}")

# 测试feedparser是否能正常导入
try:
    import feedparser
    print("feedparser导入成功")
except Exception as e:
    print(f"feedparser导入失败: {e}")

# 测试requests是否能正常导入
try:
    import requests
    print("requests导入成功")
except Exception as e:
    print(f"requests导入失败: {e}")
