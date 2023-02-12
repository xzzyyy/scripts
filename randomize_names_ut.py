import os
import shutil
import unittest
import randomize_names


class TestRandomizeNames(unittest.TestCase):

    def test_shuffle(self):
        files = ["a.jpg", "b.m4v", "c.png", "D.MOV"]

        old_new = randomize_names.shuffle(files)
        self.assertEqual(4, len(old_new))

        for old, new in old_new:
            old_name, old_ext = os.path.splitext(old)
            new_name, new_ext = os.path.splitext(new)
            self.assertEqual(old_ext, new_ext)
            self.assertTrue(new_name in {"0", "1", "2", "3"})

        files = [str(i) + ".jpg" for i in range(101)]
        old_new = randomize_names.shuffle(files)

        for old, new in old_new:
            new_name, new_ext = os.path.splitext(new)
            self.assertEqual(3, len(new_name))

    def test_add_suffix(self):
        self.assertEqual("a.sfx.jpg", randomize_names.add_suffix("a.jpg", "sfx"))

    def test_top_dir(self):
        prev_cd = os.getcwd()
        try:
            os.chdir(os.environ["TMP"])
            self.assertEqual("Temp", randomize_names.top_dir("."))
        finally:
            os.chdir(prev_cd)

    def test_filesystem(self):
        fns = {"0.jpg", "1.jpg", "2.jpg"}

        tmp_dir = os.environ["TMP"]
        tmp_dir_script = tmp_dir + "/" + "randomize_names.py"

        try:
            os.mkdir(tmp_dir_script)
            os.chdir(tmp_dir_script)

            some_dir = "gopa"
            os.mkdir(some_dir)        # should not be removed

            for fn in fns:
                f = open(fn, "w")
                f.close()

            randomize_names.shuffle_files(tmp_dir_script)
            res_fns1 = set(os.listdir(tmp_dir_script))
            randomize_names.shuffle_files(".")
            res_fns2 = set(os.listdir("."))

            for name in fns:
                base, ext = os.path.splitext(name)
                self.assertIn(base + ".randomize_names.py" + ext, res_fns1)
                self.assertIn(base + ".randomize_names.py" + ext, res_fns2)
            self.assertTrue(os.path.isdir(some_dir))

        finally:
            os.chdir(tmp_dir)
            shutil.rmtree(tmp_dir_script)


if __name__ == '__main__':
    unittest.main()
