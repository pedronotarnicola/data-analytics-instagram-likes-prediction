# Instagram Likes Prediction

## Business problem
Predict how many likes an Instagram post will get, based on account-level metrics. Content creators and marketing teams use this kind of model to forecast post performance and identify which accounts are worth prioritizing for a campaign.

## Dataset
- **Source**: Le Wagon Data Analytics Bootcamp (real-world dataset, 1,000+ Instagram posts)
- **Features**: follower count, comment count, post count, and post timestamp per author
- **Target**: number of likes on the post

## Approach
Two models were built and compared:
1. **Model 1 (baseline)**: predicts likes using only follower count
2. **Model 2**: adds `historical_likes` — the median number of likes on each author's previous posts — as a second feature, testing the hypothesis that past engagement predicts future engagement

Both models are Linear Regression, trained on a scaled 75/25 train/test split.

## Tools used
`Python` `pandas` `scikit-learn` `plotly`

## Key findings
| Model | R² (test) | MAE (test) |
|---|---|---|
| Model 1 — Followers only | 0.263 | 32.9 likes |
| Model 2 — Followers + Historical likes | 0.564 | 23.1 likes |

Adding historical engagement as a feature more than doubled the model's explanatory power (**+114% R²**) and cut the average prediction error by about 9 likes. Follower count alone is a weak predictor on its own — how an account has performed historically matters more than how large it is.

## Business recommendation
When forecasting a post's likely engagement (e.g., to evaluate an influencer for a campaign), follower count alone is not a reliable filter. A short history of an account's recent posts is a far stronger signal and should be weighted more heavily than audience size.

## Limitations
- Both models are still far from highly accurate (R² of 0.56) — engagement depends heavily on content itself (image, caption, timing), which isn't captured in this dataset.
- `historical_likes` requires an account to already have prior posts, so this approach doesn't work for brand-new accounts.

## How to run this project
```bash
git clone https://github.com/pedronotarnicola/instagram-likes-prediction.git
cd instagram-likes-prediction
pip install -r requirements.txt
jupyter notebook notebooks/analysis.ipynb
```

## Folder structure
```
instagram-likes-prediction/
├── notebooks/
│   └── analysis.ipynb
├── README.md
└── requirements.txt
```

---
[Portfolio](https://pedronotarnicola.github.io/) · [LinkedIn](https://www.linkedin.com/in/p-l-notarnicola/)
