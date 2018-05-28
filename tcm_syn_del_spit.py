import pandas as pd

def load_data_base_dict(*args):
    infile_base = args[0]  # "/opt/ztang/tcm/comb/data_tcm_syn_std_matrix.xls"
    infile_dict = args[1]  # "/opt/ztang/tcm/comb/ext_data_tcm_syn_std.xls"
    dt_base = pd.read_excel(infile_base, sheetname='Sheet1')  # HID ID PID TCM_SYN_STD_CODE DIAGNOSIS_CODE
    dt_dict = pd.read_excel(infile_dict, sheetname='Sheet1')  # PID, TCM_SYN_STD_CODE, TCM_SYN_ELM_CODE1 ...
    return dt_base, dt_dict

def process_mark(i,len_data):
    n = i + 1
    if n % int(0.1 * len_data) == 0:
        print("NO:%08i" % (n))

def tcm_syn_spit(*args):
    #load data from dataset args[0]-inputfile and args[1]-outfile
    dt_base, dt_dict = load_data_base_dict(args[0],args[1])
    str_dt1_list = list(dt_dict["TCM_SYN_STD_CODE"])
    TCM_SYN_STR = "PID,TCM_SYN_STD_CODE,TCM_SYN_CODE_TYPE\n"

    for i in range(len(dt_base)):
        str_dt_tcm_syn_code = dt_base["TCM_SYN_STD_CODE"][i]
        str_pid = dt_base["PID"][i]
        str_tcm_syn_code_type = "0"

        for j in range(len(str_dt1_list)):
            if str_dt1_list[j] == str_dt_tcm_syn_code:
                str_tcm_syn_code_type = dt_dict["TCM_SYN_CODE_TYPE"][j]
                break

        str_cell = "%s,%s,%s" % (str_pid, str_dt_tcm_syn_code, str_tcm_syn_code_type)
        TCM_SYN_STR = TCM_SYN_STR + str_cell + "\n"

    with open("F:/bigdata/python/tcm_syn_spit.csv", 'w', encoding='gbk') as f:
        # windows with encoding='gbk' linux encoding='utf-8'
        f.write(TCM_SYN_STR)

def tcm_syn_del(*args):
    #load data from dataset args[0]-inputfile and args[1]-dictfile
    dt_base, dt_dict = load_data_base_dict(args[0],args[1])
    del_list = list(dt_dict["TCM_SYN_CODE_DEL"])
    outfile=args[0]+".out.xls"

    for i in range(len(dt_base)):
        process_mark(i, len(dt_base))
        ext_i = dt_base["TCM_SYN_STD_CODE"][i]
        if ext_i in del_list:
            dt_base.drop(i,inplace=True)

    dt_base.to_excel(outfile, sheet_name='Sheet1', index="PID")

def tcm_syn_del_process():
    infile = "F:/bigdata/python/_ext_matrix_tcm_syn_std_1006_ava.xls"
    dictfile = "F:/bigdata/python/dic_tcm_syn_del.xls"
    infile1="F:/bigdata/python/_ext_matrix_tcm_syn_std_elm_1006_ava.xls"
    tcm_syn_del(infile1, dictfile)

def tcm_syn_spit_process():
    infile = "F:/bigdata/python/_ext_matrix_tcm_syn_std_1006_ava.xls"
    dictfile = "F:/bigdata/python/dic_tcm_syn_spit.xls"
    tcm_syn_spit(infile, dictfile)

if __name__ == '__main__':
    tcm_syn_del_process()
    #tcm_syn_spit_process()