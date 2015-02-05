# Flask-BCS
[百度云存储BCS](http://developer.baidu.com/cloud/stor)（Baidu Cloud Storage）Flask扩展，BCS(Baidu Cloud Storage) for Flask

## 安装
```python
pip install Flask-BCS
```
本扩展使用了[BCS Python SDK](http://developer.baidu.com/wiki/index.php?title=docs/cplat/stor/sdk)，pip安装时会自动包含该SDK。详细说明请参考[BCS 文档](http://developer.baidu.com/wiki/index.php?title=docs/cplat/bcs)。

## 配置
| 配置项 | 说明 |
|:--------------------:|:---------------------------:|
| BCS_HOST | BCS HOST |
| BCS_ACCESS_KEY | BCS Access Key |
| BCS_SECRET_KEY | BCS Secret Key |
| BCS_BUCKET_NAME | BCS 空间名称 |

## 使用
```python
from flask import Flask
from flask_bcs import BCS

BCS_HOST = 'BCS HOST'
BCS_ACCESS_KEY = 'BCS Access Key'
BCS_SECRET_KEY = 'BCS Secret Key'
BCS_BUCKET_NAME = 'BCS Bucket Name'

app = Flask(__name__)
app.config.from_object(__name__)
bcs = BCS(app)
# 或者
# bcs = BCS()
# bcs.init_app(app)

# 保存文件到BCS
@app.route('/save')
def save():
    data = 'data to save'
    filename = 'filename'
    allow_referers = ['http://*.duapp.com/*', 'http://zhangxc.com/*']
    # 不设置allow_referers为完全public
    ret = bcs.save(data, filename, allow_referers)
    return str(ret)

# 删除BCS中的文件
@app.route('/delete')
def delete():
    filename = 'filename'
    ret = bcs.delete(filename)
    return str(ret)

# 根据文件名获取对应的公开URL
@app.route('/url')
def url():
    filename = 'filename'
    return bcs.url(filename)
```
参考*tests.py*

## 返回值
`save`与`delete`返回值为[BCS Python SDK](http://developer.baidu.com/wiki/index.php?title=docs/cplat/stor/sdk)中对应API的返回值。

## 测试
```python
$ python tests.py
```

## 许可
The MIT License (MIT). 详情见 __License文件__