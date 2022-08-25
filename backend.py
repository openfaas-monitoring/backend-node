from flask import Flask, request, jsonify
from flask_cors import CORS
from logMonitor import LogMonitor

app = Flask(__name__)
CORS(app)
# app的配置选项
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"

# 日志监控对象
monitor = LogMonitor('/var/lib/docker/volumes')


@app.route('/running', methods=['GET'])
def getRunningInfoFromFunction():
    func = request.args.get('func')
    return jsonify(monitor.getRunningInfo(func))


@app.route('/', methods=['GET'])
def hello():
    return jsonify('hello')


if __name__ == '__main__':
    app.run()
