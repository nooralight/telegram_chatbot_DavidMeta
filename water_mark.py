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
        font = ImageFont.truetype('dejavu/GothamBold.ttf', 15)
        text_size = draw.textsize(text,font=font)
        #Positioning Text
        x=6
        y=6
        # Add a shadow border to the text
        for offset in range(1, 2):
            draw.text((x - offset, y), text, font=font, fill=(88, 88, 88))
            draw.text((x + offset, y), text, font=font, fill=(88, 88, 88))
            draw.text((x, y + offset), text, font=font, fill=(88, 88, 88))
            draw.text((x, y - offset), text, font=font, fill=(88, 88, 88))
        #Applying text on image via draw object
        draw.text((x, y), text, font=font,fill=(255,255,255))
        #Saving the new image
        img.save("result.png")
