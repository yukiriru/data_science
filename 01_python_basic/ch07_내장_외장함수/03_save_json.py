import json

# 저장할 dict 데이터
person_info = {
    "name": "홍길동",
    "age": 30,
    "skills": ["Python", "JavaScript", "SQL"],
    "is_active": True
}

# dict → JSON 파일 저장
with open("person.json", "w", encoding="utf-8") as f:
    json.dump(person_info, f, indent=4, ensure_ascii=False)

print("dict 데이터를 person.json 파일로 저장했습니다.")
