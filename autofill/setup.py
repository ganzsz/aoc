with open('./session.cookie', 'w+') as f:
    f.write('Cookie goes here')
    f.close()

print("Created session.cookie file")