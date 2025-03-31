from PIL import Image

from pytesseract import pytesseract
from pandas import DataFrame

from data_cln import clean_txt
from datetime import datetime

import cv2
from googletrans import Translator



micro = datetime.now().microsecond

pil_img = cv2.imread('./input/I168.png')
data = pytesseract.image_to_data(pil_img, output_type=pytesseract.Output.DICT)

    
df = DataFrame(data)
# l2: block
# l3: paragraph
# l4: line number
# L5: word
translator  = Translator()
print(df.head())
# print(df.columns)
# find missing value

# print(df.info()) # No missing values
# df.dropna(inplace=True)
# print(df.info(),"s") # No missing values

image = pil_img.copy()

headers = ['level','left', 'top', 'width','height','conf','text']
level = "word"

try:
    for l,x,y,w,h,c,txt in df[headers].values:
        if l == 5:      
            try:
                if  txt.isalpha():
                    if txt:= clean_txt(txt):
                        trans = translator.translate(txt).text    
                        cv2.rectangle(image,(x,y), (x+w, y+h), (0,0,255), 2)
                        cv2.putText(image, trans, (x,y), cv2.FONT_HERSHEY_PLAIN,2, (0,255,0),2)
                        
                        print(f"{txt} ==> {trans}")
            except TypeError as te:
                print(te)
except Exception as e:
    print("plot",e)  
        

print("done")
# Create a resizable window
cv2.namedWindow("word bounding box", cv2.WINDOW_NORMAL)

# Manually set the window size (width, height)
cv2.resizeWindow("word bounding box", 800, 800)  # Example: 800x600 window size

# cv2.namedWindow("Fitted Window", cv2.WINDOW_AUTOSIZE)


# cv2.imshow("word bounding box", image)
# cv2.waitKey()
# cv2.destroyAllWindows()
cv2.imwrite(f"images/trans_cleaned_cont_{micro}.png", image)