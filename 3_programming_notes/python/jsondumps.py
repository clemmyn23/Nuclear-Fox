import json

with open("lsr_template.json") as f:
    js = json.load(f)

j1 = json.dumps(js)
j2 = json.dumps(js, separators=(',',':') )

print(id(j2))
print(js['id'])
print(j2)
print(len(j2))
