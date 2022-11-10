from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect  
from app.forms import MLForm  
from django.template import RequestContext
import pandas as pd
import sys
import scipy
import numpy
import matplotlib
import pandas
import sklearn
import pandas as pd
import seaborn as sns
import pickle

#Loading libraries
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import os
# Create your views here.  
def indx(request):  
        if request.method == "POST":  
           form = MLForm(request.POST)  
           if form.is_valid():  
                try:  
                    c = form.cleaned_data
                    v1 = c.get('v1')
                    v2 = c.get('v2')
                    v3 = c.get('v3')
                    v4 = c.get('v4')
                    #Predicting
                    tmp={}
                    tmp[0]=float(v1)
                    tmp[1]=float(v2)
                    tmp[2]=float(v3)
                    tmp[3]=float(v4)
                    dt=pd.DataFrame({'x':tmp}).transpose()
                    print(dt)
                    #filename = 'finalized_model.sav'
                    rslt = '';
                    try:
                        module_dir = os.path.dirname(__file__)  
                        filename = os.path.join(module_dir, 'finalized_model.sav')
                        loaded_model = pickle.load(open(filename, 'rb'))
                        predictions = loaded_model.predict(dt)[0]
                    except Exception as e:
                        print('Erro: ' + str(e))                     
                        rslt = '' + e                     
                    rslt = '' + predictions          
                    return render(request,'index.html',{'rslt':rslt})  
                except: 
                    pass  
        else:    
            return render(request,'index.html',{'rslt':'No data'}) 