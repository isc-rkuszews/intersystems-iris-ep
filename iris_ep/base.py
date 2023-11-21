"""
iris_ep base module.

"""

def connect(username, password, irisNamespace, irisInstance):

    # Get the installDir
    import subprocess

    completedProcess = subprocess.run(['iris', 'qlist', irisInstance], stdout=subprocess.PIPE, text=True)
    completedProcess.check_returncode()

    installdir = completedProcess.stdout.split('^')[1]

    # Set the IRIS connection environment variables
    import os
    os.environ["IRISUSERNAME"] = username
    os.environ["IRISPASSWORD"] = password
    os.environ["IRISNAMESPACE"] = irisNamespace

    # import the following?
    # Bin libirispythonsyn.so pythonint.so

    # Add to import path
    # lib/python mgr/python

    from sys import path as __syspath

    __syspath.append(installdir + '/lib/python')
    import iris

    # Unset the IRIS connection environment variables
    del os.environ['IRISUSERNAME']
    del os.environ['IRISPASSWORD']
    del os.environ['IRISNAMESPACE']

    return iris
