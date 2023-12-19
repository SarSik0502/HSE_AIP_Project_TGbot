"""
from main import main
import pytest
def test_main_prints_ok(capsys):
    main("тест")
    captured = capsys.readouterr()
    assert "ok" in captured.out

"""
import pytest
from unittest.mock import MagicMock
from main import main, on_click

@pytest.fixture
def mock_telebot():
    return MagicMock()

def test_start_command(mock_telebot):
    message = MagicMock()
    message.text = '/start'
    main(message, telebot=mock_telebot)
    mock_telebot.send_message.assert_called_once_with(
        message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}'
    )

def test_kursy_valyut_command(mock_telebot):
    message = MagicMock()
    message.text = 'Курсы валют'
    on_click(message, telebot=mock_telebot)

def test_poluchat_novosti_command(mock_telebot):
    message = MagicMock()
    message.text = 'Получать новости'
    on_click(message, telebot=mock_telebot)

def test_kursy_kriptovalyut_command(mock_telebot):
    message = MagicMock()
    message.text = 'Курсы криптовалют'
    on_click(message, telebot=mock_telebot)