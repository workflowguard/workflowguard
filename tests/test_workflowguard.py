
from click.testing import CliRunner

from workflowguard.__main__ import main

from workflowguard import State

def test_main():
    runner = CliRunner()
    result = runner.invoke(main, [])

    assert result.output == '()\n'
    assert result.exit_code == 0

def test_create_a_state():
    state_object = State()
    assert state_object