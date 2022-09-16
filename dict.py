heros={
    "superHero":"superman",
    "age":21,
    "name":"clark kent"
}

jj=dict([
    ("enemy","lex Luther"),
    ("age",dict([("age1",29),("age2",29),("age3",29)])),
    ("name","kkk")
])
print(jj)
print(len(heros))
print(heros["age"])
heros["power"]="super fast"
print(list(heros.items()))
print(list(heros.keys()))
print(list(heros.values()))
# del heros["age"]
heros.pop("name")
print(heros)
print("superHero" in heros)
for k in heros:
    print(k)

d1={"name":"bread","price":88}

