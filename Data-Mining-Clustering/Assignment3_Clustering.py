# -*- coding: utf-8 -*-
"""Welcome To Colaboratory

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb

<p><img alt="Colaboratory logo" height="45px" src="/img/colab_favicon.ico" align="left" hspace="10px" vspace="0px"></p>

<h1>What is Colaboratory?</h1>

Colaboratory, or "Colab" for short, allows you to write and execute Python in your browser, with 
- Zero configuration required
- Free access to GPUs
- Easy sharing

Whether you're a **student**, a **data scientist** or an **AI researcher**, Colab can make your work easier. Watch [Introduction to Colab](https://www.youtube.com/watch?v=inN8seMm7UI) to learn more, or just get started below!

## **Getting started**

The document you are reading is not a static web page, but an interactive environment called a **Colab notebook** that lets you write and execute code.

For example, here is a **code cell** with a short Python script that computes a value, stores it in a variable, and prints the result:
"""

seconds_in_a_day = 24 * 60 * 60
seconds_in_a_day

"""To execute the code in the above cell, select it with a click and then either press the play button to the left of the code, or use the keyboard shortcut "Command/Ctrl+Enter". To edit the code, just click the cell and start editing.

Variables that you define in one cell can later be used in other cells:
"""

seconds_in_a_week = 7 * seconds_in_a_day
seconds_in_a_week

"""Colab notebooks allow you to combine **executable code** and **rich text** in a single document, along with **images**, **HTML**, **LaTeX** and more. When you create your own Colab notebooks, they are stored in your Google Drive account. You can easily share your Colab notebooks with co-workers or friends, allowing them to comment on your notebooks or even edit them. To learn more, see [Overview of Colab](/notebooks/basic_features_overview.ipynb). To create a new Colab notebook you can use the File menu above, or use the following link: [create a new Colab notebook](http://colab.research.google.com#create=true).

Colab notebooks are Jupyter notebooks that are hosted by Colab. To learn more about the Jupyter project, see [jupyter.org](https://www.jupyter.org).

## Data science

With Colab you can harness the full power of popular Python libraries to analyze and visualize data. The code cell below uses **numpy** to generate some random data, and uses **matplotlib** to visualize it. To edit the code, just click the cell and start editing.
"""

import numpy as np
from matplotlib import pyplot as plt

ys = 200 + np.random.randn(100)
x = [x for x in range(len(ys))]

plt.plot(x, ys, '-')
plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)

plt.title("Sample Visualization")
plt.show()

"""You can import your own data into Colab notebooks from your Google Drive account, including from spreadsheets, as well as from Github and many other sources. To learn more about importing data, and how Colab can be used for data science, see the links below under [Working with Data](#working-with-data).

## Machine learning

With Colab you can import an image dataset, train an image classifier on it, and evaluate the model, all in just [a few lines of code](https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/quickstart/beginner.ipynb). Colab notebooks execute code on Google's cloud servers, meaning you can leverage the power of Google hardware, including [GPUs and TPUs](#using-accelerated-hardware), regardless of the power of your machine. All you need is a browser.

Colab is used extensively in the machine learning community with applications including:
- Getting started with TensorFlow
- Developing and training neural networks
- Experimenting with TPUs
- Disseminating AI research
- Creating tutorials

To see sample Colab notebooks that demonstrate machine learning applications, see the [machine learning examples](#machine-learning-examples) below.

## More Resources

### Working with Notebooks in Colab
- [Overview of Colaboratory](/notebooks/basic_features_overview.ipynb)
- [Guide to Markdown](/notebooks/markdown_guide.ipynb)
- [Importing libraries and installing dependencies](/notebooks/snippets/importing_libraries.ipynb)
- [Saving and loading notebooks in GitHub](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb)
- [Interactive forms](/notebooks/forms.ipynb)
- [Interactive widgets](/notebooks/widgets.ipynb)
- <img src="/img/new.png" height="20px" align="left" hspace="4px" alt="New"></img>
 [TensorFlow 2 in Colab](/notebooks/tensorflow_version.ipynb)

<a name="working-with-data"></a>
### Working with Data
- [Loading data: Drive, Sheets, and Google Cloud Storage](/notebooks/io.ipynb) 
- [Charts: visualizing data](/notebooks/charts.ipynb)
- [Getting started with BigQuery](/notebooks/bigquery.ipynb)

### Machine Learning Crash Course
These are a few of the notebooks from Google's online Machine Learning course. See the [full course website](https://developers.google.com/machine-learning/crash-course/) for more.
- [Intro to Pandas](/notebooks/mlcc/intro_to_pandas.ipynb)
- [Tensorflow concepts](/notebooks/mlcc/tensorflow_programming_concepts.ipynb)
- [First steps with TensorFlow](/notebooks/mlcc/first_steps_with_tensor_flow.ipynb)
- [Intro to neural nets](/notebooks/mlcc/intro_to_neural_nets.ipynb)
- [Intro to sparse data and embeddings](/notebooks/mlcc/intro_to_sparse_data_and_embeddings.ipynb)

<a name="using-accelerated-hardware"></a>
### Using Accelerated Hardware
- [TensorFlow with GPUs](/notebooks/gpu.ipynb)
- [TensorFlow with TPUs](/notebooks/tpu.ipynb)

<a name="machine-learning-examples"></a>

## Machine Learning Examples

To see end-to-end examples of the interactive machine learning analyses that Colaboratory makes possible, check out these  tutorials using models from [TensorFlow Hub](https://tfhub.dev).

A few featured examples:

- [Retraining an Image Classifier](https://tensorflow.org/hub/tutorials/tf2_image_retraining): Build a Keras model on top of a pre-trained image classifier to distinguish flowers.
- [Text Classification](https://tensorflow.org/hub/tutorials/tf2_text_classification): Classify IMDB movie reviews as either *positive* or *negative*.
- [Style Transfer](https://tensorflow.org/hub/tutorials/tf2_arbitrary_image_stylization): Use deep learning to transfer style between images.
- [Multilingual Universal Sentence Encoder Q&A](https://tensorflow.org/hub/tutorials/retrieval_with_tf_hub_universal_encoder_qa): Use a machine learning model to answer questions from the SQuAD dataset.
- [Video Interpolation](https://tensorflow.org/hub/tutorials/tweening_conv3d): Predict what happened in a video between the first and the last frame.
"""

