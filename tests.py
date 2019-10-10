# tests.py

from unittest import TestCase, main as unittest_main, mock
from bson.objectid import ObjectId
from app import app

class contractorTests(TestCase):
    """Flask tests."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True

    def test_index(self):
        """Test the contractor homepage."""
        result = self.client.get('/')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'guitar', result.data)

    def test_new(self):
        """Test the new creation page."""
        result = self.client.get('/guitars/new')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'New Guitar', result.data)

    def test_edit(self):
        """Test the edit page."""
        result = self.client.get('/guitars/<guitar_id>/edit', methods=['POST'])
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Edit Guitar', result.data)

    def test_delete(self):
        """Test the delete page."""
        result = self.client.get('/guitars/<guitar_id>/delete')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Delete Guitar', result.data)



if __name__ == '__main__':
    unittest_main()
