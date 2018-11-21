# Herne
Herne is a wrapper application that can be used to configure other applications. 

## Creating a Basic Herne App
The following example creates a simple "Hello World" app using Herne as the runner. Firstly we need to define the app
using the `HerneApp` class as the template.

In a file `my_first_app.py` we add the following lines:

```
from Herne.AppBase import HerneApp
import copy

class HelloWorld(HerneApp):
    __version__ = 'v0.0.1'
    def __init__(self):
        HerneApp.__init__(self, 'HelloWorld')
        self._members = copy.deepcopy(HerneApp._members)
        self._members += ['UserName']
    
    def __call__(self):
        HerneApp.__call__(self)
        print("Hello {}!".format(self.UserName)
```

Firstly it the importance of using `deepcopy` when copying the `_members` property of `HerneApp`. Once we have copied this object
we then assign additional properties relating to our app, in this example `UserName` is added which will provide the option for
the user's name.

Secondly we redefine the `__call__` method to additionally include what we would like the app to do, in this case simply greet the user.

Another requirement of Herne Apps is the declaration of a version label using `__version__`. Although this is not used beyond being printed it is useful
when it comes to debugging in future.

## Running a Herne App
To run your Herne App you will now need to define the options file for the run, these options can also be appended to the App script
as a `__main__` however it is recommended to code them seperately as this means you can have multiple options files for vriety.

Using again the example above for our HelloWorld app, assuming the app script has been named `Confiurables` and is part of
a python application called `greeting`, an options file `run_dave.py` would take the form:

```
from greeting.Configurables import HelloWorld

HelloWorld().UserName = 'Dave'
```

That's it! Now to run our application we use the included `run` script within Herne:

`./run run_dave.py`

this would give the output:

```
===================================================================
                            test v0.0.1                            
                       Running on localhost                      
===================================================================
        
-------------------------------------------------------------------
INFO:Herne Runner	: OutputLevel : INFO
INFO:Herne Runner	: UserName : Dave
-------------------------------------------------------------------
INFO:Herne Runner	: Application Setup Successful.
Hello Dave!
INFO:Herne Runner	: Application Completed Successfully.
```
