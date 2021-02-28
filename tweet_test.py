import tweepy
import print_cedula as ced
import os


consumer_key = os.environ.get('VNG_CONS_KEY')
consumer_secret = os.environ.get('VNG_CONS_SEC')
access_token = os.environ.get('VNG_ACC_TOK')
access_token_secret = os.environ.get('VNG_ACC_TOK_SEC')
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()


def save_image_temp(image_file, message):
    name_of_file = 'temp_img.jpeg'
    image_file.save(name_of_file, "jpeg")
    api.update_with_media(name_of_file, status=message)
    os.remove(name_of_file)


save_image_temp(ced.ced, ced.tweet)
