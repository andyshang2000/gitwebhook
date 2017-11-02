from flask import Flask
from config import DevConfig
from hook import hook
# from user import user

app = Flask(__name__, template_folder="templates", static_folder="static")
app.config.from_object(DevConfig)
app.register_blueprint(hook, url_prefix='/hook')  # 注册asset蓝图，并指定前缀。
# app.register_blueprint(user)  # 注册user蓝图，没有指定前缀。

# views = __import__('views')

if __name__ == '__main__':
    app.run()
