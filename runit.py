# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 22:17:35 2021

@author: CLY
"""
import pymysql
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import pandas as pd
import numpy as np
from pymysql import NULL, cursors
import com_talents
import tkinter.font as tkFont
from tkinter import *  # 图形界面库
import tkinter.messagebox as messagebox  # 弹窗
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class StartPage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('公司-人才信息管理系统')
        self.window.geometry('400x470')  # 这里的乘是小x

        label = tk.Label(self.window, text="公司-人才信息管理系统",
                         font=("华光胖头鱼_CNKI", 20))
        label.pack(pady=100)  # pady=100 界面的长度

        tk.Button(self.window, text="公司登录", font=tkFont.Font(family="华光胖头鱼_CNKI", size=16), command=lambda: ComPage(self.window), width=40,
                  fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        tk.Button(self.window, text="人才登录", font=tkFont.Font(family="华光胖头鱼_CNKI", size=16), command=lambda: StudentPage(self.window), width=40,
                  fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        tk.Button(self.window, text="注册", font=tkFont.Font(family="华光胖头鱼_CNKI", size=16), command=lambda: RegistPage(self.window), width=40,
                  fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        tk.Button(self.window, text="关于", font=tkFont.Font(family="华光胖头鱼_CNKI", size=16), command=lambda: AboutPage(self.window), width=40,
                  fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        tk.Button(self.window, text='退出系统', font=tkFont.Font(family="华光胖头鱼_CNKI", size=16), width=40, command=self.window.destroy,
                  fg='white', bg='gray', activebackground='black', activeforeground='white').pack()

        self.window.mainloop()  # 主消息循环

# 公司登陆页面


class ComPage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('公司登录页面')
        self.window.geometry('400x450')  # 这里的乘是小x

        label = tk.Label(self.window, text='公司登录', bg='lightblue',
                         font=('华光胖头鱼_CNKI', 20), width=30, height=2)
        label.pack()

        tk.Label(self.window, text='公司编号：',
                 font=tkFont.Font(family="华光胖头鱼_CNKI", size=14)).pack(pady=25)
        self.com_username = tk.Entry(
            self.window, width=30, font=tkFont.Font(family="华光胖头鱼_CNKI", size=14), bg='Ivory')
        self.com_username.pack()

        tk.Label(self.window, text='公司密码：',
                 font=tkFont.Font(family="华光胖头鱼_CNKI", size=14)).pack(pady=25)
        self.com_pass = tk.Entry(
            self.window, width=30, font=tkFont.Font(family="华光胖头鱼_CNKI", size=14), bg='Ivory', show='*')
        self.com_pass.pack()

        tk.Button(self.window, text="登录", width=8, font=tkFont.Font(family="华光胖头鱼_CNKI",
                                                                    size=12), command=self.login).pack(pady=40)
        tk.Button(self.window, text="返回首页", width=8,
                  font=tkFont.Font(family="华光胖头鱼_CNKI", size=12), command=self.back).pack()

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def login(self):
        print(str(self.com_username.get()))
        print(str(self.com_pass.get()))
        com_pass = None

        # 数据库操作 查询管理员表
        db = pymysql.connect(host="localhost", port=3306,
                             user="root", passwd="1234", db="talents")  # 打开数据库连接
        # SQL 查询语句
        sql = "SELECT * FROM companyinfo WHERE ID = '%s'" % (
            self.com_username.get())
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                com_id = row[0]
                com_pass = row[3]
            # 打印结果
                print("admin_id=%s,admin_pass=%s" % (com_id, com_pass))
        except:
            print("Error: unable to fecth data")
            messagebox.showinfo('警告！', '用户名或密码不正确！')
        cursor.close()
        db.close()  # 关闭数据库连接

        print("正在登陆公司管理界面")
        print("self", self.com_pass.get())
        print("local", com_pass)

        if self.com_pass.get() == com_pass:
            ComManage(self.window, com_id)  # 进入公司操作界面
        else:
            messagebox.showinfo('警告！', '用户名或密码不正确！')

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口


# 学生登陆页面
class StudentPage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('人才登陆')
        self.window.geometry('400x600')  # 这里的乘是小x

        label = tk.Label(self.window, text='人才登陆', bg='lightblue',
                         font=('华光胖头鱼_CNKI', 20), width=30, height=2)
        label.pack()

        Label(self.window, text='账号：', font=tkFont.Font(
            family="华光胖头鱼_CNKI", size=14)).pack(pady=25)
        self.student_id = tk.Entry(
            self.window, width=30, font=tkFont.Font(family="华光胖头鱼_CNKI", size=14), bg='Ivory')
        self.student_id.pack()

        Label(self.window, text='姓名：', font=tkFont.Font(
            family="华光胖头鱼_CNKI", size=14)).pack(pady=25)
        self.student_name = tk.Entry(
            self.window, width=30, font=tkFont.Font(family="华光胖头鱼_CNKI", size=14), bg='Ivory')
        self.student_name.pack()

        Label(self.window, text='密码：', font=tkFont.Font(
            family="华光胖头鱼_CNKI", size=14)).pack(pady=25)
        self.student_pass = tk.Entry(
            self.window, width=30, font=tkFont.Font(family="华光胖头鱼_CNKI", size=14), bg='Ivory', show='*')
        self.student_pass.pack()

        Button(self.window, text="登录", width=8, font=tkFont.Font(family="华光胖头鱼_CNKI",
                                                                 size=12), command=self.login).pack(pady=40)
        Button(self.window, text="返回首页", width=8,
               font=tkFont.Font(family="华光胖头鱼_CNKI", size=12), command=self.back).pack()

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def login(self):
        print(str(self.student_id.get()))
        print(str(self.student_name.get()))
        print(str(self.student_pass.get()))
        stu_pass = None

        # 数据库操作 查询管理员表
        db = pymysql.connect(host="localhost", port=3306,
                             user="root", passwd="1234", db="talents")  # 打开数据库连接
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        # SQL 查询语句
        sql = "SELECT * FROM talentsinfo WHERE ID = '%s'" % (
            self.student_id.get())
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                stu_id = row[0]
                stu_name = row[1]
                stu_pass = row[5]
                # 打印结果
                print("stu_id=%s,stu_name=%s,stu_pass=%s" %
                      (stu_id, stu_name, stu_pass))
        except:
            print("Error: unable to fecth data")
            messagebox.showinfo('警告！', '用户名或密码不正确！')
        cursor.close()
        db.close()  # 关闭数据库连接

        print("正在登陆人才信息查看界面")
        print("self", self.student_pass.get())
        print("local", stu_pass)

        if self.student_name.get() == stu_name:

            if self.student_pass.get() == stu_pass:
                StudentView(self.window, self.student_id.get())  # 进入学生信息查看界面
            else:
                messagebox.showinfo('警告！', '用户名或密码不正确！')
        else:
            messagebox.showinfo('警告！', '姓名与账号不匹配！')

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口


# 公司操作界面
class ComManage:
    def __init__(self, parent_window, id):
        parent_window.destroy()  # 销毁主界面

        self.com_id = id

        self.window = Tk()  # 初始框的声明
        self.window.title('公司操作界面')

        self.frame_left_top = tk.Frame(width=300, height=200)
        self.frame_right_top = tk.Frame(width=200, height=200)
        self.frame_center = tk.Frame(width=900, height=400)
        self.frame_bottom = tk.Frame(width=950, height=50)

        # 定义下方中心列表区域
        self.columns = ("人才编号", "姓名", "入职公司编号", "公司名",
                        "入行年份", "最高学历", "学校名", "专业名")
        self.tree = ttk.Treeview(
            self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(
            self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 表格的标题
        self.tree.column("人才编号", width=80, anchor='center')  # 表示列,不显示
        self.tree.column("姓名", width=100, anchor='center')
        self.tree.column("入职公司编号", width=80, anchor='center')
        self.tree.column("公司名", width=130, anchor='center')
        self.tree.column("入行年份", width=80, anchor='center')
        self.tree.column("最高学历", width=80, anchor='center')
        self.tree.column("学校名", width=150, anchor='center')
        self.tree.column("专业名", width=150, anchor='center')

        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        # 打开数据库连接
        sql = "SELECT `人才编号`, `姓名`, `入职公司编号`,`公司名`,`入行年份`,`最高学历`,`学校名`,`专业名` FROM view_talents GROUP BY `人才编号`"  # SQL 查询语句
        talents = com_talents.SysInfo("")
        try:
            re = talents.loadInfo(sql)
            if (re != 1):
                print(re)
            talents_data = talents.showdata

            self.taid = talents_data["人才编号"]
            self.taname = talents_data["姓名"]
            self.comid = talents_data["入职公司编号"]
            self.comname = talents_data["公司名"]
            self.entrytime = talents_data["入行年份"]
            self.topgrade = talents_data["最高学历"]
            self.college = talents_data["学校名"]
            self.major = talents_data["专业名"]

        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')

        print("test***********************")
        for i in range(min(len(self.taid), len(self.taname), len(self.comid), len(self.comname), len(self.entrytime), len(self.topgrade), len(self.college), len(self.major))):  # 写入数据
            self.tree.insert('', i, values=(
                self.taid[i], self.taname[i], self.comid[i], self.comname[i], self.entrytime[i], self.topgrade[i], self.college[i], self.major[i]))

        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col,
                              command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 定义顶部区域
        # 定义左上方区域
        self.top_title = Label(self.frame_left_top,
                               text="人才信息维护:", font=('华光胖头鱼_CNKI', 20))
        self.top_title.grid(row=0, column=0, columnspan=2,
                            sticky=NSEW, padx=50, pady=10)

        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_taid = StringVar()  # 声明人才编号
        self.var_name = StringVar()  # 声明姓名
        self.var_year = StringVar()  # 声明入行年份
        self.var_comid = StringVar()  # 声明入职公司编号

        # 人才编号
        self.right_top_id_label = Label(
            self.frame_left_top, text="人才编号：", font=('华光胖头鱼_CNKI', 15))
        self.right_top_id_entry = Entry(
            self.frame_left_top, textvariable=self.var_taid, font=('华光胖头鱼_CNKI', 15))
        self.right_top_id_label.grid(row=1, column=0)  # 位置设置
        self.right_top_id_entry.grid(row=1, column=1)
        # 姓名
        self.right_top_name_label = Label(
            self.frame_left_top, text="姓名：", font=('华光胖头鱼_CNKI', 15))
        self.right_top_name_entry = Entry(
            self.frame_left_top, textvariable=self.var_name, font=('华光胖头鱼_CNKI', 15))
        self.right_top_name_label.grid(row=2, column=0)  # 位置设置
        self.right_top_name_entry.grid(row=2, column=1)
        # 入行年份
        self.right_top_gender_label = Label(
            self.frame_left_top, text="入行年份：", font=('华光胖头鱼_CNKI', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_year,
                                            font=('华光胖头鱼_CNKI', 15))
        self.right_top_gender_label.grid(row=3, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=3, column=1)
        # 入职公司
        self.right_top_gender_label = Label(
            self.frame_left_top, text="入职公司：", font=('华光胖头鱼_CNKI', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_comid,
                                            font=('华光胖头鱼_CNKI', 15))
        self.right_top_gender_label.grid(row=4, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=4, column=1)

        # 定义右上方区域
        self.right_top_title = Label(
            self.frame_right_top, text="操作：", font=('华光胖头鱼_CNKI', 20))

        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(
            self.frame_right_top, text='查询&分析', width=20, command=self.new_find)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新选中人才信息', width=20,
                                            command=self.updata_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除选中人才信息', width=20,
                                            command=self.del_row)

        # 位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=3, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=4, column=0, padx=20, pady=10)

        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.frame_left_top.tkraise()  # 开始显示主菜单
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口

    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 列
        self.row = self.tree.identify_row(event.y)  # 行

        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        self.var_taid.set(self.row_info[0])
        self.var_name.set(self.row_info[1])
        self.var_year.set(self.row_info[4])
        self.var_comid.set(self.row_info[2])
        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_taid,
                                        font=('华光胖头鱼_CNKI', 15))

        print('')

    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(
            tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

    def new_find(self):
        CalPage(self.com_id)

    def updata_row(self):
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res == True:
            if self.var_taid.get() == self.row_info[0]:  # 如果所填学号 与 所选学号一致
                # 打开数据库连接
                db = pymysql.connect(
                    host="localhost", port=3306, user="root", passwd="1234", db="talents")
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql = "UPDATE talentsinfo SET Name = '%s', EntryTime = '%s', CompanyID = '%s' \
                 WHERE ID = '%s'" % (self.var_name.get(), self.var_year.get(), self.var_comid.get(), self.var_taid.get())  # SQL 插入语句
                try:
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                    messagebox.showinfo('提示！', '更新成功！')
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '更新失败，数据库连接失败！')
                cursor.close()
                db.close()  # 关闭数据库连接

                id_index = self.taid[self.taid.values == self.row_info[0]].index.tolist()[
                    0]
                self.taname[id_index] = self.var_name.get()
                self.entrytime[id_index] = self.var_year.get()
                self.comid[id_index] = self.var_comid.get()

                self.tree.item(self.tree.selection()[0], values=(
                    self.var_taid.get(), self.var_name.get(
                    ), self.var_comid.get(), self.comname[id_index],
                    self.var_year[id_index], self.topgrade[id_index], self.college[id_index]))  # 修改对于行信息
            else:
                messagebox.showinfo('警告！', '不能修改学生学号！')

    def del_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
        if res == True:
            print(self.row_info[0])  # 鼠标选中的学号
            print(self.tree.selection()[0])  # 行号
            print(self.tree.get_children())  # 所有行
            de = com_talents.SysInfo("")
            re = de.deleteData(1, self.row_info[0])
            if re != 1:
                print(re)
                messagebox.showinfo('警告！', '删除失败，数据库连接失败！')
            else:
                messagebox.showinfo('提示！', '删除成功！')

            id_index = self.taid[self.taid.values == self.row_info[0]].index.tolist()[
                0]
            print(id_index)
            del self.taid[id_index]
            del self.taname[id_index]
            del self.entrytime[id_index]
            del self.comname[id_index]
            del self.comid[id_index]
            del self.topgrade[id_index]
            del self.college[id_index]

            print(self.taid)
            self.tree.delete(self.tree.selection()[0])  # 删除所选行
            print(self.tree.get_children())


# 图表分析页面(公司)
class VisualPage():
    def __init__(self, id):
        self.com_id = id
        self.window = Tk()  # 初始框的声明
        self.window.title('图表分析页面')
        self.window.geometry('900x550')  # 这里的乘是小x

        IDLabel = tk.Label(self.window, text='要查询的公司编号：',
                           font=tkFont.Font(family="华光胖头鱼_CNKI", size=14))
        IDLabel.grid(row=0, column=1)
        self.IDEntry = tk.Entry(self.window, fg="blue")
        self.IDEntry.grid(row=0, column=2)

        Button(self.window, text="公司员工学历分析", width=16, font=tkFont.Font(family="华光胖头鱼_CNKI",
                                                                        size=12), command=self.comdata).grid(row=0, column=3)
        Label(self.window, text='所有公司-->',
              font=tkFont.Font(family="华光胖头鱼_CNKI", size=14)).grid(row=0, column=5)
        Button(self.window, text="历年员工学历分析", width=16, font=tkFont.Font(family="华光胖头鱼_CNKI",
                                                                        size=12), command=self.education).grid(row=0, column=6)

        self.window.mainloop()

    def comdata(self):

        plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体，便于显示中文
        self.window.resizable(False, False)

        matplotlib.use('TkAgg')

        if self.IDEntry.get() != '':
            val = self.IDEntry.get()
        else:
            val = self.com_id
        # 获取数据，存储过程
        cd = com_talents.SysInfo("")
        sql = "CALL proc_comedu('%s')" % (val)
        re = cd.loadInfo(sql)
        if re != 1:
            print(re)
        df1 = cd.showdata

        pie = plt.figure(figsize=(3, 3), facecolor="#F0F0F0")
        xdata = df1["人数"]
        plt.pie(xdata, labels=tuple(df1["education"]), colors=None,
                autopct='%1.1f%%', pctdistance=0.6, shadow=True,
                labeldistance=1.1, startangle=90,
                radius=None, counterclock=True, wedgeprops=None,
                textprops={'fontsize': 12, 'color': 'k'}, center=(0, 0), frame=False)
        plt.title('该公司员工学历占比')
        canvas_statis = FigureCanvasTkAgg(pie, self.window)
        canvas_statis.get_tk_widget().place(x=50, y=70)  # 根据坐标，放在指主窗口的指定位置

    # 对年份的学历情况分析
    def education(self):
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体，便于显示中文
        self.window.resizable(False, False)

        matplotlib.use('TkAgg')
        # 获取数据，存储过程
        ed = com_talents.SysInfo("")
        sql = "CALL proc_totaledu()"
        re = ed.loadInfo(sql)
        if re != 1:
            print(re)
        df6 = ed.showdata

        df6_new = df6.fillna({'本科': 0, '硕士': 0, '博士': 0})

        pie = plt.figure(figsize=(3.6, 5), facecolor="#F0F0F0")

        # 一共有多少个x轴类别
        a = df6_new['EntryTime'].values.tolist()
        b = np.array(df6_new['本科'].values.tolist())
        c = np.array(df6_new['硕士'].values.tolist())
        d = np.array(df6_new['博士'].values.tolist())
        x_14 = list(range(len(a)))
        plt.bar(x_14, b, bottom=None, label='本科')
        plt.bar(x_14, c, bottom=b,  label='硕士')
        plt.bar(x_14, d, bottom=b+c, label='博士')
        plt.ylim(0, 12)
        plt.xlabel('入行年份')
        plt.ylabel('人数')
        plt.title('学历情况')
        plt.xticks(x_14, a, rotation=45)
        plt.legend()

        canvas_statis = FigureCanvasTkAgg(pie, self.window)
        canvas_statis.get_tk_widget().place(x=440, y=50)  # 根据坐标，放在指主窗口的指定位置


# 统计计算、查询界面,公司
class CalPage():
    def __init__(self, id):
        self.com_id = id
        self.root = tk.Tk()
        # 给窗口可视化写名字
        self.root.title("查询&分析")
        # 设定窗口的大小
        self.root.geometry('960x300')
        # 获取数据，存储过程
        co = com_talents.SysInfo("")
        sql = "CALL proc_talents()"
        re = co.loadInfo(sql)
        if re != 1:
            print(re)
        data = co.showdata
        col_list = data.columns.tolist()

        # 表格
        tree = ttk.Treeview(self.root, show="headings")
        tree.pack()
        # 定义列
        tree["columns"] = tuple(col_list)
        # 设置列属性，列不显示
        for i in col_list:
            tree.column(i, width=120)

        # 设置表头
        for j in col_list:
            tree.heading(j, text=j)

        # 添加数据
        y = 0
        for n in range(data.shape[0]):
            ls = []
            for k in range(len(data.iloc[n, ])):
                s = str(data.iloc[n, k])
                ls.append(s)
            ls_tuple = tuple(ls)
            tree.insert("", y, text=str(y+1)+".", values=ls_tuple)
            y += 1

        menubar = tk.Menu(self.root)

        # 创建“文件”菜单项及其子菜单
        file = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="基础", menu=file)
        file.add_command(label="人才信息查询", command=self.selectMenu)
        file.add_command(label="学历信息查询", command=self.eduMenu)
        file.add_command(label="专业模糊查询", command=self.fuzzyMenu)
        file.add_separator()
        file.add_command(label="退出", command=self.root.destroy)

        # 创建“分析”菜单项及其子菜单
        edit = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="统计分析", menu=edit)
        edit.add_command(label="数据", command=self.showAll)
        edit.add_command(label="描述统计", command=self.describeData)
        edit.add_command(label="分组统计", command=self.groupData)
        edit.add_command(label="相关性分析", command=self.corrData)
        edit.add_command(label="图表分析", command=self.visualData)

        self.root.config(menu=menubar)

        # 主窗口循环显示
        self.root.mainloop()

    # 显示表格的通用，在同一页面
    def showTree(self, root_show, data, col_list):
        #root_show = tk.Toplevel()
        # 给窗口可视化写名字
        # root_show.title("展示信息")
        # 表格
        tree = ttk.Treeview(root_show, show="headings")
        tree.pack()
        # 定义列
        tree["columns"] = tuple(col_list)
        # 设置列属性，列不显示
        for i in col_list:
            tree.column(i, width=80, anchor='center')

        # 设置表头
        for j in col_list:
            tree.heading(j, text=j)

        # 添加数据
        y = 0
        for n in range(data.shape[0]):
            ls = []
            for k in range(len(data.iloc[n, ])):
                s = str(data.iloc[n, k])
                ls.append(s)
            ls_tuple = tuple(ls)
            tree.insert("", y, text=str(y+1)+".", values=ls_tuple)
            y += 1
        # root_show.mainloop()

        # 显示表格的通用,另起一个页面
    def showTree2(self, data, col_list):
        root_show = tk.Toplevel()
        # 给窗口可视化写名字
        root_show.title("展示信息")
        # 表格
        tree = ttk.Treeview(root_show, show="headings")
        tree.pack()
        # 定义列
        tree["columns"] = tuple(col_list)
        # 设置列属性，列不显示
        for i in col_list:
            tree.column(i, width=80, anchor='center')

        # 设置表头
        for j in col_list:
            tree.heading(j, text=j)

        # 添加数据
        y = 0
        for n in range(data.shape[0]):
            ls = []
            for k in range(len(data.iloc[n, ])):
                s = str(data.iloc[n, k])
                ls.append(s)
            ls_tuple = tuple(ls)
            tree.insert("", y, text=str(y+1)+".", values=ls_tuple)
            y += 1
        root_show.mainloop()

    # 查询
    # 定义菜单单击函数，显示人才信息查询按钮

    def selectMenu(self):
        self.root_check = tk.Toplevel()
        self.root_check.title("查询信息")
        # 定义按钮单击函数,显示查询信息

        def checkBtClick():
            ID = IDEntry.get()
            print(type(ID))

            # 连接数据库查询，存储过程
            cc = com_talents.SysInfo("")
            sql = "CALL proc_selecttalents('%s')" % (ID)
            re = cc.loadInfo(sql)
            if re != 1:
                print(re)
                tkinter.messagebox.showerror('error', '暂无信息！')
            else:
                var_data = cc.showdata

            col_list = var_data.columns.tolist()
            self.showTree(self.root_check, var_data, col_list)

        # 在根窗口内创建学号label和Entry
        userLabel = tk.Label(
            self.root_check, text='人才编号：', font=("华光胖头鱼_CNKI", 16))
        userLabel.pack()
        IDEntry = tk.Entry(self.root_check, fg="blue")
        IDEntry.pack()
        # 在根窗口内创建按钮
        checkButton = tk.Button(
            self.root_check, text="查询", font=("华光胖头鱼_CNKI", 16), command=checkBtClick)
        checkButton.pack()

        self.root_check.mainloop()

    # 定义菜单 学历信息查询

    def eduMenu(self):
        self.root_check = tk.Toplevel()
        self.root_check.title("学历查询信息")
        # 定义按钮单击函数,显示查询信息

        def checkBtClick():
            ID = IDEntry.get()
            print(type(ID))
            # 连接数据库查询，存储过程
            cc = com_talents.SysInfo("")
            sql = "CALL proc_selectedu('%s')" % (ID)
            re = cc.loadInfo(sql)
            if re != 1:
                print(re)
                tkinter.messagebox.showerror('error', '暂无信息！')
            cda = cc.showdata

            col = cda.columns.tolist()
            self.showTree(self.root_check, cda, col)

        # 在根窗口内创建学号label和Entry
        userLabel = tk.Label(
            self.root_check, text='人才编号：', font=("华光胖头鱼_CNKI", 16))
        userLabel.pack()
        IDEntry = tk.Entry(self.root_check, fg="blue")
        IDEntry.pack()
        # 在根窗口内创建按钮
        checkButton = tk.Button(
            self.root_check, text="查询", font=("华光胖头鱼_CNKI", 16), command=checkBtClick)
        checkButton.pack()

        self.root_check.mainloop()

    # 定义菜单单击函数，显示模糊查询按钮

    def fuzzyMenu(self):
        self.root_check = tk.Toplevel()
        self.root_check.title("模糊查询信息")

        def checkBtClick2():
            entry = '%'+majorEntry.get()+'%'
            print(type(entry))
            # 连接数据库查询，视图
            con = pymysql.connect(
                host="localhost", port=3306, user="root", passwd="1234", db="talents")
            sql2 = "SELECT `人才编号`, `姓名`, `入职公司编号`,`公司名`,`入行年份`,`最高学历`,`学校名`,`专业名` FROM view_talents WHERE `专业名` LIKE %s"
            try:
                majord = pd.read_sql(sql=sql2, con=con, params={
                                     entry}, coerce_float=True)
                print(majord)
            except:
                tkinter.messagebox.showerror('error', '暂无信息！')
            con.close()

            col_list = majord.columns.tolist()
            self.showTree(self.root_check, majord, col_list)

        # 模糊查询
        majorLabel = tk.Label(
            self.root_check, text='专业名：', font=("华光胖头鱼_CNKI", 16))
        majorLabel.pack()
        majorEntry = tk.Entry(self.root_check, fg="blue")
        majorEntry.pack()
        # 在根窗口内创建按钮
        majorButton = tk.Button(
            self.root_check, text="模糊查询", font=("华光胖头鱼_CNKI", 16), command=checkBtClick2)
        majorButton.pack()

        self.root_check.mainloop()

    # 展示统计分析的数据
    def showAll(self):
        self.root_check = tk.Toplevel()
        self.root_check.title("显示所有信息")

        sa = com_talents.SysInfo("")
        sql = "SELECT companyinfo.`Name` 公司名,Top_grade 最高学历,domestic 学校是否国内,\
            statistic 专业是否统计,employee_num 入职员工数 FROM talentsinfo JOIN companyinfo ON companyinfo.ID = talentsinfo.CompanyID \
                JOIN background ON background.talentsID = talentsinfo.ID JOIN college ON college.ID = background.collegeID \
                    JOIN major ON major.ID = background.majorID"
        try:
            re = sa.loadInfo(sql)
            if (re != 1):
                print(re)
            ana_data = sa.showdata
        except:
            tkinter.messagebox.showerror('error', '暂无数据！')
        col_list = ana_data.columns.tolist()
        self.showTree(self.root_check, ana_data, col_list)
        self.root_check.mainloop()

    # 菜单描述统计函数
    def describeData(self):
        self.root_describe = tk.Toplevel()
        self.root_describe.title("描述统计")
        aLabel = tk.Label(self.root_describe, text="请选择以下某几项进行描述性统计分析",
                          font=("华光胖头鱼_CNKI", 14), fg="blue")
        aLabel.grid(row=1, column=1, sticky=tk.W)
        # 获取数据
        sa = com_talents.SysInfo("")
        sql = "SELECT companyinfo.`Name` 公司名,Top_grade 最高学历,domestic 学校是否国内,\
            statistic 专业是否统计,employee_num 入职员工数 FROM talentsinfo JOIN companyinfo ON companyinfo.ID = talentsinfo.CompanyID \
                JOIN background ON background.talentsID = talentsinfo.ID JOIN college ON college.ID = background.collegeID \
                    JOIN major ON major.ID = background.majorID"
        try:
            re = sa.loadInfo(sql)
            if (re != 1):
                print(re)

        except:
            tkinter.messagebox.showerror('error', '暂无数据！')

        # checkButton，复选按钮
        cv1 = tk.IntVar()
        cv2 = tk.IntVar()
        cv3 = tk.IntVar()
        cv4 = tk.IntVar()
        tk.Checkbutton(self.root_describe, text="最高学历", font=("华光胖头鱼_CNKI", 12), variable=cv1,
                       onvalue=1).grid(row=2, column=1, sticky=tk.W)
        tk.Checkbutton(self.root_describe, text="学校是否国内", font=("华光胖头鱼_CNKI", 12), variable=cv2,
                       onvalue=2).grid(row=2, column=2, sticky=tk.W)
        tk.Checkbutton(self.root_describe, text="专业是否统计", font=("华光胖头鱼_CNKI", 12), variable=cv3,
                       onvalue=3).grid(row=3, column=1, sticky=tk.W)
        tk.Checkbutton(self.root_describe, text="入职员工数", font=("华光胖头鱼_CNKI", 12), variable=cv4,
                       onvalue=4).grid(row=3, column=2, sticky=tk.W)

        # 按钮，可展示
        showButton = tk.Button(
            self.root_describe, text=" 确定 ", font=("华光胖头鱼_CNKI", 14))
        showButton.grid(row=4, column=2)

        def showDes(event):
            list1 = ['最高学历', '学校是否国内', '专业是否统计', '入职员工数']
            des_list = []
            if cv1.get() == 1:
                des_list.append(list1[cv1.get()-1])
            if cv2.get() == 2:
                des_list.append(list1[cv2.get()-1])
            if cv3.get() == 3:
                des_list.append(list1[cv3.get()-1])
            if cv4.get() == 4:
                des_list.append(list1[cv4.get()-1])
            sd_res = sa.dataDescribe(des_list)
            # print(sd_res)
            indexList = sd_res.index.tolist()
            # print(indexList)
            df = pd.DataFrame(pd.Series(indexList), columns=['数字特征'])
            # print(df)
            sd_res.index = df.index
            df2 = pd.concat([df, sd_res], axis=1)
            # print(df2)
            df2_list = df2.columns.tolist()
            self.showTree2(df2, df2_list)
        # 按钮绑定事件
        showButton.bind("<Button-1>", showDes)

        self.root_describe.mainloop()

    # 菜单分组统计分析函数

    def groupData(self):
        self.root_group = tk.Toplevel()
        # 给窗口可视化写名字
        self.root_group.title("分组统计")
        mLabel = tk.Label(self.root_group, text="请选择均值或中值进行分组统计分析",
                          font=("华光胖头鱼_CNKI", 14), fg="blue")
        mLabel.grid(row=1, column=1, sticky=tk.W)
        # 获取数据
        sa = com_talents.SysInfo("")
        sql = "SELECT companyinfo.`Name` 公司名,Top_grade 最高学历,domestic 学校是否国内,\
            statistic 专业是否统计,employee_num 入职员工数 FROM talentsinfo JOIN companyinfo ON companyinfo.ID = talentsinfo.CompanyID \
                JOIN background ON background.talentsID = talentsinfo.ID JOIN college ON college.ID = background.collegeID \
                    JOIN major ON major.ID = background.majorID"
        try:
            re = sa.loadInfo(sql)
            if (re != 1):
                print(re)

        except:
            tkinter.messagebox.showerror('error', '暂无数据！')

        # radioButton，单选按钮
        rv = tk.IntVar()  # 设置选项值变量
        rv.set(1)  # 设置缺省选项值
        tk.Radiobutton(self.root_group, text="均值(mean)", font=("华光胖头鱼_CNKI", 12), variable=rv, value=1).grid(
            row=2, column=1, columnspan=2, sticky=tk.W)
        tk.Radiobutton(self.root_group, text="中值(median)", font=("华光胖头鱼_CNKI", 12), variable=rv, value=2).grid(
            row=2, column=2, columnspan=2, sticky=tk.W)

        # 按钮，可展示
        showGroupButton = tk.Button(
            self.root_group, text=" 确定 ", font=("华光胖头鱼_CNKI", 14))
        showGroupButton.grid(row=6, column=2)

        def showGroup(event):
            if rv.get() == 1:
                m_num = 1
            else:
                m_num = 2
            sd_res = sa.dataGroup(m_num)

            # 创建新dataframe
            indexList2 = sd_res.index.tolist()
            dfa = pd.DataFrame(pd.Series(indexList2), columns=['公司名'])
            sd_res.index = dfa.index
            # 合并
            df_c = pd.concat([dfa, sd_res], axis=1)
            new_groupList = df_c.columns.tolist()
            self.showTree2(df_c, new_groupList)
        # 按钮绑定事件
        showGroupButton.bind("<Button-1>", showGroup)

        self.root_group.mainloop()

    # 菜单相关性分析函数
    def corrData(self):
        self.root_corr = tk.Toplevel()
        self.root_corr.title("相关性分析")
        aLabel = tk.Label(self.root_corr, text="请选择以下某几项进行相关性分析",
                          font=("华光胖头鱼_CNKI", 14), fg="blue")
        aLabel.grid(row=1, column=1, sticky=tk.W)

        # checkButton，复选按钮
        cv1 = tk.IntVar()
        cv2 = tk.IntVar()
        cv3 = tk.IntVar()
        cv4 = tk.IntVar()
        cv5 = tk.IntVar()
        cv6 = tk.IntVar()
        tk.Checkbutton(self.root_corr, text="最高学历", font=("华光胖头鱼_CNKI", 12), variable=cv1,
                       onvalue=1).grid(row=2, column=1, sticky=tk.W)
        tk.Checkbutton(self.root_corr, text="学校是否在国内", font=("华光胖头鱼_CNKI", 12), variable=cv2,
                       onvalue=2).grid(row=2, column=2, sticky=tk.W)
        tk.Checkbutton(self.root_corr, text="专业是否统计", font=("华光胖头鱼_CNKI", 12), variable=cv3,
                       onvalue=3).grid(row=3, column=1, sticky=tk.W)
        tk.Checkbutton(self.root_corr, text="入职员工数", font=("华光胖头鱼_CNKI", 12), variable=cv4,
                       onvalue=4).grid(row=3, column=2, sticky=tk.W)

        # 获取数据
        sa = com_talents.SysInfo("")
        sql = "SELECT companyinfo.`Name` 公司名,Top_grade 最高学历,domestic 学校是否国内,\
            statistic 专业是否统计,employee_num 入职员工数 FROM talentsinfo JOIN companyinfo ON companyinfo.ID = talentsinfo.CompanyID \
                JOIN background ON background.talentsID = talentsinfo.ID JOIN college ON college.ID = background.collegeID \
                    JOIN major ON major.ID = background.majorID"
        try:
            re = sa.loadInfo(sql)
            if (re != 1):
                print(re)

        except:
            tkinter.messagebox.showerror('error', '暂无数据！')

        # 按钮，可展示
        showButton = tk.Button(
            self.root_corr, text=" 确定 ", font=("华光胖头鱼_CNKI", 14))
        showButton.grid(row=5, column=2)

        def showCorr(event):
            list1 = sa.showdata.columns.tolist()
            cor_list = []
            if cv1.get() == 1:
                cor_list.append(list1[cv1.get()])
            if cv2.get() == 2:
                cor_list.append(list1[cv2.get()])
            if cv3.get() == 3:
                cor_list.append(list1[cv3.get()])
            if cv4.get() == 4:
                cor_list.append(list1[cv4.get()])
            sd_res = sa.corrData(cor_list)
            # print(sd_res)
            indexList = sd_res.index.tolist()
            # print(indexList)
            df = pd.DataFrame(pd.Series(indexList), columns=['相关性'])
            # print(df)
            sd_res.index = df.index
            df2 = pd.concat([df, sd_res], axis=1)
            # print(df2)
            df2_list = df2.columns.tolist()
            self.showTree2(df2, df2_list)
        # 按钮绑定事件
        showButton.bind("<Button-1>", showCorr)

        self.root_corr.mainloop()

    # 菜单 图表分析
    def visualData(self):
        VisualPage(self.com_id)


# 人才，查询分析，更多功能页
class StuCalPage():
    def __init__(self):
        self.root = tk.Tk()
        # 给窗口可视化写名字
        self.root.title("查询&分析")
        # 设定窗口的大小
        self.root.geometry('480x400')

        co = com_talents.SysInfo("")
        sql = "SELECT ID 公司编号,`Name` 公司名 ,Grade 公司分类,employee_num 入职员工数 FROM companyinfo"  # SQL 查询语句
        re = co.loadInfo(sql)
        if re != 1:
            print(re)
        data = co.showdata
        col_list = data.columns.tolist()

        # 表格
        tree = ttk.Treeview(self.root, show="headings")
        tree.pack()
        # 定义列
        tree["columns"] = tuple(col_list)
        # 设置列属性，列不显示
        for i in col_list:
            tree.column(i, width=120)

        # 设置表头
        for j in col_list:
            tree.heading(j, text=j)

        # 添加数据
        y = 0
        for n in range(data.shape[0]):
            ls = []
            for k in range(len(data.iloc[n, ])):
                s = str(data.iloc[n, k])
                ls.append(s)
            ls_tuple = tuple(ls)
            tree.insert("", y, text=str(y+1)+".", values=ls_tuple)
            y += 1

        menubar = tk.Menu(self.root)

        # 创建“文件”菜单项及其子菜单
        file = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="基础", menu=file)
        file.add_command(label="查询", command=self.selectMenu)
        file.add_command(label="模糊查询", command=self.fuzzyMenu)
        file.add_separator()
        file.add_command(label="退出", command=self.root.destroy)

        # 创建“分析”菜单项及其子菜单
        edit = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="对公司的统计分析", menu=edit)
        edit.add_command(label="数据", command=self.showAll)
        edit.add_command(label="清洗数据", command=self.cleanData)
        edit.add_command(label="聚类分析", command=self.cluster)
        edit.add_command(label="图表分析", command=self.visual)

        self.root.config(menu=menubar)

        # 主窗口循环显示
        self.root.mainloop()

        # 显示表格的通用
    def showTree(self, root_show, data, col_list):
        #root_show = tk.Toplevel()
        # 给窗口可视化写名字
        # root_show.title("展示信息")
        # 表格
        tree = ttk.Treeview(root_show, show="headings")
        tree.pack()
        # 定义列
        tree["columns"] = tuple(col_list)
        # 设置列属性，列不显示
        for i in col_list:
            tree.column(i, width=80, anchor='center')

        # 设置表头
        for j in col_list:
            tree.heading(j, text=j)

        # 添加数据
        y = 0
        for n in range(data.shape[0]):
            ls = []
            for k in range(len(data.iloc[n, ])):
                s = str(data.iloc[n, k])
                ls.append(s)
            ls_tuple = tuple(ls)
            tree.insert("", y, text=str(y+1)+".", values=ls_tuple)
            y += 1
        # root_show.mainloop()

    # 显示表格的通用,另起一个页面

    def showTree2(self, data, col_list):
        root_show = tk.Toplevel()
        # 给窗口可视化写名字
        root_show.title("展示信息")
        # 表格
        tree = ttk.Treeview(root_show, show="headings")
        tree.pack()
        # 定义列
        tree["columns"] = tuple(col_list)
        # 设置列属性，列不显示
        for i in col_list:
            tree.column(i, width=80, anchor='center')

        # 设置表头
        for j in col_list:
            tree.heading(j, text=j)

        # 添加数据
        y = 0
        for n in range(data.shape[0]):
            ls = []
            for k in range(len(data.iloc[n, ])):
                s = str(data.iloc[n, k])
                ls.append(s)
            ls_tuple = tuple(ls)
            tree.insert("", y, text=str(y+1)+".", values=ls_tuple)
            y += 1
        root_show.mainloop()

        # 查询
    # 定义菜单单击函数，显示查询按钮

    def selectMenu(self):
        self.root_check = tk.Toplevel()
        self.root_check.title("查询信息")
        # 定义按钮单击函数,显示查询信息

        def checkBtClick():
            ID = IDEntry.get()
            print(type(ID))
            # 连接数据库查询
            cc = com_talents.SysInfo("")
            sql = "CALL proc_cominfo('%s')" % (ID)
            re = cc.loadInfo(sql)
            if re != 1:
                print(re)
                tkinter.messagebox.showerror('error', '暂无信息！')

            var_data = cc.showdata

            col_list = var_data.columns.tolist()
            self.showTree(self.root_check, var_data, col_list)

        # 在根窗口内创建学号label和Entry
        userLabel = tk.Label(
            self.root_check, text='公司编号：', font=("华光胖头鱼_CNKI", 16))
        userLabel.pack()
        IDEntry = tk.Entry(self.root_check, fg="blue")
        IDEntry.pack()
        # 在根窗口内创建按钮
        checkButton = tk.Button(
            self.root_check, text="查询", font=("华光胖头鱼_CNKI", 14), command=checkBtClick)
        checkButton.pack()

        self.root_check.mainloop()

    # 定义菜单单击函数，显示模糊查询按钮

    def fuzzyMenu(self):
        self.root_check = tk.Toplevel()
        self.root_check.title("模糊查询信息")

        def checkBtClick2():
            entry = '%'+nameEntry.get()+'%'
            print(type(entry))
            # 连接数据库查询
            con = pymysql.connect(
                host="localhost", port=3306, user="root", passwd="1234", db="talents")
            sql2 = "SELECT ID 公司编号,`Name` 公司名 ,Grade 公司分类,employee_num 入职员工数 FROM companyinfo WHERE `Name` LIKE %s"
            try:
                majord = pd.read_sql(sql=sql2, con=con, params={
                                     entry}, coerce_float=True)
                print(majord)
            except:
                tkinter.messagebox.showerror('error', '暂无信息！')
            con.close()

            col_list = majord.columns.tolist()
            self.showTree(self.root_check, majord, col_list)

        # 模糊查询
        nameLabel = tk.Label(self.root_check, text='公司名：',
                             font=("华光胖头鱼_CNKI", 16))
        nameLabel.pack()
        nameEntry = tk.Entry(self.root_check, fg="blue")
        nameEntry.pack()
        # 在根窗口内创建按钮
        nameButton = tk.Button(
            self.root_check, text="模糊查询", font=("华光胖头鱼_CNKI", 14), command=checkBtClick2)
        nameButton.pack()

        self.root_check.mainloop()

    # 展示统计分析的数据
    def showAll(self):
        ca = com_talents.Category("")
        try:
            re = ca.loadInfo()
            if (re != 1):
                print(re)
            ana_data = ca.ccdata
        except:
            tkinter.messagebox.showerror('error', '暂无数据！')
        col_list = ana_data.columns.tolist()
        self.showTree2(ana_data, col_list)

    # 清洗数据
    def cleanData(self):
        ca = com_talents.Category("")
        re = ca.loadInfo()
        if (re != 1):
            print(re)
        ca.cleanData()
        ana_data = ca.ccdata
        col_list = ana_data.columns.tolist()
        self.showTree2(ana_data, col_list)

    # 聚类
    def cluster(self):
        root_clus = tk.Toplevel()
        root_clus.title("聚类分析")
        aLabel = tk.Label(root_clus, text="选择想要看的聚类分析结果", font=(
            "华光胖头鱼_CNKI", 14), fg="blue")
        aLabel.grid(row=0, column=1, sticky=tk.W)

        # radioButton，单选按钮
        rv = tk.IntVar()  # 设置选项值变量
        rv.set(1)  # 设置缺省选项值
        tk.Radiobutton(root_clus, text="第一类", font=("华光胖头鱼_CNKI", 14), variable=rv, value=0).grid(
            row=1, column=1, columnspan=2, sticky=tk.W)
        tk.Radiobutton(root_clus, text="第二类", font=("华光胖头鱼_CNKI", 14), variable=rv, value=1).grid(
            row=1, column=2, columnspan=2, sticky=tk.W)
        tk.Radiobutton(root_clus, text="第三类", font=("华光胖头鱼_CNKI", 14), variable=rv, value=2).grid(
            row=2, column=1, columnspan=2, sticky=tk.W)
        tk.Radiobutton(root_clus, text="所有", font=("华光胖头鱼_CNKI", 14), variable=rv, value=3).grid(
            row=2, column=2, columnspan=2, sticky=tk.W)

        # 获取数据
        ca = com_talents.Category("")
        re = ca.loadInfo()
        if (re != 1):
            print(re)
        ca.cleanData()
        cluster_res = ca.Cluster()
        print(cluster_res)
        list1 = ca.ccdata['公司名'].values.tolist()
        cluster_res = ca.Cluster()
        print(cluster_res)
        clus = list(cluster_res)
        se = pd.Series(list1)
        se2 = pd.Series(clus)
        daf = pd.DataFrame([se, se2])
        daf_T = pd.DataFrame(daf.values.T, columns=['公司名', '类别'])
        print(daf_T)
        #col_list = daf_T.columns.tolist()
        #self.showTree(daf_T, col_list)

        # 按钮，可展示
        showGroupButton = tk.Button(
            root_clus, text=" 确定 ", font=("华光胖头鱼_CNKI", 16))
        showGroupButton.grid(row=3, column=2)

        def showClus(event):
            if rv.get() == 0:
                num = 0
                df = daf_T.loc[daf_T["类别"] == num, ['公司名']]
            elif rv.get() == 1:
                num = 1
                df = daf_T.loc[daf_T["类别"] == num, ['公司名']]
            elif rv.get() == 2:
                num = 2
                df = daf_T.loc[daf_T["类别"] == num, ['公司名']]
            else:
                df = daf_T

            new_groupList = df.columns.tolist()
            self.showTree2(df, new_groupList)
        # 按钮绑定事件
        showGroupButton.bind("<Button-1>", showClus)

        root_clus.mainloop()

    # 图表分析
    def visual(self):
        VisualStuPage()


# 图表分析(人才)
class VisualStuPage():
    def __init__(self):

        self.window = Tk()  # 初始框的声明
        self.window.title('图表分析页面')
        self.window.geometry('900x550')  # 这里的乘是小x

        Button(self.window, text="各类公司占比", width=16, font=tkFont.Font(family="华光胖头鱼_CNKI",
                                                                      size=16), command=self.comdata).grid(row=0, column=1, sticky=tk.W)
        Button(self.window, text="各家公司入职人数", width=16, font=tkFont.Font(family="华光胖头鱼_CNKI",
                                                                        size=16), command=self.employee).grid(row=0, column=2, sticky=tk.W)

    # 各类公司的占比图
    def comdata(self):

        plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体，便于显示中文
        self.window.resizable(False, False)

        matplotlib.use('TkAgg')

        sa = com_talents.SysInfo("")
        sql = "SELECT Grade 公司类别, COUNT(Grade) 个数 FROM companyinfo GROUP BY Grade"
        try:
            re = sa.loadInfo(sql)
            if (re != 1):
                print(re)
            ana_data = sa.showdata
        except:
            tkinter.messagebox.showerror('error', '暂无数据！')

        pie = plt.figure(figsize=(4.6, 4), facecolor="#F0F0F0")
        xdata = ana_data["个数"]
        plt.pie(xdata, explode=[0.1, 0, 0], labels=tuple(ana_data["公司类别"]), colors=None,
                autopct='%1.1f%%', pctdistance=0.6, shadow=True,
                labeldistance=1.1, startangle=90,
                radius=None, counterclock=True, wedgeprops=None,
                textprops={'fontsize': 10, 'color': 'k'}, center=(0, 0), frame=False)
        plt.title('各类公司占比图')
        canvas_statis = FigureCanvasTkAgg(pie, self.window)
        canvas_statis.get_tk_widget().place(x=10, y=80)  # 根据坐标，放在指主窗口的指定位置

    # 各家公司入职人数的柱形图
    def employee(self):
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体，便于显示中文
        self.window.resizable(False, False)

        matplotlib.use('TkAgg')

        sa = com_talents.SysInfo("")
        sql = "SELECT ID 公司编号, employee_num 人数 FROM companyinfo "
        try:
            re = sa.loadInfo(sql)
            if (re != 1):
                print(re)
            ana2_data = sa.showdata
        except:
            tkinter.messagebox.showerror('error', '暂无数据！')

        pie = plt.figure(figsize=(4, 4.5), facecolor="#F0F0F0")

        # 一共有多少个x轴类别
        a = ana2_data['公司编号'].values.tolist()
        b = np.array(ana2_data['人数'].values.tolist())
        x_14 = list(range(len(a)))
        plt.bar(x_14, b, bottom=None, label='入职员工数')
        plt.ylim(0, 13)
        plt.xlabel('公司编号', fontsize=8)
        plt.ylabel('人数', fontsize=8)
        plt.title('各家公司入职人数情况图')
        plt.xticks(x_14, a, rotation=45)
        plt.legend()

        canvas_statis = FigureCanvasTkAgg(pie, self.window)
        canvas_statis.get_tk_widget().place(x=480, y=50)  # 根据坐标，放在指主窗口的指定位置

        self.window.mainloop()


# 学生查看信息界面
class StudentView:
    def __init__(self, parent_window, student_id):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('人才信息')
        self.window.geometry('300x550')  # 这里的乘是小x

        label = tk.Label(self.window, text='人才信息查看', bg='lightgreen',
                         font=("华光胖头鱼_CNKI", 20), width=30, height=2)
        label.pack(pady=20)

        self.id = '学号:' + ''
        self.name = '姓名:' + ''
        self.entry = '入行年份:' + ''
        self.company = '入职公司:' + ''
        # 打开数据库连接
        db = pymysql.connect(host="localhost", port=3306,
                             user="root", passwd="1234", db="talents")
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        # SQL 查询语句,视图
        sql = "SELECT * FROM view_talents WHERE 人才编号 = '%s'" % (student_id)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.id = '编号:' + row[0]
                self.name = '姓名:' + row[1]
                self.entry = '入行年份:' + row[4]
                self.company = '入职公司:' + row[3]
        except:
            print("Error: unable to fetch data")
        db.close()        # 关闭数据库连接

        Label(self.window, text=self.id, font=("华光胖头鱼_CNKI", 18)).pack(pady=5)
        Label(self.window, text=self.name, font=(
            "华光胖头鱼_CNKI", 18)).pack(pady=5)
        Label(self.window, text=self.entry, font=(
            "华光胖头鱼_CNKI", 18)).pack(pady=5)
        Label(self.window, text=self.company,
              font=("华光胖头鱼_CNKI", 18)).pack(pady=5)

        Button(self.window, text="返回首页", width=8, font=tkFont.Font(family="华光胖头鱼_CNKI",
                                                                   size=16), command=self.back).pack(pady=25)
        Button(self.window, text="查询&分析", width=8, font=tkFont.Font(family="华光胖头鱼_CNKI",
                                                                    size=16), command=self.jump).pack(pady=25)

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def jump(self):
        StuCalPage()

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口


# 注册页面
class RegistPage():
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面
        self.window = tk.Tk()  # 初始框的声明
        self.window.title('注册')
        self.window.geometry('300x280')  # 这里的乘是小x

        def checkBtClick():
            cm = com_talents.SysInfo("")
            val = (self.IDEntry.get(), self.nameEntry.get(), self.passEntry.get())
            re = cm.insertData(1, val)
            if re != 1:
                print(re)
            else:
                tkinter.messagebox.showinfo('提示', '注册成功！')

        # 在根窗口内创建学号label和Entry
        self.IDLabel = tk.Label(self.window, text='编号：',
                                font=("华光胖头鱼_CNKI", 18))
        self.IDLabel.grid(row=1, column=1)
        self.IDEntry = tk.Entry(self.window, fg="blue")
        self.IDEntry.grid(row=1, column=2)
        self.nameLabel = tk.Label(
            self.window, text='姓名：', font=("华光胖头鱼_CNKI", 18))
        self.nameLabel.grid(row=2, column=1)
        self.nameEntry = tk.Entry(self.window, fg="blue")
        self.nameEntry.grid(row=2, column=2)
        self.passLabel = tk.Label(
            self.window, text='密码：', font=("华光胖头鱼_CNKI", 18))
        self.passLabel.grid(row=3, column=1)
        self.passEntry = tk.Entry(self.window, fg="blue")
        self.passEntry.grid(row=3, column=2)

        # 在根窗口内创建按钮
        checkButton = tk.Button(self.window, text="注册", font=(
            "华光胖头鱼_CNKI", 12), command=checkBtClick)
        checkButton.grid(row=4, column=2)
        tk.Button(self.window, text="返回首页", font=("华光胖头鱼_CNKI", 12),
                  command=self.back).grid(row=5, column=2)

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口


# About页面
class AboutPage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('关于')
        self.window.geometry('300x450')  # 这里的乘是小x

        label = tk.Label(self.window, text='公司-人才信息管理系统', bg='lightblue',
                         font=("华光胖头鱼_CNKI", 20), width=30, height=2)
        label.pack()

        Label(self.window, text='作者：陈丽阳&苏蕴琪',
              font=("华光胖头鱼_CNKI", 18)).pack(pady=30)
        Label(self.window, text='2021年12月',
              font=("华光胖头鱼_CNKI", 18)).pack(pady=5)

        Button(self.window, text="返回首页", width=8, font=tkFont.Font(family="华光胖头鱼_CNKI",
                                                                   size=12), command=self.back).pack(pady=100)

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口


if __name__ == '__main__':
    try:
        # 实例化Application
        window = tk.Tk()
        StartPage(window)
    except:
        messagebox.showinfo('错误！', '连接数据库失败！')
