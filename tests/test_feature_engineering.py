from nbresult import ChallengeResultTestCase


class TestFeatureEngineering(ChallengeResultTestCase):
    def test_df_posts_new_exists(self):
        self.assertIsNotNone(
            self.result.df_posts_new_shape,
            "df_posts_new not found")

    def test_historical_likes_column(self):
        self.assertTrue(self.result.has_historical_likes,
                        "Column 'historical_likes' not found in df_posts_new")

    def test_no_nan_values(self):
        self.assertEqual(
            self.result.historical_likes_nan_count,
            0,
            f"Found {self.result.historical_likes_nan_count} NaN values in historical_likes")
