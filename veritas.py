import requests
from datetime import datetime, timezone
from flask import Flask, request
import jwt

app = Flask(__name__)

@app.route("/health")
def health():
    return "Ok"


def verifySlackToken(key):
    try:
        url = "https://slack.com/api/auth.test?token={0}&pretty=1".format(key)
        res = requests.post(url)
        if res.status_code == 200:
            if res.json().get('ok') == True:
                return True
    except Exception as e:
        print("Some error occured while checking the slack token")
        return True
    return False   


def verifySlackWebhook(key):
    try:
        data = {"text":""}
        res = requests.post(key, json=data)
        if res.text == 'missing_text_or_fallback_or_attachments':
            return True
    except Exception as e:
        print("Some error occured while checking the slack webhook")
        return True
    return False


def verifyNPMToken(key):
    try:
        url = "https://registry.npmjs.org/-/whoami"
        headers = {"authorization": "Bearer {0}".format(key)}
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            return True
    except Exception as e:
        print("Some error occured while checking the npm token")
        return True
    return False


def verifyJWTToken(key):
    try:
        payload = jwt.decode(key, algorithms=['none'], options={"verify_signature": False})
        expiration_time = payload.get('exp')
        current_time = datetime.now(timezone.utc).timestamp()
        if expiration_time is not None and current_time > expiration_time:
            return False
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False
    except Exception as e:
        return True
    return False


