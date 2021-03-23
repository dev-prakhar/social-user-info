import requests

from social_user_info.constants import MICROSOFT_API_URL, AUTHORIZATION_KEY, AUTHORIZATION_VALUE, DEFAULT_TIMEOUT
from social_user_info.social_medias.abstract_social_media import AbstractSocialMediaAPI


class MicrosoftAPI(AbstractSocialMediaAPI):
    """
        This class is used for getting user information from microsoft using microsoft api and the user's access token
    """
    PROFILE_URL = MICROSOFT_API_URL

    @staticmethod
    def get_authorization_header(access_token):
        return {AUTHORIZATION_KEY: AUTHORIZATION_VALUE.format(access_token=access_token)}

    @staticmethod
    def get_profile_picture():
        # In version 1.0 of microsoft, profile picture is not supported
        return {'profile_picture': None}

    @classmethod
    def get_transformed_keys(cls, profile_info):
        return {
            **profile_info,
            'first_name': profile_info.pop('givenName', None),
            'last_name': profile_info.pop('surname', None),
            'email': profile_info.pop('userPrincipalName', None),
            **cls.get_profile_picture()
        }

    @classmethod
    def get_user_info(cls, access_token):
        profile_api = requests.get(
            url=cls.PROFILE_URL, headers=cls.get_authorization_header(access_token), timeout=DEFAULT_TIMEOUT
        )

        if profile_api:
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
