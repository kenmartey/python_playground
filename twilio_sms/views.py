from django.shortcuts import render
from twilio.rest import Client
from twilio_sms.credentials import *
# Create your views here.


def send_sms(request):
	if request.method == "POST":
		message_body = request.POST.get('message_body')	
		client = Client(account_sid, auth_token)
		message = client.api.account.messages.create(to=my_cell, from_=my_twilio,
										body=message_body)
	# context = {
	# 'message': message
	# }
	return render(request, 'twilio/send_sms.html')