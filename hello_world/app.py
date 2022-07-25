import json
#import calc
import requests


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    import json
    #ignore all below here
    data=[]
    player=[]
    length=0
    print(event['start'])
    start= event['start']
    end = event['end']
    data=importFromURL(data,start,end)

    length = int(data["transaction_all"]["queryResults"]["totalSize"])
    print(length)

    import requests


    i = 0
    while i < length:
        transType = (data["transaction_all"]["queryResults"]["row"][i]["type"])
        if transType == "Recalled" or transType == "Selected":
            data["transaction_all"]["queryResults"]["row"][i]["type_cd"] = 'flag'
        if transType == "Status Change":
            note = data["transaction_all"]["queryResults"]["row"][i]["note"]
            if "selected" in note or "activated" in note:
                data["transaction_all"]["queryResults"]["row"][i]["type_cd"] = 'flag'
                #eventually write these to a db
                player.append(data["transaction_all"]["queryResults"]["row"][i]["note"])
        i += 1

    i = 0
    note=[]
    while i < length:
        flag = data["transaction_all"]["queryResults"]["row"][i]["type_cd"]
        if flag == "flag":
            print(data["transaction_all"]["queryResults"]["row"][i]["note"])
            note.append(data["transaction_all"]["queryResults"]["row"][i]["note"])
    #        print(player[i])
        i += 1
    print(note)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "note": note,
        }),
    }

def importFromURL(data,start,end):
    print("7")
    import requests
    import json
    url = 'http://lookup-service-prod.mlb.com/json/named.transaction_all.bam'
    params = dict(
    sport_code="\'mlb\'",
    start_date=start,
    end_date=end,
    )
    print(url,params)
    resp = requests.get(url=url,params=params)
    data = resp.json() # Check the JSON Response Content documentation below
    return data
