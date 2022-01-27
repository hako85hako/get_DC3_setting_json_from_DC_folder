import csv
import sys
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import traceback


import app
import app2
import my_config
import my_settings


def check_valid(value):
    if value == '1' :
        return True
    else :
        return False

# tab2の内容
def tab2_main(frame_setting):
    get_targets = my_config.get_targets()
    get_titles = my_config.get_titles()
    get_valids = my_config.get_valids()
    get_texts = my_config.get_texts()
    set_main_title = get_titles[0]
    set_name_title = ""
############################################################################################
## main_title_config
############################################################################################
    # Frame
    frame_table_title = ttk.Frame(frame_setting, padding=(32))
    frame_table_title.grid(sticky=W)
    #main_title
    label1 = ttk.Label(frame_table_title, text="取得項目テーブル", padding=(5, 2))
    label1.grid(row=0, column=0, sticky=W)
    label2 = ttk.Label(frame_table_title, text="jsonのkeyを上位から順に登録してください。", padding=(5, 2))
    label2.grid(row=1, column=0, sticky=W)
    label3 = ttk.Label(frame_table_title, text="該当keyが見当たらない場合、警告なしに「'null'」を格納します(改修予定)。", padding=(5, 2))
    label3.grid(row=2, column=0, sticky=W)
############################################################################################
## table
############################################################################################
    # 列の識別名を指定
    column = ( 'Level_0', 'Level_1', 'Level_2', 'Level_3', 'Level_4',
             'Level_5', 'Level_6', 'Level_7', 'Level_8', 'Level_9')
    # Frame
    frame_table_title = ttk.Frame(frame_setting, padding=(32))
    frame_table_title.grid(sticky=W)
    # Treeviewの生成
    tree = ttk.Treeview(frame_table_title, columns=column)
    # 列の設定
    tree.column('#0',width=0, stretch='no')
    tree.column('Level_0', anchor='w', width=80)
    tree.column('Level_1', anchor='w', width=80)
    tree.column('Level_2', anchor='w', width=80)
    tree.column('Level_3', anchor='w', width=80)
    tree.column('Level_4', anchor='w', width=80)
    tree.column('Level_5', anchor='w', width=80)
    tree.column('Level_6', anchor='w', width=80)
    tree.column('Level_7', anchor='w', width=80)
    tree.column('Level_8', anchor='w', width=80)
    tree.column('Level_9', anchor='w', width=80)
    # 列の見出し設定
    tree.heading('#0',text='')
    tree.heading('Level_0', text='Level_0', anchor='w')
    tree.heading('Level_1', text='Level_1', anchor='w')
    tree.heading('Level_2', text='Level_2', anchor='w')
    tree.heading('Level_3', text='Level_3', anchor='w')
    tree.heading('Level_4', text='Level_4', anchor='w')
    tree.heading('Level_5', text='Level_5', anchor='w')
    tree.heading('Level_6', text='Level_6', anchor='w')
    tree.heading('Level_7', text='Level_7', anchor='w')
    tree.heading('Level_8', text='Level_8', anchor='w')
    tree.heading('Level_9', text='Level_9', anchor='w')

    # レコードの追加
    index = 0 
    for target in get_targets:
        tree.insert(parent="",index="end", tags=index ,values=target)
        if index & 1:
            tree.tag_configure(index,background="#CCFFFF")
        index += 1
    # ウィジェットの配置
    tree.pack(pady=10)
    # ウィジェットの配置
    tree.grid(row=1, column=1, sticky=W)
    #行選択時の関数
    def on_tree_select(event):
        column_num = 0
        column_keys =[
            'Level_0','Level_1','Level_0','Level_1','Level_0',
            'Level_1','Level_0','Level_1','Level_0','Level_1']
        column_value = ""

        for id in tree.selection():
            column_key = column_keys[column_num]
            print(column_key)
            # Frame
            select_column = ttk.Frame(frame_setting, padding=(32))
            select_column.grid(sticky=W)
            #select_column_1
            select_column_1 = StringVar()
            select_column_1 = ttk.Entry(
                select_column,
                textvariable = column_value,
                width=40)
            select_column_1.grid(row=0, column=column_num, sticky=W)
            select_column_1.insert(0,tree.set(id))
            column_num += 1
            print(column_value)
        print(tree.set(tree.selection()))
    #上の関数を呼び出すための設定
    tree.bind("<<TreeviewSelect>>", on_tree_select)
    return 0






if __name__ == '__main__':
    pirnt('test用')