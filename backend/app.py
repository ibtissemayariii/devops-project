print("Hello DevOps World! 🚀")

# your app code here, e.g., Flask
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Backend is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

