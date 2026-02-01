@echo off
echo =========================================
echo 通讯行业信息整合平台 - 一键更新并查看
echo =========================================
echo.
echo 1. 正在更新通讯行业资讯...
echo.
python app.py update
echo.
echo 2. 正在生成静态HTML页面...
echo.
python generate_html.py
echo.
echo 3. 正在打开网页查看资讯...
echo.
start index.html
echo.
echo 操作完成！您现在可以在浏览器中查看最新的通讯行业资讯。
echo.
pause
