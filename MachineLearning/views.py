from django.shortcuts import render
from core.models import State,Dataset,RegionDataset
from django.core import serializers
from django.db.models import Avg, Count
import json as simplejson
import os
import numpy as np
import pandas as pd


def stateComparsion(request):
    # os.chdir("D:\\RegionDataset")
    stateName = RegionDataset.objects.values_list('SUBDIVISION', flat=True).distinct()
    dataset = RegionDataset.objects.all()
    All_Region_Rainfall_data = RegionDataset.objects.values('SUBDIVISION').annotate(ANNUAL=Avg('ANNUAL'),JAN=Avg('JAN'),FEB=Avg('FEB'),MAR=Avg('MAR'),APR=Avg('APR'),MAY=Avg('MAY'),JUN=Avg('JUN'),JUL=Avg('JUL'),AUG=Avg('AUG'),SEP=Avg('SEP'),OCT=Avg('OCT'),NOV=Avg('NOV'),DEC=Avg('DEC'),Jan_Feb=Avg('Jan_Feb'),Mar_May=Avg('Mar_May'),Jun_Sep=Avg('Jun_Sep'),Oct_Dec=Avg('Oct_Dec'))
    json_RegionDataset=serializers.serialize("json",dataset)
    # print("data:- ",All_Region_Rainfall_data)
    # os.chdir("D:\\RegionDataset")
    # df = pd.read_csv("rainfall_in_india.csv")
    # annual_rain_d, year_d = seperatingData(df)

    # df = removingNull(df, annual_rain_d, year_d)
    # annual_rain_d, year_d = seperatingData(df)
    # annual_data = simplejson.dumps(annual_rain_d)
    # list_state = list(annual_rain_d.keys())
    parameter = ["ANNUAL","JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
    data = {
        "RegionDataset": json_RegionDataset,
        "stateList": list(stateName),
        "AllRegionData":list(All_Region_Rainfall_data),
        "parameter": parameter
    }
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'machineLearning/statecomparsion.html', {"data": data,"welcome":"State Comparison"})

def index(request):
    return render(request, 'machineLearning/index.html')



def state_view(request, sid):
    #global annual_rain_d,annual_data, year_d, annual_bar_data
    # Loading Data from local disk 
    
    s = State.objects.get(pk=sid)
    A_N=RegionDataset.objects.filter(SUBDIVISION=s.name)
    All_State_Annual_Rainfall = RegionDataset.objects.values('SUBDIVISION').annotate(average_rainfall=Avg('ANNUAL'))
    All_State_Data = []
    All_State_Annual_Rainfall_data = []
    for item in All_State_Annual_Rainfall:
        for name,value in item.items():
            if(name=="SUBDIVISION"):
                All_State_Data.append(value)
            else:
                All_State_Annual_Rainfall_data.append(value)
        
    Grid_Table_data=serializers.serialize("json",A_N)
    annual_rainfall_data = A_N.values_list('YEAR', 'ANNUAL')
    linear_chart_data = simplejson.dumps(dict(annual_rainfall_data))
    mouthily_rainfall_data = RegionDataset.objects.filter(SUBDIVISION=s.name).aggregate(JAN=Avg('JAN'),FEB=Avg('FEB'),MAR=Avg('MAR'),APR=Avg('APR'),MAY=Avg('MAY'),JUN=Avg('JUN'),JUL=Avg('JUL'),AUG=Avg('AUG'),SEP=Avg('SEP'),OCT=Avg('OCT'),NOV=Avg('NOV'),DEC=Avg('DEC'))
    
    sessional_rainfall_data =  RegionDataset.objects.filter(SUBDIVISION=s.name).aggregate(Jan_Feb=Avg('Jan_Feb'),Mar_May=Avg('Mar_May'),Jun_Sep=Avg('Jun_Sep'),Oct_Dec=Avg('Oct_Dec'))
    
    json_columns = simplejson.dumps(
        ['YEAR', 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC',"ANNUAL","Jan_Feb","Mar_May","Jun_Sep","Oct_Dec"])
    
    data = {"state": s,
            "line_chart": linear_chart_data,
            "stateList": All_State_Data,
            "state_data":Grid_Table_data,
            "columns": json_columns, 
            "json_pie_data": list(sessional_rainfall_data.values()),
            "json_bar_data": list(mouthily_rainfall_data.values()),
            "json_annual_bar_data": All_State_Annual_Rainfall_data
            
    }

    
    return render(request, 'machineLearning/state_view.html', {"data": data,"welcome":"State View"})
# machineLearning/state_view.html

# os.chdir("C:\\Users\\AQIB\\Downloads\\ML")
# df = pd.read_csv("Rainfall RegionDataset 2020 - Rainfall_Data_LL.csv")
# arr = df.to_numpy()
# list_arr = arr.tolist()
# for row in list_arr:
#     c = RegionRegionDataset(SUBDIVISION=row[0].upper(), YEAR=row[1], JAN=row[2], FEB=row[3], MAR=row[4], APR=row[5], MAY=row[6], JUN=row[7], 
#     JUL=row[8], AUG=row[9], SEP=row[10], OCT=row[11], NOV=row[12], DEC=row[13], ANNUAL=row[14], Jan_Feb=row[15], Mar_May=row[16], Jun_Sep=row[17], Oct_Dec=row[18],Latitude=row[19],Longitude=row[20])
#     c.save()

# A_N=RegionDataset.objects.filter(SUBDIVISION="ANDAMAN & NICOBAR ISLANDS")
# post_list=serializers.serialize("json",A_N)
# print(post_list)