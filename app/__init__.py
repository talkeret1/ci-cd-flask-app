from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

def get_version():
    """
    Returns app version in the following priority:
    1. Git tag if available (production / CI)
    2. First line of README.md (fallback / dev)
    """
    # 1. Git tag
    try:
        tag = subprocess.check_output(
            ["git", "describe", "--tags", "--abbrev=0"],
            stderr=subprocess.STDOUT
        ).decode("utf-8").strip()
        if tag.startswith("v"):
            return tag
    # except subprocess.CalledProcessError:
    #     pass
    # except FileNotFoundError:
    #     pass

    # # 2. Fallback: read README.md first line
    # try:
    #     with open("README.md", "r") as f:
    #         line = f.readline()
    #         for part in line.split():
    #             if part.startswith("v"):
    #                 return part
     except FileNotFoundError:
        return "unknown"

    return "unknown"

@app.route("/")
def home():
    version = get_version()
    return f"""
    <html>
      <head>
        <title>Welcome to CI/CD Flask App</title>
        <!-- jQuery first -->
        <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
        <!-- Notify.js -->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/notify/0.4.2/notify.min.js"></script>
      </head>
      <body>
        <h1>CI/CD Flask App</h1>
        <p>Version: {version}</p>

        <script>
          $(function() {{
            $.notify("App is running! Version: {version}", "success");
          }});
        </script>
      </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200