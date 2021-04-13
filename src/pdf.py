import pdfplumber

pdf = pdfplumber.open("test2.pdf")
# page = pdf.pages[0]

# 循环page
for index, page in enumerate(pdf.pages):
    # 获取文档内容
    text = page.extract_text()
    print(index,'=>',text,'\n')
