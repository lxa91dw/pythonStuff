# pythonStuff
Python stuff folder holds my projects and information related to the Python programming I do.
good quick guide to using markdown files such as this one can be found <a href="https://confluence.atlassian.com/bitbucketserver/markdown-syntax-guide-776639995.html">here</a>
# Tools I use and guides
## Virtualenv
I use virtualenv to separate the requirements needed for each project I am working on.  Without this tool, every package that I have ever installed in my environment would need to be included in every project or I would need to keep track of them.  As of Python 3.3, virtualenv is included in the standard implementation of Python in package venv.  Documentation for venv can be found <a href="https://virtualenv.pypa.io/en/stable/">here</a>.  
* To start a new environment use command "virtualenv <Name of environment>" This will create a folder under current directory and create the necessary folders and files under that directory.
* use the command ". ./<Name of environment>/Scripts/activate" to activate the environment (linux) use source for Windows
* command "pip list" will show the list of packages available within this environment
* command "pip freeze" will also show the list of packages

## Pycharm
Pycharm is my tool of choice for Python development.  They have a free version, it integrates with both virtualenv and GITHUB and has a lot of the usual IDE tools that developers need such as line numbers, code syntax highlighting, package reflection, refactoring, project views as well as other tools.

