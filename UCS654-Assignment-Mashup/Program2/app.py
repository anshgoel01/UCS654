from dotenv import load_dotenv
load_dotenv("../.env")
from flask import Flask, request, render_template
import zipfile
import os
from Program1.mashup import download_videos, convert_to_audio, cut_and_merge
from flask_mail import Mail, Message


app = Flask(__name__)

#email 
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD")

mail = Mail(app)


#home page
@app.route("/")
def home():
    return render_template("index.html")


#form submit route
@app.route("/create", methods=["POST"])
def create():

    try:
        singer = request.form["singer"]
        number = int(request.form["number"])
        duration = int(request.form["duration"])
        email = request.form["email"]

        #input check
        if number <= 10 or duration <= 20:
            return "Number must be >10 and Duration must be >20"

        output_file = "output/mashup.mp3"

        #creating folders(if it does not exists)
        os.makedirs("output", exist_ok=True)

        #mashup
        download_videos(singer, number)
        convert_to_audio()
        cut_and_merge(duration, output_file)
        
        #create zip file
        zip_name = "output/result.zip"
        with zipfile.ZipFile(zip_name, 'w') as z:
            z.write(output_file)

        #send email
        msg = Message(
            "Your Mashup File",
            sender=os.getenv("MAIL_USERNAME"),
            recipients=[email]
        )

        with app.open_resource(zip_name) as fp:
            msg.attach("result.zip", "application/zip", fp.read())

        mail.send(msg)

        return "Mashup created and sent to your email!"

    except Exception as e:
        return f"Error occurred: {str(e)}"


#run app
if __name__ == "__main__":
    app.run(debug=True)


