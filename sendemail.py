import smtplib
from_addr = 'anotheremail@gmail.com'
to_addr  = 'someemail@yahoo.com' 

from_name = 'Domonique Barnett'
to_name = 'Alison Thomas'
subject = 'Please remember'
msg= 'I will not be at the last computing seminar so please remember to take (detailed) notes'
message = """From: {} <{}> To: {} <{}> 
Subject: {} 
{} """
message_to_send = message.format(from_name, from_addr, to_name, to_addr, subject, msg)

# Credentials (if needed)
username = 'email'
password = 'password'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message_to_send)
server.quit() 

   