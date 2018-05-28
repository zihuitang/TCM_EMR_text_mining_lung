import pandas as pd
import numpy as np
import scipy.stats as stas
import scipy.optimize as opt

def is_disease_set_value(*args):
    dt.set_value(args[0], "IS_DISEASE", args[1])
    dt.set_value(args[0], "HYPERTENSION_HISTORY", args[1])
    dt.set_value(args[0], "DIABETES_HISTORY", args[1])
    dt.set_value(args[0], "CHD_HISTORY", args[1])
    dt.set_value(args[0], "COPD_HISTORY", args[1])
    dt.set_value(args[0], "CANCER_HISTORY", args[1])
    dt.set_value(args[0], "STROKE_HISTORY", args[1])
    dt.set_value(args[0], "MENTAL_DISEASE_HISTORY", args[1])
    dt.set_value(args[0], "TUBERCULOSIS_HISTORY", args[1])
    dt.set_value(args[0], "HEPATITIS_HISTORY", args[1])
    dt.set_value(args[0], "INFECTIONS_HISTORY", args[1])
    dt.set_value(args[0], "OCCUPATIONAL_HISTORY", args[1])
    dt.set_value(args[0], "OTHER_DISEASE_HISTORY", args[1])


infile="/opt/ztang/demographical_info_test.csv"
dt=pd.read_csv(infile)

i=0
for i in range(len(dt)):
    str="%s"%(dt["DISEASE_HISTORY"][i])
    num_disease = 0

    if str.find("1") == 0 and len(str)==1:
        is_disease_set_value(i,0)
        dt.set_value(i,"NUMBER_DISEASE",0)
    if str.find("2")>=0:
        if str.find("2") == 0:
            dt.set_value(i, "HYPERTENSION_HISTORY", 1)
            dt.set_value(i, "IS_DISEASE", 1)
            num_disease += 1
            dt.set_value(i, "NUMBER_DISEASE", num_disease)
        elif str[str.find("2") - 1] == ",":
            dt.set_value(i, "HYPERTENSION_HISTORY", 1)
            dt.set_value(i, "IS_DISEASE", 1)
            num_disease += 1
            dt.set_value(i, "NUMBER_DISEASE", num_disease)
    if str.find("3") >= 0:
        if str.find("3") == 0:
            dt.set_value(i, "DIABETES_HISTORY", 1)
            dt.set_value(i, "IS_DISEASE", 1)
            num_disease += 1
            dt.set_value(i, "NUMBER_DISEASE", num_disease)
        elif str[str.find("3") - 1] == ",":
            dt.set_value(i, "DIABETES_HISTORY", 1)
            dt.set_value(i, "IS_DISEASE", 1)
            num_disease += 1
            dt.set_value(i, "NUMBER_DISEASE", num_disease)
    if str.find("4")>=0:
        dt.set_value(i, "CHD_HISTORY", 1)
        dt.set_value(i, "IS_DISEASE", 1)
        num_disease += 1
        dt.set_value(i, "NUMBER_DISEASE", num_disease)
    if str.find("5")>=0:
        dt.set_value(i, "COPD_HISTORY", 1)
        dt.set_value(i, "IS_DISEASE", 1)
        num_disease += 1
        dt.set_value(i, "NUMBER_DISEASE", num_disease)
    if str.find("6")>=0:
        dt.set_value(i, "CANCER_HISTORY", 1)
        dt.set_value(i, "IS_DISEASE", 1)
        num_disease += 1
        dt.set_value(i, "NUMBER_DISEASE", num_disease)
    if str.find("7")>=0:
        dt.set_value(i, "STROKE_HISTORY", 1)
        dt.set_value(i, "IS_DISEASE", 1)
        num_disease += 1
        dt.set_value(i, "NUMBER_DISEASE", num_disease)
    if str.find("8")>=0:
        dt.set_value(i, "MENTAL_DISEASE_HISTORY", 1)
        dt.set_value(i, "IS_DISEASE", 1)
        num_disease += 1
        dt.set_value(i, "NUMBER_DISEASE", num_disease)
    if str.find("9")>=0:
        dt.set_value(i, "TUBERCULOSIS_HISTORY", 1)
        dt.set_value(i, "IS_DISEASE", 1)
        num_disease += 1
        dt.set_value(i, "NUMBER_DISEASE", num_disease)
    if str.find("10")>=0:
        dt.set_value(i, "HEPATITIS_HISTORY", 1)
        dt.set_value(i, "IS_DISEASE", 1)
        num_disease += 1
        dt.set_value(i, "NUMBER_DISEASE", num_disease)
    if str.find("11")>=0:
        dt.set_value(i, "INFECTIONS_HISTORY", 1)
        dt.set_value(i, "IS_DISEASE", 1)
        num_disease += 1
        dt.set_value(i, "NUMBER_DISEASE", num_disease)
    if str.find("12")>=0:
        dt.set_value(i, "OCCUPATIONAL_HISTORY", 1)
        dt.set_value(i, "IS_DISEASE", 1)
        num_disease += 1
        dt.set_value(i, "NUMBER_DISEASE", num_disease)
    if str.find("13")>=0:
        dt.set_value(i, "OTHER_DISEASE_HISTORY", 1)
        dt.set_value(i, "IS_DISEASE", 1)
        num_disease += 1
        dt.set_value(i, "NUMBER_DISEASE", num_disease)
    i += 1

dt.to_csv(infile)