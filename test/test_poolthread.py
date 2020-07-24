import unittest
import urllib.request

from concurrent.futures import ThreadPoolExecutor, as_completed


class TestThreadPool(unittest.TestCase):
    max_workers = 1
    URLS = ['http://www.foxnews.com/',
            'http://www.cnn.com/',
            'http://google.com/',
            'http://www.bbc.co.uk/']

    def setUp(self) -> None:
        self.max_workers = 100

    def test_pool(self):
        with ThreadPoolExecutor(self.max_workers) as executor:
            future_to_url = {executor.submit(self.load_url, url, 60): url for url in self.URLS}
            for future in as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    data = future.result()
                    self.assertIsNotNone(data)
                except Exception as exc:
                    self.fail('Exception thrown!')
                else:
                    print('%r page is %d bytes' % (url, len(data)))

    def load_url(self, url, timeout):
        with urllib.request.urlopen(url, timeout=timeout) as conn:
            return conn.read()


if __name__ == '__main__':
    unittest.main()