# importing the required packages
import pandas as pd
import numpy as np
import scipy.stats
from scipy.fftpack import fft
from scipy.stats import skew
from scipy.fftpack import fft
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import normalize
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans 
from sklearn.cluster import DBSCAN
from sklearn import metrics
import statistics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_validate,train_test_split,StratifiedKFold,KFold
import pickle
from collections import OrderedDict 

#*******************************CALCULATION OF GROUND TRUTH****************************************

mydateparser_p1 = lambda x: pd.datetime.strptime(x, '%m/%d/%Y')
RAW_INSULIN_DATA_P1 = pd.read_csv('InsulinData.csv', parse_dates=['Date'], date_parser=mydateparser_p1)
RAW_INSULIN_DATA_P1 = RAW_INSULIN_DATA_P1[["Date", "Time", "BWZ Carb Input (grams)"]]  
RAW_INSULIN_DATA_P1['Time'] = pd.to_timedelta(RAW_INSULIN_DATA_P1["Time"])
#print(RAW_INSULIN_DATA)
bool_series = pd.notnull(RAW_INSULIN_DATA_P1["BWZ Carb Input (grams)"])
INSULIN_DATA_WITH_ZEROS_P1 = RAW_INSULIN_DATA_P1[bool_series]
INSULIN_DATA_P1 = INSULIN_DATA_WITH_ZEROS_P1[INSULIN_DATA_WITH_ZEROS_P1["BWZ Carb Input (grams)"]>0]
#pd.set_option('display.max_rows', INSULIN_DATA.shape[0]+1)
INSULIN_DATA_P1['Date_Time'] = INSULIN_DATA_P1['Date'] + INSULIN_DATA_P1['Time']
#print(INSULIN_DATA_P1)
INSULIN_DATA_P1.dtypes

MEAL_SORTED_INSULIN_DATA_P1 = pd.DataFrame()

total_rows_P1 = INSULIN_DATA_P1.shape[0]
index_P1=total_rows_P1-1
df1_P1 = pd.DataFrame()
while index_P1>=0:
    data_arr_P1 = INSULIN_DATA_P1.iloc[index_P1].values
    df1_P1[index_P1] = data_arr_P1[::-1]
    index_P1 = index_P1 - 1

MEAL_SORTED_INSULIN_DATA_P1 = MEAL_SORTED_INSULIN_DATA_P1.append(df1_P1.transpose())
#MEAL_SORTED_INSULIN_DATA_P1.interpolate(method='linear', inplace=True)
MEAL_SORTED_INSULIN_DATA_P1 = MEAL_SORTED_INSULIN_DATA_P1[[3, 2, 1, 0]]
MEAL_SORTED_INSULIN_DATA_P1 = MEAL_SORTED_INSULIN_DATA_P1.rename(columns={3: 'Date', 2: 'Time', 1: 'Carb_Value', 0: 'Date_Time'})
pd.set_option('display.max_columns', None)
#print('MEAL_SORTED')
#print(MEAL_SORTED_INSULIN_DATA_P1)

