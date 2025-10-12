import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

API_BASE = "http://localhost:8000"  # Change if your backend URL is different

# --- API calls ---

def fetch_products(params=None):
    try:
        resp = requests.get(f"{API_BASE}/products", params=params or {}, timeout=5)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        st.error(f"Failed to fetch products: {e}")
        return {"total": 0, "items": []}

def create_product(data):
    try:
        resp = requests.post(f"{API_BASE}/products", json=data, timeout=5)
        resp.raise_for_status()
        return True
    except Exception as e:
        st.error(f"Failed to create product: {e}")
        return False

def update_product(product_id, data):
    try:
        resp = requests.put(f"{API_BASE}/products/{product_id}", json=data, timeout=5)
        resp.raise_for_status()
        return True
    except Exception as e:
        st.error(f"Failed to update product: {e}")
        return False

def delete_product(product_id):
    try:
        resp = requests.delete(f"{API_BASE}/products/{product_id}", timeout=5)
        resp.raise_for_status()
        return True
    except Exception as e:
        st.error(f"Failed to delete product: {e}")
        return False

# --- UI functions ---

def show_dashboard(products):
    st.title("📊 Product Dashboard & Insights")

    if not products:
        st.warning("No products to show.")
        return

    df = pd.DataFrame(products)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Products", len(df))
    col2.metric("Average Price", f"₹{df['price'].mean():.2f}")
    col3.metric("Average Rating", f"{df['rating'].mean():.2f} ⭐")
    col4.metric("Total Stock", int(df['stock'].sum()))

    st.markdown("### Category Distribution")
    cat_counts = df['category'].value_counts()
    fig1, ax1 = plt.subplots()
    ax1.pie(cat_counts, labels=cat_counts.index, autopct='%1.1f%%', startangle=140)
    ax1.axis('equal')
    st.pyplot(fig1)

    st.markdown("### Price Distribution")
    fig2, ax2 = plt.subplots()
    ax2.hist(df['price'], bins=20, color='skyblue', edgecolor='black')
    ax2.set_xlabel("Price (₹)")
    ax2.set_ylabel("Number of Products")
    st.pyplot(fig2)

    st.markdown("### 🔥 Trending Products (Top Rated)")
    trending = df.sort_values(by='rating', ascending=False).head(5)
    for _, row in trending.iterrows():
        st.write(f"**{row['name']}** - ₹{row['price']} - ⭐ {row['rating']}")
        if row.get("image_url") and row["image_url"].startswith("http"):
            st.image(row["image_url"], width=120)
        st.write(f"*{row.get('description', 'No description')}*")
        st.markdown("---")

def show_product_list():
    st.title("📦 Product List & Management")

    # Filters
    st.sidebar.header("Filters")
    search = st.sidebar.text_input("Search by Name")
    category = st.sidebar.text_input("Category")
    min_price = st.sidebar.number_input("Min Price", min_value=0.0, value=0.0)
    max_price = st.sidebar.number_input("Max Price", min_value=0.0, value=100000.0)
    sort_by = st.sidebar.selectbox("Sort By", options=["", "price", "rating", "name"])
    order = st.sidebar.radio("Order", options=["asc", "desc"])

    params = {
        "search": search if search else None,
        "category": category if category else None,
        "min_price": min_price if min_price > 0 else None,
        "max_price": max_price if max_price > 0 else None,
        "sort_by": sort_by if sort_by else None,
        "order": order,
    }

    data = fetch_products(params)
    total = data.get("total", 0)
    items = data.get("items", [])

    if not items:
        st.warning("No products found with current filters.")
        return

    df = pd.DataFrame(items)

    st.write(f"### Total products found: {total}")

    # Select product to edit/delete
    product_names = df["name"].tolist()
    selected_product_name = st.radio("Select product to Edit / Delete", options=product_names)
    selected_product = df[df["name"] == selected_product_name].iloc[0]

    st.markdown(f"## Editing: {selected_product['name']}")

    if selected_product.get("image_url") and selected_product["image_url"].startswith("http"):
        st.image(selected_product["image_url"], width=200)
    else:
        st.write("No Image Available")

    with st.form(key=f"edit_form_{selected_product['id']}"):
        name = st.text_input("Name", value=selected_product["name"])
        price = st.number_input("Price", min_value=0.0, value=selected_product["price"])
        rating = st.number_input("Rating", min_value=0.0, max_value=5.0, step=0.1, value=selected_product.get("rating", 0.0))
        category_c = st.text_input("Category", value=selected_product.get("category", ""))
        stock = st.number_input("Stock", min_value=0, step=1, value=selected_product.get("stock", 0))
        description = st.text_area("Description", value=selected_product.get("description", ""))
        image_url = st.text_input("Image URL", value=selected_product.get("image_url", ""))
        update_btn = st.form_submit_button("Update Product")
        delete_btn = st.form_submit_button("Delete Product")

        if update_btn:
            updated_data = {
                "name": name,
                "price": price,
                "rating": rating,
                "category": category_c,
                "stock": stock,
                "description": description,
                "image_url": image_url,
            }
            if update_product(selected_product["id"], updated_data):
                st.success("Product updated successfully!")
                st.experimental_rerun()

        if delete_btn:
            if delete_product(selected_product["id"]):
                st.success("Product deleted successfully!")
                st.experimental_rerun()

def show_add_product():
    st.title("➕ Add New Product")

    with st.form(key="add_product_form"):
        name = st.text_input("Name")
        price = st.number_input("Price", min_value=0.0)
        rating = st.number_input("Rating", min_value=0.0, max_value=5.0, step=0.1)
        category_c = st.text_input("Category")
        stock = st.number_input("Stock", min_value=0, step=1)
        description = st.text_area("Description")
        image_url = st.text_input("Image URL")
        submit = st.form_submit_button("Add Product")

        if submit:
            if not name:
                st.error("Name is required.")
                return
            new_data = {
                "name": name,
                "price": price,
                "rating": rating,
                "category": category_c,
                "stock": stock,
                "description": description,
                "image_url": image_url,
            }
            if create_product(new_data):
                st.success("Product added successfully!")
                st.experimental_rerun()

def main():
    st.sidebar.title("Navigation")
    options = ["Dashboard", "Product List", "Add Product"]
    choice = st.sidebar.radio("Go to", options)

    if choice == "Dashboard":
        # Pass limit param properly as dict
        all_products = fetch_products(params={"limit": 1000}).get("items", [])
        show_dashboard(all_products)
    elif choice == "Product List":
        show_product_list()
    elif choice == "Add Product":
        show_add_product()

if __name__ == "__main__":
    main()
