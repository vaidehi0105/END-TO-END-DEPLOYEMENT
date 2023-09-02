import sys
#If any exception is getting controlled then this sys library will automatically have that information


def error_message_detail(error,erro_detail:sys):
    _,_,exc_tb=erro_detail.exc_info()

    # from the exc_tb will tell us
    # #which file the exception has occured 
    # #which line number it is occured
   
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
    file_name,exc_tb.tb_lineno,str(error))

    return error_message
    
# whenever my error raises i will call error_message_detail
#function

class CustomException(Exception):
    # my own custom exception class

   def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
   def __str__(self):
        return self.error_message
    
    # whenever my error raises it will print 

# whenever i raise my custom exception it will be inheriting
#the parent exception , nd whatever error message is basically 
#this particular function (super.__init_(error_message))
#will be initialized to the output of our custom exception