Meal_Indices_to_be_dropped_P1=list()
total_rows_1_P1 = MEAL_SORTED_INSULIN_DATA_P1.shape[0]
index_1_P1=total_rows_1_P1-1
required_time_diff_P1 = pd.to_timedelta('0 days 02:00:00')
for i in range(0, total_rows_1_P1-1):
  j = i+1
  a = MEAL_SORTED_INSULIN_DATA_P1['Date_Time'][index_1_P1-i]
  #print(a)
  b = MEAL_SORTED_INSULIN_DATA_P1['Date_Time'][index_1_P1-j]
  #print(b)
  time_diff_P1 = b-a
  if(time_diff_P1<required_time_diff_P1): 
    Meal_Indices_to_be_dropped_P1.insert(0,index_1_P1-i)
    #print(index_1-i)
#print(Meal_Indices_to_be_dropped_P1)

for index_1_P1 in Meal_Indices_to_be_dropped_P1:
  MEAL_SORTED_INSULIN_DATA_P1 = MEAL_SORTED_INSULIN_DATA_P1.drop(index_1_P1)

MEAL_SORTED_INSULIN_DATA_P1 = MEAL_SORTED_INSULIN_DATA_P1.reset_index(drop=True)
pd.set_option('display.max_rows', MEAL_SORTED_INSULIN_DATA_P1.shape[0]+1)
#print(MEAL_SORTED_INSULIN_DATA_P1)

mydateparser_P1 = lambda x: pd.datetime.strptime(x, '%m/%d/%Y')
RAW_CGM_DATA_P1 = pd.read_csv('CGMData.csv', parse_dates=['Date'], date_parser=mydateparser_P1)
RAW_CGM_DATA_P1 = RAW_CGM_DATA_P1[["Date", "Time", "Sensor Glucose (mg/dL)"]]  
RAW_CGM_DATA_P1['Time'] = pd.to_timedelta(RAW_CGM_DATA_P1["Time"])
RAW_CGM_DATA_P1['Date_Time'] = RAW_CGM_DATA_P1['Date'] + RAW_CGM_DATA_P1['Time']

CGM_MEAL_VECTOR_P1 = pd.DataFrame(columns=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29])
#CGM_MEAL_VECTOR = RAW_CGM_DATA[index_2-100:index_2-50]
#print(CGM_MEAL_VECTOR)

#print(MEAL_SORTED_INSULIN_DATA_P1['Carb_Value'][0])
y_P1 = MEAL_SORTED_INSULIN_DATA_P1['Date_Time'][0]
#print(y)
time_list_P1 = []
Carb_list_P1 = []
#Carb_list_P1 = MEAL_SORTED_INSULIN_DATA_P1['Carb_Value'].tolist()
time_list_P1 = RAW_CGM_DATA_P1['Date_Time'].tolist()
time_list_P1.reverse()
#print(time_list)
glucose_list_P1 = RAW_CGM_DATA_P1['Sensor Glucose (mg/dL)'].tolist()
glucose_list_P1.reverse()
#print(glucose_list)
#print(len(time_list))
#print(len(glucose_list))

i = 0
for j in range(0,len(MEAL_SORTED_INSULIN_DATA_P1['Date_Time'])):
  y_P1 = MEAL_SORTED_INSULIN_DATA_P1['Date_Time'][j]
  temp_P1 = []
  while time_list_P1[i]<y_P1  and i<len(time_list_P1):
    i=i+1
  if i>=len(time_list_P1):
    break
  temp_P1 = glucose_list_P1[i-6:i+24]
  #if(time_list[i-5]>=y-required_time_30 and time_list[i+25]<=y+required_time_2):
  if(len(temp_P1)==30):
    CGM_MEAL_VECTOR_P1.loc[len(CGM_MEAL_VECTOR_P1), :] = temp_P1
    t = MEAL_SORTED_INSULIN_DATA_P1['Carb_Value'][j]
    Carb_list_P1.append(t)
  #print(CGM_MEAL_VECTOR)
  i = i+25
#print(len(Carb_list_P1))

