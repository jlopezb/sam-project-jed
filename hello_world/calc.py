def importFromURL(data):
    print("7")
    import requests
    import json
    url = 'http://lookup-service-prod.mlb.com/json/named.transaction_all.bam'
    params = dict(
    sport_code="\'mlb\'",
    start_date=20220424,
    end_date=20220426,
    )
    print(url,params)
    resp = requests.get(url=url,params=params)
    data = resp.json() # Check the JSON Response Content documentation below
    length=int(data["transaction_all"]["queryResults"]["totalSize"]) # length of array with transactions
    print(length)
    return data