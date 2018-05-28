
import pandas as pd

def load_data_from_tcm_syn_std_code(*args):
    infile = args[0] # "F:/bigdata/python/ruikang_tcm_2_code_0930.xls"
    infile1 = args[1] # "F:/bigdata/python/dict_tcm_syn_std_2_code_0930.xls"
    dt = pd.read_excel(infile, sheetname='Sheet1')
    dt1 = pd.read_excel(infile1, sheetname='Sheet1')
    return dt, dt1

def tcm_syn_std_code(*args):
    # load data from dataset args[0]=infile and args[1]=outfile
    dt, dt1 = load_data_from_tcm_syn_std_code(args[0],args[1])
    TCM_SYN_STR = "PID,TCM_SYN,TCM_SYN_STD,TCM_SYN_CODE\n"
    str_dt1_list = list(dt1["TCM_SYN"])

    for i in range(len(dt)):
        str_dt_tcm_syn = "%s" % (dt["TCM_SYN"][i])
        str_pid = dt["PID"][i]
        str_tcm_syn_code = "0"
        str_tcm_syn_std = "0"

        for j in range(len(str_dt1_list)):
            if str_dt1_list[j] == str_dt_tcm_syn:
                str_tcm_syn_code = dt1["TCM_SYN_CODE"][j]
                str_tcm_syn_std = dt1["TCM_SYN_STD"][j]
                break
        str_cell = "%s,%s,%s,%s" % (str_pid, str_dt_tcm_syn, str_tcm_syn_std, str_tcm_syn_code)
        TCM_SYN_STR = TCM_SYN_STR + str_cell + "\n"

    with open("F:/bigdata/python/comb_tcmh_out_syn.csv", 'w', encoding='gbk') as f:
        # windows with encoding='gbk' linux encoding='utf-8'
        f.write(TCM_SYN_STR)

if __name__ == '__main__':
    infile = "F:/bigdata/python/ruikang_tcm_2_code_0930.xls"
    infile1 = "F:/bigdata/python/dict_tcm_syn_std_2_code_0930.xls"
    tcm_syn_std_code(infile, infile1)