Carb_Values_P1 = pd.DataFrame(Carb_list_P1,columns=['Meal_Amount'])
#print(len(Carb_Values_P1))
CGM_MEAL_VECTOR_P1 = pd.concat([CGM_MEAL_VECTOR_P1, Carb_Values_P1], axis=1)
#print(CGM_MEAL_VECTOR_P1)
CGM_MEAL_VECTOR_P1 = CGM_MEAL_VECTOR_P1.dropna()
#print(CGM_MEAL_VECTOR_P1)
CGM_MEAL_VECTOR_P1 = CGM_MEAL_VECTOR_P1.reset_index(drop=True)
#CGM_MEAL_VECTOR_P1 = CGM_MEAL_VECTOR_P1.head(n=200)

Carb_list_P1_refined = []
Carb_list_P1_refined = CGM_MEAL_VECTOR_P1['Meal_Amount'].tolist()
#print(Carb_list_P1_refined)
CGM_MEAL_VECTOR_P1 = CGM_MEAL_VECTOR_P1.drop(labels='Meal_Amount', axis=1)
#print(CGM_MEAL_VECTOR_P1)

min_meal_amount = min(Carb_list_P1_refined)
#print(min_meal_amount)
max_meal_amount = max(Carb_list_P1_refined)
#print(max_meal_amount)

ground_truth_list = []

i=0
while(i<len(Carb_list_P1_refined)):
    if (Carb_list_P1_refined[i]>=min_meal_amount and Carb_list_P1_refined[i]<(min_meal_amount+20)):
      ground_truth_list.append(1)
    elif (Carb_list_P1_refined[i]>=(min_meal_amount+20) and Carb_list_P1_refined[i]<(min_meal_amount+20*2)):
      ground_truth_list.append(2)
    elif (Carb_list_P1_refined[i]>=(min_meal_amount+20*2) and Carb_list_P1_refined[i]<(min_meal_amount+20*3)):
      ground_truth_list.append(3)
    elif (Carb_list_P1_refined[i]>=(min_meal_amount+20*3) and Carb_list_P1_refined[i]<(min_meal_amount+20*4)):
      ground_truth_list.append(4)
    elif (Carb_list_P1_refined[i]>=(min_meal_amount+20*4) and Carb_list_P1_refined[i]<(min_meal_amount+20*5)):
      ground_truth_list.append(5)
    elif (Carb_list_P1_refined[i]>=(min_meal_amount+20*5) and Carb_list_P1_refined[i]<(min_meal_amount+20*6)):
      ground_truth_list.append(6)
    else:
      ground_truth_list.append(7)         
    i = i+1

#print(ground_truth_list)
Ground_Truth = pd.DataFrame(ground_truth_list,columns=['Ground_Truth'])
CGM_MEAL_VECTOR_P1 = pd.concat([CGM_MEAL_VECTOR_P1, Ground_Truth], axis=1)

#print(CGM_MEAL_VECTOR_P1)

#********************************************* END OF GROUND TRUTH CALCULATION ********************************************

#********************************** FEATURE EXTRACTION *************************************************************

mydateparser_p1 = lambda x: pd.datetime.strptime(x, '%m/%d/%Y')
RAW_INSULIN_DATA_P1 = pd.read_csv('InsulinData.csv', parse_dates=['Date'], date_parser=mydateparser_p1)
RAW_INSULIN_DATA_P1 = RAW_INSULIN_DATA_P1[["Date", "Time", "BWZ Carb Input (grams)"]]  
RAW_INSULIN_DATA_P1['Time'] = pd.to_timedelta(RAW_INSULIN_DATA_P1["Time"])
#print(RAW_INSULIN_DATA)
bool_series = pd.notnull(RAW_INSULIN_DATA_P1["BWZ Carb Input (grams)"])
INSULIN_DATA_WITH_ZEROS_P1 = RAW_INSULIN_DATA_P1[bool_series]
INSULIN_DATA_P1 = INSULIN_DATA_WITH_ZEROS_P1[INSULIN_DATA_WITH_ZEROS_P1["BWZ Carb Input (grams)"]>0]
#pd.set_option('display.max_rows', INSULIN_DATA.shape[0]+1)
INSULIN_DATA_P1['Date_Time'] = INSULIN_DATA_P1['Date'] + INSULIN_DATA_P1['Time']
#print(INSULIN_DATA_P1)
INSULIN_DATA_P1.dtypes


MEAL_SORTED_INSULIN_DATA_P1 = pd.DataFrame()
NO_MEAL_SORTED_INSULIN_DATA_P1 = pd.DataFrame()

