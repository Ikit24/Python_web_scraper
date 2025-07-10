import unittest
from crawl import normalize_url


class TestCrawl(unittest.TestCase):
    def test_normalize_url(self):
        input_url = "https://blog.boot.dev/path"
        actual = normalize_url(input_url)
        expected = "blog.boot.dev/path"
        self.assertEqual(actual, expected)

    def test_normalize_url_with_trailing_slash(self):
        input_url = "https://blog.boot.dev/path/"
        actual = normalize_url(input_url)
        expected = "blog.boot.dev/path"
        self.assertEqual(actual, expected)

    def test_normalize_url_with_http(self):
        input_url = "http://blog.boot.dev/path"
        actual = normalize_url(input_url)
        expected = "blog.boot.dev/path"
        self.assertEqual(actual, expected)

    def test_normalize_url_with_http_and_trailing_slash(self):
        input_url = "http://blog.boot.dev/path/"
        actual = normalize_url(input_url)
        expected = "blog.boot.dev/path"
        self.assertEqual(actual, expected)

    def test_normalize_url_root_with_trailing_slash(self):
        input_url = "http://blog.boot.dev/"
        actual = normalize_url(input_url)
        expected = "blog.boot.dev"
        self.assertEqual(actual, expected)

    def test_normalize_url_root(self):
        input_url = "http://blog.boot.dev"
        actual = normalize_url(input_url)
        expected = "blog.boot.dev"
        self.assertEqual(actual, expected)

    def test_normalize_url_deeper_paths(self):
        input_url = "http://blog.boot.dev/path/to/page"
        actual = normalize_url(input_url)
        expected = "blog.boot.dev/path/to/page"
        self.assertEqual(actual, expected)

    def test_get_urls_from_html_absolute(self):
        input_url = "https://blog.boot.dev"
        input_body = '<html><body><a href="https://blog.boot.dev"><span>Boot.dev></span></a></body></html>'
        actual = get_urls_from_html(input_body, input_url)
        expected = ["https://blog.boot.dev"]
        self.assertEqual(actual, expected)

    def test_get_urls_from_html_is_a_string(self):
        with self.assertRaises(TypeError):
            get_urls_from_html(123, "https://blog.boot.dev")

    def test_get_urls_from_html_is_a_string_with_None(self):
        with self.assertRaises(TypeError):
            get_urls_from_html(None, "https://blog.boot.dev")

    def test_get_urls_from_html_is_a_string_with_List(self):
        with self.assertRaises(TypeError):
            get_urls_from_html([], "https://blog.boot.dev")


if __name__ == "__main__":
    unittest.main()
