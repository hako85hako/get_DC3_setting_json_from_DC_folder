import tkinter as tk
import tkinter.ttk as ttk
import sqlite3
from tkinter import messagebox
from tkinter import filedialog as tkFileDialog
from pathlib import Path
import sys

import my_settings


def db_connect():
     # データベースに接続または作成
    dbname = "config.db"
    connection = sqlite3.connect(dbname)
    return connection

def db_cursor(connection):
    c = connection.cursor()
    return c

def db_disconnect(c):
    c.close()

def db_save(connection):
    connection.commit()

def db_delete():
    try:
        connection = db_connect()
        c = db_cursor(connection)
        c.execute(
            f"""DROP TABLE IF EXISTS json_key"""
        )
        db_save(connection)
    except Exception as e:
        print("例外args:", e.args)
    finally:
        db_disconnect(c)
#未使用
def get_targets_for_next_version():
    targets = []
    try:
        connection = db_connect()
        c = db_cursor(connection)
        #json_key
        c.execute(
            f"""CREATE TABLE IF NOT EXISTS json_key(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                level_0 text,
                level_1 text,
                level_2 text,
                level_3 text,
                level_4 text,
                level_5 text,
                level_6 text,
                level_7 text,
                level_8 text,
                level_9 text
            )"""
        )
        if not c.fetchone():
            default_values = my_settings.targets
            c.executemany(
                f"""INSERT INTO json_key (
                    level_0,
                    level_1,
                    level_2,
                    level_3,
                    level_4,
                    level_5,
                    level_6,
                    level_7,
                    level_8,
                    level_9
                ) 
                values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", default_values)
        #conditions_v_valueの取り出し
        #print( c.execute("select * from json_key"))
        for columns in c.execute(f"""SELECT * FROM json_key"""):
            targets += [columns]
            #空白を弾く↓必要なら
            # count = 0
            # for column in columns:
            #     if column == '':
            #         count += 1
            # columns = columns[0:(10-count)] 
        db_save(connection)
    except Exception as e:
        print("例外args:", e.args)

    finally:
        db_disconnect(c)
    return targets

def get_targets():
    targets = []
    try:
        connection = db_connect()
        c = db_cursor(connection)
        #json_key
        c.execute(
            f"""CREATE TABLE IF NOT EXISTS json_key(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                level_0 text,
                level_1 text,
                level_2 text,
                level_3 text,
                level_4 text,
                level_5 text,
                level_6 text,
                level_7 text,
                level_8 text,
                level_9 text
            )"""
        )
        if not c.fetchone():
            default_values = my_settings.targets
            c.executemany(
                f"""INSERT INTO json_key (
                    level_0,
                    level_1,
                    level_2,
                    level_3,
                    level_4,
                    level_5,
                    level_6,
                    level_7,
                    level_8,
                    level_9
                ) 
                values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", default_values)
        #conditions_v_valueの取り出し
        #print( c.execute("select * from json_key"))
        for columns in c.execute(f"""SELECT level_0,level_1,level_2,level_3,level_4,level_5,level_6,level_7,level_8,level_9 FROM json_key"""):
            targets += [columns]
            #空白を弾く↓必要なら
            # count = 0
            # for column in columns:
            #     if column == '':
            #         count += 1
            # columns = columns[0:(10-count)] 
        db_save(connection)
    except Exception as e:
        print("例外args:", e.args)

    finally:
        db_disconnect(c)
    return targets

def get_titles():
    columns = []
    try:
        connection = db_connect()
        c = db_cursor(connection)
        #title_config
        c.execute('CREATE TABLE IF NOT EXISTS title_config(main_title,name_title,processID_title,conditions_title)')
        c.execute('SELECT * FROM title_config')
        if not c.fetchone():
            inserts_title = [
            (   my_settings.main_title,
                my_settings.name_title,
                my_settings.processID_title,
                my_settings.conditions_title    )
            ]
            c.executemany('INSERT INTO title_config values(?, ?, ?, ?)', inserts_title)
        #title取り出し
        for columns in c.execute('SELECT * FROM title_config'):
            main_title = columns[0]
            name_title = columns[1]
            processID_title = columns[2]
            conditions_title = columns[3]
    except Exception as e:
        print("例外args:", e.args)

    finally:
        db_disconnect(c)
    return columns

def get_valids():
    columns = []
    try:
        connection = db_connect()
        c = db_cursor(connection)
        #valid_config
        c.execute(
            f"""CREATE TABLE IF NOT EXISTS valid_config(
                name_is_valid,
                name_title_is_valid,
                name_text_1_is_valid,
                name_text_2_is_valid,
                processID_is_valid,
                processID_title_is_valid,
                processID_text_1_is_valid,
                processID_text_2_is_valid,
                condition_is_valid,
                condition_title_is_valid,
                conditions_text_1_is_valid,
                conditions_text_2_is_valid
            )"""
        )
        c.execute('SELECT * FROM valid_config')
        if not c.fetchone():
            inserts_valid = [(True,True,True,True,True,True,True,True,True,True,True,True)]
            c.executemany('INSERT INTO valid_config values(?,?,?,?,?,?,?,?,?,?,?,?)', inserts_valid)
        #valid取り出し
        for columns in c.execute('SELECT * FROM valid_config'):
            name_is_valid = columns[0]
            name_title_is_valid = columns[1]
            name_text_1_is_valid = columns[2]
            name_text_2_is_valid = columns[3]
            processID_is_valid = columns[4]
            processID_title_is_valid = columns[5]
            processID_text_1_is_valid = columns[6]
            processID_text_2_is_valid = columns[7]
            condition_is_valid = columns[8]
            condition_title_is_valid = columns[9]
            conditions_text_1_is_valid = columns[10]
            conditions_text_2_is_valid = columns[11]
    except Exception as e:
        print("例外args:", e.args)

    finally:
        db_disconnect(c)
    return columns

def get_texts():
    columns = []
    try:
        connection = db_connect()
        c = db_cursor(connection)

        c.execute('CREATE TABLE IF NOT EXISTS text_config(name_text_1,name_text_2,processID_text_1,processID_text_2,conditions_text_1,conditions_text_2)')
        c.execute('SELECT * FROM text_config')
        if not c.fetchone():
            inserts_text = [
            (   my_settings.name_text_1,
                my_settings.name_text_2,
                my_settings.processID_text_1,
                my_settings.processID_text_2,
                my_settings.conditions_text_1,
                my_settings.conditions_text_2   )
            ]
            c.executemany('INSERT INTO text_config values(?, ?, ?, ?, ?, ?)', inserts_text)
        #text取り出し
        for columns in c.execute('SELECT * FROM text_config'):
            name_text_1 = columns[0]
            name_text_2 = columns[1]
            processID_text_1 = columns[2]
            processID_text_2 = columns[3]
            conditions_text_1 = columns[4]
            conditions_text_2 = columns[5]
    except Exception as e:
        print("例外args:", e.args)

    finally:
        db_disconnect(c)
    return columns

def registrar_targets(targets):
    try:
        # データベースに接続または作成
        connection = db_connect()
        c = db_cursor(connection)
        #json_keyc = db_cu
        c.execute(
            'UPDATE json_key SET level_0=?,level_1=?,level_2=?,level_3=?,level_4=?,level_5=?,level_6=?,level_7=?,level_8=?,level_9=? where ID = ?',
            (
                targets[1],
                targets[2],
                targets[3],
                targets[4],
                targets[5],
                targets[6],
                targets[7],
                targets[8],
                targets[9],
                targets[10],
                targets[0]
            )
        )
        print(c.execute("select * from json_key"))
        db_save(connection)
    except Exception as e:
        print("例外args:", e.args)

    finally:
        db_disconnect(c)
    return targets

# def config():
#     try:
#         connection = db_connect()
#         #title_config
#         c.execute('CREATE TABLE IF NOT EXISTS title_config(main_title,name_title,processID_title,conditions_title)')
#         c.execute('SELECT * FROM title_config')
#         if not c.fetchone():
#             inserts_title = [
#             (   my_settings.main_title,
#                 my_settings.name_title,
#                 my_settings.processID_title,
#                 my_settings.conditions_title    )
#             ]
#             c.executemany('INSERT INTO title_config values(?, ?, ?, ?)', inserts_title)
#         #title取り出し
#         for columns in c.execute('SELECT * FROM title_config'):
#             main_title = columns[0]
#             name_title = columns[1]
#             processID_title = columns[2]
#             conditions_title = columns[3]


#         #valid_config
#         c.execute('CREATE TABLE IF NOT EXISTS valid_config('+
#             'name_is_valid,'+
#             'name_title_is_valid,'+
#             'name_text_1_is_valid,'+
#             'name_text_2_is_valid,'+
#             'processID_is_valid,'+
#             'processID_title_is_valid,'+
#             'processID_text_1_is_valid,'+
#             'processID_text_2_is_valid,'+
#             'condition_is_valid,'+
#             'condition_title_is_valid,'+
#             'conditions_text_1_is_valid,'+
#             'conditions_text_2_is_valid)'
#             )
#         c.execute('SELECT * FROM valid_config')
#         if not c.fetchone():
#             inserts_valid = [(True,True,True,True,True,True,True,True,True,True,True,True)]
#             c.executemany('INSERT INTO valid_config values(?,?,?,?,?,?,?,?,?,?,?,?)', inserts_valid)
#         #valid取り出し
#         for columns in c.execute('SELECT * FROM valid_config'):
#             name_is_valid = columns[0]
#             name_title_is_valid = columns[1]
#             name_text_1_is_valid = columns[2]
#             name_text_2_is_valid = columns[3]
#             processID_is_valid = columns[4]
#             processID_title_is_valid = columns[5]
#             processID_text_1_is_valid = columns[6]
#             processID_text_2_is_valid = columns[7]
#             condition_is_valid = columns[8]
#             condition_title_is_valid = columns[9]
#             conditions_text_1_is_valid = columns[10]
#             conditions_text_2_is_valid = columns[11]
        
#         #text_config
#         c.execute('CREATE TABLE IF NOT EXISTS text_config(name_text_1,name_text_2,processID_text_1,processID_text_2,conditions_text_1,conditions_text_2)')
#         c.execute('SELECT * FROM text_config')
#         if not c.fetchone():
#             inserts_text = [
#             (   my_settings.name_text_1,
#                 my_settings.name_text_2,
#                 my_settings.processID_text_1,
#                 my_settings.processID_text_2,
#                 my_settings.conditions_text_1,
#                 my_settings.conditions_text_2   )
#             ]
#             c.executemany('INSERT INTO text_config values(?, ?, ?, ?, ?, ?)', inserts_text)
#         #text取り出し
#         for columns in c.execute('SELECT * FROM text_config'):
#             name_text_1 = columns[0]
#             name_text_2 = columns[1]
#             processID_text_1 = columns[2]
#             processID_text_2 = columns[3]
#             conditions_text_1 = columns[4]
#             conditions_text_2 = columns[5]
        
#         #conditions_v_valid_config
#         c.execute('CREATE TABLE IF NOT EXISTS conditions_v_valid_config('+
#         'conditions_v1_is_valid,conditions_v2_is_valid,'+
#         'conditions_v3_is_valid,conditions_v4_is_valid,'+
#         'conditions_v5_is_valid,conditions_v6_is_valid,'+
#         'conditions_v7_is_valid,conditions_v8_is_valid,'+
#         'conditions_v9_is_valid,conditions_v10_is_valid)')
#         c.execute('SELECT * FROM conditions_v_valid_config')
#         if not c.fetchone():
#             inserts_conditions_v_valid = [(True,True,True,True,True,True,True,True,True,True)]
#             c.executemany('INSERT INTO conditions_v_valid_config values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', inserts_conditions_v_valid)
#         #conditions_v_valid取り出し
#         for columns in c.execute('SELECT * FROM conditions_v_valid_config'):
#             conditions_v1_is_valid = columns[0]
#             conditions_v2_is_valid = columns[1]
#             conditions_v3_is_valid = columns[2]
#             conditions_v4_is_valid = columns[3]
#             conditions_v5_is_valid = columns[4]
#             conditions_v6_is_valid = columns[5]
#             conditions_v7_is_valid = columns[6]
#             conditions_v8_is_valid = columns[7]
#             conditions_v9_is_valid = columns[8]
#             conditions_v10_is_valid = columns[9]

#         #conditions_v_value_config
#         c.execute('CREATE TABLE IF NOT EXISTS conditions_v_value_config('+
#         'conditions_v1_value,conditions_v2_value,'+
#         'conditions_v3_value,conditions_v4_value,'+
#         'conditions_v5_value,conditions_v6_value,'+
#         'conditions_v7_value,conditions_v8_value,'+
#         'conditions_v9_value,conditions_v10_value)')
#         c.execute('SELECT * FROM conditions_v_value_config')
#         if not c.fetchone():
#             inserts_conditions_v_value = [
#                 (   my_settings.conditions_v1_value,my_settings.conditions_v2_value,
#                     my_settings.conditions_v3_value,my_settings.conditions_v4_value,
#                     my_settings.conditions_v5_value,my_settings.conditions_v6_value,
#                     my_settings.conditions_v7_value,my_settings.conditions_v8_value,
#                     my_settings.conditions_v9_value,my_settings.conditions_v10_value   )
#                 ]
#             c.executemany('INSERT INTO conditions_v_value_config values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', inserts_conditions_v_value)
#         #conditions_v_valueの取り出し
#         for columns in c.execute('SELECT * FROM conditions_v_value_config'):
#             conditions_v1_value = columns[0]
#             conditions_v2_value = columns[1]
#             conditions_v3_value = columns[2]
#             conditions_v4_value = columns[3]
#             conditions_v5_value = columns[4]
#             conditions_v6_value = columns[5]
#             conditions_v7_value = columns[6]
#             conditions_v8_value = columns[7]
#             conditions_v9_value = columns[8]
#             conditions_v10_value = columns[9]
   
#         #json_key
#         #最終的には好きなところのタグを取り出せるようにする
#         c.execute(
#             f"""CREATE TABLE IF NOT EXISTS json_key(
#                 ID INTEGER PRIMARY KEY AUTOINCREMENT,
#                 level_0 text,
#                 level_1 text,
#                 level_2 text,
#                 level_3 text,
#                 level_4 text,
#                 level_5 text,
#                 level_6 text,
#                 level_7 text,
#                 level_8 text,
#                 level_9 text
#             )"""
#         )
#         c.execute('SELECT * FROM json_key')
#         if not c.fetchone():
#             default_values = my_settings.targets
#             c.executemany('INSERT INTO json_key(level_0,level_1,level_2,level_3,level_4,level_5,level_6,level_7,level_8,level_9) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', default_values)
#         #conditions_v_valueの取り出し
#         for columns in c.execute('SELECT (level_0,level_1,level_2,level_3,level_4,level_5,level_6,level_7,level_8,level_9) FROM json_key'):
#             targets += [columns]
#             #空白を弾く↓必要なら
#             # count = 0
#             # for column in columns:
#             #     if column == '':
#             #         count += 1
#             # columns = columns[0:(10-count)] 
#     except Exception as e:
#         print("例外args:", e.args)

#     finally:
#         db_disconnect(c)

### 直接起動時の内容 ###
# ----------------------------------------------
if __name__ == '__main__':
    config()