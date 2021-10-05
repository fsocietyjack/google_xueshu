import requests

url = "https://shimo.im/lizard-api/files/PhYRqqPYh3Qj3Yht/compose"

headers = {
    'content-type': 'application/json;charset=UTF-8',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'cookie': 'shimo_sid=s%3Ac965e9d9e4ec410986695a8eec1ee0a0.hoj8Z6qj7ue6QDAppjzf2SW6DLO0xJBWT7lWo0Bx4vg; deviceId=browser-def40d94-dcda-c356-eb63-046867048cca; sajssdk_2015_cross_new_user=1; sensorsdata2015session=%7B%7D; Hm_lvt_aa63454d48fc9cc8b5bc33dbd7f35f69=1630066363; udid=f01e4835ed011d06ba3eJuK53G8jXGWWtb; deviceId=svc-d69ff08b-ff43-4c74-bd8e-c00a16c65392; _bl_uid=bkkIesmFu9Fbe5fqqbbCukp1OC2s; _csrf=vroyjteyuIXdtqV_8ttZ13bh; shimo_gatedlaunch=6; shimo_kong=4; shimo_svc_edit=6132; sdk_v2_comment=266; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2271250793%22%2C%22%24device_id%22%3A%2217b8786c9a65f3-05955716537e4d-3c700c58-1fa400-17b8786c9a77b9%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2217b8786c9a65f3-05955716537e4d-3c700c58-1fa400-17b8786c9a77b9%22%7D; Hm_lpvt_aa63454d48fc9cc8b5bc33dbd7f35f69=1630068811; acw_tc=2760778d16301457638531837eb14389c6132ad4c5ffc5d725f10c0a8c8f03',
}

json_data = {
    "changeset": "7x:7v@7p@T0$7j:3@9#7d@79@D1f:3@4#19@1#7 0 1 10 11 12 13 14 15 16 2 3 4 5 6 7 8 9[\"g\",\"$blinkTooltip\",\"$fbackgroundImage\",\"$lbackgroundImageLayout\",\"$jbackgroundImageSize\",\"i\",\"$6csExpr\",\"$4icon\",\"a\",\"d\",\"2*14\",\"$bfont-family:\",\"J\",\"$9cellValue:dwa\",\"$6userId\",\"E\",\"$8authorId*71250793\"] 0[\"G:MODOC\"]",
    "clientId": "beebdd07-759f-480a-9e32-0c35796b5628", "rev": 71, "uuid": "46ba80b72b1a494f84a1de7002b86a3c"}
res = requests.post(url=url, headers=headers, json=json_data)

print(res.text)
