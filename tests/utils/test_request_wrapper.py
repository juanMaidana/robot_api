import unittest
import requests_adapter.request_adapter as wrapper


class TestRequestWrapper(unittest.TestCase):

    def test_get_request(self):
        requester = wrapper.RequestAdapter()
        requester.set_end_point("http://maps.googleapis.com/maps/api/geocode/json")
        location = "delhi technological university"
        requester.do_request('GET', None, {'address': location})
        self.assertEqual(requester.get_status(), 200)
        self.assertIsInstance(requester.get_json(), dict)
