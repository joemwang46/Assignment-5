## 🚀 How to Use This Template

This repository is a starter template for building and testing trading strategies with CI integration. Follow these steps to create your own copy and begin working:

### 🧩 Step 1: Create Your Own Repository

1. Go to [trading-ci-lab](https://github.com/sdonadio/trading-ci-lab)
2. Click the green **“Use this template”** button  
3. Name your new repository (e.g., `ci-homework-01`)  
4. Choose **Public** or **Private**  
5. Click **“Create repository from template”**

---

### 💻 Step 2: Clone Your Repository Locally

```bash
git clone git@github.com:your-username/ci-homework-01.git
cd ci-homework-01
```

> If you're using HTTPS instead of SSH:
> ```bash
> git clone https://github.com/your-username/ci-homework-01.git
> ```

---

### 🧪 Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### ⚙️ Step 4: Run Tests and Check Coverage

```bash
coverage run -m pytest
coverage report -m
```

To view an interactive HTML report:

```bash
coverage html
open htmlcov/index.html  # macOS
```

---

### 🔁 Step 5: Push Changes and Create a Pull Request

```bash
git add .
git commit -m "Implement strategy and tests"
git push
```

Then go to GitHub and open a **Pull Request** from your branch to `main`.
