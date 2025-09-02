response = {
    "response": {
        "header": {
            "resultCode": "00",
            "resultMsg": "NORMAL_SERVICE"
        },
        "body": {
            "dataType": "JSON",
            "items": {
                "item": [
                    {"baseDate": "20250829", "baseTime": "1100", "category": "PTY", "nx": 55, "ny": 127, "obsrValue": "0"},
                    {"baseDate": "20250829", "baseTime": "1100", "category": "REH", "nx": 55, "ny": 127, "obsrValue": "82"},
                    {"baseDate": "20250829", "baseTime": "1100", "category": "RN1", "nx": 55, "ny": 127, "obsrValue": "0"},
                    {"baseDate": "20250829", "baseTime": "1100", "category": "T1H", "nx": 55, "ny": 127, "obsrValue": "29.6"},
                    {"baseDate": "20250829", "baseTime": "1100", "category": "UUU", "nx": 55, "ny": 127, "obsrValue": "1.3"},
                    {"baseDate": "20250829", "baseTime": "1100", "category": "VEC", "nx": 55, "ny": 127, "obsrValue": "205"},
                    {"baseDate": "20250829", "baseTime": "1100", "category": "VVV", "nx": 55, "ny": 127, "obsrValue": "2.8"},
                    {"baseDate": "20250829", "baseTime": "1100", "category": "WSD", "nx": 55, "ny": 127, "obsrValue": "3.1"}
                ]
            },
            "pageNo": 1,
            "numOfRows": 10,
            "totalCount": 8
        }
    }
}


print(type(response))
# print(response['response'])
print(response['response']['body']['items']['item'])
