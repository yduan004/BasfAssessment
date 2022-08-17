import unittest
from unittest.mock import patch, mock_open
import sys
sys.path.append('../')
from src.string_processor import StringProcessor


class TestStringProcessor(unittest.TestCase):

    def test_append(self):
        obj = StringProcessor('')
        obj.append("hello, world")
        self.assertEqual(obj.string, "hello, world")

    def test_remove(self):
        obj = StringProcessor('hello')
        obj.remove('el')
        self.assertEqual(obj.string, "hlo")

    def test_mirror(self):
        obj = StringProcessor('hello')
        obj.mirror()
        self.assertEqual(obj.string, 'olleh')

    def test_save(self):
        fake_file_path = "fake/file/path"
        obj = StringProcessor("Test message to write on file")
        with patch('src.string_processor.open', mock_open()) as mocked_file:
            obj.save(fake_file_path)
            # assert if opened file on write mode 'w'
            mocked_file.assert_called_once_with(fake_file_path, 'w')
            # assert if the message has written to file
            mocked_file().write.assert_called_once_with("Test message to write on file")

    def test_load(self):
        file_content_mock = "Hello, this a message to test read from a file."
        fake_file_path = "fake/file/path"
        obj = StringProcessor("")
        with patch('src.string_processor.open'.format(__name__), new=mock_open(read_data=file_content_mock)) as mocked_file:
            obj.load(fake_file_path)
            # assert if opened file on write mode 'r'
            mocked_file.assert_called_once_with(fake_file_path, 'r')
            # assert if the message has been read from file
            self.assertEqual(mocked_file().read(), "Hello, this a message to test read from a file.")



if __name__ == '__main__':
    unittest.main()