total_rows_P1 = INSULIN_DATA_P1.shape[0]
index_P1=total_rows_P1-1
df1_P1 = pd.DataFrame()
while index_P1>=0:
    data_arr_P1 = INSULIN_DATA_P1.iloc[index_P1].values
    df1_P1[index_P1] = data_arr_P1[::-1]
    index_P1 = index_P1 - 1

MEAL_SORTED_INSULIN_DATA_P1 = MEAL_SORTED_INSULIN_DATA_P1.append(df1_P1.transpose())
#MEAL_SORTED_INSULIN_DATA_P1.interpolate(method='linear', inplace=True)
MEAL_SORTED_INSULIN_DATA_P1 = MEAL_SORTED_INSULIN_DATA_P1[[3, 2, 1, 0]]
MEAL_SORTED_INSULIN_DATA_P1 = MEAL_SORTED_INSULIN_DATA_P1.rename(columns={3: 'Date', 2: 'Time', 1: 'Carb_Value', 0: 'Date_Time'})
pd.set_option('display.max_columns', None)
#print('MEAL_SORTED')
#print(MEAL_SORTED_INSULIN_DATA_P1)

Meal_Indices_to_be_dropped_P1=list()
total_rows_1_P1 = MEAL_SORTED_INSULIN_DATA_P1.shape[0]
index_1_P1=total_rows_1_P1-1
required_time_diff_P1 = pd.to_timedelta('0 days 02:00:00')
for i in range(0, total_rows_1_P1-1):
  j = i+1
  a = MEAL_SORTED_INSULIN_DATA_P1['Date_Time'][index_1_P1-i]
  #print(a)
  b = MEAL_SORTED_INSULIN_DATA_P1['Date_Time'][index_1_P1-j]
  #print(b)
  time_diff_P1 = b-a
  if(time_diff_P1<required_time_diff_P1): 
    Meal_Indices_to_be_dropped_P1.insert(0,index_1_P1-i)
    #print(index_1-i)
#print(Meal_Indices_to_be_dropped_P1)

for index_1_P1 in Meal_Indices_to_be_dropped_P1:
  MEAL_SORTED_INSULIN_DATA_P1 = MEAL_SORTED_INSULIN_DATA_P1.drop(index_1_P1)

MEAL_SORTED_INSULIN_DATA_P1 = MEAL_SORTED_INSULIN_DATA_P1.reset_index(drop=True)
pd.set_option('display.max_rows', MEAL_SORTED_INSULIN_DATA_P1.shape[0]+1)
#print(MEAL_SORTED_INSULIN_DATA_P1)

mydateparser_P1 = lambda x: pd.datetime.strptime(x, '%m/%d/%Y')
RAW_CGM_DATA_P1 = pd.read_csv('CGMData.csv', parse_dates=['Date'], date_parser=mydateparser_P1)
RAW_CGM_DATA_P1 = RAW_CGM_DATA_P1[["Date", "Time", "Sensor Glucose (mg/dL)"]]  
RAW_CGM_DATA_P1['Time'] = pd.to_timedelta(RAW_CGM_DATA_P1["Time"])
RAW_CGM_DATA_P1['Date_Time'] = RAW_CGM_DATA_P1['Date'] + RAW_CGM_DATA_P1['Time']


CGM_MEAL_VECTOR_P1 = pd.DataFrame(columns=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29])
#CGM_MEAL_VECTOR = RAW_CGM_DATA[index_2-100:index_2-50]
#print(CGM_MEAL_VECTOR)

#print(MEAL_SORTED_INSULIN_DATA['Date_Time'][0])
y_P1 = MEAL_SORTED_INSULIN_DATA_P1['Date_Time'][0]
#print(y)
time_list_P1 = []
time_list_P1 = RAW_CGM_DATA_P1['Date_Time'].tolist()
time_list_P1.reverse()
#print(time_list)
glucose_list_P1 = RAW_CGM_DATA_P1['Sensor Glucose (mg/dL)'].tolist()
glucose_list_P1.reverse()
#print(glucose_list)
#print(len(time_list))
#print(len(glucose_list))

i = 0
for j in range(0,len(MEAL_SORTED_INSULIN_DATA_P1['Date_Time'])):
  y_P1 = MEAL_SORTED_INSULIN_DATA_P1['Date_Time'][j]
  temp_P1 = []
  while time_list_P1[i]<y_P1  and i<len(time_list_P1):
    i=i+1
  if i>=len(time_list_P1):
    break
  temp_P1 = glucose_list_P1[i-6:i+24]
  #if(time_list[i-5]>=y-required_time_30 and time_list[i+25]<=y+required_time_2):
  if(len(temp_P1)==30):
    CGM_MEAL_VECTOR_P1.loc[len(CGM_MEAL_VECTOR_P1), :] = temp_P1
  #print(CGM_MEAL_VECTOR)
  i = i+25
