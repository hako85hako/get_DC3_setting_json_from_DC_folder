import os
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import app
from tkinter import messagebox
import csv
import sys
import traceback
import myTools

class TkinterClass:
    def __init__(self):
        # ルートを作成
        root = Tk()
        # ''設定
        root.title('get_DC3_setting_json')
        root.resizable(True, True)

        # フレーム作成
        frame1 = ttk.Frame(root, padding=(32))
        frame1.grid()

        # ラベル作成
        label1 = ttk.Label(frame1, text='name', padding=(5, 2))
        label1.grid(row=0, column=0, sticky=E)
        label2 = ttk.Label(frame1, text='(この名前がツールに選択肢として表示される)。', padding=(5, 5))
        label2.grid(row=1, column=1, sticky=E)
        label3 = ttk.Label(frame1, text='例. \"荏原 BMU20 1系統 日射・気温なし　蓄電池あり\"', padding=(5, 5))
        label3.grid(row=2, column=1, sticky=E)

############################################################################################
##案件名の入力
############################################################################################        
        self.name = StringVar()
        name = ttk.Entry(
            frame1,
            textvariable=self.name,
            width=40)
        name.grid(row=0, column=1)
############################################################################################
##Conditionsの選択
############################################################################################
       # Frame
        oprionFrame = ttk.Frame(root, padding=(5, 5))
        oprionFrame.grid(row=6, column=0)
       # Checkbutton 1 school
        self.v1 = StringVar()
        self.v1.set('') # 初期化
        cb1 = ttk.Checkbutton(
            oprionFrame, padding=(10), text='school',
            onvalue=True, offvalue=False,
            variable=self.v1,
            command=self.school_or_kis_school)
        # Checkbutton 2 kis
        self.v2 = StringVar()
        self.v2.set('') 
        cb2 = ttk.Checkbutton(
            oprionFrame, padding=(10), text='kis',
            onvalue=True, offvalue=False,
            variable=self.v2,
            command=self.school_or_kis_kis)
        # Checkbutton 3 ebara
        self.v3 = StringVar()
        self.v3.set('') 
        cb3 = ttk.Checkbutton(
            oprionFrame, padding=(10), text='ebara',
            onvalue=True, offvalue=False,
            variable=self.v3)
        # Checkbutton 4 rpower
        self.v4 = StringVar()
        self.v4.set('') 
        cb4 = ttk.Checkbutton(
            oprionFrame, padding=(10), text='rpower',
            onvalue=True, offvalue=False,
            variable=self.v4)
        # Checkbutton 5 dc
        self.v5 = StringVar()
        self.v5.set('') 
        cb5 = ttk.Checkbutton(
            oprionFrame, padding=(10), text='dc',
            onvalue=True, offvalue=False,
            variable=self.v5)
        # Checkbutton 6 irr
        self.v6 = StringVar()
        self.v6.set('') 
        cb6 = ttk.Checkbutton(
            oprionFrame, padding=(10), text='irr',
            onvalue=True, offvalue=False,
            variable=self.v6)
        # Checkbutton 7 temp
        self.v7 = StringVar()
        self.v7.set('') 
        cb7 = ttk.Checkbutton(
            oprionFrame, padding=(10), text='temp',
            onvalue=True, offvalue=False,
            variable=self.v7)
        # Checkbutton 8 battery
        self.v8 = StringVar()
        self.v8.set('') 
        cb8 = ttk.Checkbutton(
            oprionFrame, padding=(10), text='battery',
            onvalue=True, offvalue=False,
            variable=self.v8)
        # Checkbutton 9 selfCons
        self.v9 = StringVar()
        self.v9.set('') 
        cb9 = ttk.Checkbutton(
            oprionFrame, padding=(10), text='selfCons',
            onvalue=True, offvalue=False,
            variable=self.v9)
        # Checkbutton 10 ctrl
        self.v10 = StringVar()
        self.v10.set('') 
        cb10 = ttk.Checkbutton(
            oprionFrame, padding=(10), text='ctrl',
            onvalue=True, offvalue=False,
            variable=self.v10)

        # Button
        button1 = ttk.Button(
            oprionFrame , text='OK',
            command=self.run_app)
        # Button
        button2 = ttk.Button(
            oprionFrame , text='Cancel',
            command=sys.exit)

        label4 = ttk.Label( oprionFrame , text=
                'schoolまたはkis     大人版の場合は設定しない\n'+
                'ebara	               荏原版の場合\n'+
                'rpower	               受電電力がある場合\n'+
                'dc                          直流がある場合\n'+
                'irr	              日射がある場合\n'+
                'temp	              気温がある場合\n'+
                'battery	              蓄電池がある場合\n'+
                'selfCons	              自家消費の場合\n'+
                'ctrl	               制御の場合\n'
        , padding=(5, 2))
        label4.grid(row=7, column=3, sticky=E)

       # Layout
        cb1.grid(row=5, column=1)
        cb2.grid(row=5, column=2)
        cb3.grid(row=5, column=3)
        cb4.grid(row=5, column=4)
        cb5.grid(row=5, column=5)
        cb6.grid(row=6, column=1)
        cb7.grid(row=6, column=2)
        cb8.grid(row=6, column=3)
        cb9.grid(row=6, column=4)
        cb10.grid(row=6,column=5)
        button1.grid(row=8, column=4)
        button2.grid(row=8, column=5)
############################################################################################
        root.mainloop()

    def create_conditions(self):
        conditions = []
        if self.v1.get():
            conditions += ['school']
        if self.v2.get():
            conditions += ['kis']
        if self.v3.get():
            conditions += ['ebara']
        if self.v4.get():
            conditions += ['rpower']
        if self.v5.get():
            conditions += ['dc']
        if self.v6.get():
            conditions += ['irr']
        if self.v7.get():
            conditions += ['temp']
        if self.v8.get():
            conditions += ['battery']
        if self.v9.get():
            conditions += ['selfCons']
        if self.v10.get():
            conditions += ['ctrl']
        return conditions
    
    def create_name(self):
        return self.name.get()


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
        try:
            app.app(name,conditions)
        except:
            error_flg = True
        if not error_flg:
            messagebox.showinfo('完了', '完了しました。\n内容を確認してください。')
        else:
            ex = traceback.format_exc()
            messagebox.showerror('エラー', '処理中にエラーが発生しました。\n\n'+ex)
   
if __name__=="__main__":
    TkinterClass()