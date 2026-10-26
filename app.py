from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>CI/CD Pipeline Working! 🚀</h1><p>Deployed via Jenkins + Docker + K8s</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
