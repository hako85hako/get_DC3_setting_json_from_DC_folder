
from glob import glob
import json
import my_settings

def app(name,conditions,processID):
    skiped = 0
    
    #設定項目
    database = my_settings.database
    dbs = my_settings.dbs
    tables = my_settings.tables
    tables_select_channels = my_settings.tables_select_channels
    programIDs = []

    # targetファイル名の取得
    target_file_name = glob(f'FL*.json')
    #jsonとして読み込み
    json_dict = json.load(open( str(target_file_name[0]) , 'r',encoding="utf-8"))
    tables_select_values = dict()

    if name :
        tables_select_values.setdefault(my_settings.name_key,name)

    #if programIDs :
    tables_select_values.setdefault(my_settings.programIDs_key,programIDs)
    
    if processID :
         tables_select_values.setdefault(my_settings.processID_key,processID)

    if conditions :
        tables_select_values.setdefault(my_settings.conditions_key,conditions)
    
    #[database]以下で取得するチャンネルを指定
    tables_select_values.setdefault(database,{}) 
    for db in dbs:
        tables_select_values[database].setdefault(db,{})
        #[dbs]以下で取得するチャンネルを指定
        for table in tables:
            try:
                #目的のvalueを抽出
                enter_value = json_dict[database][db][table]
                #階層作成
                tables_select_values[database][db].setdefault(table,{})
                #該当の階層に格納
                tables_select_values[database][db][table] = enter_value
            except:
                skiped += 1
            #[tables]以下で取得するチャンネルを指定
            for tables_select_channel in tables_select_channels:
                try:
                    #目的のvalueを抽出
                    enter_value = json_dict[database][db][table][tables_select_channel]
                    #該当の階層に格納
                    tables_select_values[database][db][table].setdefault(tables_select_channel,enter_value)
                except:
                    skiped += 1
    #dbタグ内を書き込み
    with open('new_'+str(target_file_name[0]), mode="w") as f:
        d = json.dumps(tables_select_values)
        f.write(d)
    
    print('飛ばされた処理：'+str(skiped)+'件')

if __name__=="__main__":
    app()