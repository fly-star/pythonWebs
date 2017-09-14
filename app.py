# coding=utf-8
from flask import Flask

from myConverter import ListConverter

app = Flask(__name__)
app.config.from_pyfile('settings.py', silent=True)
app.url_map.converters['list'] = ListConverter

@app.route('/')
def index():
    return 'hello world debug again'

# 动态URL规则
@app.route('/item/<int:id>/')
def item(id):
    return "Item: {}".format(id)

# 自定义URL转换器
@app.route('/list1/<list:page_names>/')
def list1(page_names):
    return 'Separator: {} {}'.format('+', page_names)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)