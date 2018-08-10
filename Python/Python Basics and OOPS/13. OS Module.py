import os

print(dir(os))  # It will print all the modules which are in OS

print(os.getcwd())  # It will print current working directory

#  To change the current working directory
os.chdir('/vagrant')
print(os.getcwd())
print(os.listdir())  # It will list all the files and folder of your default directory or you can pass the path

# To create the directory
os.mkdir('test')
os.makedirs('jay/test')

# To remove the directory
os.rmdir('test')
os.removedirs('jay/test')
