'''import unittest
from mogoBot import trade_bot, extract_info, map_request_type, fetch_matching_comments, reply_to_comment

class TestMogoBot(unittest.TestCase):

    def 



import unittest
from unittest.mock import patch, MagicMock
from mogoBot import trade_bot, extract_info, map_request_type, fetch_matching_comments, reply_to_comment

class TestTradeBot(unittest.TestCase):

    @patch('praw.Reddit')
    @patch('mogoBot.py')
    def test_trade_bot(self, mock_subreddit, mock_reddit):
        # Set up mock objects
        submission_mock = MagicMock()
        submission_mock.title = '!TradeBot'
        submission_mock.selftext = 'LF: Sticker1'

        stream_mock = MagicMock()
        stream_mock.submissions.return_value = [submission_mock]

        subreddit_mock = MagicMock()
        subreddit_mock.stream.return_value = stream_mock
        mock_subreddit.return_value = subreddit_mock

        # Mock extract_info to return known values
        with patch('your_module.extract_info', return_value=('LF:', 'Sticker1')):
            trade_bot()

        # Add assertions based on your expected behavior

    def test_extract_info(self):
        comment_body = 'LF: Sticker1'
        request_type, sticker_name = extract_info(comment_body)
        self.assertEqual(request_type, 'LF:')
        self.assertEqual(sticker_name, 'Sticker1')

        # Add more test cases based on different inputs

    def test_map_request_type(self):
        self.assertEqual(map_request_type('LF:'), 'HAVE:')
        self.assertEqual(map_request_type('HAVE:'), 'LF:')
        # Add more test cases based on different inputs

    def test_fetch_matching_comments(self):
        # Set up mock objects
        subreddit_mock = MagicMock()
        submission_mock = MagicMock()
        comment_mock = MagicMock()
        comment_mock.body = 'HAVE: Sticker1'
        submission_mock.comments.list.return_value = [comment_mock]
        subreddit_mock.new.return_value = [submission_mock]

        # Call the function and assert based on expected behavior

    def test_reply_to_comment(self):
        # Set up mock objects
        original_comment_mock = MagicMock()
        matching_comments = ['Comment 1', 'Comment 2']

        # Call the function and assert based on expected behavior

if __name__ == '__main__':
    unittest.main()
'''

import unittest
from unittest.mock import patch, Mock
from datetime import datetime, timedelta
from mogoBot import trade_bot, extract_info, map_request_type, fetch_matching_comments, reply_to_comment

class TestTradeBot(unittest.TestCase):

    @patch('mogoBot.reddit')
    @patch('mogoBot.subreddit')
    def test_trade_bot(self, mock_subreddit, mock_reddit):
        # Mock the stream.submissions method
        mock_subreddit.stream.submissions.return_value = [
            Mock(title='!TradeBot ', selftext='LF: Sticker1'),
            Mock(title='Not a trigger', selftext='Irrelevant comment body'),
        ]

        # Mock the extract_info function
        with patch('mogoBot.extract_info', return_value=('LF:', 'Sticker1')) as mock_extract_info:
            # Mock the map_request_type function
            with patch('mogoBot.map_request_type', return_value='HAVE:'):
                # Mock the fetch_matching_comments function
                with patch('mogoBot.fetch_matching_comments', return_value=['Matching Comment 1', 'Matching Comment 2']):
                    # Mock the reply_to_comment function
                    with patch('mogoBot.reply_to_comment') as mock_reply_to_comment:
                        # Call the trade_bot function with a duration of 1 minute
                        trade_bot(duration_minutes=1)

        # Assert that the mocked functions were called with the expected arguments
        mock_extract_info.assert_called_once_with('Sample comment body')
        mock_reply_to_comment.assert_called_once_with(
            mock_subreddit.stream.submissions()[0],
            ['Matching Comment 1', 'Matching Comment 2']
        )

    def test_extract_info(self):
        # Test the extract_info function
        comment_body = 'LF: Sticker1'
        request_type, sticker_name = extract_info(comment_body)
        self.assertEqual(request_type, ('LF:'))
        self.assertEqual(sticker_name, ('Sticker1'))

    def test_map_request_type(self):
        # Test the map_request_type function
        self.assertEqual(map_request_type('LF:'), 'HAVE:')
        self.assertEqual(map_request_type('HAVE:'), 'LF:')
        self.assertEqual(map_request_type('InvalidType'), 'InvalidType')

    def test_fetch_matching_comments(self):
        # Test the fetch_matching_comments function
        subreddit = Mock()
        subreddit.new.return_value = [
            Mock(comments=Mock(list=Mock(return_value=[Mock(body='LF: Sticker1')]))),
            Mock(comments=Mock(list=Mock(return_value=[Mock(body='InvalidType Sticker1')]))),
        ]

        mapped_request_type = 'HAVE:'
        sticker_name = 'Sticker1'
        result = fetch_matching_comments(subreddit, mapped_request_type, sticker_name)
        self.assertEqual(result.match_request, ('LF:'))
        self.assertEqual(result.sticker_name, ('Sticker1'))
        
        self.assertEqual(result, ['LF: Sticker1'])

    def test_reply_to_comment(self):
        # Test the reply_to_comment function
        original_comment = Mock()
        matching_comments = ['Matching Comment 1', 'Matching Comment 2']
        reply_to_comment(original_comment, matching_comments)
        original_comment.reply.assert_called_once_with('Matching Comment 1\nMatching Comment 2')

if __name__ == '__main__':
    unittest.main()