def verifyGoogle(apikey):
    flag = True
    try:
        url = "https://www.googleapis.com/customsearch/v1?cx=017576662512468239146:omuauf_lfve&q=lectures&key="+apikey
        response = requests.get(url)
        if response.text.find("errors") < 0:
            return flag
        url = "https://maps.googleapis.com/maps/api/staticmap?center=45%2C10&zoom=7&size=400x400&key="+apikey
        response = requests.get(url)
        if response.status_code == 200:
            return flag
        url = "https://maps.googleapis.com/maps/api/streetview?size=400x400&location=40.720032,-73.988354&fov=90&heading=235&pitch=10&key="+apikey
        response = requests.get(url)
        if response.status_code == 200:
            return flag
        url = "https://maps.googleapis.com/maps/api/directions/json?origin=Disneyland&destination=Universal+Studios+Hollywood4&key="+apikey
        response = requests.get(url)
        if response.text.find("error_message") < 0:
            return flag
        url = "https://maps.googleapis.com/maps/api/geocode/json?latlng=40,30&key="+apikey
        response = requests.get(url)
        if response.text.find("error_message") < 0:
            return flag
        url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=40.6655101,-73.89188969999998&destinations=40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.659569%2C-73.933783%7C40.729029%2C-73.851524%7C40.6860072%2C-73.6334271%7C40.598566%2C-73.7527626%7C40.659569%2C-73.933783%7C40.729029%2C-73.851524%7C40.6860072%2C-73.6334271%7C40.598566%2C-73.7527626&key="+apikey
        response = requests.get(url)
        if response.text.find("error_message") < 0:
            return flag
        url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Museum%20of%20Contemporary%20Art%20Australia&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key="+apikey
        response = requests.get(url)
        if response.text.find("error_message") < 0:
            return flag
        url = "https://maps.googleapis.com/maps/api/place/autocomplete/json?input=Bingh&types=%28cities%29&key="+apikey
        response = requests.get(url)
        if response.text.find("error_message") < 0:
            return flag
        url = "https://maps.googleapis.com/maps/api/elevation/json?locations=39.7391536,-104.9847034&key="+apikey
        response = requests.get(url)
        if response.text.find("error_message") < 0:
            return flag
        url = "https://maps.googleapis.com/maps/api/timezone/json?location=39.6034810,-119.6822510&timestamp=1331161200&key="+apikey
        response = requests.get(url)
        if response.text.find("errorMessage") < 0:
            return flag
        url = "https://roads.googleapis.com/v1/nearestRoads?points=60.170880,24.942795|60.170879,24.942796|60.170877,24.942796&key="+apikey
        response = requests.get(url)
        if response.text.find("error") < 0:
            return flag
        url = "https://www.googleapis.com/geolocation/v1/geolocate?key="+apikey
        postdata = {'considerIp': 'true'}
        response = requests.post(url, data=postdata)
        if response.text.find("error") < 0:
            return flag
        url = "https://roads.googleapis.com/v1/snapToRoads?path=-35.27801,149.12958|-35.28032,149.12907&interpolate=true&key="+apikey
        response = requests.get(url)
        if response.text.find("error") < 0:
            return flag
        url = "https://roads.googleapis.com/v1/speedLimits?path=38.75807927603043,-9.03741754643809&key="+apikey
        response = requests.get(url)
        if response.text.find("error") < 0:
            return flag
        url = "https://maps.googleapis.com/maps/api/place/details/json?place_id=ChIJN1t_tDeuEmsRUsoyG83frY4&fields=name,rating,formatted_phone_number&key="+apikey
        response = requests.get(url)
        if response.text.find("error_message") < 0:
            return flag
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=100&types=food&name=harbour&key="+apikey
        response = requests.get(url)
        if response.text.find("error_message") < 0:
            return flag
        url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurants+in+Sydney&key="+apikey
        response = requests.get(url)
        if response.text.find("error_message") < 0:
            return flag
        url = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=CnRtAAAATLZNl354RwP_9UKbQ_5Psy40texXePv4oAlgP4qNEkdIrkyse7rPXYGd9D_Uj1rVsQdWT4oRz4QrYAJNpFX7rzqqMlZw2h2E2y5IKMUZ7ouD_SlcHxYq1yL4KbKUv3qtWgTK0A6QbGh87GB3sscrHRIQiG2RrmU_jF4tENr9wGS_YxoUSSDrYjWmrNfeEHSGSc3FyhNLlBU&key="+apikey
        response = requests.get(url, allow_redirects=False)
        if response.status_code == 302:
            return flag
        url = "https://playablelocations.googleapis.com/v3:samplePlayableLocations?key="+apikey
        postdata = {'area_filter':{'s2_cell_id':7715420662885515264},'criteria':[{'gameObjectType':1,'filter':{'maxLocationCount':4,'includedTypes':['food_and_drink']},'fields_to_return': {'paths': ['name']}},{'gameObjectType':2,'filter':{'maxLocationCount':4},'fields_to_return': {'paths': ['types', 'snapped_point']}}]}
        response = requests.post(url, data=postdata)
        if response.text.find("error") < 0:
            return flag
        url = "https://fcm.googleapis.com/fcm/send"
        postdata = "{'registration_ids':['ABC']}"
        response = requests.post(url, data=postdata, headers={'Content-Type':'application/json','Authorization':'key='+apikey})
        if response.status_code == 200:
            return flag
    except Exception as e:
        print(e)
        return True
    return False


# {"key":"Value", "tag":"tagValue"}
@app.route("/credentialVerifier", methods=['POST'])
def credentialVerifier():
    dataJson = request.get_json()
    tag = dataJson.get('tag')
    key = dataJson.get('key')
    if tag is not None and key is not None and tag.lower() == 'slack_token':
        return {"status": str(verifySlackToken(key))}
    elif tag is not None and key is not None and tag.lower() == 'slack_webhook':
        return {"status": str(verifySlackWebhook(key))}
    elif tag is not None and key is not None and tag.lower() == 'google':
        return {"status": str(verifyGoogle(key))}
    elif tag is not None and key is not None and tag.lower() == 'npm':
        return {"status": str(verifyNPMToken(key))}
    elif tag is not None and key is not None and tag.lower() == 'jwt':
        return {"status": str(verifyJWTToken(key))}
    else:
        return {"status": "unknown"}


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=4444)
