#!/bin/bash
# 韩国女团随机抽取器启动脚本
DIR="$(cd "$(dirname "$0")" && pwd)"

# 找一个空闲端口
PORT=$(python3 -c "import socket; s=socket.socket(); s.bind(('',0)); print(s.getsockname()[1]); s.close()")

echo "正在启动韩国女团随机抽取器..."
echo "地址: http://localhost:$PORT"

# 启动服务器并打开浏览器
cd "$DIR"
python3 -c "
import webbrowser, threading, http.server, socketserver

PORT = $PORT
handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(('', PORT), handler)

threading.Timer(0.5, lambda: webbrowser.open(f'http://localhost:{PORT}')).start()

print(f'服务器已启动，按 Ctrl+C 停止')
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print('\n已停止')
    httpd.shutdown()
"
