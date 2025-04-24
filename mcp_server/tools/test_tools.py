import unittest
import hello_world
import generate_code
import debug_code
import analyze_code
import file_management
import task_management

class TestTools(unittest.TestCase):

    def test_hello_world(self):
        self.assertEqual(hello_world.hello_world("Test"), "Hello, Test!")

    def test_generate_code(self):
        self.assertTrue("class MyClass:" in generate_code.generate_code("class", "MyClass"))
        self.assertTrue("def my_function():" in generate_code.generate_code("function", "my_function"))

    def test_debug_code(self):
        self.assertTrue("Debugging started" in debug_code.debug_code("test code", [1, 2]))

    def test_analyze_code(self):
        result = analyze_code.analyze_code("def my_function(x):\n  y = x + 1\n return y")
        self.assertTrue(isinstance(result, dict))

    def test_file_management(self):
        file_management.create_file("test_file.txt", "test content")
        self.assertEqual(file_management.read_file("test_file.txt"), "test content")
        file_management.write_file("test_file.txt", "new content")
        self.assertEqual(file_management.read_file("test_file.txt"), "new content")
        file_management.delete_file("test_file.txt")
        self.assertTrue("No such file" in file_management.read_file("test_file.txt"))

    def test_task_management(self):
        task_management.create_task("Test Task", "Test Description")
        self.assertTrue("Test Task" in task_management.list_tasks())
        task_management.update_task_status("Test Task", "closed")
        self.assertTrue("(closed)" in task_management.list_tasks())

if __name__ == '__main__':
    unittest.main()
