# SURESH SAHU
# 1901CE52
# END_SEM_QUESTION
import pandas as pd
def feedback_not_submitted():
    ltp_mapping_feedback_type = {1: 'lecture', 2: 'tutorial', 3: 'practical'}
    output_file_name = "course_feedback_remaining.xlsx"
    temp_df = pd.read_csv('course_registered_by_all_students.csv')
    temp1_df = pd.read_csv('course_master_dont_open_in_excel.csv')
    temp2_df = pd.read_csv('course_feedback_submitted_by_students.csv')
    temp3_df = pd.read_csv('studentinfo.csv')
    pd.options.mode.chained_assignment = None
    dat3 = temp2_df.groupby(["stud_roll", "course_code"]).size().reset_index(name="row_freq")
    dat3.rename(columns={'stud_roll': 'rollno','course_code': 'subno'}, inplace=True)
    temp1_df.loc[:,['non_zero']] = temp1_df.apply(lambda row: 3-str(row.ltp).count('0'), axis=1)
    dat1 = temp1_df.loc[:,['subno', 'non_zero']]
    dat = temp_df.loc[:,['rollno', 'subno']]
    dat5 = temp3_df.loc[:,['Name', 'Roll No', 'email', 'aemail', 'contact']]
    dat5.rename(columns={'Roll No': 'rollno'}, inplace=True)
    dat4 = temp_df.loc[:,['rollno', 'register_sem', 'schedule_sem', 'subno']]
    res = pd.merge(dat, dat1, on="subno")
    res1 = pd.merge(dat3, res, how='outer',on=["rollno", "subno"])
    res1=res1.fillna(0)
    cond = res1[(res1['non_zero'] <= res1["row_freq"])].index
    res1.drop(cond, inplace=True)
    res2 = pd.merge(res1, dat4, on=["rollno", "subno"])
    res3 = pd.merge(dat5, res2, on=["rollno"])
    res3.drop(['row_freq', 'non_zero'], inplace=True, axis=1)
    res3.to_excel('course_feedback_remaining.xlsx')
feedback_not_submitted()