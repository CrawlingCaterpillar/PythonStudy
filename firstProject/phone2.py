from twilio.rest import TwilioRestClient


account_sid = "ACa9b16c3bb61de2ed3a9ef78261120b62"
auth_token = "879a480e41672b5f6f811c535e5bf369"

client = TwilioRestClient(account_sid, auth_token)

message = client.message.create(
    to="+8618101519736",
    from_="+12706813036",
    body="Hello!!!!")

print(message.sid)
