from tkinter.font import names
from django.shortcuts import render
from sklearn import metrics
from core.models import State,Dataset,RegionDataset
from django.core import serializers
from django.db.models import Avg, Count
from django.http import JsonResponse
import json as simplejson
import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression



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
    return render(request, 'machineLearning/statecomparsion.html', {"data": data,"welcome":"State Comparison","statecomparison":"active"})

def index(request):
    return render(request, 'machineLearning/index.html')

def rainPredication(request):
    stateName = RegionDataset.objects.values_list('SUBDIVISION', flat=True).distinct()
    data = {
        "stateList": list(stateName)
    }
    return render(request,"machineLearning/prediction.html", {"data": data,"welcome":"Prediction Page","rainpredictor":"active"})

def makePrediction(request):
    Data = request.POST["dataset"]
    dict_data = simplejson.loads(Data)
    print(type(dict_data))
    nameSate = dict_data["stateinput"]
    print(nameSate)
    prepare_dataset = RegionDataset.objects.filter(SUBDIVISION=dict_data['stateinput']).values("ANNUAL","Jan_Feb","Mar_May","Jun_Sep","Oct_Dec");
    dataset = pd.DataFrame(prepare_dataset)
    X = dataset[['Jan_Feb', 'Mar_May', 'Jun_Sep','Oct_Dec']]
    Y = dataset['ANNUAL'].values.reshape(-1,1)
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.20,random_state=1)
    regr = LinearRegression()
    regr.fit(X_train, Y_train)
    y2_pred = regr.predict(X_test)
    final_test = pd.DataFrame({"Jan_Feb":[int(dict_data['jan_feb'])], "Mar_May":[int(dict_data['mar_may'])], "Jun_Sep":[int(dict_data["jun_sep"])], "Oct_Dec":[int(dict_data["oct_dec"])]})
    print(final_test)
    final_output = regr.predict(final_test)
    print(final_output[0][0])
    data = {"final_output":final_output[0][0],"mean_square_error" : metrics.mean_squared_error(Y_test, y2_pred), "root_mean_square_error" : np.sqrt(metrics.mean_squared_error(Y_test, y2_pred))}
    return JsonResponse({"data": data})
    #return render(request,"machineLearning/prediction.html",{"data": data})
    
def state_view(request, sid):
    #global annual_rain_d,annual_data, year_d, annual_bar_data
    # Loading Data from local disk []
    
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
