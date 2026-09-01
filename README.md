# 🎯 Instructions

## 📁 Setup

To make challenge completion simpler, we have added terminal instructions to challenges that have test suites.

If you haven't already, **copy the terminal instructions at the top of this page and run them in your terminal**.

This will:

- Download a repository containing all of the files for this challenge from github
- Create and navigate to a directory (folder) for this challenge in your terminal
- Set up a new github repository
- Open the challenge in vs code
- Run the test suite for this challenge

Run the following command in the terminal to check you are in the right directory:

```bash
pwd
```

Your result should look like this:

```bash
~/code/<user.github_nickname>/{{ local_path_to("07-Machine-Learning/02-Python-For-AI-Regression/01-Instagram-Likes-Prediction") }}/
```

❌ If it doesn't, consult a TA!

✅ If it does, then you are ready to take on this challenge!

## Jupyter Notebooks

**📍 In your terminal**, run this command to start Jupyter:

```bash
jupyter notebook
```

This will:

1. Start a Jupyter server in your terminal
2. Open your web browser automatically
3. Show a file browser with your challenge files

**👉 Click on the `.ipynb` file to open your challenge notebook.**

## 💻 Working with Multiple Terminal Tabs

**Important:** When you run `jupyter notebook`, it will start a server that keeps running in your terminal. This means you won't be able to run other commands (like git commands) in that same terminal tab.

### Here's what to do:

1. **Open a new terminal tab** (usually `Cmd + T` on Mac or `Ctrl + Shift + T` on Windows/Linux)
2. Use this new tab for running git commands (`git add`, `git commit`, etc.)
3. Keep the original tab running Jupyter Notebook - don't close it while you're working!

### When you're finished with the challenge:

1. **Save your notebook** (File → Save in Jupyter, or `Cmd/Ctrl + S`)
2. Go back to the terminal tab where Jupyter is running
3. Press `Ctrl + C` to stop the Jupyter server
4. You'll see a message asking: `Shutdown this notebook server (y/[n])?`
5. Type `y` and press Enter to confirm

Now you can use that terminal tab for other commands again! ✅

## 🧪 Understanding the Automated Tests

This challenge includes automated tests to validate your work. Here's what you need to know:

### ⚠️ First Run: Tests Will Fail

**Don't worry!** When you first run the challenge setup, all tests will fail. This is expected - you haven't written any code yet.

Once you complete the exercises in the notebook and run tests again, they should pass.

### What Are Test Parameters?

Tests check specific **variables** in your code to ensure you've completed the required steps. For example, a test might check:

- That a variable called `df` exists and contains data
- That `X_train` has the correct shape
- That your model produces reasonable predictions

**Important:** Follow the variable names specified in the instructions. If the instructions say "store your result in `model`", the test will look for a variable called exactly `model`.

### Reading Test Error Messages

When a test fails, you'll see an error message. Here's how to interpret it:

```python
AssertionError: Expected X_train to have at least 4 columns, got 3
```

#### What this tells you:

- **What was checked:** `X_train` column count
- **What was expected:** At least 4 columns
- **What you have:** 3 columns
- **How to fix:** Add the missing feature(s) to your `X` selection

### Common Test Patterns

- **Shape checks:** `AssertionError: Expected shape (100, 4), got (100, 3)` → You're missing a column or row
- **Type checks:** `AssertionError: Expected DataFrame, got ndarray` → Convert your data structure
- **Existence checks:** `AttributeError: 'ChallengeResult' object has no attribute 'model'` → You didn't create or didn't name a required variable
- **Value checks:** `AssertionError: Score should be between 0 and 1` → Check your calculation logic

### Tips for Success

🔍 **Follow variable names exactly** as specified in the instructions

🔍 **Read error messages carefully** - they tell you what's wrong

🔍 **Check your variable names** - `Model` ≠ `model`

👍 **You can add extra columns** to DataFrames for exploration - tests check for minimum requirements

♻️ **Run tests frequently** to catch issues early
