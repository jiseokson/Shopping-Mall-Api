import os
from datetime import datetime

if not os.path.exists('logs'):
    os.makedirs('logs/')
    os.makedirs('logs/gunicorn/')

workers = 3
bind = 'unix:/run/gunicorn.sock'
accesslog = f"./logs/gunicorn/log_{datetime.now().strftime('%Y-%m-%d')}.log"
errorlog = f"./logs/gunicorn/log_{datetime.now().strftime('%Y-%m-%d')}.log"
