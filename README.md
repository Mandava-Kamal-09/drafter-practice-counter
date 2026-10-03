# Kamal's Counter

A Drafter V2 counter for Final Project Practice. Use +1, -1, and Reset to change the count. Reloading starts a new counter at zero.

Run locally with Python 3.10 or newer:

```text
python -m pip install -r requirements.txt
python app.py
```

Build a static site:

```text
python -m drafter app.py --compile --output-directory _site --production
```

For deployment, upload this directory's files to a public GitHub repository on the main branch. In repository Settings, set Pages Source to GitHub Actions. The deployment workflow runs on push or through Actions > Run workflow. Open the deployed github.io URL and check all three buttons before submitting that live URL to Canvas.

The app sets a browser-tab title, fills the About information, and hides the debug panel. It includes four startup checks using Drafter's testing functions.

References: [counter tutorial](https://drafter-edu.github.io/drafter/start/first-app/), [release settings](https://drafter-edu.github.io/drafter/your-project/deploy/prepare/), and [GitHub Actions deployment](https://drafter-edu.github.io/drafter/extend/github-actions/).
