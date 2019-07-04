# HTMLSimilarity
根据网页结构判断页面相似性(Determine page similarity based on HTML page structure)

[![PyV](https://img.shields.io/badge/python-3.7-brightgreen.svg)]()

使用方法
-----------

```
from htmlsimilarity import get_html_similarity

is_similarity, value = get_html_similarity(html_doc1, html_doc2)
```

说明
-----------

##### 输入参数：
* HTML文档1
* HTML文档2
* 降维后的维数，默认是5000

##### 返回值：
* 是否相似
* 相似值（value<0.2时相似，value>0.2时不相似）


判断方法
-----------

参考：[李景阳, 张波. 网页结构相似性确定方法及装置:.](http://cprs.patentstar.com.cn/Search/Detail?ANE=9HCC7BGA7AHACGEA7GAA8BHA5ADA9FGF8CBA9EDA9BDC9FCG)

原理参考上述专利文章，对其判断相似性部分进行简单实现。

用途
-----------

判断越权时，需要对response进行对比，当后端返回渲染后HTML的情况下，无法直接判断是否出现了越权，利用常规的文本相似度对比如difflib，通过分词或最长公共子串等方法进行判断并不适用于用来判断越权，所以使用根据页面结构判断相似度，确定是否出现了越权。