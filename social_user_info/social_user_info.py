from social_user_info import constants
from social_user_info import status_codes
from social_user_info.social_medias import GoogleAPI, FacebookAPI, GitHubAPI


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
