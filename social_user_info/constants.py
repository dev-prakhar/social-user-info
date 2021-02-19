# ------------------------------------------ API URLs ------------------------------------------------------------------

GOOGLE_PROFILE_API_URL = 'https://www.googleapis.com/userinfo/v2/me'
FACEBOOK_PROFILE_API_URL = 'https://graph.facebook.com/v3.2/me'
FACEBOOK_PROFILE_PIC_API_URL = 'https://graph.facebook.com/v3.2/me/picture'
GITHUB_PROFILE_API_URL = 'https://api.github.com/user'
GITHUB_EMAIL_API_URL = 'https://api.github.com/user/emails'

# ------------------------------------------ Service Constants ---------------------------------------------------------

AUTHORIZATION_KEY = 'Authorization'
AUTHORIZATION_VALUE = 'Bearer {access_token}'
FACEBOOK_PROFILE_FIELDS = 'email,first_name,last_name'

DEFAULT_TIMEOUT = 5 # 5 Seconds

# ------------------------------------------ Auth Source Constants -----------------------------------------------------

AUTH_SOURCE_GOOGLE = 'google'
AUTH_SOURCE_FACEBOOK = 'facebook'
AUTH_SOURCE_GITHUB = 'github'

INVALID_AUTH_SOURCE_ERROR = "{} source is not supported in this service"

# ----------------------------------------------------------------------------------------------------------------------
