
from click.testing import CliRunner

from workflowguard.__main__ import main

from workflowguard import State, Action, FlowUnit, Transition, Actions, States, Transitions
from workflowguard.middleware import change_flow_unit_state, dummy_action


def test_main():
    runner = CliRunner()
    result = runner.invoke(main, [])

    assert result.output == '()\n'
    assert result.exit_code == 0

def test_state():
    state_name1 = 'state1'
    state_label1 =  'state label 1'
    state1 = State(state_name1, state_label1)
    assert state1.name == state_name1
    assert state1.label == state_label1

def test_flow_unit():
    flow_unit_name1 = 'flow_unit1'
    flow_unit_name2 = 'flow_unit2'
    state_name1 = 'state1'
    state_label1 =  'state label 1'
    state1 = State(state_name1, state_label1)
    flow_unit1 = FlowUnit(flow_unit_name1, state1)
    assert flow_unit1.name == flow_unit_name1
    assert flow_unit1.state == state1

def test_action():
    action_name1 = 'action1'
    action1 = Action(action_name1,dummy_action)
    assert action1.name == action_name1
    assert action1(None) == None

def test_transition():
    action_name1 = 'action1'
    action1 = Action(action_name1,dummy_action)
    state_name1 = 'state1'
    state_label1 =  'state label 1'
    state1 = State(state_name1, state_label1)
    transition = Transition(state1, action1)
    assert transition.state == state1
    assert transition.action == action1

def test_actions():
    action_name1 = 'action1'
    action1 = Action(action_name1,dummy_action)
    actions = Actions(action1)
    assert actions
    assert len(actions()) == 1
    assert actions.contains(action1)
    action_name2 = 'action2'
    action2 = Action(action_name2,dummy_action)
    actions.add(action2) # test another action can be added
    assert actions.contains(action2)
    assert len(actions()) == 2
    actions.add(action2) # try adding it again
    assert len(actions()) == 2

def test_states():
    state_name1 = 'state1'
    state_label1 =  'state label 1'
    state1 = State(state_name1, state_label1)
    state_name2 = 'state2'
    state_label2 =  'state label 2'
    state2 = State(state_name2, state_label2)
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
    state_name1 = 'state1'
    state_label1 =  'state label 1'
    state1 = State(state_name1, state_label1)
    state_name2 = 'state2'
    state_label2 =  'state label 2'
    state2 = State(state_name2, state_label2)
    action1 = Action('action1', dummy_action)
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

