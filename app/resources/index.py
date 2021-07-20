from flask import Blueprint, redirect, request, render_template, url_for
from app.utils.helper import get_access_token, is_authorized
from app.utils.fetch import fetch_all_deals_and_save

bp = Blueprint('/', __name__, url_prefix='/')


@bp.route('/', methods=['GET'])
def index():
    user_id = request.cookies.get('sessionid', '111')
    # Check if the users already have a token
    authorized = is_authorized(user_id = user_id)
    if not authorized:
        # If the user is not authorized, he will be redirected to install the app
        return redirect(url_for('oauth.oauth_install'))
    
    # if user don't have a token, get a new one
    access_token = get_access_token(user_id = user_id)

    # fetch data from HubSpot using the access token
    deals = fetch_all_deals_and_save(access_token= access_token.get('access_token'))

    return render_template('deals.html', deals = deals)


    
