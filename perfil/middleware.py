from social.apps.django_app.middleware import SocialAuthExceptionMiddleware
# from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from social import exceptions as social_exceptions

class SocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
	def process_exception(self, request, exception):
		if hasattr(social_exceptions, 'AuthCanceled'):
			return redirect('main:home')
		else:
			raise exception

# class SocialAuthBaseException(SocialAuthBaseException): 
# 	def process_exception(self,request,exception):
# 		if hasattr()