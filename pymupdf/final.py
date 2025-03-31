import fitz  # PyMuPDF
import pymupdf
from googletrans import Translator

translator = Translator()


def extract_font_info_and_images(pdf_path):
    doc = pymupdf.open(pdf_path)
    font_info_list = []
    images_info_list = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
    
        blocks = page.get_text("dict")["blocks"]
        # print(blocks)
        for block in blocks:
            print(type(block))
            print(block.keys())
            try:
                for line in block.get("lines"):
                    for span in line["spans"]:
                        text = span["text"]
                        font = span["font"]
                        size = span["size"]
                        bbox = span["bbox"]
                        font_info_list.append({
                            "page_num": page_num,
                            "text": text,
                            "font": font,
                            "size": size,
                            "bbox": bbox
                        })
            except:
                pass
        image_list = page.get_images(full=True)
        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            images_info_list.append({
                "page_num": page_num,
                "xref": xref,
                "bbox": img[3],
                "image_bytes": image_bytes
            })

    doc.close()
    return font_info_list, images_info_list


def translate_text(text):
    try:
        translated = translator.translate(text, dest='en')
    except Exception as e:
        print(f"Translation error: {e}, text: {text}")
        return text
    return translated.text


def create_translated_pdf(pdf_path, output_path, font_info_list, images_info_list):
    doc = pymupdf.open(pdf_path)
    new_doc = pymupdf.open()  # Create a new PDF


    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        new_page = new_doc.new_page(width=page.rect.width, height=page.rect.height)

        # Add images to the new page
        for img_info in images_info_list:
            if img_info["page_num"] == page_num:
                if isinstance(img_info.get("bbox"),tuple):

                    print(img_info["bbox"])
                    new_page.insert_image(img_info["bbox"], stream=img_info["image_bytes"])
                else:
                    print("error in image info")
        # Add translated text to the new page
        for info in font_info_list:
            if info["page_num"] == page_num:
                translated_text = translate_text(info["text"])
                bbox = fitz.Rect(info["bbox"])

                # Add a semi-transparent rectangle (light blur effect)
                blur_rect = bbox
                # new_page.draw_rect(blur_rect, color=(0.9, 0.9, 0.9), fill=(0.9, 0.9, 0.9), overlay=True)

                # Draw the translated text over the original text
                new_page.insert_text(
                    bbox.bl,  # bottom-left corner of the bounding box
                    translated_text,
                    fontsize=info["size"],
                    color=(0, 0, 0)  # black color
                )

    new_doc.save(output_path)


# Example usage
pdf_path = "invoice_ocr_4.pdf"
output_path = "translated_example1.pdf"

# Step 1: Extract font information and images
font_info, images_info = extract_font_info_and_images(pdf_path)
#
# print(images_info)
# print(font_info)
# Step 2: Create a new PDF with translated text and original images
create_translated_pdf(pdf_path, output_path, font_info, images_info)

print(f"Translated PDF saved as: {output_path}")
