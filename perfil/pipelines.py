# from django.core.files.base import ContentFile
from requests import request, ConnectionError
from .models import UserProfile
from django.contrib.auth.models import User


def save_profile_picture(backend, user, response, is_new,  *args, **kwargs):
    '''
    Get the user avatar (and any other details you're interested in)
    and save them to the userprofile
    '''
    if backend.name == 'facebook' and is_new:
        user_model=user
        user_profile=UserProfile()
        user_profile.user=user_model

        if user_profile.photo:
            pass
        else:
            url = 'http://graph.facebook.com/{0}/picture'.format(response['id'])
            try:
                response = request('GET', url, params={'type': 'large'})
                response.raise_for_status()
            except ConnectionError:
                pass
            else:
            	# user_profile.photo.save(u'',
             #                     ContentFile(response.content),
             #                     save=False
             #                     )
				user_profile.photo=url
            	user_profile.save()
