import requests

from social_user_info import constants
from social_user_info import status_codes


class AbstractSocialMediaAPI:
    class Meta:
        abstract = True

    @staticmethod
    def get_response_status(status_code):
        return {'status': status_code}

    @classmethod
    def get_user_info(cls, access_token):
        raise NotImplementedError('get_user_info() must be implemented')


class GoogleAPI(AbstractSocialMediaAPI):
    """
    This class is used for getting user information from google using google api and the user's access token
    """
    PROFILE_URL = constants.GOOGLE_PROFILE_API_URL

    @staticmethod
    def get_authorization_header(access_token):
        return {constants.AUTHORIZATION_KEY: constants.AUTHORIZATION_VALUE.format(access_token=access_token)}

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
        profile_api = requests.get(url=cls.PROFILE_URL, headers=cls.get_authorization_header(access_token))

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


class FacebookAPI(AbstractSocialMediaAPI):
    """
    This class is used for getting user information from facebook using facebook api and the user's access token
    """
    PROFILE_URL = constants.FACEBOOK_PROFILE_API_URL
    PROFILE_PIC_URL = constants.FACEBOOK_PROFILE_PIC_API_URL

    @staticmethod
    def get_profile_api_params(access_token):
        return {
            'access_token': access_token,
            'fields': constants.FACEBOOK_PROFILE_FIELDS
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
        profile_pic_api = requests.get(url=cls.PROFILE_PIC_URL, params=cls.get_profile_pic_api_params(access_token))
        return {
            **{'profile_picture': profile_pic_api.json().get('data', {}).get('url')},
            **cls.get_response_status(profile_pic_api.status_code)
        }

    @classmethod
    def get_user_info(cls, access_token):
        profile_api = requests.get(url=cls.PROFILE_URL, params=cls.get_profile_api_params(access_token))

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


class GitHubAPI(AbstractSocialMediaAPI):
    """
    This class is used for getting user information from facebook using facebook api and the user's access token
    """
    PROFILE_URL = constants.GITHUB_PROFILE_API_URL

    @staticmethod
    def get_authorization_header(access_token):
        return {constants.AUTHORIZATION_KEY: constants.AUTHORIZATION_VALUE.format(access_token=access_token)}

    @staticmethod
    def get_transformed_keys(response):
        return {
            **response,
            'first_name': response.get('name', '').split(' ')[0],
            'last_name': response.pop('name', '').split(' ')[-1],
            'profile_picture': response.pop('avatar_url', None)
        }

    @classmethod
    def get_user_info(cls, access_token):
        profile_api = requests.get(url=cls.PROFILE_URL, headers=cls.get_authorization_header(access_token))

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


class APIService:
    SOURCE_TO_SOCIAL_API = {
        constants.AUTH_SOURCE_GOOGLE: GoogleAPI,
        constants.AUTH_SOURCE_FACEBOOK: FacebookAPI,
        constants.AUTH_SOURCE_GITHUB: GitHubAPI,
    }

    @classmethod
    def get_user_info(cls, access_token, auth_source):
        """
        Method of a util class that delegates the work for getting user info to the required SocialMedia
        Service based on the incoming auth source
        :param access_token:
        :param auth_source:
        :return: user_info
        """
        user_info = {
            'status': status_codes.HTTP_BAD_REQUEST,
            'error': constants.INVALID_AUTH_SOURCE_ERROR.format(auth_source)
        }

        api_class = cls.get_api(auth_source)
        if api_class:
            user_info = api_class.get_user_info(access_token)
        return user_info

    @classmethod
    def get_api(cls, auth_source):
        """
        Method that returns the social media api class corresponding to source
        :param auth_source:
        :return:
        """
        return cls.SOURCE_TO_SOCIAL_API.get(auth_source)
