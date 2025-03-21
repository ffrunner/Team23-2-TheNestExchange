import unittest
import app

class ListingTestCase(unittest.TestCase):

  def setUp(self):
    # Configure the app for testing
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Team23_2@localhost/test_db'
    self.client = app.test_client()

    # Create tables in the test database
    with app.app_context():
      db.create_all()

  def tearDown(self):
    with app.app_context():
      db.session.remove()
      db.drop_all() # Drop all tables after tests

  def test_get_listings_by_category(self):
    response = self.client.get('/listings/Textbooks')
    self.assertEqual(response.status_code, 200)
    data = json.loads(response.data)
    self.assertTrue(isinstance(data, list))
    self.assertGreaterEqual(len(data), 1)

  def test_report_listing(self):
    payload = {
      "listing_id": self.listing_id,
      "reason": "Inappropriate content",
      "reported_by": 1
    }
    response = self.client.post('/listings/report', data=json.dumps(payload), content_type='application/json')
    self.assertEqual(response.status_code, 200)
    data = json.loads(response.data)
    self.assertEqual(data["message"], "Report submitted")

    # Check that the report record was created in the database
    with app.app_context():
      result = db.session.execute("SELECT COUNT(*) FROM reports WHERE listing_id = :lid", {'lid': self.listing_id})
      count = result.scalar()
      self.assertGreaterEqual(count, 1)

  def test_create_listing(self):
    payload = {
      "user_id": 1,
      "category": "Textbooks",
      "description": "A test textbook",
      "image_url": "https://media.istockphoto.com/id/162833242/photo/blank-book.jpg?s=612x612&w=0&k=20&c=9OAgWObWA4uLTvM8gcw6wlmY6Fp9HESggfArIDT524s="
    }
    response = self.client.post('/listings', data=json.dumps(payload), content_type='application/json')
    self.assertEqual(response.status_code, 201)
    data = json.loads(response.data)
    self.assertIn("id", data)

  def test_edit_listing(self):
    edit_payload = {
      "user_id": 1,
      "new_description": "New description",
      "new_image_url": "https://as2.ftcdn.net/jpg/00/21/52/03/1000_F_21520349_p8wbJaQQah5s0SDLq9HBTxEeuqROGLPv.jpg"
    }
    response = self.client.put(f'/listings/{listing_id}', data=json.dumps(edit_payload), content_type='application/json')
    self.assertEqual(response.status_code, 200)
    data = json.loads(response.data)
    self.assertEqual(data["message"], "Listing updated")

  def test_delete_listing(self):
    response = self.client.delete(f'/listings/{listing_id}?user_id=1')
    self.assertEqual(response.status_code, 200)
    data = json.loads(response.data)
    self.assertEqual(data["message"], "Listing removed")

  def test_view_user_listings(self):
    response = self.client.get('/listings/user/10')
    self.assertEqual(response.status_code, 200)
    data = json.loads(response.data)
    self.assertIn("listings", data)
    listing_ids = [listing["id"] for listing in data["listings"]]
    self.assertIn(self.listing_id, listing_ids)

  def test_add_claim(self):
    claim_payload = {
      "claimer_id": 1,
      "message": "I want this textbook."
    }
    response = self.client.post(f'/claims/{listing_id}', data=json.dumps(claim_payload), content_type='application/json')
    self.assertEqual(response.status_code, 200)
    data = json.loads(response.data)
    self.assertEqual(data["message"], "Claim submitted")

  def test_get_claims_for_user(self);
    claim_payload = {
      "claimer_id": 1,
      "message": "I want this textbook."
    }
    self.client.post(f'/claims/{listing_id}', data=json.dumps(claim_payload), content_type='application/json')
    response = self.client.get('/claims/user/3')
    self.assertEqual(response.status_code, 200)
    data = json.loads(response.data)
    self.assertEqual(data["claimer_id"], 3)
    self.assertGreaterEqual(len(data["claims"]), 1)

  def test_get_claims_for_listing(self);
    claim_payload = {
      "claimer_id": 1,
      "message": "I want this textbook."
    }
    self.client.post(f'/claims/{listing_id}', data=json.dumps(claim_payload), content_type='application/json')
    response = self.client.get(f'/claims/listing/{listing_id}')
    self.assertEqual(response.status_code, 200)
    data = json.loads(response.data)
    self.assertEqual(data["listing_id"], listing_id)
    self.assertGreaterEqual(len(data["claims"]), 1)
