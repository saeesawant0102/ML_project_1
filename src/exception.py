import sys
from src.logger import logging

#whenever error raises this function is called
def error_message_detail(error,error_detail:sys): #sys will have the error details
    _,_,exc_tb=error_detail.exc_info() #exc_tb will have exact info where the erro has occured in which file and all
    file_name=exc_tb.tb_frame.f_code.co_filename #filename in which error has occured
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

    

class CustomException(Exception): 
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message) #inheriting the __init__ function
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    #whenever CustomException is raised. It is inheriting the parent exception.Whatever error message is coming from there, it is assigned to the error_message variable. 
    def __str__(self):
        return self.error_message #so whenever printing, error_message will be displayed
    
'''
if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by zero error")
        raise CustomException(e,sys)
'''