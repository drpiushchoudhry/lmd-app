# Copyright © 2017–2025 Dr. Piush Choudhry / Layveer Medical Division
# All Rights Reserved

from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

# Simple login page
@app.get("/", response_class=HTMLResponse)
def login_page():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>LMD Login</title>
        <style>
            body {
                font-family: Arial;
                background: #0f172a;
                color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .box {
                background: #1e293b;
                padding: 30px;
                border-radius: 10px;
                text-align: center;
                width: 300px;
            }
            input {
                width: 90%;
                padding: 10px;
                margin: 10px;
                border-radius: 5px;
                border: none;
            }
            button {
                padding: 10px 20px;
                background: #3b82f6;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h2>LMD Secure Login</h2>
            <form action="/login" method="post">
                <input name="username" placeholder="Username" required><br>
                <input name="password" type="password" placeholder="Password" required><br>
                <button type="submit">Login</button>
            </form>
        </div>
    </body>
    </html>
    """

# Login check
@app.post("/login", response_class=HTMLResponse)
def login(username: str = Form(...), password: str = Form(...)):
    if username == "admin" and password == "1234":
        return "<h2 style='color:green;text-align:center'>Login Successful ✅</h2>"
    else:
        return "<h2 style='color:red;text-align:center'>Invalid Credentials ❌</h2>"