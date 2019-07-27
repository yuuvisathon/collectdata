"""
push the data to yuuvis
"""
import requests
import json
import os


BASE_META = {
    "objects": [{
        "properties": {
            "enaio:objectTypeId": {
                "value": "lucent"
            },
            "machineid": {
                "value": ""
            },
            "datatype": {
                "value": ""
            }
        },
        "contentStreams": [{
            "cid": "cid_63apple"
        }]
    }]
}


def push_file(data, machine_id, which_type):
    headerDict = {}
    paramDict = {}
    baseUrl = 'https' + '://' + 'api.yuuvis.io'

    headerDict['Ocp-Apim-Subscription-Key'] = os.environ['YUUVIS']
    session = requests.Session()
    multipart_form_data = {
        'data': ('metadata.json', json.dumps(BASE_META), 'application/json'),
        'cid_63apple': ('data.txt', data, 'text/plain')
    }

    response = session.post(str(baseUrl+'/dms/objects'), files=multipart_form_data, headers=headerDict)
    return response.json()

    
