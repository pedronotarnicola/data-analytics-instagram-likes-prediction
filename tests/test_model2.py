from nbresult import ChallengeResultTestCase


class TestModel2(ChallengeResultTestCase):
    def test_X_shape(self):
        self.assertGreaterEqual(
            self.result.X_shape[1],
            2,
            f"X should have at least 2 feature columns, got {self.result.X_shape[1]}")
        self.assertLessEqual(
            self.result.X_shape[1],
            5,
            f"X should be a focused feature selection. Got {self.result.X_shape[1]} features")

    def test_model_2_score(self):
        r2 = self.result.model_2_r2
        self.assertGreater(r2, 0.3, f"Model 2 R2 score {r2:.2f} is too low")
        self.assertLess(
            r2, 1.0, f"Model 2 R2 score {r2:.2f} is suspiciously high")

    def test_model_improvement(self):
        self.assertGreater(
            self.result.model_2_r2,
            self.result.model_1_r2,
            f"Model 2 (R2={self.result.model_2_r2:.2f}) should perform better than Model 1 (R2={self.result.model_1_r2:.2f})")

    def test_r2_not_suspiciously_perfect(self):
        """Defensive check: Detect if model was evaluated on training data"""
        r2 = self.result.model_2_r2
        self.assertLess(
            r2, 0.98, f"R² of {r2:.3f} is suspiciously high. "
            f"Did you evaluate on training data? Use: model_2.score(X_test_scaled, y_test)")

    def test_both_models_not_evaluated_on_train(self):
        """Defensive check: Detect if both models were evaluated on training data"""
        # If both models have suspiciously high R², likely evaluated on train
        # data
        if self.result.model_1_r2 > 0.9 and self.result.model_2_r2 > 0.9:
            self.fail(
                f"Both models have very high R² (Model 1: {self.result.model_1_r2:.3f}, Model 2: {self.result.model_2_r2:.3f}). "
                f"Did you evaluate on training data? Both should use: model.score(X_test_scaled, y_test)")
