# API'S
from flask import Flask,render_template,jsonify,request
#importing the required functions from flask

#import our flower class from utils.py and project_app folder
from Project_app.utils import Flower

# Creates the Flask instance.
#  __name__ is the name of the current Python module.
#  The app needs to know where it's located to set up some paths.
#  __name__ is a convenient way to tell it that.
app = Flask(__name__)

######################################################################
############################## BASE / HOME API #######################
######################################################################

@app.route('/')
def Hello_Flask():
    print('Welcome to the Base API')
    return 'HI THIS BASE API'


@app.route('/predict_pl')
def get_predicted_p1():    
    
    SepalLengthCm   = 7.1 
    SepalWidthCm    = 3
    PetalWidthCm    = 2.1
    Species         = 'Iris-virginica'

    #creating instance of class
    fl = Flower(SepalLengthCm,SepalWidthCm,PetalWidthCm,Species)
    pl = fl.get_predicted_pl()
    
    return jsonify({'Result':f'Predicted PetalLengthCm of the test data is: {pl}'})
    

if __name__ == '__main__':
    app.run()                     
# it Allows You to Execute Code When the File Runs as a Script,
# but Not When It's Imported as a Module.
