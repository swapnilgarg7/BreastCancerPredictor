
# Breast Cancer Predictor

A GUI program that predicts whether the patient has Breast Cancer or not using Machine Learning. 

# Libaries Used
[Tkinter](https://docs.python.org/3/library/tkinter.html)

[Joblib](https://joblib.readthedocs.io/en/latest/)

[Scikit-Learn](https://scikit-learn.org/)

[Numpy](https://numpy.org/doc/stable/)

[Pandas](https://pandas.pydata.org/pandas-docs/stable/)

[Seaborn](https://seaborn.pydata.org/)

[Matplotlib](https://matplotlib.org/stable/index.html)








# How to run the program

First install the modules by running the following command in terminal

```bash
  pip install -r requirements.txt
```

Then open the BCP.ipynb jupyter notebook if you want to train the model yourself, or you can skip this step and use the pre-loaded BCP_model.joblib file.

Run all cells in the jupyter notebook. This will create your BCP_model.joblib file

Then you can run the main program by running this in terminal:


```bash
  python3 main.py
```
After it launches, click the Predict button so the program starts.

Then enter the values of the paramaters given and then click Submit

The program will than show a popup message box telling whether the patient has breast cancer(malignant) or not(benign)





# How it works

**Machine Learning**

The dataset was obtained from [kaggle](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data?resource=download)

First the data was analysed with the help of pandas library for information and matplotlib and seaborn libraries for graphical analysis

The data was then pre-processed and then split to training and testing set.

[Random Forest Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)
was used as it gave the best accuracy and was the most efficient model to use
for this project. 

After the model was trained, it was saved to a joblib file so that it can be accessed in the main GUI program


**GUI**

The graphical interface was made using tkinter module. When the patient's details are entered
regarding the breast, these are sent to the saved ML model to predict whether the patient has cancer or not.

Depending on the result(0 or 1), a message box is displayed with the respective result.
# Demo Images

**Case 1 : Patient has Breast Cancer**
![image](https://user-images.githubusercontent.com/32569674/165743041-3ed8d473-9571-490a-bc5f-1175cad4e35d.png)
![image](https://user-images.githubusercontent.com/32569674/165743075-e8992e46-0362-4627-896a-7b22a80e713f.png)

**Case 2 : Patient does not have Breast Cancer**
![image](https://user-images.githubusercontent.com/32569674/165742889-1eb612b4-3973-4c46-91d4-9ee344b841d2.png)
![image](https://user-images.githubusercontent.com/32569674/165742943-5877f95d-7a86-4e66-b1cd-456f7a0419e2.png)
)

