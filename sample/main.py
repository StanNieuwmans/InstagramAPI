from InstagramAPI.InstagramBusinessAPI import InstagramBusinessAPI
from dotenv import load_dotenv
import os

if __name__ == '__main__':
    load_dotenv()
    IG_USER_ID = os.getenv('IG_USER_ID')
    ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')

    insta = InstagramBusinessAPI(ig_user_id=IG_USER_ID, access_token=ACCESS_TOKEN)
    img_container = insta.ImageContainer("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F441563938470171685%2F&psig=AOvVaw1-BpG1NgnVMHPDpdeV6Ute&ust=1670330141317000&source=images&cd=vfe&ved=0CA8QjRxqFwoTCMDF_eW-4vsCFQAAAAAdAAAAABAE", "Test Image")
    insta.post_local_container_to_instagram(img_container)

