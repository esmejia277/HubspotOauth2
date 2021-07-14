""" Functions to fetch data from HubSpot using an access token """

import requests as req
from app.models import Deal

def fetch_all_deals_and_save(access_token):
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    url = 'https://api.hubapi.com/crm/v3/objects/deals?includeAssociations=true'
    response = req.get(url, headers=headers).json()
    response = response.get('results')
    if response:
        # create a list of Deals objects to save all data in a single time
        for deal in response:
            deal_properties = deal.get('properties')
            Deal(
                deal_id = deal.get('id'),
                name = deal_properties.get('dealname'),
                stage = deal_properties.get('dealstage'),
                close_date = deal_properties.get('closedate'),
                amount = deal_properties.get('amount'),
                deal_type = deal_properties.get('dealtype'),
            ).save()

    return response