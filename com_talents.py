# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 09:27:08 2021

@author: CLY
"""

import pymysql
import pandas as pd
import numpy as np
from pylab import *  #后面做聚类
from scipy.cluster.vq import * #后面做聚类

class SysInfo:
    def __init__(self,showdata):
        self.showdata = showdata
        
    #从文件中读取学生信息
    def loadInfo(self,sql):
        try:
            con = pymysql.connect(host="localhost",port=3306,user="root",passwd="1234",db="talents")             
            self.showdata = pd.read_sql(sql=sql,con=con,coerce_float=True)
            con.close()
        except Exception as e:
            return e        
        print("Load file successfully!\n")     
        return 1
    
    #清洗数据
    def cleanData(self):
        try: 
            columns = self.showdata.columns.values.tolist()
            for col in columns:
                self.showdata.fillna({col:0},inplace=True)            
        except Exception as e:
            return e
        return 1
    
    #插入数据记录
    def insertData(self,num,val):
        
        con = pymysql.connect(host="localhost",port=3306,user="root",passwd="1234",db="talents")             
        cur = con.cursor()
        if num == 1:
            sql = "INSERT INTO talentsinfo(ID,`Name`,Password) VALUES(%s,%s,%s)"
        else:
            sql = "INSERT INTO companyinfo(ID,`Name`,Password) VALUES(%s,%s,%s)"
        
        try:
            cur.execute(sql,val) #执行SQL语句
            con.commit()  #提交更新
            print("insert successfully!")
        except:
            print ("Error: unable to insert data")
            con.rollback()  #出错回滚
    
        cur.close() #关闭游标
        con.close()
        return 1
        
    #删除记录
    def deleteData(self,num,val):
        con = pymysql.connect(host="localhost",port=3306,user="root",passwd="1234",db="talents")             
        cur = con.cursor()
        if num == 1:
            sql = "DELETE FROM talentsinfo WHERE ID = %s"
        else:
            sql = "DELETE FROM companyinfo WHERE ID = %s"
        
        try:
            cur.execute(sql,val) #执行SQL语句
            con.commit()  #提交更新
            print("delete successfully!")
        except:
            print ("Error: unable to delete data")
            con.rollback()  #出错回滚
    
        cur.close() #关闭游标
        con.close()
        return 1

    #按照需求排序
    def sortValue(self,res,methods):

        cdata = self.showdata.sort_values(by=res,ascending=methods)

        return cdata

    #选择几列数据描述性统计（可在窗口选择）
    def dataDescribe(self,list1):
        data_des = self.showdata[list1].describe()
        return data_des
    
    #按公司分组求均值或中值（可在窗口选择）
    def dataGroup(self,num):
        colist = self.showdata.columns.values.tolist()
        if num == 1:
            grouped = self.showdata.groupby(colist[0])
            dd= grouped.aggregate({colist[1]:np.mean,colist[2]:np.mean,colist[3]:np.mean})
        else:
            grouped = self.showdata.groupby(colist[0])
            dd= grouped.aggregate({colist[1]:np.median,colist[2]:np.median,colist[3]:np.median})
        return dd
    
    #相关性分析
    def corrData(self,list1):
        res = self.showdata[list1].corr()
        return res
   
    
    
class Category:
    def __init__(self,ccdata):
        self.ccdata = ccdata
        
    #从文件中读取汇总信息
    def loadInfo(self):
        try:
            con = pymysql.connect(host="localhost",port=3306,user="root",passwd="1234",db="talents")             
            #公司里最高学历是985、211和研究院的人数
            sql_t1 = "SELECT companyinfo.`Name` 公司名,COUNT(college.category) 员工国内学校数 FROM talentsinfo JOIN background ON background.talentsID = talentsinfo.ID AND background.education_grade=talentsinfo.Top_grade JOIN companyinfo ON companyinfo.ID = talentsinfo.CompanyID JOIN college ON college.ID = background.collegeID WHERE domestic=1 AND college.category='985' OR college.category='211' OR college.category='研究院'  GROUP BY CompanyID"
            try:
                df_t1 = pd.read_sql(sql=sql_t1,con=con,coerce_float=True)
            except:
                print("Error:unable to fetch data")
            #公司里最高学历是QS前200的人数  
            sql_t2 = "SELECT companyinfo.`Name` 公司名,COUNT(college.category) 员工国外学校数 FROM talentsinfo JOIN background ON background.talentsID = talentsinfo.ID AND background.education_grade=talentsinfo.Top_grade JOIN companyinfo ON companyinfo.ID = talentsinfo.CompanyID JOIN college ON college.ID = background.collegeID WHERE domestic=0 AND college.category='QS101-200' OR college.category='QS前100' GROUP BY CompanyID"
            try:
                df_t2 = pd.read_sql(sql=sql_t2,con=con,coerce_float=True)
            except:
                print("Error:unable to fetch data") 

            self.ccdata = df_t1
            self.ccdata['员工国外学校数']=df_t2['员工国外学校数']
            sql_t3 = "SELECT companyinfo.`Name` 公司名,COUNT(Top_grade) 人数 FROM talentsinfo JOIN companyinfo ON companyinfo.ID = talentsinfo.CompanyID WHERE Top_grade = %s GROUP BY CompanyID"
            list1=['本科人数','硕士人数','博士人数']
            for i in range(3):
                try:
                    df_t3 = pd.read_sql(sql=sql_t3,con=con,params={i+1},coerce_float=True)
                    print(df_t3)
                    self.ccdata[list1[i]]=df_t3['人数']
                except:
                    print("Error:unable to fetch data")
            con.close()
        except Exception as e:
            return e        
        print("Load file successfully!\n")     
        return 1
    
    #清洗数据
    def cleanData(self):
        try: 
            co=self.ccdata.columns.values.tolist()
            for col in co:
                self.ccdata.fillna({col:0},inplace=True)
        except Exception as e:
            return e
        return 1

    #聚类分析
    def Cluster(self):
        col = self.ccdata.columns.values.tolist()
        data_array=np.array(self.ccdata.iloc[:,1:len(col)])

        ##聚类
        centroids,_=kmeans(data_array,3)
        results,_=vq(data_array,centroids)
        return results
    
    #相关性分析
    def corrData(self,list1):
        res = self.ccdata[list1].corr()
        return res
   
    
    
#主程序
def main():
    #以下是测试
    cd = SysInfo("")
    sql_6="SELECT view_gradetotal.EntryTime,总人数, 本科,硕士,博士 FROM view_gradetotal LEFT JOIN view_grade1 ON view_gradetotal.EntryTime = view_grade1.EntryTime LEFT JOIN view_grade2 ON view_grade2.EntryTime=view_gradetotal.EntryTime LEFT JOIN view_grade3 ON view_grade3.EntryTime=view_gradetotal.EntryTime"

    sql = "SELECT ID 公司编号,`Name` 公司名, Grade 公司分类, employee_num 入职员工数 FROM companyinfo"
    cdata = cd.loadInfo(sql_6)
    if( cdata != 1 ):
        
        print( cdata )
    else:   
        r=cd.cleanData()
        print(r)
        print(cd.showdata)
  
    sql_2="SELECT companyinfo.`Name` 公司名,Top_grade 最高学历,domestic 学校是否国内,statistic 专业是否统计,employee_num 入职员工数 FROM talentsinfo JOIN companyinfo ON companyinfo.ID = talentsinfo.CompanyID JOIN background ON background.talentsID = talentsinfo.ID JOIN college ON college.ID = background.collegeID JOIN major ON major.ID = background.majorID"
    res = cd.loadInfo(sql_2)
    if( res != 1 ):
        print( res )
    else:        
        print(cd.showdata)
    
    
    
    dd=cd.dataDescribe(['最高学历'])
    print(dd)
    print(type(dd))
    indexList=dd.index.tolist()
    print(indexList)
    df=pd.DataFrame(pd.Series(indexList),columns=['数字特征'])
    print(df)
    dd.index=df.index
    df2=pd.concat([df,dd],axis=1)
    print(df2)
    
    sd_res = cd.dataGroup(1)
    print(sd_res)
    print(type(sd_res))
    indexList2=sd_res.index.tolist()
    print(indexList2)
    dfa=pd.DataFrame(pd.Series(indexList2),columns=['公司名'])
    print(dfa)
    sd_res.index=dfa.index
    df3=pd.concat([dfa,sd_res],axis=1)
    print(df3)
        



    cordd=cd.corrData(['最高学历','学校是否国内'])
    print(cordd)
    print(cordd.columns.tolist())
    
    
    ca = Category("")
    resc=ca.loadInfo()
    if( resc != 1 ):
        print( resc )
    else:   
        r=ca.cleanData()
        print(r)
        print(ca.ccdata)
    list1=ca.ccdata['公司名'].values.tolist()
    len(list1)
    cluster_res=ca.Cluster()
    print(cluster_res)
    print(len(cluster_res))
    clus = list(cluster_res)
    se = pd.Series(list1)
    se2=pd.Series(clus)
    daf = pd.DataFrame([se,se2])
    print(daf)
    daf_T = pd.DataFrame(daf.values.T,columns=['公司名','类别'])
    print(daf_T)
    daf_T.loc[daf_T["类别"]==1,['公司名']]
    daf_T.loc[:,['公司名']]
    
    sql_1 = "SELECT * FROM talentsinfo"
    du = SysInfo("")
    du.loadInfo(sql_1)
    val = ('C78','dawf','darha124')
    du.insertData(1,val)
    du.loadInfo(sql_1)
    print(du.showdata)
    du.deleteData(1,'C78')
    du.loadInfo(sql_1)
    print(du.showdata)
    
    cc = SysInfo("")
    sql_c="SELECT talentsID `人才编号`,talentsinfo.`Name` `姓名`,education `学历`,college.`Name` `学校名`,major.`Name` `专业名` FROM background JOIN talentsinfo ON talentsinfo.ID = background.talentsID JOIN educationinfo ON educationinfo.Grade = background.education_grade JOIN college ON college.ID = background.collegeID JOIN major ON major.ID = background.majorID ORDER BY talentsID"
    cc.loadInfo(sql_c)
    cda=cc.showdata
    col = cda.columns.tolist()
    cda.loc[cda["人才编号"]=='P001',col]
    
    ff = SysInfo("")
    sql="CALL proc_cominfo('C01')"
    ff.loadInfo(sql)
    ff.showdata


if __name__ == '__main__': main()