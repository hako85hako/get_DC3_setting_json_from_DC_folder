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
def tab3_main(frame_config):
    get_titles = my_config.get_titles()
    get_valids = my_config.get_valids()
    get_texts = my_config.get_texts()
    set_main_title = get_titles[0]
    set_name_title = ""
############################################################################################
## main_title_config
############################################################################################
    # Frame
    frame_main_title = ttk.Frame(frame_config, padding=(32))
    frame_main_title.grid(sticky=W)
    #main_title
    label1 = ttk.Label(frame_main_title, text="メインタイトル", padding=(5, 2))
    label1.grid(row=0, column=0, sticky=W)
    main_title = StringVar()
    main_title = ttk.Entry(
        frame_main_title,
        textvariable = get_titles[0] ,
        width=40)
    main_title.grid(row=0, column=1, sticky=W)
    main_title.insert(0,get_titles[0])
############################################################################################
## name_config
############################################################################################
    # Frame
    frame_name = ttk.Frame(frame_config, padding=(32))
    frame_name.grid(sticky=W)
    # name_valid
    name_valid = StringVar()
    name_valid.set(check_valid(get_valids[0])) # 初期化
    name_config_cb1 = ttk.Checkbutton(
        frame_name, padding=(10), text='name表示',
        onvalue=1, offvalue=0,
        variable=get_valids[0]
       )
    name_config_cb1.grid(row=0, column=0, sticky=W)
    # name_title_valid
    name_title_valid = StringVar()
    name_title_valid.set(check_valid(get_valids[1])) # 初期化
    name_config_cb2 = ttk.Checkbutton(
        frame_name, padding=(10), text='name_title表示',
        onvalue=1, offvalue=0,
        variable=get_valids[1]
       )
    name_config_cb2.grid(row=0, column=1, sticky=W)
    # name_text1_valid
    name_text1_valid = StringVar()
    name_text1_valid.set(check_valid(get_valids[2])) # 初期化
    name_config_cb3 = ttk.Checkbutton(
        frame_name, padding=(10), text='name_text1表示',
        onvalue=1, offvalue=0,
        variable=get_valids[2]
       )
    name_config_cb3.grid(row=0, column=2, sticky=W)
    # name_text2_valid
    name_text2_valid = StringVar()
    name_text2_valid.set(check_valid(get_valids[3])) # 初期化
    name_config_cb4 = ttk.Checkbutton(
        frame_name, padding=(10), text='name_text2表示',
        onvalue=1, offvalue=0,
        variable=get_valids[3]
       )
    name_config_cb4.grid(row=0, column=3, sticky=W)
    #name_title
    label1 = ttk.Label(frame_name, text="nameタイトル", padding=(5, 2))
    label1.grid(row=1, column=0, sticky=W)
    name_title = StringVar()
    name_title = ttk.Entry(
        frame_name,
        textvariable = get_titles[1] ,
        width=40)
    name_title.grid(row=1, column=1, sticky=W)
    name_title.insert(0,get_titles[1])
    #name_text_1
    label2 = ttk.Label(frame_name, text="nameテキスト1", padding=(5, 2))
    label2.grid(row=2, column=0, sticky=W)
    name_text_1 = StringVar()
    name_text_1 = ttk.Entry(
        frame_name,
        textvariable = get_texts[0] ,
        width=40)
    name_text_1.grid(row=2, column=1, sticky=W)
    name_text_1.insert(0,get_texts[0])
    #name_text_2
    label3 = ttk.Label(frame_name, text="nameテキスト2", padding=(5, 2))
    label3.grid(row=3, column=0, sticky=W)
    name_text_1 = StringVar()
    name_text_1 = ttk.Entry(
        frame_name,
        textvariable = get_texts[1] ,
        width=40)
    name_text_1.grid(row=3, column=1, sticky=W)
    name_text_1.insert(0,get_texts[1])
