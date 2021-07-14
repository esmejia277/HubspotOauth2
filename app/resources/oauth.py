""" Handle Oauth process """

import os
from flask import Blueprint, redirect, request
from app.utils.helper import exchange_for_tokens

bp = Blueprint('oauth', __name__, url_prefix='/oauth')

@bp.route('/install', methods=['GET'])
def oauth_install():
    """ Build URL authentication to install the app """

    auth_url = f'https://app.hubspot.com/oauth/authorize?client_id={os.getenv("CLIENT_ID")}&scope={os.getenv("SCOPE")}&redirect_uri={os.getenv("REDIRECT_URI")}'
    return redirect(auth_url)


@bp.route('/oauth-callback', methods=['GET'])
def oauth_callback():
    """ Receive the authorization code and process it from query parameters """

    code = request.args.get('code')
    if code:
        auth_code_proof = {
            'grant_type': 'authorization_code',
            'client_id': os.getenv("CLIENT_ID"),
            'client_secret': os.getenv('CLIENT_SECRET'),
            'redirect_uri': os.getenv("REDIRECT_URI"),
            'code': code
        }

        # Exchange the authorization code and save the token in mongo
        exchange_for_tokens(
            auth_code_proof=auth_code_proof
        )

        return redirect('/')
    


        


