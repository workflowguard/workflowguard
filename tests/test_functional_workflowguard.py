"""
Functional tests for workflowguard
"""
from workflowguard import State, Action, FlowUnit, Transition, Transitions
from workflowguard.middleware import change_flow_unit_state


"""
Test a simple flow with a transition that allows an action that changes the flow_unit state.
"""

def test_work_flow_simple_action():
    """
    This functional test creates a transition that allows a flow unit to have an action carried out upon it that changes
    its state from 'first_state' to another state and tests that the it cna not be changed again since there is no
    tranisition that allows the change for the new state
    :return:
    """
    #set up
    first_state = State('first_state', 'The first state')
    second_state = State('second_state', 'The second state')
    action1 = Action('action1', change_flow_unit_state)
    transition = Transition(first_state, action1)
    transitions = Transitions(transition)
    flow_unit = FlowUnit('flow_unit', first_state)

    #first test change state from first_state to second_state
    for transition in transitions():
        if flow_unit.state == transition.state:
            transition.action(flow_unit, second_state)
    assert flow_unit.state == second_state

    #second test do not change state as no allowable transition is present
    for transition in transitions():
        if flow_unit.state == transition.state:
            transition.action(flow_unit, first_state)
    assert flow_unit.state == second_state
test_work_flow_simple_action()