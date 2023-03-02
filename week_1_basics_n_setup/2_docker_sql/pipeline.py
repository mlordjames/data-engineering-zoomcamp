import requests
import pandas as pd

headers = {
    'authority': 'api-endpoint.cons-prod-us-central1.kw.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,lb;q=0.8,ar;q=0.7',
    'authorization': '',
    'content-type': 'application/json',
    'origin': 'https://www.kw.com',
    'referer': 'https://www.kw.com/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'x-datadog-origin': 'rum',
    'x-datadog-parent-id': '649127333007336842',
    'x-datadog-sampling-priority': '1',
    'x-datadog-trace-id': '8268107750695424943',
    'x-shared-secret': 'MjFydHQ0dndjM3ZAI0ZHQCQkI0BHIyM=',
}

Final_Result = pd.DataFrame()
d = []
pp = ("UPA-6617836770657718275-9","UPA-6592957343859630085-6","UPA-6587385304577757187-4",
      "UPA-6587384954687057925-9","UPA-6587385375090491398-9","UPA-6587385271729012738-8",
      "UPA-6592971962345472002-8")

for x in pp:
    lat = x
    json_data = {
        'operationName': 'agentProfileQuery',
        'variables': {
            'id': lat,
        },
        'query': 'query agentProfileQuery($id: IDProfileAgentScalar, $personID: Int, $slug: String) {\n  AgentProfileQuery(id: $id, personID: $personID, slug: $slug) {\n    id\n    isAgent\n    isActive\n    name {\n      full\n      initials\n      given\n      __typename\n    }\n    team\n    insights {\n      totalCount\n      __typename\n    }\n    startDate\n    numberOfSales\n    location {\n      address {\n        state\n        city\n        __typename\n      }\n      __typename\n    }\n    bio\n    kwuid\n    neighborhoods {\n      display\n      __typename\n    }\n    languages\n    phone {\n      entries {\n        ... on ContactSetEntryEmail {\n          email\n          __typename\n        }\n        ... on ContactSetEntryMobile {\n          number\n          __typename\n        }\n        ... on ContactSetEntryLandline {\n          number\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    image\n    website\n    brokeragePhone\n    brokerageLicense\n    agentLicenses {\n      licenseNumber\n      state\n      __typename\n    }\n    specialties\n    serviceAreas\n    isAgentLuxuryEnabled\n    designations\n    logo {\n      dba_logo\n      team_logo\n      __typename\n    }\n    marketCenter {\n      market_center_name\n      market_center_address1\n      market_center_address2\n      __typename\n    }\n    social {\n      facebook\n      instagram\n      linkedin\n      twitter\n      youtube\n      __typename\n    }\n    __typename\n  }\n}\n',
    }

    response = requests.post('https://api-endpoint.cons-prod-us-central1.kw.com/graphql', headers=headers, json=json_data)


    jdata = response.json()
    r = jdata["data"]["AgentProfileQuery"]
    code = r["id"]
    name = r["name"]["full"]
    brokerageLicense=r["brokerageLicense"]
    brokeragePhone=r["brokeragePhone"]
    designations=r["designations"]
    isActive=r["isActive"]
    isAgent=r["isAgent"]
    isAgentLuxuryEnabled=r["isAgentLuxuryEnabled"]
    website=r["website"]
    team=r["team"]
    
    
    d.append(
        {
            'name': name,
            'id':code,
            'brokerageLicense':brokerageLicense,
            "brokeragePhone":brokeragePhone,
            "designations":designations,
            "isActive":isActive,
            "isAgent":isAgent,
            "isAgentLuxuryEnabled":isAgentLuxuryEnabled,
            "website":website,
            "team":team
        }
    )
test4 = pd.DataFrame(d)
test4 = test4.drop_duplicates()
Final_Result = Final_Result.append(test4)
print(Final_Result.head(10))
import sys
dated = sys.argv[1]
print(f'Task Sucessful for {dated}')