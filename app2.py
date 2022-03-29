
from glob import glob
import json
import my_settings
import my_config

def app2(name,conditions,processID,targets):
    skiped = 0
    
    #設定項目
    #lkey_1 = my_settings.database
    #dbs = my_settings.dbs
    #tables = my_settings.tables
    #tables_select_channels = my_settings.tables_select_channels
    programIDs = []

    # targetファイル名の取得
    target_file_name = glob(f'FL*.json')
    #jsonとして読み込み
    json_dict = json.load(open( str(target_file_name[0]) , 'r',encoding="utf-8"))
    #json_dict = json.load(open( str(target_file_name[0]) , 'r'))

    #json作成
    json_create = dict()

    if name :
        json_create.setdefault(my_settings.name_key,name)

    #if programIDs :
    json_create.setdefault(my_settings.programIDs_key,programIDs)
    
    if processID :
         json_create.setdefault(my_settings.processID_key,processID)

    if conditions :
        json_create.setdefault(my_settings.conditions_key,conditions)
    
    
    for target in targets:
        #変数格納用
        #level = []
        rank = target_get(target)
        #print(rank)

        #第1階層で取得するチャンネルを指定
        json_create.setdefault(target[0],{})
        # 各Levelが存在しない場合は作成
        if rank >= 0 :
            if not target[0] in json_create:
                json_create.setdefault(target[0],{})
        if rank >= 1 :
            if not target[1] in json_create[target[0]]:
                json_create[target[0]].setdefault(target[1],{})
        if rank >= 2 :
            if not target[2] in json_create[target[0]][target[1]]:
                json_create[target[0]][target[1]].setdefault(target[2],{})
        if rank >= 3 :
            if not target[3] in json_create[target[0]][target[1]][target[2]]:
                json_create[target[0]][target[1]][target[2]].setdefault(target[3],{})
        if rank >= 4 :
            if not target[4] in json_create[target[0]][target[1]][target[2]][target[3]]:
                json_create[target[0]][target[1]][target[2]][target[3]].setdefault(target[4],{})
        if rank >= 5 :
            if not target[5] in json_create[target[0]][target[1]][target[2]][target[3]][target[4]]:
                json_create[target[0]][target[1]][target[2]][target[3]][target[4]].setdefault(target[5],{})
        if rank >= 6 :
            if not target[6] in json_create[target[0]][target[1]][target[2]][target[3]][target[4]][target[5]]:
                json_create[target[0]][target[1]][target[2]][target[3]][target[4]][target[5]].setdefault(target[6],{})
        if rank >= 7 :
            if not target[7] in json_create[target[0]][target[1]][target[2]][target[3]][target[4]][target[5]][target[6]]:
                json_create[target[0]][target[1]][target[2]][target[3]][target[4]][target[5]][target[6]].setdefault(target[7],{})
        if rank >= 8 :
            if not target[8] in json_create[target[0]][target[1]][target[2]][target[3]][target[4]][target[5]][target[6]][target[7]]:
                json_create[target[0]][target[1]][target[2]][target[3]][target[4]][target[5]][target[6]][target[7]].setdefault(target[8],{})
        if rank >= 9 :
            if not target[9] in json_create[target[0]][target[1]][target[2]][target[3]][target[4]][target[5]][target[6]][target[7]][target[8]]:
                json_create[target[0]][target[1]][target[2]][target[3]][target[4]][target[5]][target[6]][target[7]][target[8]].setdefault(target[9],{})
        try:
            if rank == 0 :
                json_create[target[0]] = json_dict[target[0]]
            if rank == 1 :
                json_create[target[0]][target[1]] = json_dict[target[0]][target[1]]
            if rank == 2 :
                json_create[target[0]][target[1]][target[2]] = json_dict[target[0]][target[1]][target[2]]
            if rank == 3 :
                json_create[target[0]][target[1]][target[2]][target[3]] = json_dict[target[0]][target[1]][target[2]][target[3]]
            if rank == 4 :
                json_create[target[0]][target[1]][target[2]][target[3]][target[4]] = json_dict[target[0]][target[1]][target[2]][target[3]][target[4]]
            if rank == 5 :
                json_create[target[0]][target[1]][target[2]][target[3]][target[4]][target[5]] = json_dict[target[0]][target[1]][target[2]][target[3]][target[4]][target[5]]
            if rank == 6 :
                json_create[target[0]][target[1]][target[2]][target[3]][target[4]][target[5]][target[6]] = json_dict[target[0]][target[1]][target[2]][target[3]][target[4]][target[5]][target[6]]
            if rank == 7 :
                json_create[target[0]][target[1]][target[2]][target[3]][target[4]][target[5]][target[6]][target[7]] = json_dict[target[0]][target[1]][target[2]][target[3]][target[4]][target[5]][target[6]][target[7]]
            if rank == 8 :
                json_create[target[0]][target[1]][target[2]][target[3]][target[4]][target[5]][target[6]][target[7]][target[8]] = json_dict[target[0]][target[1]][target[2]][target[3]][target[4]][target[5]][target[6]][target[7]][target[8]]
            if rank == 9 :
                json_create[target[0]][target[1]][target[2]][target[3]][target[4]][target[5]][target[6]][target[7]][target[8]][target[9]] = json_dict[target[0]][target[1]][target[2]][target[3]][target[4]][target[5]][target[6]][target[7]][target[8]][target[9]]
        except KeyError:
            KeyError_value = 'null'
            if rank == 0 :
                json_create[target[0]] = KeyError_value
            if rank == 1 :
                json_create[target[0]][target[1]] = KeyError_value
            if rank == 2 :
                json_create[target[0]][target[1]][target[2]] = KeyError_value
            if rank == 3 :
                json_create[target[0]][target[1]][target[2]][target[3]] = KeyError_value
            if rank == 4 :
                json_create[target[0]][target[1]][target[2]][target[3]][target[4]] = KeyError_value
            if rank == 5 :
                json_create[target[0]][target[1]][target[2]][target[3]][target[4]][target[5]] = KeyError_value
            if rank == 6 :
                json_create[target[0]][target[1]][target[2]][target[3]][target[4]][target[5]][target[6]] =KeyError_value
            if rank == 7 :
                json_create[target[0]][target[1]][target[2]][target[3]][target[4]][target[5]][target[6]][target[7]] = KeyError_value
            if rank == 8 :
                json_create[target[0]][target[1]][target[2]][target[3]][target[4]][target[5]][target[6]][target[7]][target[8]] = KeyError_value
            if rank == 9 :
                json_create[target[0]][target[1]][target[2]][target[3]][target[4]][target[5]][target[6]][target[7]][target[8]][target[9]] =KeyError_value
        except Exception as e:
            print("例外args:", e.args)


    # # dbタグ内を書き込み
    with open('new_'+str(target_file_name[0]), mode="w", encoding='utf-8') as f:
    # with open('test', mode="w") as f:
        d = json.dumps(json_create,indent=2,ensure_ascii=False)
        f.write(d)
    # print('飛ばされた処理：'+str(skiped)+'件')

def target_get(target):
    rank = -1
    for target_value in target:
        if not target_value == '':
            rank += 1
        else :
            return rank
    return rank


if __name__=="__main__":
    print('app2を試験する場合は、メイン呼び出し以下をコメントアウト解除')
    # name = 'test'
    # conditions = ['school']
    # processID = 'test'
    # targets = config.config()
    # test(name,conditions,processID,targets)



