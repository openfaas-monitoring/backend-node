import os


# 监控日志的变化，从中解析出函数的动态运行情况
class LogMonitor:
    def __init__(self, volume_dir):
        self.volume_dir = volume_dir
        self.volume_map = self.getMappingInfo()

    # 获取volume目录下的映射关系
    def getMappingInfo(self):
        volume_map = dict()
        for name in os.listdir(self.volume_dir):
            path = self.volume_dir + '/' + name
            if not os.path.isdir(path):
                continue
            if not os.path.exists(path + '/_data'):
                continue
            for file_name in os.listdir(path + '/_data'):
                if os.path.isdir(path + '/_data' + '/' + file_name):
                    volume_map[file_name] = '/'.join([self.volume_dir, name, '_data', 'function.log'])
                    break
        return volume_map

    # 动态获取运行日志
    def getRunningInfo(self, func):
        with open(self.volume_map[func], 'r') as f:
            log = f.readlines()
        explained_info = self.explainLog(log)
        res = {'status': 'success', 'running_status': explained_info[0], 'running_info': explained_info[1]}
        return res

    # 解析日志，获取当前函数的运行信息，包括运行列表和运行状态
    def explainLog(self, log):
        running_list = list()
        running_status = 'running'
        for info in log:
            splits = info.split(' ')
            if len(splits) == 5:
                running_status = 'stop'
                continue
            thread, func_name, status = splits[3], splits[4], splits[5]
            if status == 'started\n':
                if func_name == 'all':
                    continue
                if thread == 'MainThread':
                    running_list.append('main-' + func_name)
                else:
                    running_list.append(thread + '-' + func_name)
        running_list = list(set(running_list))
        return running_status, running_list


if __name__ == '__main__':
    logMonitor = LogMonitor('./resource')
    print(logMonitor.getRunningInfo('branchtest'))
