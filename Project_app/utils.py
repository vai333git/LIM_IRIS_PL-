# Write small Python functions and classes to make common patterns shorter and easier 
# it is not a complete collections

import pickle
import json
import config
import numpy as np

class Flower():
    
    def __init__(self,SepalLengthCm,SepalWidthCm,PetalWidthCm,Species):
        #constructor for creating instances of all the variables    
             
        self.SepalLengthCm  = SepalLengthCm
        self.SepalWidthCm   = SepalWidthCm      
        self.PetalWidthCm   = PetalWidthCm
        self.Species        = Species 
        

    def load_model(self):
        print('we are in load_module_function')
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)
        
        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)

    def get_predicted_pl(self):
        self.load_model()

        test_array = np.zeros(len(self.json_data['columns']))

        test_array[0] = self.SepalLengthCm
        test_array[1] = self.SepalWidthCm
        test_array[2] = self.PetalWidthCm
        test_array[3] = self.json_data["Species"][self.Species]
        

        print('test array is :' , test_array)
        predicted_pl=self.model.predict([test_array])

        return predicted_pl
