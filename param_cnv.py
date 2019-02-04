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

param_file = argvs[1]
write_file = argvs[2]

dic_file = "dic.txt" # �Ή��\���L�ڂ����e�L�X�g�t�@�C����ǂݍ���

# make dic
dic = {} # �����^�Ƀp�����[�^�̑Ή��\��ۑ�
with open(dic_file, "r") as dp:
    lines = dp.readlines()
    for line in lines:
        k, v = line.split() # keyword��value�����ꂼ��擾
        dic[k] = v

with open(param_file, "r") as rp:
    with open(write_file, "w") as wp:
        lines = rp.readlines() # 1�s���ƌĂяo��
        for line in lines:
            if (line.find("write_param") != -1): # write_param�̍s�̂ݓǂݍ���
                s_line = line.split()
                print(s_line)
                if (s_line[1] in dic): # �����ɑΉ�����p�����[�^���ۑ����Ă���邩
                    wp.write(dic[s_line[1]] + " " + str(int(s_line[2], 0)) + "\n") # �ۑ����Ă���ꍇ�A���O��Ή�������̂ɕύX���āA�l�ƂƂ��ɏ������ށB�l�́A10,16�i�ǂ���ł���.
