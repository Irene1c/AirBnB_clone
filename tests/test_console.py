#!/usr/bin/python3
""" test cases for the command interpreter """
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch
import unittest


class TestConsole(unittest.TestCase):
    """ class to test the console """

    def setUp(self):
        """ The setup """

        self.console = HBNBCommand()

    def tearDown(self):
        """ The teardown """

        self.console = None

    def test_quit(self):
        """ test for quit cmd """

        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("quit")
            self.assertEqual(output.getvalue(), "")

    def test_EOF(self):
        """ test for EOF """

        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("EOF")
            self.assertEqual(output.getvalue(), "\n")

    def test_emptyline(self):
        """ test for emptyline """

        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("\n")
            self.assertEqual(output.getvalue(), "")

    def test_create_missing_class(self):
        """ test for create with no arguments """

        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("create")
            self.assertEqual("** class name missing **\n", output.getvalue())

    def test_create_invalid_class(self):
        """ test for create with invalid class """

        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("create InvalidClass")
            self.assertEqual("** class doesn't exist **\n", output.getvalue())

    def test_create_valid_class(self):
        """ test for create with valid class """

        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("create User")
            obj_id = output.getvalue().strip()
            self.assertTrue(len(obj_id) > 0)

    def test_show_missing_class(self):
        """ test for show with no arguments """

        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("show")
            self.assertEqual("** class name missing **\n", output.getvalue())

    def test_show_invalid_class(self):
        """ test for show with invalid class """

        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("show InvalidClass")
            self.assertEqual("** class doesn't exist **\n", output.getvalue())

    def test_show_missing_instance_id(self):
        """ test for show with missing id """

        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("show User")
            self.assertEqual("** instance id missing **\n", output.getvalue())

    def test_show_invalid_instance(self):
        """ test for show with invalid instance """

        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("show User 123")
            self.assertEqual("** no instance found **\n", output.getvalue())

    def test_destroy_missing_class(self):
        """ test for destroy with no arguments """

        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("destroy")
            self.assertEqual("** class name missing **\n", output.getvalue())

    def test_destroy_invalid_class(self):
        """ test for destroy with invalid class """

        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("destroy InvalidClass")
            self.assertEqual("** class doesn't exist **\n", output.getvalue())

    def test_destroy_missing_instance_id(self):
        """ test for destroy with missing instance id """

        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("destroy User")
            self.assertEqual("** instance id missing **\n", output.getvalue())

    def test_destroy_invalid_instance(self):
        """ test destroy with invalid instance """

        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("destroy User 123")
            self.assertEqual("** no instance found **\n", output.getvalue())

    def test_destroy_valid_instance(self):
        """ test destroy with valid instance """

        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("create User")
            obj_id = output.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd(f"destroy User {obj_id}")
            self.assertEqual("", output.getvalue())


if __name__ == "__main__":
    unittest.main()
