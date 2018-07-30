# Chinese-public-firm-prospectuses-analysis
Crawl and download IPO prospectuses from CSRC website(http://ipo.csrc.gov.cn/), convert PDF file into txt file and extract information from texts. 从中国证监会网站爬去并下载IPO招股说明书之后转换成txt格式，然后提取文本信息。

## spider.py
读取一个Excel文件，里面保存所需爬取的公司名称，之后从http://ipo.csrc.gov.cn/ 爬取相应公司的招股说明书的pdf文件。

## format_converter.py
用xpdf，将pdf文件转换为txt文件。

## info_extracter.py
将招股说明书中的信息提取出来。在这一例子中，我需要在文本正文中提取公司CEO的出生日期并转换为xx年代的格式，比如，1943年出生转化为40。由于该信息在正文中并且没有统一格式，所以需要使用正则表达式匹配各种情况。
