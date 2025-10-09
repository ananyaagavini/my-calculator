"""
Unit Tests for CLI using click.testing.CliRunner
"""

import pytest
from click.testing import CliRunner
from src.cli import calculate

runner = CliRunner()


class TestCLI:
    def test_cli_add(self):
        result = runner.invoke(calculate, ["add", "2", "3"])
        assert result.exit_code == 0
        assert result.output.strip() == "5"

    def test_cli_multiply(self):
        result = runner.invoke(calculate, ["multiply", "4", "5"])
        assert result.exit_code == 0
        assert result.output.strip() == "20"

    def test_cli_divide(self):
        result = runner.invoke(calculate, ["divide", "10", "2"])
        assert result.exit_code == 0
        assert result.output.strip() == "5.0"

    def test_cli_divide_by_zero(self):
        result = runner.invoke(calculate, ["divide", "10", "0"])
        assert result.exit_code == 1
        assert "Cannot divide by zero" in result.output

    def test_cli_invalid_operation(self):
        result = runner.invoke(calculate, ["foo", "1", "2"])
        assert result.exit_code == 1
        assert "Unknown operation" in result.output

    def test_cli_square_root(self):
        result = runner.invoke(calculate, ["sqrt", "16"])
        assert result.exit_code == 0
        assert result.output.strip() == "4.0"
