import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from verify import verify

class VerifyTests(unittest.TestCase):
    def test_agent_claim_cannot_replace_evidence(self):
        task = {"agent_reported_status": "complete", "acceptance_criteria": ["tested"], "evidence": [], "owner_approved": True}
        self.assertEqual(verify(task)["status"], "UNVERIFIED")

    def test_evidence_still_requires_approval(self):
        task = {"acceptance_criteria": ["tested"], "evidence": ["tested"], "owner_approved": False}
        self.assertEqual(verify(task)["status"], "AWAITING_APPROVAL")

    def test_complete_with_evidence_and_approval(self):
        task = {"acceptance_criteria": ["tested"], "evidence": ["tested"], "owner_approved": True}
        self.assertEqual(verify(task)["status"], "VERIFIED")

    def test_missing_acceptance_criteria(self):
        self.assertEqual(verify({})["status"], "BLOCKED")

if __name__ == "__main__":
    unittest.main()