############################################################################################
## processID_config
############################################################################################
    # Frame
    frame_prcessID = ttk.Frame(frame_config, padding=(32))
    frame_prcessID.grid(sticky=W)
    # prcessID_valid
    prcessID_valid = StringVar()
    prcessID_valid.set(check_valid(get_valids[4])) # 初期化
    prcessID_config_cb1 = ttk.Checkbutton(
        frame_prcessID, padding=(10), text='prcessID表示',
        onvalue=1, offvalue=0,
        variable=get_valids[4]
       )
    prcessID_config_cb1.grid(row=0, column=0, sticky=W)
    # prcessID_title_valid
    prcessID_title_valid = StringVar()
    prcessID_title_valid.set(check_valid(get_valids[5])) # 初期化
    prcessID_config_cb2 = ttk.Checkbutton(
        frame_prcessID, padding=(10), text='prcessID_title表示',
        onvalue=1, offvalue=0,
        variable=get_valids[5]
       )
    prcessID_config_cb2.grid(row=0, column=1, sticky=W)
    # prcessID_text1_valid
    prcessID_text1_valid = StringVar()
    prcessID_text1_valid.set(check_valid(get_valids[6])) # 初期化
    prcessID_config_cb3 = ttk.Checkbutton(
        frame_prcessID, padding=(10), text='prcessID_text1表示',
        onvalue=1, offvalue=0,
        variable=get_valids[6]
       )
    prcessID_config_cb3.grid(row=0, column=2, sticky=W)
    # prcessID_text2_valid
    prcessID_text2_valid = StringVar()
    prcessID_text2_valid.set(check_valid(get_valids[7])) # 初期化
    prcessID_config_cb4 = ttk.Checkbutton(
        frame_prcessID, padding=(10), text='prcessID_text2表示',
        onvalue=1, offvalue=0,
        variable=get_valids[7]
       )
    prcessID_config_cb4.grid(row=0, column=3, sticky=W)
    #prcessID_title
    label1 = ttk.Label(frame_prcessID, text="prcessIDタイトル", padding=(5, 2))
    label1.grid(row=1, column=0, sticky=W)
    prcessID_title = StringVar()
    prcessID_title = ttk.Entry(
        frame_prcessID,
        textvariable = get_titles[2] ,
        width=40)
    prcessID_title.grid(row=1, column=1, sticky=W)
    prcessID_title.insert(0,get_titles[2])
    #prcessID_text_1
    label2 = ttk.Label(frame_prcessID, text="prcessIDテキスト1", padding=(5, 2))
    label2.grid(row=2, column=0, sticky=W)
    prcessID_text_1 = StringVar()
    prcessID_text_1 = ttk.Entry(
        frame_prcessID,
        textvariable = get_texts[2] ,
        width=40)
    prcessID_text_1.grid(row=2, column=1, sticky=W)
    prcessID_text_1.insert(0,get_texts[2])
    #prcessID_text_2
    label3 = ttk.Label(frame_prcessID, text="prcessIDテキスト2", padding=(5, 2))
    label3.grid(row=3, column=0, sticky=W)
    prcessID_text_1 = StringVar()
    prcessID_text_1 = ttk.Entry(
        frame_prcessID,
        textvariable = get_texts[3] ,
        width=40)
    prcessID_text_1.grid(row=3, column=1, sticky=W)
    prcessID_text_1.insert(0,get_texts[3])
############################################################################################
## Conditions_config
############################################################################################
    # Frame
    frame_Conditions = ttk.Frame(frame_config, padding=(32))
    frame_Conditions.grid(sticky=W)
    # Conditions_valid
    Conditions_valid = StringVar()
    Conditions_valid.set(check_valid(get_valids[8])) # 初期化
    Conditions_config_cb1 = ttk.Checkbutton(
        frame_Conditions, padding=(10), text='Conditions表示',
        onvalue=1, offvalue=0,
        variable=get_valids[8]
       )
    Conditions_config_cb1.grid(row=0, column=0, sticky=W)
    # Conditions_title_valid
    Conditions_title_valid = StringVar()
    Conditions_title_valid.set(check_valid(get_valids[9])) # 初期化
    Conditions_config_cb2 = ttk.Checkbutton(
        frame_Conditions, padding=(10), text='Conditions_title表示',
        onvalue=1, offvalue=0,
        variable=get_valids[9]
       )
    Conditions_config_cb2.grid(row=0, column=1, sticky=W)
    # Conditions_text1_valid
    Conditions_text1_valid = StringVar()
    Conditions_text1_valid.set(check_valid(get_valids[10])) # 初期化
    Conditions_config_cb3 = ttk.Checkbutton(
        frame_Conditions, padding=(10), text='Conditions_text1表示',
        onvalue=1, offvalue=0,
        variable=get_valids[10]
       )
    Conditions_config_cb3.grid(row=0, column=2, sticky=W)
    # Conditions_text2_valid
    Conditions_text2_valid = StringVar()
    Conditions_text2_valid.set(check_valid(get_valids[5])) # 初期化
    Conditions_config_cb4 = ttk.Checkbutton(
        frame_Conditions, padding=(10), text='Conditions_text2表示',
        onvalue=1, offvalue=0,
        variable=get_valids[11]
       )
    Conditions_config_cb4.grid(row=0, column=3, sticky=W)
    #Conditions_title
    label1 = ttk.Label(frame_Conditions, text="Conditionsタイトル", padding=(5, 2))
    label1.grid(row=1, column=0, sticky=W)
    Conditions_title = StringVar()
    Conditions_title = ttk.Entry(
        frame_Conditions,
        textvariable = get_titles[3] ,
        width=40)
    Conditions_title.grid(row=1, column=1, sticky=W)
    Conditions_title.insert(0,get_titles[3])
    #Conditions_text_1
    label2 = ttk.Label(frame_Conditions, text="Conditionsテキスト1", padding=(5, 2))
    label2.grid(row=2, column=0, sticky=W)
    Conditions_text_1 = StringVar()
    Conditions_text_1 = ttk.Entry(
        frame_Conditions,
        textvariable = get_texts[4] ,
        width=40)
    Conditions_text_1.grid(row=2, column=1, sticky=W)
    Conditions_text_1.insert(0,get_texts[4])
    #Conditions_text_2
    label3 = ttk.Label(frame_Conditions, text="Conditionsテキスト2", padding=(5, 2))
    label3.grid(row=3, column=0, sticky=W)
    Conditions_text_1 = StringVar()
    Conditions_text_1 = ttk.Entry(
        frame_Conditions,
        textvariable = get_texts[5] ,
        width=40)
    Conditions_text_1.grid(row=3, column=1, sticky=W)
    Conditions_text_1.insert(0,get_texts[5])



    return 0