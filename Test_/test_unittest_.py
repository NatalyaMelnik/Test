import unittest
import main
from unittest.mock import patch



class TestFunc(unittest.TestCase):
    def setUp(self) -> None:
        print("Test working secretary")

    def test_check_document_existance(self):
        self.assertEqual(main.check_document_existance("11-2"), True)
        self.assertNotEqual(main.check_document_existance("10006"), False)
        self.assertFalse(main.check_document_existance(bool("10006") is True))

    @patch('builtins.input')
    def test_get_doc_owner_name(self, doc_input):
        doc_input.side_effect = ['2207 876234']
        self.assertEqual(main.get_doc_owner_name(), 'Василий Гупкин')
        doc_input.side_effect = ['2207 876234']
        self.assertNotEqual(main.get_doc_owner_name(), 'Аристарх Павлов')
        doc_input.side_effect = None
        self.assertNotEqual(main.get_doc_owner_name(), 'Gorge')

    def test_remove_doc_from_shelf(self):
        main.remove_doc_from_shelf("11-2")
        self.assertEqual(main.directories["1"], ['2207 876234', '5455 028765'])

    @patch("builtins.input")
    def test_add_new_shelf(self, shelf_input):
        shelf_input.side_effect = ['4']
        self.assertEqual(main.add_new_shelf(), ('4', True))

    @patch('builtins.input')
    def test_delete_doc(self, doc_input):
        doc_input.side_effect = ['10006']
        self.assertTrue(main.delete_doc(), '10006')

    @patch('builtins.input')
    def test_move_doc_to_shelf(self, doc_input):
        doc_input.side_effect = ['10006', "3"]
        main.move_doc_to_shelf()
        self.assertEqual(main.directories["3"], ["10006"])

    def test_get_doc_owners_names(self):
        self.assertEqual(main.get_all_doc_owners_names(), {'Василий Гупкин', 'Аристарх Павлов', "Геннадий Покемонов"})
        self.assertEqual(main.get_all_doc_owners_names(), {'Аристарх Павлов', 'Геннадий Покемонов', "Василий Гупкин"})

    @patch('builtins.input')
    def test_add_new_doc(self, doc_input):
        new_date = ['123', 'pass', 'Melnik', '2']
        doc_input.side_effect = new_date
        main.add_new_doc()
        self.assertEqual(new_date[:3],
                         [main.documents[-1]["number"], main.documents[-1]["type"], main.documents[-1]["name"]])
        self.assertIn(new_date[0], main.directories[new_date[-1]])

    def tearDown(self) -> None:
        print("Testing finished")
