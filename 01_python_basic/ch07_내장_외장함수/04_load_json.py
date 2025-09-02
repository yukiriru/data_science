import json

# JSON 파일 → dict 로드
with open("person.json", "r", encoding="utf-8") as f:
    loaded_person = json.load(f)

print("JSON 파일에서 로드한 dict 데이터:", loaded_person)

# 데이터 타입과 키 확인
print("데이터 타입:", type(loaded_person))
print("이름:", loaded_person["name"])
print("나이:", loaded_person["age"])
print("보유 기술:", ", ".join(loaded_person["skills"]))
print("활성 여부:", loaded_person["is_active"])
