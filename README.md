# How to Develop END-TO-END Projects on github with different modules?

## Below are the steps involved in this Process (this is the template file , we can use this file for any projects)

### 1. Set Up a Git Hub Repository 

1. Create a git hub repository and clone it into a folder.
2. Open VS code in the repository folder so that we can create modules in it.
3. Create two file in vscode :
   a. Setup.py : Setup script is the center of all the activities in building,distributing and installing modules.
   b. requirements.txt: It will consist of necessary libraries which will be required to implement this project.
4. Once we created the setup.py model ow to find out how many packages are there ?

- Create a new folder you can name anything you want i will name it src
-  So whenever the find_packages() will run in setup.py the file called __init__.py will be automatically consider thius source as a package itself and try to built it and we can import it anywhere.

5. There will be scenarios where we need many packages to automate this we write all the packages name in requirements.txt.
6. In requirements.txt I have written -e . then it triggers setup.py , now we need ensure that  -e . should not come in list of requirements.txt 
7. run the command in the terminal '''' pip install -r requirements.txt ''''


### Step 2 : Creating entire project structure and Creating common functionalities like logging, exception handling etc.

1. Create components folder in the src folder.Create an __init__.py file. This file is created because components will be created as a package and it can also be exported and imported. So here components are like modules such as data ingestion (reading data from some other location or database). Thus create another file in components named as data_ingestion , data_transformation, model_trainer.

2. Data Ingestion will have all the code of reading a data.
Dividing data into train , test validation 

3. Data Transformation.py will contain all data transformation techniques such as categorical to numerical features, one hot encoding,label encoding etc.

4. Model_trainer.py  Specially about training a model (training module), different types of model to be used, model testing parameters like confusion matric, r2 square.(Easist way to push the model directly from here to cloud)


5. Now create another folder in src naming pipeline. Here we define what kind of pipeline we are going to create. There are mainly two types of pipeline training pipeline and prediction pipeline. Create a file in pipeline named as train_pipeline. So from here you will trigger the components for training purpose. Create another pipeline called predict_pipeline.py here we will predict the new data.Also create __init__.py to import these pipelines in pipeline folder.

6. Since entire project implementation will be happening inside the src create three new files naming logger.py (For logs), exception.py(exception handling) and utils.py (any functionalities that we repeatedly use)

#### -------------------------------------------------------

#### Exception handling 

1. Here we are going to create our custom exception. So whenever we catches an exception in try and catch block the exception will be printed out from our own custom exception class  called error_message_detail .

2. Here we inherit the CustomException class and intialize our own custom message using error_message_detail.

3. It will then display which module, which line and what is the error

#### -------------------------------------------------------
#### Logging








