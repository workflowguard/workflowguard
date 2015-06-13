
from click.testing import CliRunner

from workflowguard.__main__ import main

from workflowguard import State
from workflowguard import Action
from workflowguard import FlowUnit

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
    name2 = 'flow_unit2'
    flow_unit1 = FlowUnit(name1)
    assert flow_unit1.name == name1
    assert flow_unit1.state.name == 'initial'
    state_object1 = State('state1', 'state label 1')
    flow_unit2 = FlowUnit(name2, state=state_object1)
    assert flow_unit2.state.name == state_object1.name


def test_action():
    name1 = 'action1'
    name2 = 'action2'
    action2_text = 'action2 text'
    action1 = Action(name1)
    assert action1.name == name1
    flow_unit1 = FlowUnit('flow_unit1')
    action1.perform(flow_unit1)
    def change_state(flow_unit, *args, **kwargs):
        flow_unit.state = kwargs.get('state' or None)
    second_state = State('2ndState', 'Second State')
    action2 = Action('action2', action=change_state)
    action2.perform(flow_unit1, state=second_state)
    assert flow_unit1.state == second_state
