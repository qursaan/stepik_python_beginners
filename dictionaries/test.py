# 1
phones = {'Zoe':'232-43-58', 'Alice':'165-88-56'}
print(phones['Zoe'])
# 232-43-58


# 2
phones['Zoe'] = '658-99-55'
phones['Bill'] = '342-18-25'
print(phones)
# {'Zoe': '658-99-55', 'Alice': '165-88-56', 'Bill': '342-18-25'}


# 3
d = {}
d['key'] = 1
d['Key'] = 2
d['KEY'] = 3
print(d)
# {'key': 1, 'Key': 2, 'KEY': 3}


# 4
if 'Peter' in phones:
    print("We know Peter's phone")
else:
    print("We don't know Peter's phone")
# We don't know Peter's phone


# 5
phones = {'Zoe':'232-43-58', 'Alice':'165-88-56'}
del phones['Zoe']
print(phones)
# {'Alice': '165-88-56'}
