import smtplib
import email.message
import os
import dotenv
dotenv.load_dotenv()
import logging

def send_email(token, email_receiver):
    body = (
        """
    <head>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
                display: flex;
                align-items: center;
                justify-content: center;
                height: 100vh;
            }

            .confirmation-container {
                text-align: center;
                background-color: #fff;
                border-radius: 8px;
                padding: 20px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }

            h1 {
                color: #333;
            }

            p {
                color: #666;
                margin-bottom: 20px;
            }

            .confirmation-button {
                display: inline-block;
                padding: 10px 20px;
                background-color: #4CAF50;
                color: #fafafa;
                text-decoration: none;
                border-radius: 5px;
                transition: background-color 0.3s;
                border: none;
            }

            .confirmation-button:hover {
                background-color: #45a049;
                cursor: pointer;
            }
        </style>
    </head>
    <body>

        <div class="confirmation-container">
            <h1>Confirmação de Email</h1>
            <p>Seu email foi registrado com sucesso e sua conta no todo app. Por favor, clique no botão abaixo para confirmar seu email e liberar seu acesso:</p>
            <a href="https://www.example.com/confirm/""" 
    + token +
    """ 
        " class="confirmation-button">Confirmar Email</a>
    </body>
    """
    )

    msg = email.message.Message()
    msg["Subject"] = "Confirmação de email ToDo App"
    msg["From"] = os.getenv("EMAIL")
    msg["To"] = email_receiver
    password = os.getenv("EMAIL_PASSWORD")
    msg.add_header("Content-Type", "text/html")
    msg.set_payload(body)

    try:
        s = smtplib.SMTP("smtp.gmail.com:587")
        s.starttls()
        s.login(msg["From"], password)
        s.sendmail(msg["From"], [msg["To"]], msg.as_string().encode("utf-8"))
    except Exception as error:
        logging.error(error.args)
        print(error)