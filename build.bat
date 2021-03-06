@ECHO OFF

::修改console默认encoding为utf8，避免中文乱码
CHCP 65001

echo.
echo     此文件为自动编译计算器为exe程序脚本,需提前安装以下依赖
echo       - python
echo       - pyinstaller
echo       - PyQt5
echo     如需自动根据submit更新CHANGELOG并生成更新日志,需提前安装以下依赖
echo       - node.js
echo       - pandoc
echo     如需自动上传到蓝奏云,需要提前安装以下依赖
echo       - lanzou-api
echo.

pause

@REM 检查python

@REM for /f "tokens=2" %%h in ('python -h ^| findstr /C:"usage:"') do ^
@REM set PYVER2=%%h
@REM if "%PYVER2%" != "python" (@echo 未安装python)

echo.
echo [提示]: 开始发布版本
echo.

echo [提示]: 开始生成exe文件
::使用pyinstaller打包
pyinstaller.exe --hidden-import pkg_resources.py2_warn  --noconsole -F -i ./ResourceFiles/img/logo.ico "main.py"

DEL /Q "AutoRelese\Publish\*.*"
DEL /Q "main.spec"
COPY /Y "dist\main.exe" "main.exe"
RMDIR /S /Q "build" "dist" "__pycache__" "logs" ".\Part\__pycache__" ".\PublicReference\__pycache__"
for /d %%i in (ResourceFiles\*) do if exist "%%i\set" RMDIR /s /q "%%i\set"

echo [提示]: 生成结束

if not exist AutoRelese\Publish MD AutoRelese\Publish

if exist AutoRelese\Rar.exe echo [提示]: 开始压缩打包版本
::复制生成的结果后删除临时文件
::rar压缩
if exist AutoRelese\Rar.exe AutoRelese\Rar.exe a "AutoRelese\publish\DNF计算器%Date:~5,2%.%Date:~8,2%.zip" "main.exe" "ResourceFiles"
if exist AutoRelese\Rar.exe AutoRelese\Rar.exe a "AutoRelese\publish\源码%Date:~5,2%.%Date:~8,2%.zip" "ResourceFiles" "main.py" "Part" "PublicReference"
if exist AutoRelese\Rar.exe AutoRelese\Rar.exe rn "AutoRelese\publish\DNF计算器%Date:~5,2%.%Date:~8,2%.zip" "main.exe" "DNF计算器%Date:~5,2%.%Date:~8,2%.exe"
if exist AutoRelese\Rar.exe DEL /Q "main.exe"
if exist AutoRelese\Rar.exe echo [提示]: 打包结束

if exist AutoRelese\release_produce.js echo [提示]: 开始记录更新日志
if exist AutoRelese\release_produce.js node AutoRelese/release_produce.js
::pandoc将md转换为docx
if exist AutoRelese\release_produce.js pandoc -s CHANGELOG.md -o "AutoRelese\publish\更新日志%Date:~5,2%.%Date:~8,2%.docx"
if exist AutoRelese\release_produce.js echo [提示]: 记录结束

if exist AutoRelese\upload_lanzouyun.py echo [提示]: 开始上传到网盘
if exist AutoRelese\upload_lanzouyun.py python AutoRelese/upload_lanzouyun.py
if exist AutoRelese\upload_lanzouyun.py echo [提示]: 上传结束

echo.
echo [提示]: 发布结束,发布包参见AutoRelese\Publish文件夹
echo.


set /p var=任意键继续:
pause