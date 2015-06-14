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
    def __init__(self, name, state, *args, **kwargs):
        """Create an instance of FlowUnit
        Arguments:
        name: -- the name of this flow_unit
        Keyword arguments:
        state -- initial state
        """
        self.name = name
        self.state = state


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
        action -- the function that will be performed when this action is called
        """
        self.name = name
        self.action = kwargs.get('action', self._default_function)

    def __call__(self, flow_unit, *args, **kwargs):
        """Carries out the action on the provided flow_unit
        Arguments:
        flow_unit - the flow_unit instance that will have the processing carried out upon it.
        Keyword arguments:
        as required by the action function for this Action instance.
        """
        self.action(flow_unit, *args, **kwargs)


class Actions(object):
    """
    Actions class
    Holds a set of actions
    """
    def __init__(self, to_add=None):
        if not to_add:
            to_add = []
        try:
            self._actions = set(to_add)
        except:
            self._actions = set()
            self._actions.add(to_add)

    def __call__(self, *args, **kwargs):
        return self._actions

    def contains(self, obj):
        """
        Arguments:
        obj of type action
        Returns:
        True - if obj is contained within self._actions
        False - if obj is not contained within self._actions
        """
        return obj in self._actions

    def add(self, elem):
        """
        adds elem to self.actions if not already present
        Arguments:
        elem obj of type action
        """
        self._actions.add(elem)


class States(object):
    """
    States class
    Holds a set of states
    """
    def __init__(self, to_add=None):
        if not to_add:
            to_add = []
        try:
            self._states = set(to_add)
        except:
            self._states = set()
            self._states.add(to_add)

    def __call__(self, *args, **kwargs):
        return self._states

    def contains(self, obj):
        """
        Arguments:
        obj of type action
        Returns:
        True - if obj is contained within self._states
        False - if obj is not contained within self._states
        """
        return obj in self._states

    def add(self, elem):
        """
        adds elem to self._states if not already present
        Arguments:
        elem obj of type state
        """
        self._states.add(elem)


class Transition(object):
    """
    Transition class
    An instance of this class holds a State instance and an associated Action instance. A FlowUnit instance is allowed
    to carry out any action that is held by a transition with a state that matches the flow_unit state
    """
    def __init__(self, state, action, *args, **kwargs):
        """Create an instance of Transition
        Arguments:
        state: -- a State object associated with this transition
        action: -- a Action object that is allowed for the state
        """
        self.state = state
        self.action = action
