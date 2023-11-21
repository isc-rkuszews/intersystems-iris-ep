
# TODO: Anything else?

from . import base

def connect(username='_SYSTEM', password='SYS', irisNamespace='USER', irisInstance='iris'):
    """
    Makes this Python process part of the named InterSystems IRIS instance running on this machine.

    This process must already be running in an account in the IRIS group in order to connect.

    Returns the `iris` module for the instance

        iris = intersystems-iris-ep.connect()

    """

    return base.connect(username, password, irisNamespace, irisInstance)
