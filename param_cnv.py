# coding: UTF-8

# �g����
# �������F�ϊ�����param�t�@�C��
# �������F�ϊ����param�t�@�C��
# �ϊ����A��ł̃p�����[�^���̑Ή��\�ɂ��ẮA���̃t�@�C���Ɠ����ꏊ��dic.txt�Ƃ��č쐬����
# python param_cnv.py [1] [2]

import os
import sys

argvs = sys.argv
argc = len(argvs)

dic = {} # �����^�Ƀp�����[�^�̑Ή��\��ۑ�

# make dic
def read_dic_file(dic_file):
    with open(dic_file, "r") as dp:
        lines = dp.readlines()
        for line in lines:
            k, v = line.split() # keyword��value�����ꂼ��擾
            dic[k] = v

def write_param(param_file, write_file):
    with open(param_file, "r") as rp: # open param file
        with open(write_file, "w") as wp: # open write param file
            lines = rp.readlines() # 1�s���ƌĂяo��
            for line in lines:
                if (line.find("write_param") != -1): # write_param�̍s�̂ݓǂݍ���
                    s_line = line.split()
                    if (s_line[1] in dic): # �����ɑΉ�����p�����[�^���ۑ����Ă���邩
                        wp.write(dic[s_line[1]] + " " + str(int(s_line[2], 0)) + "\n") # �ۑ����Ă���ꍇ�A���O��Ή�������̂ɕύX���āA�l�ƂƂ��ɏ������ށB�l�́A10,16�i�ǂ���ł���.

def read_input_file(param_file):
    with open(param_file, "r") as rp: # open param file
        lines = rp.readlines() # 1�s���ƌĂяo��
        flg = 0
        input_file = []
        for line in lines:
            if (flg == 1):
                if (line.find("write_param") == -1):
                    s_line = line.split()
                    input_file.append(s_line[1])
            if (line.find("input") != -1):
                flg = 1
        return input_file

if __name__ == "__main__":
# �p�����[�^�t�@�C�����X�g��ǂݍ���ł���΁A���̒�����Ainput�t�@�C���Aparam�t�@�C������邱�Ƃ��ł���
    param_file = argvs[1]
    write_file = "param_write.txt" # write param file path
    dic_file = "dic.txt" # �Ή��\���L�ڂ����e�L�X�g�t�@�C����ǂݍ���

    read_dic_file(dic_file) # make dic

    write_param(param_file, write_file) # write param file

    input_file = read_input_file(param_file) # read input data path

    print(input_file)
