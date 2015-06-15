__author__ = 'brendan'


def change_state(flow_unit, *args, **kwargs):
    """
    :param flow_unit: The FlowUnit whose state is changing
    :param args:
    :param kwargs:
      'state': a State object that flow_unit.state will now hold.
    :return: None
    """
    flow_unit.state = kwargs.get('state' or None)
