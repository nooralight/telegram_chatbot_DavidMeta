from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

class Water_Mark:
    def __init__(self,url):
        self.url = url
    
    def get_result(self):
        
        response = requests.get(self.url)
        img = Image.open(BytesIO(response.content)) 
        #Creating draw object
        draw = ImageDraw.Draw(img) 

        #Creating text and font object
        text = "GenAiToken.com"
        font = ImageFont.truetype('arial.ttf', 20)

        #Positioning Text
        
        x=0
        y=0

        #Applying text on image via draw object
        draw.text((x, y), text, font=font) 

        #Saving the new image
        img.save("result.png")
