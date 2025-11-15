# 🇮🇳 Bharat Products – Made in India Platform

Bharat Products is a scalable, full-stack platform designed to promote and support Made-in-India products. It combines a powerful backend with a functional UI for product management, discovery, and intelligent recommendations — all aimed at building a self-reliant Bharat.

⚡ Built with FastAPI, Streamlit, Redis, PostgreSQL, and Docker
🚀 Fully deployed: Real APIs + Interactive UI + Admin Tools

Screenshots
<img width="546" height="637" alt="image" src="https://github.com/user-attachments/assets/f5233dd7-28cb-43d4-8ab1-9a29610a62e3" />
Search filter products
<img width="1900" height="892" alt="Screenshot 2025-11-09 115321" src="https://github.com/user-attachments/assets/35014ef3-fee1-407d-8e57-82ce420ed6af" />
Dashboard
<img width="1704" height="957" alt="Screenshot 2025-11-09 115007" src="https://github.com/user-attachments/assets/4241dcd1-cba7-4c1d-ace0-017764389742" />
<img width="1843" height="661" alt="Screenshot 2025-11-09 115041" src="https://github.com/user-attachments/assets/ac83d5ab-c6f8-4e59-94db-19feaf43a3a9" />
Add products local brands
<img width="1518" height="824" alt="Screenshot 2025-11-09 115113" src="https://github.com/user-attachments/assets/c383cf51-fa8d-4a08-8857-8377139938ac" />
New feature need help search
<img width="220" height="517" alt="Screenshot 2025-11-09 115122" src="https://github.com/user-attachments/assets/5b5920c5-bec6-4bc9-abb0-cd32302c48d1" />


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
