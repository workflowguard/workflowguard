__author__ = 'brendan'

"""
This module is used for any common functions that can be used to access the WorkFlowGuard core classes
"""

def dummy_action(flow_unit):
    return flow_unit

def change_flow_unit_state(flow_unit, state, *args, **kwargs):
    """
    :param flow_unit: The FlowUnit whose state is changing
    :param args:
    :param kwargs:
      'state': a State object that flow_unit.state will now hold.
    :return: None
    """
    flow_unit.state = state
