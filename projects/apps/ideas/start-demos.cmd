@echo off
setlocal
cd /d "%~dp0"

echo Starting the demo server at http://127.0.0.1:8765 ...
echo Keep the "Agentic Demo Server" window open while you browse.
echo Close that window to stop the server.

start "Agentic Demo Server" py -m http.server 8765 --bind 127.0.0.1
timeout /t 2 /nobreak >nul
start "" "http://127.0.0.1:8765/index.html"

endlocal
