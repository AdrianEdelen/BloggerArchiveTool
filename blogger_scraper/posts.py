import requests, json

def get_all_posts(blog_id, api_key):
    posts = []
    next_page_token = ''
    url = f'https://www.googleapis.com/blogger/v3/blogs/{blog_id}/posts'
    print(f'-------------------------------------------------------------')
    print(f'Attempting to scrape: {blog_id}')
    while True:
        full_url = f'{url}?key={api_key}&maxResults=100'
        if next_page_token:
            print(f'Next Page Token: {next_page_token}')
            full_url += f'&pageToken={next_page_token}'
        response = requests.get(full_url)
        if response.status_code == 200:
            data = response.json()
            posts.extend(data['items'])
            next_page_token = data.get('nextPageToken', '')
            if not next_page_token:
                print(f'no next page token, finishing up.')
                break
        else:
            print(f'Failed to retrieve posts: {response.status_code}')
            break
    print(f'total posts obtained: {len(posts)}')
    return posts

def save_posts_to_json(posts, filename='data/blog_posts.json'):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(posts, file, ensure_ascii=False, indent=4)