""" Helper functions """

import os
import requests as req
from app.models import User
from flask import request

def exchange_for_tokens(auth_code_proof):
    """
    Exchange the authorization code received from Oauth2 server, 
    for an access token

    Returns:
        dict: Tokens

    """
    try:
        response = req.post(
            url='https://api.hubapi.com/oauth/v1/token',
            data=auth_code_proof
        )
        tokens = response.json()
        if tokens:
            # get the session id from flask request object
            # Save tokens in mongo
            User(
                client_id = request.cookies.get('sessionid'), 
                access_token = tokens['access_token'],
                refresh_token = tokens['refresh_token'],
                expires_in = tokens['expires_in']
            ).save()

            return tokens

    except Exception as e:
        print('Error', e)



def refresh_access_token(user_id):
    
    """
    Check if the access token has expired and
    retrieve a new one using the refresh token

    Returns:
        dict: Tokens
    """

    token = User.objects.values().get({'_id': user_id})
    if token:
        refresh_token_proof = {
            'grant_type': 'refresh_token',
            'client_id': os.getenv('CLIENT_ID'),
            'client_secret': os.getenv('CLIENT_SECRET'),
            'redirect_uri': os.getenv('REDIRECT_URI'),
            'refresh_token': token.get('refresh_token')
        }
        return exchange_for_tokens(refresh_token_proof)



def get_access_token(user_id):
    """ Check if the access token has expired and
    retrieve a new one using the refresh token 
    
    Returns:
        dict: Tokens
    """
    
    return refresh_access_token(user_id=user_id)


def is_authorized(user_id: str) -> bool:
    """ Check if the users already have a token
    
    Returns:
        bool: If user it's authorized or not
    """
    try:
        User.objects.values().get({'_id': user_id})
        return True
    except User.DoesNotExist:
        return False
    