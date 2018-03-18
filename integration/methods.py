"""
An entire file for you to expand. Add methods here, and the client should be
able to call them with json-rpc without any editing to the pipeline.
"""
from final_predictor import *
# some data in text 
def predict_delay(number):
    input = number.split(" ")
    return give_answer(input[0],input[1])


#print(predict_delay("14512 2017-03-03"))