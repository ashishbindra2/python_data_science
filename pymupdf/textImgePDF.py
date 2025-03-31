import pymupdf

greetings = (
    "Hello, World!",  # english
    "Hallo, Welt!",  # german
    "سلام دنیا!",  # persian
    "வணக்கம், உலகம்!",  # tamil
    "สวัสดีชาวโลก!",  # thai
    "Привіт Світ!",  # ucranian
    "שלום עולם!",  # hebrew
    "ওহে বিশ্ব!",  # bengali
    "你好世界！",  # chinese
    "こんにちは世界！",  # japanese
    "안녕하세요, 월드!",  # korean
    "नमस्कार, विश्व !",  # sanskrit
    "हैलो वर्ल्ड!",  # hindi
)
doc = pymupdf.open()
page = doc.new_page()
rect = (50, 50, 200, 500)

# join greetings into one text string
text = " ... ".join([t for t in greetings])

# the output of the above is simple:
page.insert_htmlbox(rect, text)
doc.save(__file__.replace(".py", ".png"))