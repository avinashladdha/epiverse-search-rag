import unittest
from unittest.mock import patch, MagicMock
import sys
import os
import requests

# Add api folder to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.rag import generate_answer

class TestRAG(unittest.TestCase):

    @patch('app.rag.requests.post')
    def test_generate_answer_success(self, mock_post):
        # Mock successful response
        mock_response = MagicMock()
        mock_response.json.return_value = {"response": "The Epiverse is a set of R packages."}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        query = "What is epiverse?"
        context = ["Epiverse is a collaborative project.", "It produces R packages."]
        
        answer = generate_answer(query, context)
        
        self.assertEqual(answer, "The Epiverse is a set of R packages.")
        # Verify context was injected
        args, kwargs = mock_post.call_args
        self.assertIn("Epiverse is a collaborative project.", kwargs['json']['prompt'])

    @patch('app.rag.requests.post')
    def test_generate_answer_failure(self, mock_post):
        # Mock failure (e.g., connection error)
        mock_post.side_effect = requests.exceptions.RequestException("Connection refused")

        query = "What is epiverse?"
        context = ["Some context"]
        
        answer = generate_answer(query, context)
        
        self.assertIn("Error", answer)
        self.assertIn("unavailable", answer)

    def test_generate_answer_no_context(self):
        answer = generate_answer("query", [])
        self.assertEqual(answer, "No relevant documents found to generate an answer.")

if __name__ == '__main__':
    unittest.main()
