from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Cloud Computing Lab - CI/CD Pipeline - AUTO DEPLOYED!"
    
@app.route("/student")
def student():
    return {
        "name": "Student",
        "course": "Cloud Computing and DevOps",
        "experiment": "CI/CD using Jenkins"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