#print(CGM_MEAL_VECTOR)

CGM_MEAL_VECTOR_P1 = CGM_MEAL_VECTOR_P1.dropna()      
CGM_MEAL_VECTOR_P1 = CGM_MEAL_VECTOR_P1.reset_index(drop=True)
#CGM_MEAL_VECTOR_P1 = CGM_MEAL_VECTOR_P1.head(n=200)
#print(CGM_MEAL_VECTOR_P1);

Feature_Matrix_Meal_Data = pd.DataFrame() 
 
# Feature 1 - Windowed Mean (for 30 min interval)
win_size=6
total_vals = CGM_MEAL_VECTOR_P1.shape[1]-win_size
for index in range(0, total_vals, win_size):
    dm = CGM_MEAL_VECTOR_P1.iloc[:, index:index + win_size].mean(axis=1)
    Feature_Matrix_Meal_Data['Mean ' + str(index)] = dm

#Feature_Matrix_Meal_Data = Feature_Matrix_Meal_Data.drop('Mean ' + str(index), axis=1)
#print(Feature_Matrix_Meal_Data.shape)

    
# Feature 2 - Windowed Standard Deviation (for 30 min interval)
win_size=6
total_vals = CGM_MEAL_VECTOR_P1.shape[1]-win_size
for index in range(0, total_vals, win_size):
    dstd = CGM_MEAL_VECTOR_P1.iloc[:, index:index + win_size].std(axis=1)
    Feature_Matrix_Meal_Data['Std_deviation ' + str(index)] = dstd

#Feature_Matrix_Meal_Data = Feature_Matrix_Meal_Data.drop('Std_deviation ' + str(index), axis=1)        
#print(Feature_Matrix_Meal_Data.shape)
    
    
# Feature 3 - Fast Fourier Transform
FFT = pd.DataFrame()
def calculate_fft_vals(series):
    FFT_abs = abs(fft(series))
    FFT_abs.sort()
    return np.flip(FFT_abs)[0:8]

FFT['FFT_vals'] = CGM_MEAL_VECTOR_P1.apply(lambda series: calculate_fft_vals(series), axis=1)
FFT_Vals= pd.DataFrame(FFT.FFT_vals.tolist(), columns=['FFT1', 'FFT2', 'FFT3', 'FFT4', 'FFT5', 'FFT6', 'FFT7','FFT8'],index=FFT.FFT_vals.index)
Feature_Matrix_Meal_Data = pd.concat([Feature_Matrix_Meal_Data,FFT_Vals],axis=1)
    
#print(Feature_Matrix_Meal_Data.shape)
    
 
# Feature 4 - Max of CGM Velocity 
    
Velocity_Data = pd.DataFrame()
win_size=6
total_vals=CGM_MEAL_VECTOR_P1.shape[1]-win_size

for index in range(0, total_vals):
    dv = CGM_MEAL_VECTOR_P1.iloc[:, index + win_size] - CGM_MEAL_VECTOR_P1.iloc[:, index]
    Velocity_Data['vel'+str(index)] = dv

Feature_Matrix_Meal_Data['Max CGM Vel']=Velocity_Data.max(axis = 1,skipna=True)
    
#print(Feature_Matrix_Meal_Data.shape)
   
    
# Feature 5 - Skewness
def calculate_skewness(series):
    series_counts = series.value_counts()
    skewness_vals = skew(series_counts)
    return skewness_vals

Feature_Matrix_Meal_Data['skewness'] = CGM_MEAL_VECTOR_P1.apply(lambda row: calculate_skewness(row), axis=1)
    
#print(Feature_Matrix_Meal_Data.shape)

#*******************************************END OF FEATURE MATRIX CALCULATION*************************************

#***************************Standardize feature matrix**********************************
Feature_Matrix_Meal_Data = StandardScaler().fit_transform(Feature_Matrix_Meal_Data)
#print(Feature_Matrix_Meal_Data.shape)

# Normalize the data so that the data follows a Gaussian distribution
Feature_Matrix_norm = normalize(Feature_Matrix_Meal_Data)
Feature_Matrix_norm = pd.DataFrame(Feature_Matrix_norm)
    
# Do PCA
pca=PCA(n_components=2)
X_principal = pca.fit_transform(Feature_Matrix_norm)
X_principal = pd.DataFrame(X_principal)
X_principal.columns = ['PCA1','PCA2']

