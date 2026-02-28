# Mashup Assignment (UCS654)

This project is made as part of **UCS654** assignment.
Goal of this project is to create a mashup generator using python. It has two parts — one command line program and one small web app using Flask.

---

## 📌 What this project does

Basically user gives:

* Singer Name
* Number of videos
* Duration (seconds)
* Email Id (for web version)

Program will:

1. Download videos from Youtube
2. Convert videos into audio files
3. Cut first *Y seconds* from each audio
4. Merge all parts into one mashup file
5. (Web version) send result as zip through email

---

## 🧱 Project Structure

```
Program1/
   102317042.py
   mashup.py

Program2/
   app.py
   mashup.py
   templates/
```

Program1 is command line based.
Program2 is Flask web service.

---

## ▶️ How to Run Program 1

Open terminal inside Program1 folder:

```
python 102317042.py "Singer Name" 20 25 output.mp3
```

Example:

```
python 102317042.py "Sharry Maan" 20 25 mashup.mp3
```

---

## 🌐 How to Run Program 2

Go to Program2 folder and run:

```
python app.py
```

Then open browser:

```
http://127.0.0.1:5000
```

Fill form and submit.

---

## ⚙️ Libraries Used

* Flask
* yt-dlp
* moviepy
* pydub
* flask-mail
* python-dotenv

FFmpeg is also required for audio merging.

---

## 🔐 Note About Email

Email credentials are not hardcoded in project.
They are loaded using `.env` file for safety.

---

## 💭 My Learning

While doing this assignment I learned:

* how to work with APIs and external libraries
* basic flask routing
* handling files and folders in python
* little bit about git and branches also 😅

---

Project is simple but it helped me understand how backend services work together.

Thanks 👍
