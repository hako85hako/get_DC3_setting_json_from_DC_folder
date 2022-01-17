
from glob import glob
import json

def app():
    error = 0
    database = 'database'
    dbs = {
        'datadb':[
            'filename',
            'index',
            {'tables':[
                'tbl_conf_alert_icon_group',
                'tbl_conf_board',
                'tbl_conf_disp_background',
                'tbl_conf_disp_data',
                'tbl_conf_disp_graph_axis',
                'tbl_conf_disp_graph_axis_item',
                'tbl_conf_disp_icon',
                'tbl_conf_disp_monitor',
                'tbl_conf_disp_pr_monitor',
                'tbl_conf_disp_pr_monitor_icon',
                'tbl_conf_disp_report',
                'tbl_conf_formula',
                'tbl_conf_prmode',
                'tbl_conf_target'
                ]
            }
        ]
    }
if __name__=="__main__":
    app()