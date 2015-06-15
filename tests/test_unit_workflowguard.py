
from click.testing import CliRunner

from workflowguard.__main__ import main

from workflowguard import State, Action, FlowUnit, Transition, Actions, States, Transitions
from workflowguard.middleware import change_state


def test_main():
    runner = CliRunner()
    result = runner.invoke(main, [])

    assert result.output == '()\n'
    assert result.exit_code == 0

def test_state():
    name1 = 'state1'
    label1 =  'state label 1'
    state_object1 = State(name1, label1)
    assert state_object1.name == name1
    assert state_object1.label == label1

def test_flow_unit():
    name1 = 'flow_unit1'
    state_name1 = 'state1'
    name2 = 'flow_unit2'
    state_object1 = State(state_name1, 'state label 1')
    flow_unit1 = FlowUnit(name1, state_object1)
    assert flow_unit1.name == name1
    assert flow_unit1.state.name == state_name1
    flow_unit2 = FlowUnit(name2, state_object1)
    assert flow_unit2.state.name == state_object1.name

def test_action():
    name1 = 'action1'
    name2 = 'action2'
    action2_text = 'action2 text'
    action1 = Action(name1)
    assert action1.name == name1
    state_object1 = State('state1', 'state label 1')
    flow_unit1 = FlowUnit('flow_unit1', state_object1)
    action1(flow_unit1)
    second_state = State('2ndState', 'Second State')
    action2 = Action('action2', action=change_state)
    action2(flow_unit1, second_state)
    assert flow_unit1.state == second_state

def test_transition():
    action1 = Action('action1')
    state_object1 = State('state1', 'state label 1')
    transition = Transition(state_object1, action1)
    assert transition.state == state_object1
    assert transition.action == action1

def test_actions():
    action1 = Action('action1')
    actions = Actions(action1)
    assert actions
    assert len(actions()) == 1
    assert actions.contains(action1)
    action2 = Action('action2')
    actions.add(action2) # test another action can be added
    assert actions.contains(action2)
    assert len(actions()) == 2
    actions.add(action2) # try adding it again
    assert len(actions()) == 2

def test_states():
    state1 = State('state1', 'first State')
    state2 = State('state2', 'second State')
    states = States(state1)
    assert states
    assert states.contains(state1)
    assert len(states()) == 1
    states.add(state2) # test another state can be added
    assert states.contains(state2)
    assert len(states()) == 2
    states.add(state2) # try adding it again
    assert len(states()) == 2

def test_transitions():
    state1 = State('state1', 'first State')
    state2 = State('state2', 'second State')
    action1 = Action('action1')
    transition1 = Transition(state1, action1)
    transition2 = Transition(state2, action1)
    transitions = Transitions(transition1)
    assert transitions
    assert transitions.contains(transition1)
    assert len(transitions()) == 1
    transitions.add(transition2) # test another state can be added
    assert transitions.contains(transition2)
    assert len(transitions()) == 2
    transitions.add(transition2) # try adding it again
    assert len(transitions()) == 2
