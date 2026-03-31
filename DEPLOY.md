# 🛰 SatChange AI — Deploy Guide

## HuggingFace Spaces pe FREE Deploy (No Card!)

### Step 1: HuggingFace Account
1. huggingface.co pe jaao
2. FREE account banao (no credit card)
3. GitHub se login kar sakte ho

### Step 2: New Space banao
1. huggingface.co/new-space pe jaao
2. Fill karo:
   - Space name: satchange-ai
   - License: MIT
   - **SDK: Docker** ← zaroor select karo
3. "Create Space" click karo

### Step 3: Code Upload karo
Option A — GitHub se:
```
git init
git add .
git commit -m "SatChange AI"
git remote add hf https://huggingface.co/spaces/TUMHARA_USERNAME/satchange-ai
git push hf main
```

Option B — Directly upload karo files:
- HuggingFace Space ke andar "Files" tab
- Drag & drop karo saare files

### Step 4: Wait karo ~3 min
- HuggingFace automatically Docker build karega
- URL milega: https://TUMHARA_USERNAME-satchange-ai.hf.space

### Bas! Live ho gaya 🎉

---

## Real Satellite Data Enable karna (Optional, FREE)

1. earthengine.google.com pe FREE account banao
2. Terminal mein:
```bash
pip install earthengine-api
earthengine authenticate
```
3. backend/app.py mein:
```python
# Line dhundo:
# In production: call model/predict.py here
# Wahan replace karo:
from model.predict import fetch_real_images_gee, predict_change
img1, img2 = fetch_real_images_gee(req.lat, req.lon, req.date1, req.date2)
result = predict_change(img1, img2)
```

---

## Paise Kaise Kamao

### Free tier:
- 10 analyses/month free
- Watermarked results

### Paid plans (add Stripe baad mein):
- Researcher: $29/month — 100 analyses
- NGO: $99/month — 500 analyses
- Enterprise: $499/month — unlimited + API access

### Direct clients:
- Environment NGOs (WWF, Greenpeace type)
- Insurance companies (flood risk assessment)
- Government land departments
- Climate tech startups

---

## Project Structure
```
satchange/
├── backend/
│   └── app.py          ← FastAPI server
├── model/
│   └── predict.py      ← ML model (Siamese U-Net)
├── frontend/
│   └── index.html      ← Dashboard UI
├── Dockerfile          ← HuggingFace deploy
├── requirements.txt
└── README.md
```
