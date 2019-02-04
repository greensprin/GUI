# coding: UTF-8

# 使い方
# 第一引数：変換元のparamファイル
# 第二引数：変換先のparamファイル
# 変換元、先でのパラメータ名の対応表については、このファイルと同じ場所にdic.txtとして作成する
# python param_cnv.py [1] [2]

import os
import sys

argvs = sys.argv
argc = len(argvs)

param_file = argvs[1]
write_file = argvs[2]

dic_file = "dic.txt" # 対応表を記載したテキストファイルを読み込む

# make dic
dic = {} # 辞書型にパラメータの対応表を保存
with open(dic_file, "r") as dp:
    lines = dp.readlines()
    for line in lines:
        k, v = line.split() # keywordとvalueをそれぞれ取得
        dic[k] = v

with open(param_file, "r") as rp:
    with open(write_file, "w") as wp:
        lines = rp.readlines() # 1行ごと呼び出し
        for line in lines:
            if (line.find("write_param") != -1): # write_paramの行のみ読み込み
                s_line = line.split()
                print(s_line)
                if (s_line[1] in dic): # 辞書に対応するパラメータが保存してあれるか
                    wp.write(dic[s_line[1]] + " " + str(int(s_line[2], 0)) + "\n") # 保存してある場合、名前を対応するものに変更して、値とともに書き込む。値は、10,16進どちらでも可.
