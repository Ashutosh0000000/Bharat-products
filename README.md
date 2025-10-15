🇮🇳 Bharat Products – Made in India Platform

Bharat Products is a scalable, full-stack platform designed to promote and support Made-in-India products. It combines a powerful backend with a functional UI for product management, discovery, and intelligent recommendations — all aimed at building a self-reliant Bharat.

⚡ Built with FastAPI, Streamlit, Redis, PostgreSQL, and Docker
🚀 Fully deployed: Real APIs + Interactive UI + Admin Tools

🚀 Features

🔍 Product Catalog: List of Indian products with categories, pricing, stock, and ratings.

✍️ Admin Panel: Add, Edit, Delete products via secure interface.

💬 Need Help Choosing?: Recommends products based on user-described needs (natural language input).

📊 Dashboard: Monitor views, inventory, and trends.

⚡ Redis Caching: Faster API responses using smart cache with TTL + invalidation.

🧱 Clean Architecture: Scalable codebase using async Python & modular design.

🧰 Tech Stack
Layer	Tech
Backend	FastAPI (async), Python 3.11
Database	PostgreSQL (with async SQLAlchemy)
Caching	Redis (async, TTL-based)
Frontend	Streamlit (admin UI + filters)
Deployment	Docker + Render
🔗 Live Links

🧪 API Docs (Swagger): https://bharat-products-e0et.onrender.com/docs

🌐 Streamlit App: https://ashutosh0000000-bharat-products-made-in-in-streamlit-app-zxycey.streamlit.app

📸 Screenshots
<details> <summary>Click to view</summary>

</details>
🛠️ Run Locally
git clone https://github.com/Ashutosh0000000/Bharat-Products-Made-in-India.git
cd Bharat-Products-Made-in-India/app
pip install -r requirements.txt
uvicorn main:app --reload

Or with Docker
docker-compose up --build

📌 Future Improvements

✅ Add user authentication (OAuth or JWT)

✅ Add user reviews and ratings

✅ Pagination and sorting

✅ ML-based personalized recommendations

🧑‍💻 Contributors

@Ashutosh0000000
