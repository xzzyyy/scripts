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

    def test_dest_fn_exists(self):
        fns = {"0.jpg", "1.jpg", "2.jpg"}

        tmp_dir = os.environ["TMP"]
        tmp_dir_script = tmp_dir + "/randomize_names.py"
        os.mkdir(tmp_dir_script)
        os.chdir(tmp_dir_script)

        for fn in fns:
            f = open(fn, "w")
            f.close()

        try:
            randomize_names.shuffle_files(tmp_dir_script)
        except FileExistsError:
            pass
        res_fns = set(os.listdir("."))

        os.chdir(tmp_dir)
        shutil.rmtree(tmp_dir_script)

        self.assertEqual(fns, res_fns)


if __name__ == '__main__':
    unittest.main()
