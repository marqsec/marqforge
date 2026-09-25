import unittest
import marqforge

class TestMarqForgeMetadata(unittest.TestCase):
    def test_version_output(self)  -> None:
        """Memastikan fungsi get_version mengembalikan struktur data yang benar."""
        version_info = marqforge.get_version()
        self.assertIn("major", version_info)
        self.assertIn("full", version_info)
        self.assertIsInstance(version_info["major"], int)

    def test_project_output(self) -> None:
        """Memastikan profil proyek MarqForge terbaca dengan benar dari metadata."""
        project_info = marqforge.get_project()
        self.assertEqual(project_info["name"], "marqforge")
        self.assertEqual(project_info["author"], "Marq (MarqSec)")
        self.assertIn("://github.com", project_info["repository"])

    def test_runtime_output(self) -> None:
        """Memastikan informasi lingkungan runtime Python dan OS berhasil diambil."""
        runtime_info = marqforge.get_runtime()
        self.assertIn("python", runtime_info)
        self.assertIn("platform", runtime_info)

if __name__ == "__main__":
    unittest.main()
