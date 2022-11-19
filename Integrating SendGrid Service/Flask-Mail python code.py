#As SendGrid is not working we make use of Flask-Mail#

from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app) # instantiate the mail class

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'yourId@gmail.com' #for ex, kganeshkumar011_ec@mepcoeng.ac.in
app.config['MAIL_PASSWORD'] = '*****'            #for ex, password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
	msg = Message(
				'Hello',
				sender ='yourId@gmail.com',              #for ex, kganeshkumar011_ec@mepcoeng.ac.in
				recipients = ['receiver’sid@gmail.com']  #for ex, sample@gmail.com
			)
	msg.body = 'Hello Flask message sent from Flask-Mail'
	mail.send(msg)
	return 'Sent'

if __name__ == '__main__':
	app.run(debug = True)
