
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
    state_object = State(name1)
    assert state_object
    assert state_object.get_name() == name1
    state_object.set_name(name2)
    assert state_object.get_name() == name2