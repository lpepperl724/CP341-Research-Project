#fetches images from the website 
#'thispersondoesnotexist.com'
import requests
from PIL import Image


class ImageFetcher:
    def __init__(self):
        return

    def getImage(self, url, img_saveloc, width, height):     
        img_data = requests.get(url).content
        # save the image
        with open(img_saveloc, 'wb') as handler:
            handler.write(img_data)       
        img = Image.open(img_saveloc)
        img = img.resize((width, height))
        
        return img
