from nbresult import ChallengeResultTestCase


class TestDataPreprocessing(ChallengeResultTestCase):
    def test_df_shape(self):
        rows, cols = self.result.df_shape
        self.assertGreater(rows, 100, f"DataFrame has too few rows: {rows}")
        self.assertGreater(cols, 5, f"DataFrame has too few columns: {cols}")

    def test_unique_authors(self):
        self.assertEqual(
            self.result.df_shape[0],
            self.result.unique_authors,
            "Number of rows should equal number of unique authors after deduplication")

    def test_sorted_by_timestamp(self):
        self.assertTrue(
            self.result.is_sorted,
            "DataFrame should be sorted by timestamp in ascending order")
