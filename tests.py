# tests.py

from unittest import TestCase, main as unittest_main, mock
from bson.objectid import ObjectId
from app import app

sample_guitar_id = ObjectId('5da005918edd63f14c355675')
sample_guitar = {
    'title': 'Gretsch White Falcon',
    'description': 'electric',
    'price': '$850',
    'jpgs':
        'https://www.dawsons.co.uk/media/catalog/product/cache/1/image/1200x/6b9ffbf72458f4fd2d3cb995d92e8889/g/i/gibson_les_paul_classic_electric_guitar_-_heritage_cherry_sunburst_-_front.jpg',
}
sample_form_data = {
    'title': sample_guitar['title'],
    'description': sample_guitar['description'],
    'price': sample_guitar['price'],
    'jpgs': '\n'.join(sample_guitar['jpgs'])
}

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

    @mock.patch('pymongo.collection.Collection.update_one')
    def test_edit_guitar(self, mock_update):
       """Test editing a single guitar entry."""
       mock_update.return_value = sample_guitar
       result = self.client.get(f'/guitars/{sample_guitar_id}')
       self.assertEqual(result.status, '200 OK')
       self.assertIn(b'Edit Guitar', result.data)

    @mock.patch('pymongo.collection.Collection.delete_one')
    def test_delete_guitar(self, mock_delete):
       form_data = {'_method': 'DELETE'}
       result = self.client.post(f'/guitars/{sample_guitar_id}/delete', data=form_data)
       self.assertEqual(result.status, '302 FOUND')
       mock_delete.assert_called_with({'_id': sample_guitar_id})

if __name__ == '__main__':
    unittest_main()
