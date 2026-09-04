# HavenFlo 🌿

**HavenFlo** is a secure, multi-location, enterprise-grade residential tracking dashboard designed specifically for sober living networks. Moving beyond standard property management metrics, HavenFlo integrates an algorithmic **Trauma-Informed Placement (TIP)** engine to score and prioritize bed assignments based on safety, client autonomy, sensory needs, and geographic stability.

Built entirely from scratch as a solo CIS Senior Capstone project, this application showcases robust database normalization, secure role-based access controls (RBAC), and clean, responsive UI/UX engineering.

---

## 🚀 Core Features

### 🏢 Multi-Location Portfolio Control
*   **Global Census Monitoring:** Aggregate real-time data visualizations displaying capacity metrics across multiple properties simultaneously.
*   **Granular Interactive Grids:** Drill-down views rendering individual property floor plans, rooms, and specific bed designations (e.g., lower vs. upper bunks).
*   **Role-Based Access Control (RBAC):** Strict data concealment protocols separating global admin privileges from localized house manager views to support data minimization.

### 🧠 Trauma-Informed Placement (TIP) Engine
*   **Geographic Safety Buffers:** Automated backend filtering that leverages spatial coordinates to exclude placement choices located within a critical proximity radius of a resident's documented trauma triggers.
*   **Sensory & Environmental Trait Matching:** An algorithmic weighted matrix that de-prioritizes high-traffic rooms or upper bunks for residents presenting with severe anxiety, panic disorders, or claustrophobia.
*   **The Power of Choice Interface:** Instead of arbitrary automated system assignment, the dashboard computes and generates the "Top 3 Safest Options" so intake workers can present agency and choice directly to the resident.

---

## 🛠️ Tech Stack & Architecture

*   **Language & Backend Framework:** Python 3 (Django MVC/MVT Architecture)
*   **Frontend UI/UX:** Semantic HTML5, Custom CSS3 Grid/Flexbox Layouts, JavaScript (Vanilla)
*   **Database Engine:** PostgreSQL (Optimized for relational entity tracking and structural mapping)
*   **Version Control & Deployment:** Git & GitHub

```text
├── core_project/           # Central project configuration and security settings
├── apps/
│   ├── matching_engine/    # Python algorithms governing trauma scoring matrices
│   └── dashboard/          # HTML/CSS view controllers handling multi-property grids
├── static/                 # Custom CSS stylesheets, assets, and modular UI components
├── templates/              # Server-side rendered Django HTML templates
├── .gitignore              # Strict environmental and database file exclusion rules
├── requirements.txt        # Consolidated Python package dependencies
└── README.md               # Primary project documentation
```

---

## 🔒 Security & Data Compliance Design

Designed with strict adherence to systems security principles studied throughout the UMA Computer Information Systems curriculum:
*   **Vulnerability Mitigation:** Native mitigation vectors against SQL Injection, Cross-Site Scripting (XSS), and Cross-Site Request Forgery (CSRF).
*   **HIPAA & 42 CFR Part 2 Awareness:** Structural isolation of Personally Identifiable Information (PII) and Protected Health Information (PHI). Resident identities and trauma profiles are concealed until an authorized staff member explicitly initiates a placement audit.

---

## ⚙️ Local Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd havenflo
   ```

2. **Create and activate a isolated Python virtual environment:**
   ```bash
   python -m venv env
   # On Windows:
   env\Scripts\activate
   # On macOS/Linux:
   source env/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Initialize local development server:**
   ```bash
   python manage.py runserver
   ```
   Navigate to `http://127.0.0` in your web browser.

---

## 📝 Academic Portfolio Context
This project serves as a Senior Capstone demonstrating competencies in software engineering, database management systems, and web architecture acquired through the **University of Maine at Augusta (UMA)** Computer Information Systems (CIS) program.
