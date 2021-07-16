import json

json_str = """{
   "이름": "홍길동", 
   "나이": 25, 
   "문장": "첫 줄 문장 \\n 두 번째 문장" 
}
"""

jdata_obj = json.loads(json_str)
print (type(jdata_obj))
print (jdata_obj)


# jdata_obj = json.loads(json_str, strict=False)
# print (type(jdata_obj))
# print (jdata_obj)
