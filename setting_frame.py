import csv
import sys
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import traceback
import json

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
    get_targets_for_next_version = my_config.get_targets_for_next_version()
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
    column = ('ID', 'Level_0','Level_1', 'Level_2', 'Level_3', 'Level_4',
             'Level_5', 'Level_6', 'Level_7', 'Level_8', 'Level_9')
    # Frame
    frame_table_title = ttk.Frame(frame_setting, padding=(10))
    frame_table_title.grid(sticky=W)
    # Treeviewの生成
    tree = ttk.Treeview(frame_table_title, columns=column)
    # 列の設定
    tree.column('#0',width=0, stretch='no')
    tree.column('ID', anchor='center',width=20)
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
    tree.heading('ID', text='ID')
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
    #print(get_targets_for_next_version)
    for target in get_targets_for_next_version:
        tree.insert(parent="",index="end", iid=index ,values=target)
        index += 1
    
    select_column = ttk.Frame(frame_setting, padding=(10))
    select_column.grid(row=2, column=0,sticky=W)



    # ウィジェットの配置
    tree.pack(pady=10)
    # ウィジェットの配置
    tree.grid(row=1, column=1, sticky=W)

    #行選択時の関数
    def on_tree_select(event):
        
        column_num = 0
        column_keys =[
            'ID','Level_0','Level_1','Level_2','Level_3','Level_4',
            'Level_5','Level_6','Level_7','Level_8','Level_9']
        #column_value = ""
        
        for id in tree.selection():
            column_values = list()
            # Frame
            select_column = ttk.Frame(frame_setting, padding=(10))
            select_column.grid(row=2, column=0,sticky=W)
            for column_key in column_keys:
                try:
                    #select_column_1
                    select_column_1 = StringVar()
                    select_column_1 = ttk.Entry(
                        select_column,
                        #textvariable = column_value,
                        width=30)
                    select_column_1.grid(row=column_num, column=1, sticky=W)
                    #select_column_1.insert(0,tree.set(id))
                    select_column_1.insert(0,tree.set(id)[column_key])
                    label2 = ttk.Label(select_column, text=column_key, padding=(5, 2))
                    label2.grid(row=column_num, column=0, sticky=W)
                    column_num += 1
                    column_values += [tree.set(id)[column_key]]
                except:
                    print("ここだ！")
        # Button
        button1 = ttk.Button(
            select_column , text='登録',
            # command=my_config.registrar_targets(column_values)
             command=print('btn_click')
        )
            
        button1.grid(row=column_num+1, column=1,sticky=E)
    #上の関数を呼び出すための設定
    tree.bind("<<TreeviewSelect>>",on_tree_select)






if __name__ == '__main__':
    pirnt('test用')