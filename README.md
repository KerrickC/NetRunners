# NetRunners

A tool for penetration testing purposes that will allow a user to enter text into forms on a website in a way that appears to be from actual keystrokes.

## How to run [Windows]

1. Setup a python virtual environment
   - (a) Run `pip install virtualenv`
   - (b) Run `mkdir env`
   - (c) Run 
            `python -m venv [/dir/of/project/env]` (i.e. C:\NetRunners\env)
   - (d) Run `cd [/dir/of/project/env/scripts] (i.e. C:\NetRunners\env\Scripts)`
   - (e) Run `activate`

2. Install dependencies
   - (a) Run `cd [/dir/of/project] (i.e. C:\NetRunners)`
   - (b) Run `pip install -r requirements.txt`

3. Start program
   - (a) Run `cd [/dir/of/project/src] (i.e. C:\NetRunners\src)`
   - (b) Run `python main.py`


## Steps to re-run program during different session [Windows] ## 
1. Setup a python virtual environment
   - (a) Run `cd [/dir/of/project/env/scripts] (i.e. C:\NetRunners\env\Scripts)`
   - (b) Run `activate`

2. Start program
   - (a) Run `cd [/dir/of/project/src] (i.e. C:\NetRunners\src)`
   - (b) Run `python main.py`
   
   
## How to run [Mac]
1. Setup a python virtual environment
   - (a) Run `pip install virtualenv`
   - (b) Run `python -m venv [/dir/of/project]/NetRunners/env`
   - (c) Run `source [/dir/of/project]/NetRunners/env/Scripts/activate`

2. Install dependencies
   - (a) Run `pip install -r ./requirements.txt`

3. Start program
   - (a) Run `python ./src/main.py`


## Steps to re-run program during different session [Mac] ## 
1. Setup a python virtual environment
   - (a) Run `source [/dir/of/project]/NetRunners/env/Scripts/activate`

2. Start program
   - (a) Run `python ./src/main.py`
