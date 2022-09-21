import unittest
import ya_api_c


class TestApi(unittest.TestCase):

    def setUp(self):
        print("Set up for test")

    def test_dev_folder(self):
        self.assertEqual(ya_api_c.dev_folder("test"), 201)
        print("Successfuliy")

    def test_dev_folder_pass(self):
        self.assertEqual(ya_api_c.dev_folder("test_pass"), 409)
        print("unSuccessfuliy")

    def tearDown(self):
        ya_api_c.del_folder(
            "test"
        )
        print("Tear down for test")


if __name__ == '__main__':
    unittest.main()
