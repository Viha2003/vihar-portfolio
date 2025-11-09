import streamlit as st
from datetime import date

# ---------- Page Config ----------
st.set_page_config(
    page_title="Vihar Konda | Portfolio",
    page_icon="📊",
    layout="wide"
)

# ---------- Helper: Link Button ---------

def link_button(label: str, url: str, key: str = None):
    st.markdown(
        f"""
        <a href="{url}" target="_blank">
            <button style="padding:8px 14px;border-radius:12px;border:1px solid rgba(0,0,0,0.1);cursor:pointer;background:#f7f7f8;">{label}</button>
        </a>
        """,
        unsafe_allow_html=True,
    )

# ---------- Sidebar Navigation ----------
sections = [
    "Home",
    "About",
    "Projects",
    "Skills",
    "Education",
    "Internships",
    "Courses & Certifications",
    "Contact",
]

with st.sidebar:
    st.title("📌 Navigate")
    choice = st.radio("Go to", sections, index=0)
    st.markdown("---")
    st.caption("© " + str(date.today().year) + " · Vihar Konda | Data & AI Professional")

# ---------- Header (Persistent) ----------
col1, col2 = st.columns([1, 3], vertical_alignment="center")
with col1:
    st.image(
        "https://lh3.googleusercontent.com/d/1Wa9XSw500o7mcvkAheOHGVUc96HKGNBa",
        caption="Vihar Konda",
        use_container_width=True,
    )
with col2:
    st.title("Vihar Konda")
    st.subheader("Turning Data into Decisions — AI • ML • Business Analytics • SQL")
    top_col1, top_col2, top_col3, top_col4 = st.columns(4)
    with top_col1:
        link_button("LinkedIn", "https://www.linkedin.com/in/konda-vihar-65291b239/")
    with top_col2:
        link_button("GitHub", "https://github.com/Viha2003")
    with top_col3:
        link_button("Email", "mailto:viharkonda999@gmail.com")
    with top_col4:
        link_button("Download Resume", "#")  # replace with your resume link

st.markdown("---")

# ---------- Content Sections ----------

if choice == "Home":
    st.header("👋 Hello!")
    st.write(
        """
        I'm an aspiring **AI/ML & Business Analytics** engineer who loves building
        data products that convert raw data into **clear, actionable insights**.
        
        - ✅ Strong foundation in **Python, ML, SQL, and Visualization**
        - ✅ Experienced with **EDA, data cleaning, and forecasting**
        - ✅ Comfortable turning business questions into **data-driven answers**
        
        Explore my projects, experience, and certifications — and feel free to reach out!
        """
    )

if choice == "About":
    st.header("👨‍🎓 About Me")
    st.write(
        """
        I'm pursuing an **Integrated M.Tech at VIT Chennai** with a **CGPA of 8.84/10**.
        I've completed **50+ courses and certifications** across AI, ML, and Business Analytics (Coursera, Great Learning)
        and cleared **TCS NQT** with a **score of 2271.46/3000 (75.72%)**.

        I'm currently a **Engineering Trainee at Infosys (since August 2026)**, gaining hands-on experience in real-world development environments.

        I'm passionate about building **interactive visualization tools**,
        **machine learning and data science models**, and **user-friendly analytics apps** that help
        stakeholders make better decisions.
        """
    )

    st.markdown("### Highlights")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Courses & Certifications", "50+", "AI/ML/BA")
    with c2:
        st.metric("TCS NQT", "2271.46/3000", "+75.72%")
    with c3:
        st.metric("Focus", "AI • ML • SQL • BA", "End-to-End")
