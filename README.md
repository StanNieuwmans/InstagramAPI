# InstagramAPI
Package for the Instagram Business API - Python


# InstagramAPI - Python Package
A small demo library for a Medium publication about publishing libraries.

### Installation
```
pip install python-InstagramBusinessAPI
```

### Get started
How to post an image to Instagram with this package.

```Python
from InstagramAPI.InstagramBusinessAPI import InstagramBusinessAPI

instagram_api = InstagramBusinessAPI(ig_user_id=IG_USER_ID, access_token=ACCESS_TOKEN)
img_container = instagram_api.ImageContainer("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F441563938470171685%2F&psig=AOvVaw1-BpG1NgnVMHPDpdeV6Ute&ust=1670330141317000&source=images&cd=vfe&ved=0CA8QjRxqFwoTCMDF_eW-4vsCFQAAAAAdAAAAABAE", "Test Image")
instagram_api.post_local_container_to_instagram(img_container)
```


# Thanks to
Skolo Online Learning for this amazing [article](https://levelup.gitconnected.com/automating-instagram-posts-with-python-and-instagram-graph-api-374f084b9f2b).