"""
How to use a pymupdf font with method Page.insert_htmlbox().
"""
import pymupdf

# Example text
text = """Lorem ipsum dolor sit amet, consectetur adipisici elit, sed
    eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad
    minim veniam, quis nostrud exercitation <b>ullamco <i>laboris</i></b>
    nisi ut aliquid ex ea commodi consequat. Quis aute iure
    <span style="color: red;">reprehenderit</span>
    in <span style="color: green;font-weight:bold;">voluptate</span> velit
    esse cillum dolore eu fugiat nulla pariatur. Excepteur sint obcaecat
    cupiditat non proident, sunt in culpa qui
    <a href="https://www.artifex.com">officia</a> deserunt mollit anim id
    est laborum."""

"""
This is similar to font file support. However, we can use a convenience
function for creating required CSS definitions.
We still need an Archive for finding the font binaries.
"""
arch = pymupdf.Archive()

# We request to use "myfont" throughout the text.
css = pymupdf.css_for_pymupdf_font("ubuntu", archive=arch, name="myfont")
css += "* {font-family: myfont;text-align: justify;}"

doc = pymupdf.Document()

page = doc.new_page(width=150, height=150)

page.insert_htmlbox(page.rect, text, css=css, archive=arch, rotate=90)

doc.subset_fonts(verbose=True)
doc.ez_save(__file__.replace(".py", ".pdf"))