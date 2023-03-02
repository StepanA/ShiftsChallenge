# ShiftsChallenge
Second place ShiftsChallenge Weather track solution  
Data, metrics and other information about challenge can be found here https://research.yandex.com/shifts/weather  
Solution description can be found here https://github.com/StepanA/ShiftsChallenge/blob/main/report/Shifts%20ChallengeWeather%20Prediction.pdf

## Reproduce the solution
To reproduce the result, follow these steps:
1. Copy the files train.csv, dev_in.csv, dev_out.csv, eval.csv to the data\raw folder
2. Create a virtual environment. The required package versions are specified in the requirements.txt file. The virtual environment has been configured for python version 3.9.5
3. Run all cells in the notebook "1_Preprocess_data.ipynb"
   1. Two new features are generated 
   2. Missing values are filled
   3. Due to type casting, the size of the used memory is reduced
   4. Data will be saved to pickle files
4. Run all cells in notebooks starting with the prefix "2_Train ..." (5 notebooks in total), you can also download trained models from https://disk.yandex.ru/d/LxIgfxPf7yUeqA
   1. "2_Train Bronze.ipynb" and "2_Train Orange Box.ipynb" are used for uncertainty predictions
   2. "2_Train Purple Box.ipynb", "2_Train Aqua Box.ipynb" and "2_Train Silver Box.ipynb" are used for temperature predictions
5. Run all cells in the notebook "3_Inference Steel.ipynb"
   1. Uncertainty forecasts are blended with ensemble_uncertainties_regression function
   2. The mean of the model predictions is used as the temperature prediction
   3. Uncertainty forecasts are adjusted by the standard deviation of temperature forecasts
   4. Uncertainty predictions are adjusted for differences in feature distributions

