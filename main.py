import requests
from datetime import datetime, timezone
import smtplib

MY_LAT = # Enter your latitude
MY_LONG = # Enter your longitude
MY_EMAIL = # Enter your email
PASSWORD = # Enter password (SEE README)

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


def send_email():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg="Subject: ISS May Be In Sight\n\nLook up and see if you can spot the ISS!"
    )


def it_is_nighttime():
    if sunrise >= hour_now >= sunset:
        return True


def iss_is_close():
    if abs(abs(iss_latitude) - abs(MY_LAT)) >= 5 and abs(abs(iss_longitude) - abs(MY_LONG)) >= 5:
        return True


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now(timezone.utc)
hour_now = time_now.hour

if iss_is_close() and it_is_nighttime():
    send_email()
