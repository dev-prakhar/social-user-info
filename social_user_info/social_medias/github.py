import requests

from social_user_info import status_codes
from social_user_info.constants import DEFAULT_TIMEOUT, GITHUB_PROFILE_API_URL, AUTHORIZATION_KEY, AUTHORIZATION_VALUE, \
    GITHUB_EMAIL_API_URL
from social_user_info.social_medias.abstract_social_media import AbstractSocialMediaAPI


class GitHubAPI(AbstractSocialMediaAPI):
    """
    This class is used for getting user information from facebook using facebook api and the user's access token
    """
    PROFILE_URL = GITHUB_PROFILE_API_URL
    EMAIL_URL = GITHUB_EMAIL_API_URL

    @staticmethod
    def get_authorization_header(access_token):
        return {AUTHORIZATION_KEY: AUTHORIZATION_VALUE.format(access_token=access_token)}

    @staticmethod
    def get_transformed_keys(response):
        return {
            **response,
            'first_name': response.get('name', '').split(' ')[0],
            'last_name': response.pop('name', '').split(' ')[-1],
            'profile_picture': response.pop('avatar_url', None)
        }

    @classmethod
    def get_user_email(cls, access_token):
        email_api = requests.get(
            url=cls.EMAIL_URL, headers=cls.get_authorization_header(access_token), timeout=DEFAULT_TIMEOUT
        )

        response = {'email': None}
        if email_api.status_code == status_codes.HTTP_OK_REQUEST:
            private_emails = email_api.json()

            response['email'] = private_emails[0]['email']
            for private_email in private_emails:
                if private_email['primary']:
                    response['email'] = private_email['email']

        return response

    @classmethod
    def get_user_info(cls, access_token):
        profile_api = requests.get(
            url=cls.PROFILE_URL, headers=cls.get_authorization_header(access_token), timeout=DEFAULT_TIMEOUT
        )

        if profile_api.status_code == status_codes.HTTP_OK_REQUEST:
            user_info = {
                **cls.get_transformed_keys({**profile_api.json(), **cls.get_user_email(access_token)}),
                **cls.get_response_status(profile_api.status_code)
            }
        else:
            user_info = {
                **profile_api.json(),
                **cls.get_response_status(profile_api.status_code)
            }

        return user_info
