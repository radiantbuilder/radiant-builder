from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch VM status
    vm_status = os.popen("gcloud compute instances list --format='table(name,status)'").read()
    
    # Read the latest logs
    with open("/home/affiliatework2016/cloud_control.log", "r") as file:
        logs = file.readlines()[-10:]  # Get the last 10 lines

    return render_template('index.html', vm_status=vm_status, logs=logs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
