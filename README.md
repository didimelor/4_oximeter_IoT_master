# Pulsimeter_IoT
This pulsimeter takes the heart rate through an Arduino sensor and stores that data into an sql database, it uses the user's phone number as a primery key to store separately each user's data. The pulsimeter uses Twilio api to send information to the user, with any message that Twilio recieves, it sends the user a tutorial on how to use the sensor, then if the user messages Twillio "Heart rate", Twillio will return a chart with all the historic heart rates registered of the user for the sql data base.

Video: https://youtu.be/eVLHqwVu1gQ
