import csv
import sys
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import traceback
from glob import glob

import app
import app2
import config_frame
import setting_frame
import my_config
import my_settings


class TkinterClass():    
    def __init__(self):
        my_config.db_delete()
        # ルートを作成
        root = Tk()
        # 設定
        root.title(my_settings.main_title)
        root.resizable(True, True)

         #メインウィンドウにnotebookを作成する。
        nb = ttk.Notebook(root)
        #notebookに関するフレームを3つ作る。
        frame_main = ttk.Frame(nb, padding=(32))
        frame_setting = ttk.Frame(nb, padding=(32))
        frame_config = ttk.Frame(nb, padding=(32))
        
    
        #notebookに対してtab1, 2, 3をそれぞれ追加する。
        nb.add(frame_main, text="main")
        #nb.add(frame_setting, text="setting")
        #nb.add(frame_config, text="config")
        

        #メインフレームでのnotebook配置を決定する。
        nb.pack(expand=1,fill="both")
        self.tab1_main(frame_main)
        #setting_frame.tab2_main(frame_setting)
        #config_frame.tab3_main(frame_config)
        #self.tab2_main(frame_config)        
        #self.tab3_main(frame_conditions)
        root.mainloop()
    


    # tab1の内容
    def tab1_main(self,frame_main):
    ############################################################################################
    ## 名前の入力
    ############################################################################################
        # Frame
        frame_name = ttk.Frame(frame_main, padding=(32))
        frame_name.grid(sticky=W)
        if my_settings.name_is_valid:
            # ラベル作成
            if my_settings.name_title_is_valid:
                label1 = ttk.Label(frame_name, text=my_settings.name_title, padding=(5, 2))
                label1.grid(row=0, column=0, sticky=W)
            if my_settings.name_text_1_is_valid:
                label2 = ttk.Label(frame_name, text=my_settings.name_text_1, padding=(5, 5))
                label2.grid(row=2, column=1, sticky=W)
            if my_settings.name_text_2_is_valid:
                label3 = ttk.Label(frame_name, text=my_settings.name_text_2, padding=(5, 5))
                label3.grid(row=3, column=1, sticky=W)
            self.name = StringVar()
            name = ttk.Entry(
                frame_name,
                textvariable=self.name,
                width=40)
            name.grid(row=1, column=1, sticky=W)


    ############################################################################################
    ##processIDの入力
    ############################################################################################        
        # フレーム作成
        frame_processID = ttk.Frame(frame_main, padding=(32))
        frame_processID.grid(sticky=W)
        if my_settings.processID_is_valid:
            # ラベル作成
            if my_settings.processID_title_is_valid:
                label1 = ttk.Label(frame_processID, text=my_settings.processID_title, padding=(5, 2))
                label1.grid(row=0, column=0, sticky=W)
            if my_settings.processID_text_1_is_valid:
                label2 = ttk.Label(frame_processID, text=my_settings.processID_text_1, padding=(5, 5))
                label2.grid(row=2, column=1, sticky=W)
            if my_settings.processID_text_2_is_valid:
                label3 = ttk.Label(frame_processID, text=my_settings.processID_text_2, padding=(5, 5))
                label3.grid(row=3, column=1, sticky=W)

            self.processID = StringVar()
            processID = ttk.Entry(
                frame_processID,
                textvariable=self.processID,
                width=40)
            processID.grid(row=1, column=1, sticky=W)

    ############################################################################################
    ##Conditionsの選択
    ############################################################################################
        # Frame
        frame_conditions = ttk.Frame(frame_main, padding=(32))
        frame_conditions.grid(row=6, column=0, sticky=W)
        if my_settings.condition_is_valid:
            # ラベル作成
            if my_settings.condition_title_is_valid:
                label1 = ttk.Label(frame_conditions, text=my_settings.conditions_title, padding=(5, 2))
                label1.grid(row=0, column=0, sticky=W)
            if my_settings.conditions_text_1_is_valid:
                label2 = ttk.Label(frame_conditions, text=my_settings.conditions_text_1, padding=(5, 5))
                label2.grid(row=1, column=1, sticky=W)
            if my_settings.conditions_text_2_is_valid:
                label3 = ttk.Label(frame_conditions, text=my_settings.conditions_text_2, padding=(5, 5))
                label3.grid(row=2, column=1, sticky=W)
        # Checkbutton 1
            if my_settings.conditions_v1_is_valid:
                self.v1 = StringVar()
                self.v1.set('') # 初期化
                cb1 = ttk.Checkbutton(
                    frame_conditions, padding=(10), text=my_settings.conditions_v1_text,
                    onvalue=1, offvalue=0,
                    variable=self.v1,
                    command=self.school_or_kis_school)
                cb1.grid(row=3, column=1, sticky=W)
            
            # Checkbutton 2
            if my_settings.conditions_v2_is_valid:
                self.v2 = StringVar()
                self.v2.set('') 
                cb2 = ttk.Checkbutton(
                    frame_conditions, padding=(10), text=my_settings.conditions_v2_text,
                    onvalue=1, offvalue=0,
                    variable=self.v2,
                    command=self.school_or_kis_kis)
                cb2.grid(row=4, column=1, sticky=W)

            # Checkbutton 3
            if my_settings.conditions_v3_is_valid:
                self.v3 = StringVar()
                self.v3.set('') 
                cb3 = ttk.Checkbutton(
                    frame_conditions, padding=(10), text=my_settings.conditions_v3_text,
                    onvalue=1, offvalue=0,
                    variable=self.v3)
                cb3.grid(row=5, column=1, sticky=W)
            
            # Checkbutton 4
            if my_settings.conditions_v4_is_valid:
                self.v4 = StringVar()
                self.v4.set('') 
                cb4 = ttk.Checkbutton(
                    frame_conditions, padding=(10), text=my_settings.conditions_v4_text,
                    onvalue=1, offvalue=0,
                    variable=self.v4)
                cb4.grid(row=6, column=1, sticky=W)

            # Checkbutton 5
            if my_settings.conditions_v5_is_valid:
                self.v5 = StringVar()
                self.v5.set('') 
                cb5 = ttk.Checkbutton(
                    frame_conditions, padding=(10), text=my_settings.conditions_v5_text,
                    onvalue=1, offvalue=0,
                    variable=self.v5)
                cb5.grid(row=7, column=1, sticky=W)
            
            # Checkbutton 6
            if my_settings.conditions_v6_is_valid:
                self.v6 = StringVar()
                self.v6.set('') 
                cb6 = ttk.Checkbutton(
                    frame_conditions, padding=(10), text=my_settings.conditions_v6_text,
                    onvalue=1, offvalue=0,
                    variable=self.v6)
                cb6.grid(row=8, column=1, sticky=W)
            
            # Checkbutton 7
            if my_settings.conditions_v7_is_valid:
                self.v7 = StringVar()
                self.v7.set('') 
                cb7 = ttk.Checkbutton(
                    frame_conditions, padding=(10), text=my_settings.conditions_v7_text,
                    onvalue=1, offvalue=0,
                    variable=self.v7)
                cb7.grid(row=9, column=1, sticky=W)
            
            # Checkbutton 8
            if my_settings.conditions_v8_is_valid:
                self.v8 = StringVar()
                self.v8.set('') 
                cb8 = ttk.Checkbutton(
                    frame_conditions, padding=(10), text=my_settings.conditions_v8_text,
                    onvalue=1, offvalue=0,
                    variable=self.v8)
                cb8.grid(row=10, column=1, sticky=W)
            
            # Checkbutton 9
            if my_settings.conditions_v9_is_valid:
                self.v9 = StringVar()
                self.v9.set('') 
                cb9 = ttk.Checkbutton(
                    frame_conditions, padding=(10), text=my_settings.conditions_v9_text,
                    onvalue=1, offvalue=0,
                    variable=self.v9)
                cb9.grid(row=11, column=1, sticky=W)
            
            # Checkbutton 10
            if my_settings.conditions_v10_is_valid:
                self.v10 = StringVar()
                self.v10.set('') 
                cb10 = ttk.Checkbutton(
                    frame_conditions, padding=(10), text=my_settings.conditions_v10_text,
                    onvalue=1, offvalue=0,
                    variable=self.v10)
                cb10.grid(row=12,column=1, sticky=W)

        # Button
        button1 = ttk.Button(
            frame_conditions , text='OK',
            command=self.run_app)
        # Button
        button2 = ttk.Button(
            frame_conditions , text='Cancel',
            command=sys.exit)

        # Layout
        button1.grid(row=13, column=3)
        button2.grid(row=13, column=4)
        return 0
    ############################################################################################

    def create_conditions(self):
        conditions = []
        #print(self.v1.get())
        if self.v1.get() == '1':
            conditions += [my_settings.conditions_v1_value]
        if self.v2.get() == '1':
            conditions += [my_settings.conditions_v2_value]
        if self.v3.get() == '1':
            conditions += [my_settings.conditions_v3_value]
        if self.v4.get() == '1':
            conditions += [my_settings.conditions_v4_value]
        if self.v5.get() == '1':
            conditions += [my_settings.conditions_v5_value]
        if self.v6.get() == '1':
            conditions += [my_settings.conditions_v6_value]
        if self.v7.get() == '1':
            conditions += [my_settings.conditions_v7_value]
        if self.v8.get() == '1':
            conditions += [my_settings.conditions_v8_value]
        if self.v9.get() == '1':
            conditions += [my_settings.conditions_v9_value]
        if self.v10.get() == '1':
            conditions += [my_settings.conditions_v10_value]
        return conditions
    
    def create_name(self):
        return self.name.get()

    def create_processID(self):
        return self.processID.get()


    def school_or_kis_school(self):
        if self.v2.get():
            self.v2.set(False)

    def school_or_kis_kis(self):
        if self.v1.get():
            self.v1.set(False)

    def run_app(self):
        error_flg = False
        name = self.create_name()
        conditions = self.create_conditions()
        processID = self.create_processID()
        targets = my_config.get_targets()
        #階層指定用の「setting.csv」あるならそこを参照
        #なければデフォルト
        setting_csv = glob(f'setting.csv')
        if setting_csv:
            with open(setting_csv[0]) as f:
                reader = csv.reader(f)
                targets = [row for row in reader]
        try:
            #app.app(name,conditions,processID)
            #print(targets)
            app2.app2(name,conditions,processID,targets)
        except Exception as e:
            print("例外args:", e.args)
            error_flg = True
        if not error_flg:
            messagebox.showinfo('完了', '完了しました。\n内容を確認してください。')
        else:
            ex = traceback.format_exc()
            messagebox.showerror('エラー', '処理中にエラーが発生しました。\n\n'+ex)
   
if __name__=="__main__":
    
    TkinterClass()