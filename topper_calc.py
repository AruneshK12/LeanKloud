import pandas as pd

#importing the dataset
#print("Importing Dataset...")
dataset_marks=pd.read_csv("Student_marks_list.csv")
#print("Import complete!")
maths,bio,eng,phy,chem,hin=0,0,0,0,0,0
maths_name=[]
bio_name=[]
eng_name=[]
phy_name=[]
chem_name=[]
hin_name=[]
first=second=third=-1
first_name=[]
second_name=[]
third_name=[]
#calculating the toppers for each subject
#math_set=dataset_marks[["Name","Maths"]]
for index,row in dataset_marks.iterrows():
    temp_sum=int(row["Maths"])+int(row["Biology"])+int(row["English"])+int(row["Physics"])+int(row["Chemistry"])+int(row["Hindi"])
    if(temp_sum>first):
        third=second
        second=first
        first=temp_sum
    elif(temp_sum>second):
        third=second
        second=temp_sum
    elif(temp_sum>third):
        third=temp_sum
    if(int(row["Maths"])>=maths):
        maths=int(row["Maths"])
    if(int(row["Biology"])>=bio):
        bio=int(row["Biology"])
    if(int(row["English"])>=eng):
        eng=int(row["English"])
    if(int(row["Physics"])>=phy):
        phy=int(row["Physics"])
    if(int(row["Chemistry"])>=chem):
        chem=int(row["Chemistry"])
    if(int(row["Hindi"])>=hin):
        hin=int(row["Hindi"])

for index,row in dataset_marks.iterrows():
    temp_sum=int(row["Maths"])+int(row["Biology"])+int(row["English"])+int(row["Physics"])+int(row["Chemistry"])+int(row["Hindi"])
    if(first==temp_sum):
        first_name.append(row["Name"])
    if(second==temp_sum):
        second_name.append(row["Name"])
    if(third==temp_sum):
        third_name.append(row["Name"])
    
    if(maths==int(row["Maths"])):
        maths_name.append(row["Name"])
    if(bio==int(row["Biology"])):
        bio_name.append(row["Name"])
    if(eng==int(row["English"])):
        eng_name.append(row["Name"])
    if(phy==int(row["Physics"])):
        phy_name.append(row["Name"])
    if(chem==int(row["Chemistry"])):
        chem_name.append(row["Name"])
    if(hin==int(row["Hindi"])):
        hin_name.append(row["Name"])
    
if(len(maths_name)==1):
    print("Topper of Maths is ",maths_name[0])
else:
    print("Topper of Maths are ",end=" ")
    for i in range(0,len(maths_name)):
        if(i==len(maths_name)-1):
            print(maths_name[i],end="")
        else:
            print(maths_name[i],end=",")
    print()

if(len(bio_name)==1):
    print("Topper of Biology is ",bio_name[0])
else:
    print("Topper of Biology are ",end=" ")
    for i in range(0,len(bio_name)):
        if(i==len(bio_name)-1):
            print(bio_name[i],end="")
        else:
            print(bio_name[i],end=",")
    print()

if(len(eng_name)==1):
    print("Topper of English is ",eng_name[0])
else:
    print("Topper of English are ",end=" ")
    for i in range(0,len(eng_name)):
        if(i==len(eng_name)-1):
            print(eng_name[i],end="")
        else:
            print(eng_name[i],end=",")
    print()

if(len(phy_name)==1):
    print("Topper of Physics is ",phy_name[0])
else:
    print("Topper of Physics are ",end=" ")
    for i in range(0,len(phy_name)):
        if(i==len(phy_name)-1):
            print(phy_name[i],end="")
        else:
            print(phy_name[i],end=",")
    print()

if(len(chem_name)==1):
    print("Topper of Chemistry is ",chem_name[0])
else:
    print("Topper of Chemistry are ",end=" ")
    for i in range(0,len(chem_name)):
        if(i==len(chem_name)-1):
            print(chem_name[i],end="")
        else:
            print(chem_name[i],end=",")
    print()

if(len(hin_name)==1):
    print("Topper of Hindi is ",hin_name[0])
else:
    print("Topper of Hindi are ",end=" ")
    for i in range(0,len(hin_name)):
        if(i==len(hin_name)-1):
            print(hin_name[i],end="")
        else:
            print(hin_name[i],end=",")
    print()

print("Best Students in the class are ",first_name[0],",",second_name[0]," and ",third_name[0])
print()