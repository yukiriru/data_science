response = {
	"response":{
		"header":{"resultCode":"0000","resultMsg":"OK"},
		"body":{
			"items":{
				"item":{
					"ed":"국민해외관광객",
					"edCd":"D",
					"natCd":100,
					"natKorNm":"한  국",
					"num":1683022,
					"rnum":1,
					"ym":202305
				}
			},
			"numOfRows":10,
			"pageNo":1,
			"totalCount":1
		}
	}
}
print(type(response))
# print(response['response'])
print(response['response']['body']['items']['item'])
