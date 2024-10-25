# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 13:39:54 2024

@author: ASUS
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#columns  axis =1 
#rows axis = 0
print("Welcome manager this the data say you want me to process it")
data = pd.read_csv(r"C:\Users\ASUS\Downloads\Meteorite_Landings.csv")
print(data.info())
print("_>" * 80)
#الان انا عملت هاي الحركه عشان اعرف نوعية البيانات الي عندي 
f=data.describe()
print(data.describe(include="object"))
#هسا انا عملت هون وصف للبيانات الي من نوع ال string عشان اعرف شو الكولومز الي رح اعبيها اذا كانت categorical
print("_>" * 80)


print(data.describe(include="int64"))
print(data.describe(include = "float64"))
#هسا هيك انا عرفت كل الداتا الي عندي شو نوعيتها 
print("_>" * 80)


print(data.loc[:10 ,["name" ,"id" , "recclass"]])
print(data.loc[5:50,["reclat","nametype","mass (g)"]])
print(data.columns)

print(data.iloc[20:51,3:7])
#هون حبيت اني اتعمق بالبيانات اكثر عن طريق ال loc و ال iloc 
print("_>" * 80)

print(data.index)
#عملت هاي الحركه عشان اعرف شو الاندكس لهاي الداتا شو رح تكون

print("_>" * 80)

print(data.columns)
#هاي الحركه ممكن اعملها عشان اذا بدي اوصل للكولومز يكون اسهل الي اعرف اسمائهم 
print("_>" * 80)
print(data.dtypes)

print("_>" * 80)
#هاي اذا حبيت اني اتأكد مره ثانيه  من نوعية هاي الداتا 
#print(data.select_dtypes("int64")) ارجعلها بس تعمل filter للداتا ضروري
print(data.head(50))
print(data.tail(50))
#هون انا رجعت اول خمسين واخر خمسين لمعرفة البيانات بشكل اكبر
print("_>" * 80)

#الان رح ابلش اعرف اذا البيانات عندي فيها missing او لا من خلال 
print(data.isna().sum())
# الان عندي الكولومز الاتيه فيها missing 
#[GeoLocation,reclong,reclat,year,mass,]
print("_>" * 80)

#الان بدي ارجع استذكر كل واحد فيهم شو نوعه عشان اعرف اعبيه
print(data.dtypes)
#type_data=data["GeoLocation","reclong","reclat","year","mass"]
print(data["mass (g)"].value_counts)
mass=data[["mass (g)"]]
print(mass.dtypes)
#الان انا رح اشتغلت على اول كولوم فيه missing data 
#رح اطلع ال mean ل ال  mass 
#وهو عباره عن Numeric 

print(round(data["mass (g)"].mean()))
fill_mass=data["mass (g)"].fillna(13240,inplace =True)
print(data.isna().sum())
print("_>" * 80)

#الان رح ابلش اشتغل على ال columns  الثاني وهو ال reclong
print(data["reclong"].value_counts())
print(round(data["reclong"].mean()))
fill_recoling=data["reclong"].fillna(61,inplace = True )
print(data.isna().sum())

print("_>" * 80)

#هسا رح نشتغل على ال GeoLocation
ty=data["GeoLocation"].value_counts()
mod_Geo=data["GeoLocation"].mode()
print(mod_Geo)
fill_Geo=data["GeoLocation"].fillna(("0.0, 0.0"),inplace = True)
print(data.isna().sum())
#الان زي ما منلاحظ اشتغلنا هون على داتا نوعها categorical data وكانت القيمه الي اكثر تكرارا هي ال (0.0, 0.0) عباره عن tuple بس خزنتها ك str

print("_>" * 80)
 #هسا رح نشتغل على الyear
y=data["year"].value_counts()
print(round(data["year"].mean()))
fill_year=data["year"].fillna(1992,inplace = True )
print(data.isna().sum())

print("_>" * 80)

# هسا رح نشتغلل على اخر كولوم وهو ال reclat
z=data["reclat"].value_counts()
print(round(data["reclat"].mean()))
fill_year=data["reclat"].fillna(-39,inplace = True )
print(data.isna().sum())

print("_>" * 80)

