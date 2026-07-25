import contextlib
import io
import unittest

from youtube_downloader import build_options, make_parser


class CliTests(unittest.TestCase):
    def test_video_defaults_are_private_and_require_a_url(self):
        parser = make_parser()
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            parser.parse_args(["video"])

        options = build_options(parser.parse_args(["video", "https://example.com/video"]))
        self.assertNotIn("cookiesfrombrowser", options)
        self.assertTrue(options["noplaylist"])
        self.assertEqual(options["subtitleslangs"], ["en", "en-orig"])

    def test_playlist_uses_an_archive(self):
        options = build_options(make_parser().parse_args(["playlist", "https://example.com/playlist"]))
        self.assertFalse(options["noplaylist"])
        self.assertIn("download_archive", options)


if __name__ == "__main__":
    unittest.main()
