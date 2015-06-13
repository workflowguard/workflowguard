__version__ = "0.0.1"


class State(object):
    """A State class"""
    def __init__(self, name, label=''):
        """Create an instance of State
        Arguments:
        name: -- the name of this State
        label: -- a short description of the state
        """
        self.name = name
        self.label = label


class FlowUnit(object):
    """FlowUnit Class
    This is a core class of the library. A flow_unit instance holds the current state. It is passed to the a
    relevant Action instance when the actions perform method is called. The available Action objects are defined by the
    Transition class and are dependant on the flow_units current state.
    """
    def __init__(self, name, *args, **kwargs):
        """Create an instance of FlowUnit
        Arguments:
        name: -- the name of this flow_unit
        Keyword arguments:
        state -- initial state
        """
        self.name = name
        self.state = kwargs.get('state', State('initial', 'initial state'))


class Action(object):
    """
    Action Class
    An instance of this class should be created for each action that is required by the system. An action carries out
    processing on a FlowUnit instance and is what causes the State instance of a FlowUnit instance to change.
    """
    def _default_function(flow_unit, *args, **kwargs):
        """Return an informative message as we shouldn't ever need this function. """
        print("default function your action has been created with no action function, surely you didn't mean to do this!")

    def __init__(self, name, *args, **kwargs):
        """Create an instance of Action
        Arguments:
        name: -- the name of this action
        Keyword arguments:
        action -- the function that will be performed when this actions perform method is called
        """
        self.name = name
        self.action = kwargs.get('action', self._default_function)

    def perform(self, flow_unit, *args, **kwargs):
        """Carries out the action on the provided flow_unit
        Arguments:
        flow_unit - the flow_unit instance that will have the processing caried out upon it.
        Keyword arguments:
        as required by the action function for this Action instance.
        """
        self.action(flow_unit, *args, **kwargs)
