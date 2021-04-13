#https://python-docx.readthedocs.io/en/latest/

from docx import Document

# 不支持 test.doc
document = Document('test.docx')
for para in document.paragraphs:
    print(para.text)
