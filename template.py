import os
from pathlib import Path
import logging

while True:
    project_name = input("Enter your project name: ") # src, abc, xyz
    if project_name !='':
        break



# we want some folder and some files -> 
# 1. We need to defiene / ask user to enter  Project name -> Project SOurce Dir
# 2. WHicht types of the project folder and files we want
# 3. we need to split complete folder and complete files
# 4. we need to define our main project folder dir /  main source dir.
# 5. Create your complete folder and files




list_of_files = [

    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/utils/__init__.py",
    f"config/config.yaml",
    "schema.yaml",
    "requirements.txt",
    "setup.py",
    "main.py",
    "README.md"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating a new directory at : {filedir} for file: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating a new file: {filename} for path: {filepath}")
    else:
        logging.info(f"file is already present at: {filepath}")