import requests

import settings

base_url = 'https://api.mapbox.com'
token_part = '?access_token={}'.format(settings.MAPBOX_TOKEN)
credentials_url = '{}/uploads/v1/{}/credentials{}'.format(
    base_url,
    settings.MAPBOX_USERNAME,
    token_part
    )

a = requests.post(credentials_url)

# it's incomplete
