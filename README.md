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

