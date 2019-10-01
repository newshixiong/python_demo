# -*- coding: utf-8 -*-

import hashlib
import os
import shutil


# TODO 1.备份出错需要记录详细信息，from --> to
#     2.进行邮件通知


success_copy = []
failed_copy = []


def md5check(filename):
    m = hashlib.md5()
    # 以二进制的方式打开文件
    with open(filename, 'rb') as f:
        while True:
            # 只读取前面4字节
            data = f.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexdigest()


def copy(path):
    new_path = path
    new_path = new_path.replace(old_source, new_source)
    # print(new_path)
    # 如果是个文件类型，则需要比较md5值
    if os.path.isfile(new_path):
        old_md5 = md5check(path)
        new_md5 = md5check(new_path)
        # md5一致则说明文件没有变化，不需要copy
        if old_md5 != new_md5:
            try:
                shutil.copy(path, new_path)
                success_copy.append(path)
            except:
                failed_copy.append(path)
    # 如果是文件夹，则需要创建文件夹
    else:
        dirname = os.path.dirname(new_path)
        if os.path.exists(dirname):
            shutil.copy(path, new_path)
        else:  # 目录不存在，则直接创建目录并复制文件
            try:
                os.makedirs(dirname)
                shutil.copy(path, new_path)
            except WindowsError:
                failed_copy.append("create dir failed:" + path)


# 查找所有目录文件的递归函数
def lsdir(folders):
    path = os.listdir(folders)
    for line in path:
        line = folders + '/' + line
        if os.path.isdir(line):
            lsdir(line)
        else:
            copy(line)


if __name__ == '__main__':
    global old_source
    global new_source
    print('例子:d:/directory，请输入要备份的目录所在地址、以及目标地址：')
    old_source = "G:/code/code_git/xmind/"
    new_source = "F:/13_bak"
    lsdir(old_source)

    if success_copy.count() != 0:
        pass

    if failed_copy.count() != 0:
        pass


    """
    try:
        shutil.copy("C:/log.txt", "D:/log.txt")
    except:
        print("copy file error")
    """
