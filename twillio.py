from twilio.rest import Client

threshold = 0.01
account_sid = 'ACb7fbf2db900d9b942e6e0a44386f3438'
auth_token = '8944858c7672456fe0d84e8e4b88510e'
client = Client(account_sid, auth_token)

def sendMsg(msg):
	message = client.messages \
					.create(
						body=msg,
						from_='19386665757',
						to='18016967027'
						)
	print(message.sid)

def sendi(r, n): #r is rotten apples, n is total apples
	if ((r/n) > threshold):
		sendMsg("WARNING: In the latest batch there was a percentage of " + (r/n) + " rotten apples.")
		