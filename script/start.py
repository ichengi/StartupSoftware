# -*-coding:utf-8-*-
'''
主程序
'''
import os
import subprocess
import json

def start_program(path:str,args:str)->int:
    """打开exe程序"""
    # 获取文件的文件夹路径
    program_dir = os.path.dirname(path)
    # subprocess的cwd参数指改变工作目录，因为程序可能不在当前目录下
    state = subprocess.Popen([path, args],cwd=program_dir)
    return state.returncode

if __name__ == '__main__':
    # 读取程序配置文件
    program_config = json.load(open(r'config/program.json', 'r', encoding='utf-8'))
    # 读取程序列表
    program_list = program_config['programs']
    for program in program_list:
        program_path = program['program_path']
        program_args =" ".join(program['parameters'])
        # 打开程序
        open_state = start_program(program_path,program_args)
        if open_state is None:
            print(rf'{program["name"]}启动成功')
