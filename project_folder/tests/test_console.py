import unittest
from unittest.mock import patch
from io import StringIO
import uuid
from  console import HBNBCommand
from models.base_model import BaseModel
from models import storage

class TestConsole(unittest.TestCase):
    
    # def test_create(self):
    #     with patch('sys.stdout', new=StringIO()) as f:
    #         HBNBCommand().onecmd("create BaseModel")
    #         output = f.getvalue().strip()
    #         self.assertTrue(len(output) > 0, "Output is empty")
    #         try:
    #             uuid.UUID(output, version=4)
    #         except ValueError as e:
    #             self.fail(f"Output is not a valid UUID: {e}")
            
    #         # Verify that the instance was actually created
    #         key = f"BaseModel.{output}"
    #         self.assertIn(key, storage.all(), f"Instance with key {key} not found in storage")
        
    
    def test_help_show(self):
        """Test the help command for the show method."""
        expected_output = "Show an instance based on the class name and id\n        Usage: show <class name> <id>\n"
        
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            self.assertEqual(f.getvalue(), expected_output)
            
            
            
if __name__ == "__main__":
    unittest.main()
        