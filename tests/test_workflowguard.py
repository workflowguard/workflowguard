
from click.testing import CliRunner

from workflowguard.__main__ import main

from workflowguard import State

def test_main():
    runner = CliRunner()
    result = runner.invoke(main, [])

    assert result.output == '()\n'
    assert result.exit_code == 0

def test_create_a_state():
    name1 = 'test1'
    name2 = 'test2'
    label1 =  'test label 1'
    state_object1 = State(name1)
    state_object2 = State(name1, label1)
    assert state_object1.name == name1
    assert state_object1.label == ''
    assert state_object2.label == label1