if choice == "Projects":
    st.header("🧩 Projects")

    projects = [
        {
            "title": "INSIGHTIFY DATA — Smart Visualization & Forecasting",
            "tags": ["Streamlit", "Python", "scikit-learn", "pandas", "matplotlib"],
            "desc": "Capstone app that lets users upload data, clean, perform EDA, create visualizations (2D/3D), split train/test, choose ML models, view metrics (Accuracy, RMSE), and make predictions.",
            "code": "https://github.com/",
            "demo": "https://streamlit.io/"
        },
        {
            "title": "Crop Recommendation System",
            "tags": ["Python", "scikit-learn"],
            "desc": "Recommends optimal crops based on soil and weather parameters using supervised ML.",
            "code": "https://github.com/",
            "demo": ""
        },
        {
            "title": "Sales Prediction Model",
            "tags": ["Regression", "pandas", "scikit-learn"],
            "desc": "Predicts product sales; achieved ~90% accuracy on validation data.",
            "code": "https://github.com/",
            "demo": ""
        },
        {
            "title": "Business Insights Dashboard",
            "tags": ["Tableau", "Power BI"],
            "desc": "Interactive dashboards to communicate KPIs and trends for decision-makers.",
            "code": "https://github.com/",
            "demo": ""
        },
    ]

    for p in projects:
        with st.container(border=True):
            st.subheader(p["title"]) 
            st.caption(" • ".join(p["tags"]))
            st.write(p["desc"])
            b1, b2 = st.columns(2)
            with b1:
                if p["code"]:
                    link_button("View Code", p["code"], key=p["title"]+"code")
            with b2:
                if p["demo"]:
                    link_button("Live Demo", p["demo"], key=p["title"]+"demo")

if choice == "Skills":
    st.header("🧠 Skills")

    st.markdown("#### Programming")
    st.write("Python, Java, C, R, SQL")

    st.markdown("#### Data & ML")
    st.write("Data Cleaning, EDA, Regression, Classification, Clustering, Statistical Analysis")

    st.markdown("#### Visualization")
    st.write("Tableau, Power BI, Matplotlib, (Seaborn if needed)")

    st.markdown("#### Soft Skills")
    st.write("Collaborative communication, problem-solving, adaptability, innovation")

if choice == "Education":
    st.header("🎓 Education")

    with st.container(border=True):
        st.subheader("Integrated M.Tech — VIT Chennai (2020–2025)")
        st.write("CGPA: **8.84/10.00**")

    c1, c2 = st.columns(2)
    with c1:
        with st.container(border=True):
            st.subheader("Class XII — Sri Chaitanya Junior Kalashala (2020)")
            st.write("Score: **951/1000**")
    with c2:
        with st.container(border=True):
            st.subheader("Class X — Jeevadan High School (2018)")
            st.write("CGPA: **9.2/10.00**")

if choice == "Internships":
    st.header("🧪 Internships")
    with st.container(border=True):
        st.subheader("Python Intern — Mallikarjuna Infosys (Microsoft Collaboration)")
        st.caption("Jun 2023 – Aug 2023")
        st.write("Developed Python applications, debugging and collaborating in an agile team.")
    with st.container(border=True):
        st.subheader("AI Intern — Edunet (IBM & AICTE Collaboration)")
        st.caption("Aug 2023 – Oct 2023")
        st.write("Applied ML techniques to real datasets; strengthened foundations in AI.")

if choice == "Courses & Certifications":
    st.header("📜 Courses & Certifications")
    st.write("Completed 50+ courses in AI, ML, and Business Analytics from Coursera, Great Learning, and IBM AICTE.")
    st.markdown(
        """[Click here to view all certificates](https://drive.google.com/drive/folders/1ETag3ZNW2PLQOD4h5R-STfmRHjgV5-Wj)"""
    )

if choice == "Contact":
    st.header("📬 Contact Me")
    st.write("I'd love to connect for roles, collaborations, or feedback.")

    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send")

    if submitted:
        st.success("Thanks! This demo form doesn't send email on Streamlit Cloud. Replace with a webhook or mailto link.")
        st.info("Tip: Use services like Formspree or Basin to receive form submissions.")

# ---------- Footer ----------
st.markdown("---")
st.caption("Developed by Vihar Konda · Data & AI Professional · © 2025")
