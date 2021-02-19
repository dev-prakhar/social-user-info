import requests

from social_user_info import status_codes
from social_user_info.constants import GOOGLE_PROFILE_API_URL, AUTHORIZATION_KEY, AUTHORIZATION_VALUE, DEFAULT_TIMEOUT
from social_user_info.social_medias.abstract_social_media import AbstractSocialMediaAPI


class GoogleAPI(AbstractSocialMediaAPI):
    """
    This class is used for getting user information from google using google api and the user's access token
    """
    PROFILE_URL = GOOGLE_PROFILE_API_URL

    @staticmethod
    def get_authorization_header(access_token):
        return {AUTHORIZATION_KEY: AUTHORIZATION_VALUE.format(access_token=access_token)}

    @staticmethod
    def get_transformed_keys(response):
        return {
            **response,
            'first_name': response.pop('given_name', None),
            'last_name': response.pop('family_name', None),
            'profile_picture': response.pop('picture', None)
        }

    @classmethod
    def get_user_info(cls, access_token):
        profile_api = requests.get(
            url=cls.PROFILE_URL, headers=cls.get_authorization_header(access_token), timeout=DEFAULT_TIMEOUT
        )

        if profile_api.status_code == status_codes.HTTP_OK_REQUEST:
            user_info = {
                **cls.get_transformed_keys(profile_api.json()),
                **cls.get_response_status(profile_api.status_code)
            }
        else:
            user_info = {
                **profile_api.json(),
                **cls.get_response_status(profile_api.status_code)
            }

        return user_info
