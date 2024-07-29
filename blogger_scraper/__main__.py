import json, dotenv
from os import getenv
import images, posts

if __name__ == '__main__':
    dotenv.load_dotenv()

    BASE_URL = getenv('BASE_URL')
    BLOG_ID= getenv('BLOG_ID')
    API_KEY= getenv('API_KEY')
    IMAGE_BASE_URL = getenv('IMAGE_BASE_URL') 

    posts_data = posts.get_all_posts(BLOG_ID, API_KEY)
    posts.save_posts_to_json(posts=posts_data, filename='data/blog_posts.json')

    with open('data/blog_posts.json', 'r') as f:
        data = json.load(f)

    images_info = images.download_images(data)
    images.save_images_info(images_info=images_info)



