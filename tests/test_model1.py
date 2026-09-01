from nbresult import ChallengeResultTestCase


class TestModel1(ChallengeResultTestCase):
    def test_X_shape(self):
        self.assertGreaterEqual(
            self.result.X_shape[1],
            1,
            f"X should have at least 1 feature column, got {self.result.X_shape[1]}")
        self.assertLessEqual(
            self.result.X_shape[1],
            3,
            f"X should be a focused feature selection, not all columns. Got {self.result.X_shape[1]} features")

    def test_predictions_exist(self):
        self.assertIsNotNone(self.result.pred_length, "pred_model_1 not found")

    def test_r2_score(self):
        r2 = self.result.model_1_r2
        self.assertGreater(r2, -0.5, f"Model 1 R2 score {r2:.2f} is too low")
        self.assertLess(
            r2, 1.0, f"Model 1 R2 score {r2:.2f} is suspiciously high")

    def test_r2_not_suspiciously_perfect(self):
        """Defensive check: Detect if model was evaluated on training data"""
        r2 = self.result.model_1_r2
        self.assertLess(
            r2, 0.95, f"R² of {r2:.3f} is suspiciously high. "
            f"Did you evaluate on training data? Use: model_1.score(X_test_scaled, y_test)")

    def test_r2_suggests_proper_training(self):
        """Defensive check: Very low R² may indicate training on unscaled data"""
        r2 = self.result.model_1_r2
        self.assertGreater(
            r2,
            -0.3,
            f"R² of {r2:.3f} is very low. "
            f"Did you train on unscaled data or use wrong features? "
            f"Use: model_1.fit(X_train_scaled, y_train)"
        )
