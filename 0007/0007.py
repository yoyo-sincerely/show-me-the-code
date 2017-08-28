#!/usr/bin/python3
# -*- coding:utf8 -*-
import codecs
import os, re

FILE_PATH = 'code\\'

def Prin(text):
    for i in text:
        print(i)
    # print("跑到这了！")


def analize_code(codefile):
    '''
    打开一个py文件，统计其中的代码行数，包括空行和注释
    返回含该文件总行数，注释行数，空行数的列表
    '''
    total_line = 0
    comment_line = 0
    blank_line = 0
    with open(codefile, 'r',encoding="utf8") as f:
        lines = f.readlines()
        # Prin(lines)
        total_line = len(lines)
        line_index = 0
        # 遍历每一行
        while line_index < total_line:
            line = lines[line_index]
            # 检查# 与 ''' 注释
            if re.match("#.*", line) is not None:
                comment_line += 1
            elif re.match("\s*'''", line) is not None:
                comment_line += 1
                while re.match(".*'''$", line) is None:
                    line = lines[line_index]
                    comment_line += 1
                    line_index += 1
            elif line == '\n':
                blank_line += 1
            line_index += 1
    print ("在%s中：" % codefile)
    print ("代码行数：", total_line)
    print ("注释行数：", comment_line, "占%0.2f%%" % (comment_line*100.0/total_line))
    print ("空行数：  ", blank_line, "占%0.2f%%" % (blank_line*100.0/total_line))
    return [total_line, comment_line, blank_line]

def run(FILE_PATH):
    os.chdir(FILE_PATH)
    
    retval = os.getcwd()
    print("当前目录为：" + retval)
    
    # 遍历该目录下的py文件
    total_lines = 0
    total_comment_lines = 0
    total_blank_lines = 0
    for i in os.listdir(os.getcwd()):
        if os.path.splitext(i)[1] == '.py':
            line = analize_code(i)
            total_lines, total_comment_lines, total_blank_lines = total_lines + line[0], total_comment_lines + line[1], total_blank_lines + line[2]
    print ("总代码行数：", total_lines)
    print ("总注释行数：", total_comment_lines, "占%0.2f%%" % (total_comment_lines*100.0/total_lines))
    print ("总空行数：  ", total_blank_lines, "占%0.2f%%" % (total_blank_lines*100.0/total_lines))


if __name__ == '__main__':
    run(FILE_PATH)