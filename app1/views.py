from django.shortcuts import render,HttpResponse
import pickle
import joblib
# Create your views here.
def hello(request):
    return render(request,'app.html')
def predict(request):
    if request.method == 'POST':
        # load the model
        model=joblib.load('./app1/savedModels/appliance_Model.joblib')
        # get the input values from the form 
        temp=int(request.POST.get('temperature'))
        y_pred=model.predict([[temp]])
        print(f'y pred is {y_pred}')
        # return HttpResponse(f"The predicted appliance energy consumption is: {model.predict([[temp]])[0]}")

        return render(request,'app.html',{'result':y_pred})
    return render(request,'app.html')