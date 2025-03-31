import fitz  # PyMuPDF
from googletrans import Translator
from io import BytesIO

def translate_text(text, src_lang='auto', dest_lang='en'):
    translator = Translator()
    return translator.translate(text, src=src_lang, dest=dest_lang).text

def translate_pdf(input_path, output_path, src_lang='auto', dest_lang='en'):
    # Open the input PDF
    document = fitz.open(input_path)
    output_document = fitz.open()

    # Iterate through each page
    for page_num in range(document.page_count):
        page = document.load_page(page_num)
        text_blocks = page.get_text("blocks")

        # Create a new page in the output document with the same dimensions
        output_page = output_document.new_page(width=page.rect.width, height=page.rect.height)
        img_list = page.get_images(full=True)
        
        # Copy images to the new page
        for img_index in range(len(img_list)):
            try:
                img = img_list[img_index]
                xref = img[0]
                base_image = document.extract_image(xref)
                image_bytes = base_image["image"]

                img_stream = BytesIO(image_bytes)
                pix = fitz.Pixmap(fitz.open("png", img_stream))

                # Get the position and dimensions of the image on the page
                bbox = page.get_image_bbox(img_index)
                if bbox:
                    output_page.insert_image(bbox, pixmap=pix)
            except Exception as e:
                print(f"Error processing image on page {page_num + 1}, image {img_index}: {e}")

        # Copy text blocks to the new page with translation
        for block in text_blocks:
            x0, y0, x1, y1, text, block_no, block_type, *_ = block
            if block_type == 0:  # Only translate text blocks
                try:
                    translated_text = translate_text(text, src_lang, dest_lang)
                    output_page.insert_text((x0, y0), translated_text, fontsize=12, color=(0, 0, 0))
                except Exception as e:
                    print(f"Error translating text on page {page_num + 1}, block {block_no}: {e}")
            else:
                output_page.insert_text((x0, y0), text, fontsize=12, color=(0, 0, 0))

    # Save the output PDF
    output_document.save(output_path)
    output_document.close()

# Example usage
# translate_pdf("input.pdf", "output_translated.pdf", src_lang='auto', dest_lang='en')

# Example usage
translate_pdf("Holidays.pdf", "opt2.pdf", src_lang='auto', dest_lang='en')

