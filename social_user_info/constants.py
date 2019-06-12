# ------------------------------------------ API URLs ------------------------------------------------------------------

GOOGLE_PROFILE_API_URL = 'https://www.googleapis.com/userinfo/v2/me'
FACEBOOK_PROFILE_API_URL = 'https://graph.facebook.com/v3.2/me'
FACEBOOK_PROFILE_PIC_API_URL = 'https://graph.facebook.com/v3.2/me/picture'

# ------------------------------------------ Service Constants ---------------------------------------------------------

AUTHORIZATION_KEY = 'Authorization'
AUTHORIZATION_VALUE = 'Bearer {access_token}'
FACEBOOK_PROFILE_FIELDS = 'email,first_name,last_name'

# ------------------------------------------ Auth Source Constants -----------------------------------------------------

AUTH_SOURCE_GOOGLE = 'google'
AUTH_SOURCE_FACEBOOK = 'facebook'

INVALID_AUTH_SOURCE_ERROR = "{} source is not supported in this service"

# ----------------------------------------------------------------------------------------------------------------------
