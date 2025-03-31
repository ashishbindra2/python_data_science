from cv2 import imread
# from cv2 import waitKey
# from cv2 import destroyAllWindows
# from cv2 import imshow
from cv2 import imwrite
from cv2 import rectangle
from cv2 import putText
from cv2 import FONT_HERSHEY_PLAIN
# from cv2 import resize

from pytesseract import image_to_data
from pandas import DataFrame

col_int = ['level', 'page_num', 'block_num','par_num', 'line_num', 'word_num', 'left', 'top', 'width','height','conf']

def image_detect(image_path, output_path, level ='word'):
    inv_img = imread(image_path)
    data = image_to_data(inv_img)
    
    data_list = list(map(lambda x : x.split('\t'),data.split('\n')))

    df = DataFrame(data_list[1:], columns=data_list[0])
    df = df.dropna()
    

    df[col_int] = df[col_int].astype(float, copy=True).astype(int)
    image = inv_img.copy()

    for l, x, y, w, h, c, txt in df[['level', 'left', 'top', 'width', 'height', 'conf','text']].values:
        
        if level == 'page':
            if l == 1:
                rectangle(img=image, pt1=(x,y),pt2=(x+w,y+h), color=(0,0,0),thickness=2)
            else:
                continue
        elif level == 'block':
            if l == 2:
                rectangle(img=image, pt1=(x,y),pt2=(x+w,y+h), color=(255,0,0),thickness=2)
            else:
                continue
        elif level == 'para':
            if l == 3:
                rectangle(img=image, pt1=(x,y),pt2=(x+w,y+h), color=(0,255,0),thickness=2)
            else:
                continue
        elif level == 'line':
            if l == 4:
                rectangle(img=image, pt1=(x,y),pt2=(x+w,y+h), color=(0,0,255),thickness=2)
            else:
                continue
        elif level == 'word':
            if l == 5:
                rectangle(img=image, pt1=(x,y),pt2=(x+w,y+h), color=(0,255,0),thickness=2)
                putText(image,txt,(x,y),FONT_HERSHEY_PLAIN,1,(255, 0, 0),2)
            else:
                continue
    
        # imgg = resize(image, (1000, 1100))
        imwrite(output_path,image)