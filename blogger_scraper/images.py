from bs4 import BeautifulSoup
import os, requests, json

def extract_image_urls(post_content):
    soup = BeautifulSoup(post_content, 'html.parser')
    images = soup.find_all('img')
    return [img['src'] for img in images if 'src' in img.attrs]


def download_image(url, folder):
    image_name = os.path.basename(url.split('?')[0])  # results in just the filename of the image
    image_path = os.path.join(folder, image_name)
    if os.path.exists(image_path): 
        print(f"Image {image_path} already exists")
        return None
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(image_path, 'wb') as file:
                file.write(response.content)
            return image_name
        else:
            print(f'Failed to download image: {url}')
        return None
    except:
        print("something went wrong trying to get the image")

def download_images(posts):
    images_info = []
    os.makedirs('images', exist_ok=True)
    print(len(posts))
    postC = 0
    for post in posts:
        post_id = post['id']
        post_url = post['url']
        post_content = post['content']
        image_urls = extract_image_urls(post_content)
        downloaded_images = []
        for img_url in image_urls:
            image_name = download_image(img_url, 'data/images')
            if image_name:
                downloaded_images.append(image_name)
        images_info.append({
            'post_id': post_id,
            'post_url': post_url,
            'images': downloaded_images
        })
        postC += 1
        print(postC)
    return images_info

def save_images_info(images_info, filename='data/images_info.json'):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(images_info, file, ensure_ascii=False, indent=4)