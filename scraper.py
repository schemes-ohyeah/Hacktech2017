import http.client, urllib.request, urllib.parse, urllib.error, base64
# Store keys in a separate file because don't push them to github
import config

def getTagImage(imageURL):
    body = {"url" : imageURL}
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '{}'.format(config.API_VISION),
    }

    params = urllib.parse.urlencode({
        # This API call does not need params
    })

    try:
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/vision/v1.0/tag?%s" % params, "{}".format(body), headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
    except Exception as e:
        data = "HTTPSConnection failed"
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
    return data

def getCelebrity(imageURL):
    body = {"url" : imageURL}
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '{}'.format(config.API_VISION),
    }

    params = urllib.parse.urlencode({

    })

    try:
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/vision/v1.0/models/{model}/analyze?%s" % params, "{}".format(body), headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
    except Exception as e:
        data = "HTTPSConnection failed"
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
    return data

def getOCR(imageURL):
    body = {"url" : imageURL}
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '{}'.format(config.API_VISION),
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'language': 'unk',
        'detectOrientation ': 'true',
    })

    try:
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/vision/v1.0/ocr?%s" % params, "{}".format(body), headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
    except Exception as e:
        data = "HTTPSConnection failed"
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
    return data