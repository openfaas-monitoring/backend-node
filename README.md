# openfaas-monitoring backend-node

监控平台的后端工程，部署在Node节点上的后端程序。

## Code Framework

- `backend.py`：Flask后端的入口文件
- `logMonitor.py`：监控自定义日志文件并进行解析

提供running接口，向前端返回当前函数的运行状态以及需要更改状态的节点。