# Tạo folder & git init
mkdir discord-bypass-bot
cd discord-bypass-bot
git init

# Copy bot.py + requirements.txt vào folder

# .gitignore
echo ".env" >> .gitignore
echo "venv/" >> .gitignore
echo "__pycache__/" >> .gitignore

# Commit & push lên GitHub
git add .
git commit -m "initial discord bot"
git branch -M main
git remote add origin https://github.com/USERNAME/discord-bypass-bot.git
git push -u origin main
