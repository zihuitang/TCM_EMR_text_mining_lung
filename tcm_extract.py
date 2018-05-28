import pandas as pd

def tcm_ext_huashan(): # code for huashan hospital data format extract ...
    infile = "/opt/ztang/tcm/huashan/2017_08_sum_used_bk.csv"
    dt = pd.read_csv(infile)

    TCM_DIAGNOSIS_STR = "PID,TCM_DIAGNOSIS\n"
    tcm_syn_start0_txt = "中医辨证："
    tcm_syn_start1_txt = "证属"
    tcm_syn_end0_txt = "治"
    txt_deleted = ["：", "，", " 。", "“", "” ", "于"]

    for i in range(len(dt)):
        str = "%s" % (dt["FIRST_RECORD"][i])
        start_tcm_syn_pos0 = str.find(tcm_syn_start0_txt) + len(tcm_syn_start0_txt)
        str = str[start_tcm_syn_pos0:]
        start_tcm_syn_pos1 = str.find(tcm_syn_start1_txt) + len(tcm_syn_start1_txt)
        str = str[start_tcm_syn_pos1:]

        if len(str) > 10:
            end_tcm_syn_pos = str.find(tcm_syn_end0_txt)
            str = str[:end_tcm_syn_pos]

            for x in txt_deleted:
                str = str.replace(x, "")

            if len(str) < 10:
                str_cell = "%i,%s" % (dt["PID"][i], str)
                TCM_DIAGNOSIS_STR = TCM_DIAGNOSIS_STR + str_cell + "\n"
            else:
                str_cell = "%i,%s" % (dt["PID"][i], "")
                TCM_DIAGNOSIS_STR = TCM_DIAGNOSIS_STR + str_cell + "\n"

    fs = open("/opt/ztang/tcm/huashan/2017_08_sum_used_bk_tcm_diag.csv", 'w')
    fs.write(TCM_DIAGNOSIS_STR)
    fs.close()


def tcm_extract_changde_tcmh(): #code for changde tcmh data format extract ...
    infile = "/opt/ztang/tcm/changde/changde_1114_case_file_sum.csv"
    dt = pd.read_csv(infile)

    TCM_SYN_STR = "PID,TCM_SYN\n"
    tcm_syn_start0_txt = "为"
    tcm_syn_start1_txt = "属"
    tcm_syn_start2_txt = "是"
    txt_deleted = [" ", "\r", "\n", "。", "，", "“", "”", "：", "于", "证", "症", "征", "型", "像", "象", "的", "喘", "之", "侯"]
    txt_deleted.append("中医")
    txt_deleted.append("表现")
    txt_deleted.append("心悸")
    txt_deleted.append("心痛")
    txt_deleted.append("胸痛")
    txt_deleted.append("咯血")
    txt_deleted.append("咳嗽")
    txt_deleted.append("肺胀")
    txt_deleted.append("感冒")
    txt_deleted.append("眩晕")
    txt_deleted.append("肺癌")
    txt_deleted.append("发热")
    txt_deleted.append("外感")
    txt_deleted.append("吐血")
    txt_deleted.append("中风")
    txt_deleted.append("中经络")

    for i in range(len(dt)):
        str = "%s" % (dt["TCM_BZ"][i])
        str = str[len(str) - 16:]
        str_cell = "%i," % (dt["PID"][i])

        TCM_SYN_STR = TCM_SYN_STR + str_cell
        start_tcm_syn_pos0 = str.rfind(tcm_syn_start0_txt) + len(tcm_syn_start0_txt)
        if start_tcm_syn_pos0 != 0:
            str = str[start_tcm_syn_pos0:]

        start_tcm_syn_pos1 = str.rfind(tcm_syn_start1_txt) + len(tcm_syn_start1_txt)
        if start_tcm_syn_pos1 != 0:
            str = str[start_tcm_syn_pos1:]

        start_tcm_syn_pos2 = str.rfind(tcm_syn_start2_txt) + len(tcm_syn_start2_txt)
        if start_tcm_syn_pos2 != 0:
            str = str[start_tcm_syn_pos2:]

        if len(str) > 0:
            for x in txt_deleted:
                # str=str.strip(x).lstrip(x).rstrip(x)
                str = str.replace(x, "")

            if len(str) < 10:
                str_cell = "%s" % (str)
                TCM_SYN_STR = TCM_SYN_STR + str_cell + "\n"
            else:
                str_cell = "%s" % ("")
                TCM_SYN_STR = TCM_SYN_STR + str_cell + "\n"

    # print(TCM_SYN_STR)
    fs = open("/opt/ztang/tcm/changde/changde_1114_case_file_sum_cmb.csv", 'w')
    fs.write(TCM_SYN_STR)
    fs.close()


def tcm_extract_danyang_tcmh():  #code for danyang tcmh data format extract ...
    infile = "/opt/ztang/tcm/danyang/danyang_tcmh_out.csv"
    dt = pd.read_csv(infile)

    TCM_SYN_STR = "PID,TCM_SYN\n"
    tcm_syn_start0_txt = "【初步诊断】"
    tcm_syn_start1_txt = "中医诊断："
    tcm_syn_txt = " "
    tcm_syn_end0_txt = "西医"
    txt_deleted = ["\r", "\n", "：", "，", " 。", "“", "” ", ".", "证", "症", "病", "肺炎喘嗽", "-", "咯血", " ", "咳嗽", "?", "*"]
    txt_deleted.append("骨断筋伤")

    for i in range(len(dt)):
        str = "%s" % (dt["FIRST_RECORD"][i])
        start_tcm_syn_pos0 = str.find(tcm_syn_start0_txt) + len(tcm_syn_start0_txt)
        str = str[start_tcm_syn_pos0:]
        start_tcm_syn_pos1 = str.find(tcm_syn_start1_txt) + len(tcm_syn_start1_txt)
        str = str[start_tcm_syn_pos1:]

        if 0 < len(str) < 1024:
            end_tcm_syn_pos0 = str.find(tcm_syn_end0_txt)
            str = str[:end_tcm_syn_pos0]
            str = str.strip(' ')
            start_tcm_syn_pos2 = str.find(tcm_syn_txt) + len(tcm_syn_txt)
            str = str[start_tcm_syn_pos2:]

            for x in txt_deleted:
                str = str.replace(x, "")

            if len(str) < 12:
                str_cell = "%i,%s" % (dt["PID"][i], str)
                TCM_SYN_STR = TCM_SYN_STR + str_cell + "\n"
            else:
                str_cell = "%i,%s" % (dt["PID"][i], "")
                TCM_SYN_STR = TCM_SYN_STR + str_cell + "\n"
        else:
            str_cell = "%i,%s" % (dt["PID"][i], "")
            TCM_SYN_STR = TCM_SYN_STR + str_cell + "\n"

    print(TCM_SYN_STR)
    fs = open("/opt/ztang/tcm/danyang/danyang_tcmh_out_syn.csv", 'w')
    fs.write(TCM_SYN_STR)
    fs.close()


#tcm_extract_danyang_tcmh()


