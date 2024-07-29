import requests, json

def get_all_posts(blog_id, api_key):
    posts = []
    next_page_token = ''
    url = f'https://www.googleapis.com/blogger/v3/blogs/{blog_id}/posts'
    while True:
        url = f'{url}?key={api_key}&maxResults=100'
        if next_page_token:
            url += f'&pageToken={next_page_token}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            posts.extend(data['items'])
            next_page_token = data.get('nextPageToken', '')
            if not next_page_token:
                break
        else:
            print(f'Failed to retrieve posts: {response.status_code}')
            break
    return posts

def save_posts_to_json(posts, filename='blog_posts.json'):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(posts, file, ensure_ascii=False, indent=4)