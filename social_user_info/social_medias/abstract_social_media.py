class AbstractSocialMediaAPI:
    class Meta:
        abstract = True

    @staticmethod
    def get_response_status(status_code):
        return {'status': status_code}

    @classmethod
    def get_user_info(cls, access_token):
        raise NotImplementedError('get_user_info() must be implemented')
