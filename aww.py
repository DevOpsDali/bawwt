import json

def post_score(x):
    return x['data']['score']

with open('/tmp/aww.json') as json_file:
    data = json.load(json_file)


img_posts = []
for post in data['data']['children']:
    if not post['data']['is_video']:
        img_posts.append(post)

sorted_posts = {}
sorted_posts['payload'] = sorted(img_posts, key = post_score, reverse = True )[:10]

for post in sorted_posts['payload']:
    print(post['data']['title'])
    print(post['data']['url'])
print('----')
print(json.dumps(sorted_posts))
