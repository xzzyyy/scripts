import os.path
import unittest
import randomize_names


class TestRandomizeNames(unittest.TestCase):

    def test_shuffle(self):

        files = ["a.jpg", "b.m4v", "c.png"]
        old_new = randomize_names.shuffle(files)

        for old, new in old_new:
            old_name, old_ext = os.path.splitext(old)
            new_name, new_ext = os.path.splitext(new)
            self.assertEqual(old_ext, new_ext)
            self.assertTrue(new_name in {"0", "1", "2"})

        files = [str(i) + ".jpg" for i in range(101)]
        old_new = randomize_names.shuffle(files)

        for old, new in old_new:
            new_name, new_ext = os.path.splitext(new)
            self.assertEqual(3, len(new_name))


if __name__ == '__main__':
    unittest.main()
