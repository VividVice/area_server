from flask import Flask, send_from_directory
from modules.config.config import Config
import os
from flask import current_app
# ... your existing code ...

app = Config().GetApp()

@app.route('/client.apk', methods=['GET'])
def download_apk():
    uploads = os.path.join(current_app.root_path, 'build')
    print(uploads)
    return send_from_directory(uploads, 'client.apk')

