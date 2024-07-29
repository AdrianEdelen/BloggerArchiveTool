from bs4 import BeautifulSoup
import json

def replace_image_urls_in_content(post_content, image_replacements):
    soup = BeautifulSoup(post_content, 'html.parser')
    images = soup.find_all('img')
    for img in images:
        img_url = img['src']
        for original_url, new_image_name in image_replacements:
            if img_url == original_url:
                img['src'] = os.path.join(IMAGE_BASE_URL, new_image_name)
    return str(soup)

def update_post_content(posts, images_info):
    updated_posts = []
    for post in posts:
        post_id = post['id']
        post_content = post['content']
        for info in images_info:
            if info['post_id'] == post_id:
                post['content'] = replace_image_urls_in_content(post_content, info['images'])
        updated_posts.append(post)
    return updated_posts

def save_updated_posts(posts, filename='updated_posts.json'):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(posts, file, ensure_ascii=False, indent=4)