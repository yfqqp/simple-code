import requests

user = input(' Enter inst user=  ')

r = requests.get(f'https://api-v2.nextcounts.com/api/instagram/user/{user}').json()
#print(r)

user = r['username']
nic = r['nickname']
id = r['id2']
priv = ['private']
fols= r['followers']
foln = r['following']
post = r['posts']

print(f'''  
Good Vreified Instagram
-------------------------
user - {user}
name = {nic}
ID - {id}
Followers - {fols}
Following - {foln}
post - {post}
-------------------------
inst= @txh6
''')