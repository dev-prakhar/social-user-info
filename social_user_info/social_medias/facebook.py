import requests

from social_user_info import status_codes
from social_user_info.constants import DEFAULT_TIMEOUT, FACEBOOK_PROFILE_FIELDS, FACEBOOK_PROFILE_PIC_API_URL, \
    FACEBOOK_PROFILE_API_URL
from social_user_info.social_medias.abstract_social_media import AbstractSocialMediaAPI


class FacebookAPI(AbstractSocialMediaAPI):
    """
    This class is used for getting user information from facebook using facebook api and the user's access token
    """
    PROFILE_URL = FACEBOOK_PROFILE_API_URL
    PROFILE_PIC_URL = FACEBOOK_PROFILE_PIC_API_URL

    @staticmethod
    def get_profile_api_params(access_token):
        return {
            'access_token': access_token,
            'fields': FACEBOOK_PROFILE_FIELDS
        }

    @staticmethod
    def get_profile_pic_api_params(access_token, height=100, width=100):
        return {
            'access_token': access_token,
            'redirect': 'false',
            'height': height,
            'width': width
        }

    @classmethod
    def get_profile_picture_url(cls, access_token):
        profile_pic_api = requests.get(
            url=cls.PROFILE_PIC_URL, params=cls.get_profile_pic_api_params(access_token), timeout=DEFAULT_TIMEOUT
        )

        return {
            **{'profile_picture': profile_pic_api.json().get('data', {}).get('url')},
            **cls.get_response_status(profile_pic_api.status_code)
        }

    @classmethod
    def get_user_info(cls, access_token):
        profile_api = requests.get(
            url=cls.PROFILE_URL, params=cls.get_profile_api_params(access_token), timeout=DEFAULT_TIMEOUT
        )

        if profile_api.status_code == status_codes.HTTP_OK_REQUEST:
            user_info = {
                **profile_api.json(),
                **cls.get_profile_picture_url(access_token)
            }
        else:
            user_info = {
                **profile_api.json(),
                **cls.get_response_status(profile_api.status_code)
            }

        return user_info
