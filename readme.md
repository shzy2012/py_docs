# 文档搜索系统


python 对文件的操作
```
pdfplumber==0.5.27
python-pptx==0.6.18
python-docx==0.8.10
xlrd==2.0.1
```

### 文档存储格式

```json
{
    "文件":"招标书.doc",
    "原始内容":"xxxxx-文档内容",
    "预处理":[
        {
            "page":1,
            "context":"xxxxx-page-X内容",
        },
        {
            "page":2,
            "context":"xxxxx-page-X内容",
        }
    ],
    "时间":"2020-01-03"
}
```

