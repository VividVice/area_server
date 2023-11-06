from flask import Flask, send_from_directory
from modules.config.config import Config
# ... your existing code ...

app = Config().GetApp()

@app.route('/client.apk', methods=['GET'])
def download_apk():
    return send_from_directory('./build', 'w.apk')

