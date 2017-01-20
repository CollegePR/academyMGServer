# -*- coding: cp949 -*-
from academyMGS.models import *
import datetime
import random
import sys
import time
from openpyxl import load_workbook

from academyMGS.models import *

def run(*args):
    cols = ['B', 'C', 'D', 'F', 'G', 'I', 'J', 'N', 'O', 'Q', 'R', 'S', 'T']
    rows = 1
    filename = "./util/db_import/" + args[0]
    wb = load_workbook(filename)
    sheets = wb.get_sheet_names()

    name = ""
    sex = True
    phone_num = ""
    address = ""
    school_name = ""
    grade = 0
    school_class = 0
    status_of_sign = 0
    date_of_admission = datetime.date.today()
    date_of_readdmission = datetime.date.today()
    date_of_exit = datetime.date.today()
    birthday = datetime.date.today()
    academy_class = 0
    admissionData = None
    readdmissionData = None
    exitData = None
    birthdayData = None
    classCount = AcademyClass.objects.count()
    idCheck = []

    rows = 1
    sheet_ranges = wb[sheets[0]]
    maxRow=getMaxRow(sheet_ranges)
    cnt=0
    progress=0
    progress_bar_old=0
    start = time.time()
    while True:
        rows = rows + 1
        check = False
        for col in cols:
            if col == 'B':
                if sheet_ranges[col + str(rows)].value != None:
                    if sheet_ranges[col + str(rows)].value in idCheck:
                        check=True
                        break
                    else:
                        idCheck.append(sheet_ranges[col + str(rows)].value)
            if col == 'C':
                if sheet_ranges[col + str(rows)].value != None:
                    name = sheet_ranges[col + str(rows)].value
                else:
                    name = None
            if col == 'D':
                if sheet_ranges[col + str(rows)].value != None:
                    _sex = ""
                    _sex = sheet_ranges[col + str(rows)].value
                    if _sex == "남자":
                        sex = True
                    if _sex == "여자":
                        sex = False
                else:
                    _sex = True
            if col == 'F':
                if sheet_ranges[col + str(rows)].value != None:
                    _birthday = sheet_ranges[col + str(rows)].value
                    birthdayData = _birthday.strftime('%Y-%m-%d')
                    birthdayData = birthdayData.split('-')
                    birthdayData_year = int(birthdayData[0])
                    birthdayData_month = int(birthdayData[1])
                    birthdayData_day = int(birthdayData[2])
                    birthdayData = datetime.date(birthdayData_year, birthdayData_month, birthdayData_day)
                    birthday = birthdayData
            if col == 'G':
                if sheet_ranges[col + str(rows)].value != None:
                    _phone_num = sheet_ranges[col + str(rows)].value
                else:
                    _phone_num = "010-0000-0000"
            if col == 'I':
                if sheet_ranges[col + str(rows)].value != None:
                    _date_of_admission = sheet_ranges[col + str(rows)].value
                    admissionData = _date_of_admission.strftime('%Y-%m-%d')
                    admissionData = admissionData.split('-')
                    admissionData_year = int(admissionData[0])
                    admissionData_month = int(admissionData[1])
                    admissionData_day = int(admissionData[2])
                    admissionData = datetime.date(admissionData_year, admissionData_month, admissionData_day)
                    date_of_admission = admissionData
            if col == 'J':
                if sheet_ranges[col + str(rows)].value != None:
                    _date_of_exit = sheet_ranges[col + str(rows)].value
                    date_of_exit_d = _date_of_exit.strftime('%Y-%m-%d')
                    date_of_exit_d = date_of_exit_d.split("-")
                    date_of_exit_d_year = int(date_of_exit_d[0])
                    date_of_exit_d_month = int(date_of_exit_d[1])
                    date_of_exit_d_day = int(date_of_exit_d[2])
                    exitData = datetime.date(date_of_exit_d_year, date_of_exit_d_month,
                                             date_of_exit_d_day)
                    date_of_exit = exitData
            if col == 'N':
                if sheet_ranges[col + str(rows)].value != None:
                    address = sheet_ranges[col + str(rows)].value
                else:
                    address = "청와대"
            if col == 'O':
                if sheet_ranges[col + str(rows)].value != None:
                    _status_of_sign = sheet_ranges[col + str(rows)].value
                    if _status_of_sign == "수강자":
                        status_of_sign = 1
                    if _status_of_sign == "미수강자":
                        status_of_sign = 3
                    if date_of_exit is not None:
                        status_of_sign = 2
                else:
                    _status_of_sign = 3
            if col == 'Q':
                if sheet_ranges[col + str(rows)].value != None:
                    school_name = sheet_ranges[col + str(rows)].value
                else:
                    school_name = "군대"
            if col == 'R':
                if sheet_ranges[col + str(rows)].value != None:
                    grade = sheet_ranges[col + str(rows)].value
                else:
                    grade = 100
            if col == 'S':
                if sheet_ranges[col + str(rows)].value != None:
                    school_class = sheet_ranges[col + str(rows)].value
                else:
                    school_class = 1
            if col == 'T':
                if sheet_ranges[col + str(rows)].value != None:
                    _date_of_readdmission = sheet_ranges[col + str(rows)].value
                    readdmissionData = _date_of_readdmission.strftime('%Y-%m-%d')
                    readdmissionData = readdmissionData.split("-")
                    readdmissionData_year = int(readdmissionData[0])
                    readdmissionData_month = int(readdmissionData[1])
                    readdmissionData_day = int(readdmissionData[2])
                    readdmissionData = datetime.date(readdmissionData_year, readdmissionData_month,
                                                     readdmissionData_day)
                    date_of_readdmission = readdmissionData

        if (rows-2 == maxRow):
            progress=100
            progress_bar_old=20
            os.system("cls")
            for i in range(0, progress_bar_old):
                sys.stdout.write("■")
            for i in range(0, 20 - progress_bar_old):
                sys.stdout.write("□")
            print()
            print(str(progress)+"%")
            break
        academy_class = random.randint(1, classCount)
        student = Student(
            name=name,
            sex=sex,
            phone_num=phone_num,
            address=address,
            school_name=school_name,
            school_class=school_class,
            grade=grade,
            status_of_sign=status_of_sign,
            date_of_admission=admissionData,
            date_of_readdmission=readdmissionData,
            date_of_exit=exitData,
            birthday=birthdayData,
            acdemy_class=academy_class,
            image=None,
        )
        if(check==False):
            student.save()
            cnt=cnt+1

        if progress_bar_old != int((rows-2) / maxRow*20):
            if(progress_bar_old<=20):
                progress_bar_old = int((rows-2) / maxRow * 20)

        if progress_bar_old != int((rows-2) / maxRow * 100):
            if(progress<=100):
                progress = int((rows-2) / maxRow * 100)
                os.system("cls")
                for i in range(0, progress_bar_old):
                    sys.stdout.write("■")
                for i in range(0, 20 - progress_bar_old):
                    sys.stdout.write("□")
                print()
                now = time.time()
                print(str(rows-2)+" / "+str(maxRow)+"  db에 넣는데 오래걸리니 잠시 화장실에 다녀오셔도 좋습니다. ")
                print("예상 소요시간 : "+str(int((now-start)*(100-progress)))+"초 ")
                print("진행도 : "+str(progress)+"%")
                start=now
    print("file rows = "+str(maxRow)+" insert rows = " + str(cnt)+" skipped rows = "+str(maxRow-cnt))


def getMaxRow(sheet_ranges):
    rows=0
    while True:
        rows = rows + 1
        if sheet_ranges['A' + str(rows)].value == None:
            break
    return rows-2