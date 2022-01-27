#tab.py
#タブを3つ持つGUIウィンドウを作成する。
 
#import
import tkinter as tk
import tkinter.ttk as ttk

import my_settings

def sample():
 
    #メインウィンドウ作成
    main_view = tk.Tk()
 
    #メインウィンドウのタイトルを変更
    main_view.title("Test title")
 
    #メインウィンドウの大きさを設定
    main_view.geometry("1000x500")
 
    #メインウィンドウにnotebookを作成する。
    nb = ttk.Notebook(main_view)
 
    #notebookに関するフレームを3つ作る。
    tab1 = tk.Frame(nb)
    tab2 = tk.Frame(nb)
    tab3 = tk.Frame(nb)
 
    #notebookに対してtab1, 2, 3をそれぞれ追加する。
    nb.add(tab1, text="main", padding=3)
    nb.add(tab2, text="setting", padding=3)
    nb.add(tab3, text="tab3", padding=3)
 
    #メインフレームでのnotebook配置を決定する。
    nb.pack(expand=1, fill="both")
 
    #各タブの内容を記載する。
    tab1_main(tab1)
    tab2_main(tab2)
    tab3_main(tab3)
 
    #main_viewを表示する無限ループ
    main_view.mainloop()
 
    return 0
 
def tab1_main(tab1):
    if my_settings.name_is_valid:
        if my_settings.name_title_is_valid:
            label1 = ttk.Label(tab1, text=my_settings.name_title, padding=(5, 2))
            label1.place(x=10, y=10)
            if my_settings.name_text_1_is_valid:
                label2 = ttk.Label(tab1, text=my_settings.name_text_1, padding=(5, 5))
                label2.place(x=10, y=60)
            if my_settings.name_text_2_is_valid:
                label3 = ttk.Label(tab1, text=my_settings.name_text_2, padding=(5, 5))
                label3.place(x=10, y=80)
        name = tk.StringVar()
        #name.set()
        name = tk.Entry(
            tab1,
            textvariable=name,
            width=40)
        name.place(x=20, y=40)
    
    if my_settings.processID_is_valid:
        if my_settings.processID_title_is_valid:
            label1 = ttk.Label(tab1, text=my_settings.processID_title, padding=(5, 2))
            label1.place(x=10, y=120)
            if my_settings.processID_text_1_is_valid:
                label2 = ttk.Label(tab1, text=my_settings.processID_text_1, padding=(5, 5))
                label2.place(x=10, y=180)
            if my_settings.processID_text_2_is_valid:
                label3 = ttk.Label(tab1, text=my_settings.processID_text_2, padding=(5, 5))
                label3.place(x=10, y=200)
        processID = tk.StringVar()
        #name.set()
        processID = tk.Entry(
            tab1,
            textvariable=processID,
            width=40)
        processID.place(x=20, y=150)
    
    

    return 0
 
def tab2_main(tab2):
    #文字を表示する。
    param_name = tk.Label(tab2, text="タブ2の内容")
    param_name.place(x=10, y=20)
    return 0
 
def tab3_main(tab3):
    #文字を表示する。
    param_name = tk.Label(tab3, text="タブ3の内容")
    param_name.place(x=10, y=30)
    return 0
 
if __name__ == "__main__":
    sample()