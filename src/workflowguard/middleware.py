__author__ = 'brendan'

"""
This module is used for any common functions that can be used to access the WorkFlowGuard core classes
"""

def dummy_action(flow_unit):
    """
    This a dummy function used by the unit tests it does nothing but returns what is passed to it.
    :param flow_unit:
    :return: flow_unit
    """
    return flow_unit

def change_flow_unit_state(flow_unit, state, *args, **kwargs):
    """
    :param
    flow_unit: a FlowUnit object whose state is to be changed
    state: a State object that flow_unit.state will now be set to.
    :param args:
    :param kwargs:
    :return: None
    """
    flow_unit.state = state
