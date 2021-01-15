The clustering of mealData is done by using meal amount data to predict the labels.
Programming Language: Python 3.6.8 64-bit
IDE: Google Colab

Data-input:
CGMData.csv      (Patient 1)
InsulinData.csv  (Patient 1)

For the above project we have imported below libraries
1. Pandas
2. pickle
3. csv
4. numpy
5. scipy
6. sklearn

Execution
---------
To obtain the result.csv file, run the Assignment3_Clustering.py



Submission Details
------------------
Assignment3_Clustering.py
results.csv
READ_ME file

Results:
----------------- K-means---------------
SSE of K_means clustering is :  33.673487069091095
Entropy_i
 [2.129467615801554, 2.2138652555979847, 1.94601841961535, 2.1436142040184207, 2.20105307512157, 2.019957462697487]
Purity_i
 [0.36893203883495146, 0.3142857142857143, 0.373134328358209, 0.2972972972972973, 0.2903225806451613, 0.36363636363636365]
Whole Entropy =  2.1192900735187843
Whole Purity =  0.3333333333333333

----------------- DBSCAN---------------
SSE of DBSCAN Clustering is:  187.61694868113133
Entropy_i
 [1.9764438290006863, 2.1435581332485114, 2.2253772246670707, 1.8048956511448035, 1.539484756931502, 1.1567796494470395]
Purity_i
 [0.4, 0.2876712328767123, 0.29338842975206614, 0.391304347826087, 0.45454545454545453, 0.7]
Whole Entropy =  2.12296281275061
Whole Purity =  0.31601731601731603

[33.673487069091095, 187.61694868113133, 2.1192900735187843, 2.12296281275061, 0.3333333333333333, 0.31601731601731603]