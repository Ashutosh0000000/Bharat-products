# 🇮🇳 Bharat Products – Made in India Platform

**Bharat Products** is a scalable backend and UI platform built to promote and support **Made-in-India** products. More than a catalog, it’s a step towards building a self-reliant (AatmaNirbhar Bharat) product ecosystem.

---

## 🚀 Project Highlights

- Manage and discover Indian products with categories, ratings, and stock info.
- Natural language “Need Help Choosing?” feature to suggest products based on user problems.
- Real-time trending products with Redis caching for fast and efficient queries.
- Deployed backend using FastAPI, PostgreSQL, Redis, and Docker.

---

## 🧰 Tech Stack

- **Backend:** FastAPI, Python 3.11, async SQLAlchemy  
- **Database:** PostgreSQL (async)  
- **Caching:** Redis  
- **Frontend:** Streamlit (prototype UI)  
- **Deployment:** Docker, Render

---

## 🔗 Try the Backend API

Test the live backend on Render:  
https://bharat-products-e0et.onrender.com/docs

Explore the OpenAPI docs and test endpoints directly.

---

## 🛠️ Run Locally

```bash
git clone https://github.com/Ashutosh0000000/Bharat-Products-Made-in-India.git
cd Bharat-Products-Made-in-India/app
pip install -r requirements.txt
uvicorn main:app --reload
Or use Docker:

bash
Copy code
docker-compose up --build
