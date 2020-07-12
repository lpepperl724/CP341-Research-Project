#fetches images from the website 
#'thispersondoesnotexist.com'

def getImage():    
    
    image_url = 'http://thispersondoesnotexist.com/image'
    
    img_data = requests.get(image_url).content
    
    # save the image
    with open('static/img/profile_image.jpg', 'wb') as handler:
        handler.write(img_data)
        
    # get and resize the image
    my_image = io.imread('static/img/profile_image.jpg')
    my_image = resize(my_image, (220, 220))
    
    # resave the image
    io.imsave('static/img/image_resized.jpg', my_image)
