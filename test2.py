import pdfplumber
from googletrans import Translator  # You might need to install `googletrans`

def translate_pdf(input_pdf, output_docx, target_lang="en"):
  """
  Extracts text from a PDF, translates it, and saves to a DOCX file.

  Args:
      input_pdf (str): Path to the input PDF file.
      output_docx (str): Path to save the translated DOCX file.
      target_lang (str, optional): Target language for translation. Defaults to "en" (English).
  """
  translator = Translator()

  with pdfplumber.open(input_pdf) as pdf:
    text = ""
    for page in pdf.pages:
      text += page.extract_text() + "\n"  # Add newline between pages

  translated_text = translator.translate(text, dest=target_lang).text

  # You can use a library like `docx` to create and format the DOCX file here.
  # This example just saves the translated text as plain text in the DOCX.

  with open(output_docx, "w") as docx_file:
    docx_file.write(translated_text)

# Example usage
input_pdf = "Holidays.pdf"

output_docx = "translated.docx"
target_lang = "es"  # Change to your desired language code

translate_pdf(input_pdf, output_docx, target_lang)
print(f"PDF translated to {target_lang} and saved as {output_docx}")
