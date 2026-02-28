from flask import Flask, request
import os
import smtplib
from email.message import EmailMessage
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def run_topsis():

    if request.method == "GET":
        return """
        <h2>Topsis Web Service</h2>
        <form method="POST" enctype="multipart/form-data">
            File: <input type="file" name="file"><br><br>
            Weights: <input type="text" name="weights"><br><br>
            Impacts: <input type="text" name="impacts"><br><br>
            Email: <input type="text" name="email"><br><br>
            <input type="submit" value="Run Topsis">
        </form>
        """


    file = request.files['file']
    weights = request.form['weights']
    impacts = request.form['impacts']
    email = request.form['email']


    input_name = "input.csv"
    output_name = "result.csv"

    file.save(input_name)

    subprocess.run(["topsis", input_name, weights, impacts, output_name])

    msg = EmailMessage()
    msg['Subject'] = 'Topsis Result'
    msg['From'] = "library.12.manage@gmail.com"
    msg['To'] = email
    msg.set_content("Your Topsis result is attached.")

    with open(output_name,'rb') as f:
        msg.add_attachment(f.read(),maintype='application',subtype='csv',filename=output_name)

    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login("your@gmail.com","yourpassword")
    server.send_message(msg)
    server.quit()

    return "Email Sent Successfully"

if __name__ == "__main__":
    app.run(debug=True)
