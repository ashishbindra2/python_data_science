import cv2 # pip install opencv-contrib-python


img_path = './BusinessCardData/Selected/052.jpeg'

img_cv = cv2.imread(img_path)

# cv2.imshow("Bysiness Card", img_cv)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# print(type(img_cv)) # <class 'numpy.ndarray'>

# # ### To load the impage from PIL

from PIL import Image # pip install Pillow

img_pl = Image.open(img_path)

# print(type(img_pl)) # <class 'PIL.JpegImagePlugin.JpegImageFile'>

# img_pl.show()

#### Extract the text using pytessreact
# - support both opencv and pill


from pytesseract import image_to_string ## pip install pytesseract
#  using cv2
text_cv = image_to_string(img_cv)

# print(text_cv)

# using pillow

text_pil = image_to_string(image=img_pl)

# print(text_pil)


# IMage to Data
from pytesseract import image_to_data

data = image_to_data(image=img_cv)

# print(data)

# print(data.split('\n'))

data_list = list(map(lambda x : x.split('\t'),data.split('\n')))

# print(data_list)

for dat in data_list:
    print(dat)
# print(data_list[0],"Sd")
# convert into data frame
from pandas import DataFrame

df = DataFrame(data_list[1:], columns=data_list[0])

# print(df)
print(df.head())

# draw the graph on paragraph and word

print(df.info())
# data cleaning
# remove null values
#  data type should be in proper formate

print(df.dropna(inplace=True)) # drop the missing value in rows

col_int = ['level', 'page_num', 'block_num','par_num', 'line_num', 'word_num', 'left', 'top', 'width','height','conf']


print(df.dtypes)
print(df[col_int])

df[col_int] = df[col_int].astype(float, copy=True).astype(int)

print(df.dtypes)


# print column values

image = img_cv.copy()

for l,x,y,w,h,c in df[['level', 'left', 'top', 'width', 'height', 'conf']].values:
    print(l,x,y,w,h,c)
    
# page leve
image = img_cv.copy()

level ='word'

for l, x, y, w, h, c, txt in df[['level', 'left', 'top', 'width', 'height', 'conf','text']].values:
    
    if level == 'page':
        if l == 1:
            cv2.rectangle(img=image, pt1=(x,y),pt2=(x+w,y+h), color=(0,0,0),thickness=2)
        else:
            continue
    elif level == 'block':
        if l == 2:
            cv2.rectangle(img=image, pt1=(x,y),pt2=(x+w,y+h), color=(255,0,0),thickness=2)
        else:
             continue
    elif level == 'para':
        if l == 3:
            cv2.rectangle(img=image, pt1=(x,y),pt2=(x+w,y+h), color=(0,255,0),thickness=2)
        else:
             continue
    elif level == 'line':
        if l == 4:
            cv2.rectangle(img=image, pt1=(x,y),pt2=(x+w,y+h), color=(0,0,255),thickness=2)
        else:
             continue
    elif level == 'word':
        if l == 5:
            cv2.rectangle(img=image, pt1=(x,y),pt2=(x+w,y+h), color=(0,255,255),thickness=2)
            cv2.putText(image,txt,(x,y),cv2.FONT_HERSHEY_PLAIN,1,(255, 0, 0),2)
        else:
             continue

# cv2.imshow("Bounding Box", image)
# cv2.waitKey()
# cv2.destroyAllWindows()

