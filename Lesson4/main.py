s = "Hello my dear Friend.Hi my name is Yerassyl.Are you?"
w = s.split(" ")
key="my"
key_count=0
for i in w:
    if i == key:
        key_count = key_count + 1
print(key_count)
        
