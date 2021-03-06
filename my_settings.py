

# DB初期値書き込み
# json設定 ############################################################################
# jsonのkey名
database = 'database'
conditions_key = 'conditions'
name_key = 'name'
processID_key = 'processID'
programIDs_key = 'programIDs'

targets = [
    ('database','masterdb','filename','','','','','','',''),
    ('database','masterdb','index','','','','','','',''),
    ('database','masterdb','tables','tbl_conf','','','','','',''),
    ('database','masterdb','tables','tbl_conf_alert_icon_group','','','','','',''),
    ('database','masterdb','tables','tbl_conf_board','','','','','',''),
    ('database','masterdb','tables','tbl_conf_disp_background','','','','','',''),
    ('database','masterdb','tables','tbl_conf_disp_data','','','','','',''),
    ('database','masterdb','tables','tbl_conf_disp_graph_axis','','','','','',''),
    ('database','masterdb','tables','tbl_conf_disp_graph_axis_item','','','','','',''),
    ('database','masterdb','tables','tbl_conf_disp_icon','','','','','',''),
    ('database','masterdb','tables','tbl_conf_disp_monitor','','','','','',''),
    ('database','masterdb','tables','tbl_conf_disp_pr_monitor','','','','','',''),
    ('database','masterdb','tables','tbl_conf_disp_pr_monitor_icon','','','','','',''),
    ('database','masterdb','tables','tbl_conf_disp_report','','','','','',''),
    ('database','masterdb','tables','tbl_conf_formula','','','','','',''),
    ('database','masterdb','tables','tbl_conf_prmode','','','','','',''),
    ('database','masterdb','tables','tbl_conf_target','','','','','',''),
]




# 表示設定 ############################################################################
# タイトル
main_title = 'get_DC3_setting_json'

#案件名入力フォーム
name_is_valid = True
#title
name_title_is_valid = True
name_title = '〇 nameの設定'
#text
name_text_1_is_valid = True
name_text_1 = 'この名前がツールに選択肢として表示される'
name_text_2_is_valid = True
name_text_2 = 'exp)荏原 BMU20 1系統 日射・気温なし　蓄電池あり'

#プロセスID入力フォーム
processID_is_valid = True
#title
processID_title_is_valid = True
processID_title = '〇 processIDの設定'
#text
processID_text_1_is_valid = True
processID_text_1 = 'このビューモデル設定jsonファイルに対応するプロセスIDを指定する'
processID_text_2_is_valid = True
processID_text_2 = 'exp)ebara_BMU20_s1'


#コンディションの選択フォーム
condition_is_valid = True
#title
condition_title_is_valid = True
conditions_title = '〇 conditionsの設定'
#text
conditions_text_1_is_valid = False
conditions_text_1 = ''
conditions_text_2_is_valid = False
conditions_text_2 = ''


#v1
conditions_v1_is_valid = True
conditions_v1_text = "school：大人版の場合は設定しない"
conditions_v1_value = "school"
#v2
conditions_v2_is_valid = True
conditions_v2_text = "kis：大人版の場合は設定しない"
conditions_v2_value = "kis"
#v3
conditions_v3_is_valid = True
conditions_v3_text = "ebara：荏原版の場合"
conditions_v3_value = "ebara"
#v4
conditions_v4_is_valid = True
conditions_v4_text = "rpower：受電電力がある場合"
conditions_v4_value = "rpower"
#v5
conditions_v5_is_valid = True
conditions_v5_text = "dc：直流がある場合"
conditions_v5_value = "dc"
#v6
conditions_v6_is_valid = True
conditions_v6_text = "irr：日射がある場合"
conditions_v6_value = "irr"
#v7
conditions_v7_is_valid = True
conditions_v7_text = "temp：気温がある場合"
conditions_v7_value = "temp"
#v8
conditions_v8_is_valid = True
conditions_v8_text = "battery：蓄電池がある場合"
conditions_v8_value = "battery"
#v9
conditions_v9_is_valid = True
conditions_v9_text = "selfCons：自家消費の場"
conditions_v9_value = "selfCons"
#v10
conditions_v10_is_valid = True
conditions_v10_text = "ctrl：制御の場合"
conditions_v10_value = "ctrl"