print(data[["nametype"]])
re_bet_NT=data[data["nametype"]=="Valid"]
print(re_bet_NT)
relict=data[data["nametype"]=="relict"]
print(relict)
#استنتاجا من هون طلع عندي كل النيازك صالحه ولم تتأثر بالظروف الجويه
print(data.isna().sum())
re_bet_Valid_Fell=data[(data["nametype"]=="Valid") & (data["fall"]=="Fell")]
#هسا حاولت اتعرف اكثر اذا موجود نيزك صالح وسقط وتمت ملاحظته 
print(re_bet_Valid_Fell)
#هون لقيت انه عندي 1107 سقط وكان صالح وتمت ملاحظة سقوطه 
re_bet_Valid_Found=data[(data["nametype"]=="Valid") & (data["fall"]=="Found")]
print(re_bet_Valid_Found)
#هون لقيت انه عندي 44534 من النيازك سقطت وتم العثور عليها
year7TO8=data[(data["year"]>=1700) & (data["year"]<1800)]
print(year7TO8)
#هون لقيت انه كان عندي عباره عن 38 نيزك سقط في الفتره ما بين ال 1700 TO 1800
year8TO9=data[(data["year"]>=1800) & (data["year"]<1900)]
print(year8TO9)
#هون لقيت انه كان عندي عباره عن 668 نيزك سقط في الفتره ما بين ال 1800 و 1900

year9TO20=data[(data["year"]>=1900) & (data["year"]<2000)]
print(year9TO20)
#هون لقيت انه كان عندي عباره عن 25267 نيزك سقط في الفتره ما بين ال 1900 TO 2000

year2OTO2024=data[(data["year"]>=2000) & (data["year"]<2024)]
print(year2OTO2024)
#هون لقيت انه كان عندي عباره عن 19720 نيزك سقط في الفتره ما بين ال 2000 TO 2024
####################################################################################
#هيك انا اوجدت بعض العلاقات المهمه للتعرف على البيانات
print("_>" * 80)
#هيك البيانات انا جاهزه عندي بالكامل هسا رح ننتقل لمرحلة التمثيل بالصور
data_len=len(data)
print(data_len)
x=(data.isna().sum()/data_len)*100
print(x)
mass_mean_Valid = len(data[data["year"] >= 1900])
Mass_anything = len(data[data["year"] >= 2000])

visu_nametype = plt.pie([mass_mean_Valid, Mass_anything], labels=["mass_mean_Valid", "Mass_anything"], autopct="%1.3f%%")

print("_>" * 80)
#الان رح نيجي لمرحلة ال Encoding والاخيره وهي ك الاتي 
print(data.dtypes)
#رح الاحظ انه عندي البيانات الي categorical هي 
#[name,GeoLocation,fall,recclass,nametype]


print(data.info())

data=pd.get_dummies(data,columns=["nametype"])

#هاي عشان ا.جيب اسم الكولوم الي عملتله encoding 
data.drop(columns=["nametype_Valid"],axis = 1 ,inplace=True)
print(data.info())
# الان رح نحذف كولوم ال name لانه ما اله علاقه بال target تبعنا 
del data["name"]
print(data.info())

print("_>" * 80)

#عشان اشيك اذا حذفت كولوم ال name
print(data.columns)
print(data["GeoLocation"].dtype)
print(data["GeoLocation"].value_counts)
#هون حاولت اعرف نوع البيانات الي عندي وطلع نوعها str 
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
data['Geolocation_encoding_data'] = label_encoder.fit_transform(data['GeoLocation'])
#هون حولت ال GeoLocation ل بيانات رقميه
del data["GeoLocation"]
#هون رجعت حذفت الكولوم الأصلي 
print(data.info())

#وهون رجعت شيكت على هاي البيانات 
print("_>" * 80)
#هسا رح نشتغل على كولوم ال fall
print(data["fall"].value_counts)
#Found ,Fellطلع عندي عباره عن وهون انا بحتاج اعمله Getdumis
data=pd.get_dummies(data,columns=["fall"])
#هون انا عملت ال encoding 
print(data.columns[9])
#هون استدعيت اسم الكولوم الي بدي احذفه عن طريق الاندكس 
del data["fall_Found"]
print(data.info())
#هون زي ما منلاحظ صار عندي كولوم ال fall_Found عباره عن bool 
print("_>" * 80)
#هسا رح نشتغل على كولوم ال recclass وهو اخر كولوم بعديها البيانات عندي رح تكون جاهزه 
print(data["recclass"].value_counts)

#print(data["recclass"].head(50))
#print(data["recclass"].tail(50))
#بس عشان اتاكد من نوعيه هاي البيانات اكثر وشو طريقة الا encoding الي المفروض اني اعملها 
from sklearn.preprocessing import LabelEncoder
reclass_label_encoder = LabelEncoder()
data["reclass_encoded_data"] = reclass_label_encoder.fit_transform(data["recclass"])
print(data.columns[1])

del data["recclass"]


