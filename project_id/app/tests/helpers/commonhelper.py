__copyright__ = "Copyright (c) 2024 Helium Edu"
__license__ = "MIT"

from unittest import mock


def given_urlopen_response_value(status, mock_urlopen):
    magic_mock = mock.MagicMock()
    magic_mock.getcode.return_value = status
    mock_urlopen.return_value = magic_mock
