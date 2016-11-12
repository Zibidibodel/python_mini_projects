from twilio.rest import TwilioRestClient

account_sid = "ACc32c4e36dd6757ca238cf6cd3bc1166e" # Your Account SID from www.twilio.com/console
auth_token  = "682ab72781ab5f3445e7d429e4f41c30"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body="My name is Ron Burgundy?",
    to="+15092805707",    # Replace with your phone number
    from_="+15093090515") # Replace with your Twilio number

print(message.sid)