#print(X_principal)
#********************************* END *********************************************

#*********************** K-MEANS CLUSTERING ****************************************

print("----------------- K-means---------------")
      
clusterNum = 6
k_means = KMeans(init = "k-means++", n_clusters = clusterNum, n_init = 6)
k_means.fit(X_principal)
kmeans_labels = k_means.labels_
#print("K-means labels", kmeans_labels)
   
SSE_K_MEANS = k_means.inertia_
#print("-----------------------------------------")
print("SSE of K_means clustering is : ", SSE_K_MEANS)
#print("-----------------------------------------")
    
# Categorize all the rows into clusters formed by K-means
KMeans_Clusters = []                                                           
for bin in range (0, 6):                               
    new = []                  
    for i in range (0,len(kmeans_labels)):
        if(kmeans_labels[i]==bin):
            new.append(i)
    if new:            
      KMeans_Clusters.append(new)

#print(KMeans_Clusters)
       

Entropy_i_KMeans = []
Purity_i_KMeans = []
Cluster_list_KMeans =[]
Sum_of_each_row_KMeans = []

# Loop through each K-means cluster   
for c in range(0,6):
    kmeans_cluster = KMeans_Clusters[c]
    updated_label = 0 
    true_labels = []
    # Determine the ground truth label for the kmeans cluster based on majority
    for i in range(0,len(kmeans_cluster)):
        val = kmeans_cluster[i]
        true_labels.append(ground_truth_list[val])

    temp_series_KMeans = pd.Series(true_labels).value_counts()
    Cluster_list_KMeans.append(temp_series_KMeans.tolist())
    #print('List i\n', temp_series)
    sum_i_KMeans = sum(temp_series_KMeans)
    Sum_of_each_row_KMeans.append(sum_i_KMeans)
    purity_val_KMeans = (temp_series_KMeans).max()/sum(temp_series_KMeans)
    Purity_i_KMeans.append(purity_val_KMeans)
    entropy_val_KMeans = scipy.stats.entropy(temp_series_KMeans, base=2)
    Entropy_i_KMeans.append(entropy_val_KMeans)
    #print('entropy i', entropy_val)
   

#print('Cluster_list\n', Cluster_list_KMeans)
#print('Sum of each row\n', Sum_of_each_row_KMeans)
total_KMeans = sum(Sum_of_each_row_KMeans)
#print('Total\n', total_KMeans)
print('Entropy_i\n', Entropy_i_KMeans)
print('Purity_i\n', Purity_i_KMeans)

whole_Entropy_KMeans = 0
whole_Purity_KMeans = 0
for i in range(len(Entropy_i_KMeans)):
  whole_Entropy_KMeans = whole_Entropy_KMeans + (Sum_of_each_row_KMeans[i]/total_KMeans)*Entropy_i_KMeans[i]
  whole_Purity_KMeans = whole_Purity_KMeans + (Sum_of_each_row_KMeans[i]/total_KMeans)*Purity_i_KMeans[i]
print('Whole Entropy = ', whole_Entropy_KMeans)  
print('Whole Purity = ', whole_Purity_KMeans)  

#**************************** END OF K-MEANS CLUSTERING **********************************************************

#*********************Standardize CGM_MEAL_VECTOR_P1************************************

CGM_MEAL_VECTOR_PCA = StandardScaler().fit_transform(CGM_MEAL_VECTOR_P1)
#print(CGM_MEAL_VECTOR_PCA.shape)

# Normalize the data so that the data follows a Gaussian distribution
CGM_MEAL_VECTOR_PCA = normalize(CGM_MEAL_VECTOR_PCA)
CGM_MEAL_VECTOR_PCA = pd.DataFrame(CGM_MEAL_VECTOR_PCA)

#print(CGM_MEAL_VECTOR_PCA.shape)   

# Do PCA
pca=PCA(n_components=2)
PCA_principal = pca.fit_transform(CGM_MEAL_VECTOR_PCA)
PCA_principal = pd.DataFrame(PCA_principal)
PCA_principal.columns = ['PCA1','PCA2']

#print(PCA_principal)
#******************************* END *****************************************************

#************************** DBSCAN CLUSTERING ********************************************

print("----------------- DBSCAN---------------")
db = DBSCAN(eps=0.130, min_samples=7)
db.fit(X_principal)
db_labels = db.labels_
#print("DBSCAN labels", db_labels)
n_clusters_ = len(set(db_labels)) - (1 if -1 in db_labels else 0)
#print(n_clusters_)  
# Categorize all the rows into clusters formed by DBSCAN
DBSCAN_Clusters = []                                                           
for bin in range (-1, 6):                               
    new = []                  
    for i in range (0,len(db_labels)):
        if(db_labels[i]==bin):
            new.append(i) 
    if new:            
      DBSCAN_Clusters.append(new)




