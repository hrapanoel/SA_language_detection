# South African language detection

This is the code to build a South African languages detection using a Mulinomial Naive Bayes classifier on character n-grams. Training and testing data are from https://github.com/praekelt/feersum-lid-shared-task/tree/master/lid_task_2017a

# Code

The model is trained in `South African language detection.ipynb`

The trained model is saved in `language_detect.joblib` but due to the size limitation, it cant be uploaded on github. You will have to generate it yourself (it doesnt take long).

`language_detection.py` renders a jupyter notebook widgets. The input is a sentence in any of the 11 languages and the output is the detected language. It requires the trained model to work.

## Dependencies for the jupyter widgets server

 * ipywidget_server
 * ipywidgets
 
## To use the widget

To serve the widget, go to the directory containing `language_detection.py` and run:

```$ ipywidgets-server language_detection:container```

This will serve the widget on `http://localhost:8866`
