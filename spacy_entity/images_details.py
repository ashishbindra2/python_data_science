import cv2
import os
import warnings

from pandas import DataFrame
from pandas import concat

from glob import glob
from tqdm import tqdm

from pathlib import Path
from pytesseract import image_to_data


img_paths = glob('./BusinessCardData/Selected/*.jpeg')
all_busness_card = DataFrame(columns=['id', 'text'])
# print(img_path)
# for img in img_path:
#     print(Path(img).stem)

for img_path in tqdm(img_paths, desc="Business Cards" ):
    
    # print(os.path.splitext('//'))
    # print( os.path.split(img_path))
    _, file_name = os.path.split(img_path)
    
    # Extract data and text
    image = cv2.imread(img_path)
    data = image_to_data(image)
    
    data_list = list(map(lambda x: x.split('\t'), data.split('\n')))
    
    # print(data_list)
    df = DataFrame(data=data_list[1:], columns=data_list[0])
    df.dropna(inplace=True)
    df['conf'] = df['conf'].astype(float).astype(int)
    
    usefull_data = df.query('conf >= 30')
    
    # print(usefull_data)
    # DataFram
    business_card = DataFrame()
    business_card['text'] = usefull_data['text']
    business_card['id'] = file_name
    
    # print(business_card)
    
    # Concate
    all_busness_card = concat((all_busness_card, business_card))

print(all_busness_card)

all_busness_card.to_csv("business_cards.csv")