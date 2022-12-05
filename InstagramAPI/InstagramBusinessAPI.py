import requests
import json


class InstagramBusinessAPI:
    """Contains an easy way to create a container and post it to Instagram"""
    def __init__(self, ig_user_id, access_token, APIv="13.0"):
        self.APIv = APIv
        self.ig_user_id = ig_user_id
        self.access_token = access_token

    def ImageContainer(self, image_url, caption):
        """Container for image to post to instagram"""
        ## image_url={image-url} &is_carousel_item={is-carousel-item}&caption={caption}&location_id={location-id}&user_tags={user-tags}&product_tags={product-tags}
        imageContainer = {
            'image_url': image_url,
            'caption': caption,
            'access_token': self.access_token
        }
        return imageContainer

    def VideoContainer(self, video_url, caption):
        """WORK IN PROGRESS; NOT TESTED"""
        ##?media_type=VIDEO&video_url={video-url}&is_carousel_item={is-carousel-item}&caption={caption}&location_id={location-id}&thumb_offset={thumb-offset}&product_tags={product-tags}&access_token={access-token}
        videoContainer = {
            'media_type': "VIDEO",
            'video_url': video_url,
            'caption': caption,
            'access_token': self.access_token
        }
        return videoContainer

    def ReelContainer(self, video_url, caption, share_to_feed):
        """WORK IN PROGRESS; NOT TESTED"""
        ##?media_type=REELS&video_url={reel-url}&caption={caption}&location_id={location-id}&thumb_offset={thumb-offset}&share_to_feed={share-to-feed}&access_token={access-token}
        reelContainer = {
            'media_type': "REELS",
            'video_url': video_url,
            'caption': caption,
            'share_to_feed': share_to_feed,
            'access_token': self.access_token
        }
        return reelContainer

    def post_local_container_to_instagram(self, local_container):
        """Post and Publish container to Instagram"""
        postResult = requests.post('https://graph.facebook.com/v{}/{}/media'.format(self.APIv, self.ig_user_id),
                                   data=local_container)
        result = json.loads(postResult.text)

        if 'id' in result:
            creation_id = result['id']
            second_url = 'https://graph.facebook.com/v{}/{}/media_publish'.format(self.APIv, self.ig_user_id)
            second_payload = {
                'creation_id': creation_id,
                'access_token': self.access_token
            }
            r = requests.post(second_url, data=second_payload)
            print('--------Just posted to instagram--------')
            print(r.text)
        else:
            print('Something went wrong.')