#print(DBSCAN_Clusters);    
       


Entropy_i_DBSCAN = []
Purity_i_DBSCAN = []
Cluster_list_DBSCAN =[]
Sum_of_each_row_DBSCAN = []

temp_df = pd.DataFrame()
temp_df_1 = pd.DataFrame()
temp_df_diff = pd.DataFrame()
temp_df_diff_square = pd.DataFrame()
temp_df_diff_square_sum = pd.DataFrame()
#sse = pd.DataFrame()
SSE_DBSCAN = []

# Loop through each DBSCAN cluster   
for c in range(0,len(DBSCAN_Clusters)):
    db_cluster = DBSCAN_Clusters[c]
    updated_label = 0 
    true_labels = []
    temp_df = PCA_principal.iloc[db_cluster,:]
    #print(temp_df)
    #[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
    temp_df_1 = temp_df[['PCA1','PCA2']].mean()
    #print(temp_df_1)
    temp_df_diff = temp_df.sub(temp_df_1, axis=1)
    #print(temp_df_diff)
    temp_df_diff_square = temp_df_diff**2
    #print(temp_df_diff_square)
    temp_df_diff_square_sum = temp_df_diff_square[['PCA1','PCA2']].sum()
    #print(temp_df_diff_square_sum)
    sse = sum(temp_df_diff_square_sum.tolist())
    SSE_DBSCAN.append(sse)
    

    # Determine the ground truth label for the dbscan cluster based on majority
    for i in range(0,len(db_cluster)):
        val = db_cluster[i]
        true_labels.append(ground_truth_list[val])

    temp_series_DBSCAN = pd.Series(true_labels).value_counts()
    #print(temp_series_DBSCAN)
    Cluster_list_DBSCAN.append(temp_series_DBSCAN.tolist())
    #print('List i\n', temp_series)
    sum_i_DBSCAN = sum(temp_series_DBSCAN)
    Sum_of_each_row_DBSCAN.append(sum_i_DBSCAN)
    purity_val_DBSCAN = (temp_series_DBSCAN).max()/sum(temp_series_DBSCAN)
    Purity_i_DBSCAN.append(purity_val_DBSCAN)
    entropy_val_DBSCAN = scipy.stats.entropy(temp_series_DBSCAN, base=2)
    Entropy_i_DBSCAN.append(entropy_val_DBSCAN)
    #print('entropy i', entropy_val)

Total_SSE_DBSCAN = sum(SSE_DBSCAN)
print('SSE of DBSCAN Clustering is: ', Total_SSE_DBSCAN)

#print('Cluster_list\n', Cluster_list_DBSCAN)
#print('Sum of each row\n', Sum_of_each_row_DBSCAN)
total_DBSCAN = sum(Sum_of_each_row_DBSCAN)
#print('Total\n', total_DBSCAN)
print('Entropy_i\n', Entropy_i_DBSCAN)
print('Purity_i\n', Purity_i_DBSCAN)

whole_Entropy_DBSCAN = 0
whole_Purity_DBSCAN = 0
for i in range(len(Entropy_i_DBSCAN)):
  whole_Entropy_DBSCAN = whole_Entropy_DBSCAN + (Sum_of_each_row_DBSCAN[i]/total_DBSCAN)*Entropy_i_DBSCAN[i]
  whole_Purity_DBSCAN = whole_Purity_DBSCAN + (Sum_of_each_row_DBSCAN[i]/total_KMeans)*Purity_i_DBSCAN[i]
print('Whole Entropy = ', whole_Entropy_DBSCAN)  
print('Whole Purity = ', whole_Purity_DBSCAN)

#**************************************** END OF DBSCAN CLUSTERING **************************************************

#SSE for Kmeans	SSE for DBSCAN	Entropy for Kmeans	Entropy for DBSCAN	Purity for K means	Purity for DBSCAN

result = []
result.append(SSE_K_MEANS)
result.append(Total_SSE_DBSCAN)
result.append(whole_Entropy_KMeans)
result.append(whole_Entropy_DBSCAN)
result.append(whole_Purity_KMeans)
result.append(whole_Purity_DBSCAN)

print(result)

results = pd.DataFrame(columns=[0,1,2,3,4,5])

results.loc[0,:]=result
results.to_csv('results.csv',header=None,index=False)