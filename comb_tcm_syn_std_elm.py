import pandas as pd

def comb_tcm_syn_std_elm():
    infile = "/opt/ztang/tcm/comb/dict_tcm_syn_elm_used.xls"
    infile1 = "/opt/ztang/tcm/comb/data_tcm_syn_matrix_1.xls"
    dt = pd.read_excel(infile, sheetname='Sheet1')
    dt1 = pd.read_excel(infile1, sheetname='Sheet3')

    for i in range(len(dt)):
        dt1.set_value(i, "ID", dt["ID"][i])
        dt1.set_value(i, "TCM_SYN_STD_CODE", dt["TCM_SYN_STD_CODE"][i])
        for k in range(len(dt1.columns)):
            if k >= 2:
                dt1.iloc[i][k] = 0
        for j in range(len(dt.columns)):
            if j >= 2:
                tcm_syn_elm_i = dt.iloc[i][j]
                if tcm_syn_elm_i > 0:
                    dt1.iloc[i][tcm_syn_elm_i + 1] = 1
    dt1.to_excel(infile1, sheet_name='Sheet3')

def process_mark(i,len_data):
    n = i + 1
    if n % (0.1 * len_data) == 0:
        print("percent %i" % (n))

def load_data_from_tcm_syn_std_elm(*args):
    infile_base = args[0]  # "/opt/ztang/tcm/comb/data_tcm_syn_std_matrix.xls"
    infile_elm_ext = args[1]  # "/opt/ztang/tcm/comb/ext_data_tcm_syn_std_elm.xls"
    # HID ID PID TCM_SYN_STD_CODE DIAGNOSIS_CODE
    dt_base = pd.read_excel(infile_base, sheetname='base')
    # ID TCM_SYN_STD_CODE TCM_SYN_ELM_CODE1..
    dt_dict_std_elm = pd.read_excel(infile_base, sheetname='dict_tcm_syn_std_elm')
    # PID, TCM_SYN_STD_CODE, TCM_SYN_ELM_CODE1 ...
    dt_elm_ext = pd.read_excel(infile_elm_ext, sheetname='Sheet1')
    return dt_base, dt_dict_std_elm, dt_elm_ext

def tcm_syn_std_elm_ext(*args):
    #load data from dataset args[0]-inputfile and args[1]-outfile
    dt_base, dt_dict_std_elm, dt_elm_ext=load_data_from_tcm_syn_std_elm(args[0],args[1])

    for i in range(len(dt_base)):
        process_mark(i, len(dt_base))
        dt_elm_ext.set_value(i, "PID", dt_base["ID"][i])
        dt_elm_ext.set_value(i, "TCM_SYN_STD_CODE", dt_base["TCM_SYN_STD_CODE"][i])
        for k in range(len(dt_elm_ext.columns)):
            if k >= 2:
                dt_elm_ext.iloc[i][k] = 0
        for j in range(len(dt_dict_std_elm)):
            if dt_dict_std_elm["TCM_SYN_STD_CODE"][j] == dt_base["TCM_SYN_STD_CODE"][i]:
                for k in range(len(dt_dict_std_elm.columns)):
                    if k >= 2:
                        dt_elm_ext.iloc[i][k] = dt_dict_std_elm.iloc[j][k]
    dt_elm_ext.to_excel(args[1], sheet_name='Sheet1')

def tcm_syn_std_elm_ext_process():
    infile = "F:/bigdata/python/ruikang_data_base_1004.xls"
    outfile = "F:/bigdata/python/ext_data_tcm_syn_std_elm_ruikang.xls"
    tcm_syn_std_elm_ext(infile, outfile)

def load_tcm_syn_std_ext_data(*args):
    infile_base = args[0]  # "/opt/ztang/tcm/comb/data_tcm_syn_std_matrix.xls"
    infile_std_ext = args[1]  # "/opt/ztang/tcm/comb/ext_data_tcm_syn_std.xls"
    dt_base = pd.read_excel(infile_base, sheetname='base')  # HID ID PID TCM_SYN_STD_CODE DIAGNOSIS_CODE
    dt_std_ext = pd.read_excel(infile_std_ext, sheetname='Sheet1')  # PID, TCM_SYN_STD_CODE, TCM_SYN_ELM_CODE1 ...
    return dt_base, dt_std_ext


def tcm_syn_std_ext(*args):
    #load data from dataset args[0]-inputfile and args[1]-outfile
    dt_base, dt_std_ext = load_tcm_syn_std_ext_data(args[0],args[1])

    for i in range(len(dt_base)):
        process_mark(i, len(dt_base))
        dt_std_ext.set_value(i, "PID", dt_base["PID"][i])
        dt_std_ext.set_value(i, "TCM_SYN_STD_CODE", dt_base["TCM_SYN_STD_CODE"][i])
        ext_i = dt_base["TCM_SYN_STD_CODE"][i]
        for k in range(len(dt_std_ext.columns)):
            if k >= 2:
                dt_std_ext.iloc[i][k] = 0
                dt_std_ext.iloc[i][ext_i + 1] = 1
    dt_std_ext.to_excel(args[1], sheet_name='Sheet1')

def tcm_syn_std_ext_process():
    infile = "F:/bigdata/python/ruikang_data_base_1004.xls"
    outfile = "F:/bigdata/python/ext_data_tcm_syn_std_ruikang.xls"
    tcm_syn_std_ext(infile, outfile)

if __name__ == '__main__':
    tcm_syn_std_elm_ext_process()
    #tcm_syn_std_ext_process()
