import subprocess

subprocess.run(['pyinstaller', '--onefile', '--windowed', 'UI.py'])
#pyinstaller --onefile --windowed --add-data "github_logo.png;." UI.py
# pyinstaller --onefile --windowed --add-data="img/github_logo.png;img" UI.py
