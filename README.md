# Social User Info
A python package that helps getting the user info from social apps

## Installation
```
Required Python Version >= 3
```
```
pip install social-user-info
```


## Supported Social Media

* Google
* Facebook

## How it works?

The package has a method `APIService.get_user_info(access_token, auth_source)`.
This method accepts the access_token and auth_source(`google`, `facebook`) and returns the user info corresponding to the given access token

## Testing

#### Get your google access token:
* Navigate to: https://developers.google.com/oauthplayground/
* In Step 1, select **Google OAuth2 API v2** and add `https://www.googleapis.com/auth/userinfo.email` and `https://www.googleapis.com/auth/userinfo.profile`. Click on Authorize APIs
* Login/Select the account you want the access token of
* In Step 2, Click on **Exchange Authorization Code for Tokens**
* Get the `access_token` from the returned JSON

#### Get you facebook access token
* Read through this: https://developers.facebook.com/docs/facebook-login/access-tokens/

#### Obtain user info
```python
from social_user_info.social_user_info import APIService

APIService.get_user_info(access_token={access_token_from_above_step}, auth_source='google')
APIService.get_user_info(access_token={access_token_obtained_from_facebook}, auth_source='facebook')
```
