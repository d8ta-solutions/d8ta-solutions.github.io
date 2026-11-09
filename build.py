"""Builds the d8ta.solutions portfolio site (index + one page per project) from the data below.
Run:  python build.py      (writes index.html and projects/*.html next to this file)
"""
import html, os

ROOT = os.path.dirname(os.path.abspath(__file__))
EMAIL = "d8ta.solutions.ql@gmail.com"
LINKEDIN = ""  # set to the profile URL to show the LinkedIn link
TIKTOK = "https://www.tiktok.com/@d8ta.solutions"

PROJECTS = [
    {
        "slug": "retail", "label": "Retail", "title": "Retail Sales Performance",
        "client": "US office-supplies retailer", "data": "Sample Superstore · 9,994 order lines · FY2014–FY2017",
        "summary": "Executive view of sales, profit and margin with year-over-year comparisons, the products and states that lose money, and how discounts erode margin.",
        "pages": [
            ("Executive Overview", "Sales, profit, margin, orders, AOV and customers with YoY change; monthly trend vs. prior year; region, category and segment mix."),
            ("Profitability", "Profit by sub-category with losses highlighted, discount depth vs. margin, products with the largest losses."),
            ("Customers & Markets", "State scorecard, loss-making states, top customers and fulfillment time by ship mode."),
        ],
        "findings": [
            "FY2017 sales reached $733K, +20.4% vs. FY2016.",
            "Margin is 29.5% on full-price sales but turns negative (−37.3%) above a 20% discount.",
            "Tables, Bookcases and Supplies lose money; Tables alone loses $17.7K.",
            "10 of 49 states operate at a loss (combined −$98K), led by Texas, Ohio and Pennsylvania.",
        ],
        "model": "Star schema built in Power Query: Sales fact plus Product, Customer and a generated Date table marked for time intelligence. 40 DAX measures in display folders, including YoY comparisons, top/bottom-N rankings and dynamic narrative subtitles. Data prep fixed 5-digit postal codes, non-breaking spaces and 32 duplicate product IDs.",
        "tools": ["Power BI", "Power Query", "DAX", "Star schema", "Time intelligence"],
        "video": ("retail-sales", "Why this store kept losing money"),
    },
    {
        "slug": "telco", "label": "Churn", "title": "Telecom Customer Churn",
        "client": "Subscription business", "data": "IBM Telco Customer Churn · 7,043 customers",
        "summary": "Who is leaving, how much monthly revenue walks out with them, and which services and contract types keep customers.",
        "pages": [
            ("Churn Overview", "Churn rate, churned customers and lost monthly revenue; churn by tenure, contract, payment method, internet service and age group."),
            ("Services & Pricing", "Churn with vs. without each service, churn by monthly bill and by number of protection add-ons."),
            ("Revenue at Risk", "Lost revenue by contract and internet segment, the high-risk customer profile and a segment scorecard."),
        ],
        "findings": [
            "26.5% of customers churned, taking $139K of $456K in monthly recurring revenue (30.5%).",
            "Month-to-month contracts churn at 42.7% vs. 2.8% on two-year contracts.",
            "First-year customers churn at 47.4% vs. 9.5% after four years.",
            "High-risk profile (month-to-month + fiber + electronic check): 18.6% of customers, 60.4% churn, 49% of lost revenue.",
        ],
        "model": "Customers table plus a Services table unpivoted in Power Query (one row per customer and service) with a bidirectional relationship, so churn can be compared for subscribers and non-subscribers of every service on one chart. 38 DAX measures, with groups above the average churn highlighted automatically.",
        "tools": ["Power BI", "Power Query", "DAX", "Unpivot modeling", "Conditional formatting"],
        "video": None,
    },
    {
        "slug": "hr", "label": "HR", "title": "HR Attrition Analytics",
        "client": "People analytics", "data": "IBM HR Analytics Employee Attrition · 1,470 employees",
        "summary": "Why employees leave, which roles and pay bands are most at risk, and what turnover costs the business.",
        "pages": [
            ("Workforce Overview", "Headcount, leavers, attrition rate, age, pay and tenure; attrition by job role, age, department and marital status."),
            ("Attrition Drivers", "Overtime, tenure, job satisfaction and business travel."),
            ("Compensation & Career", "Attrition by pay band, pay of leavers vs. stayers by job level and a retention scorecard by role."),
        ],
        "findings": [
            "Overall attrition is 16.1%; Sales Representatives reach 39.8% (2.5×).",
            "Employees working overtime leave at 30.5%, 2.9× the rate of those who don't.",
            "43% of leavers had 2 years of tenure or less.",
            "Leavers earned 30% less per month than employees who stayed; estimated replacement cost is $6.8M.",
        ],
        "model": "Single employee table shaped in Power Query: constant columns removed, 1–4 survey scores mapped to labels, and age, tenure and income bands with sort orders. 39 DAX measures, including a selection-aware benchmark that drives the conditional colors and dynamic subtitles.",
        "tools": ["Power BI", "Power Query", "DAX", "Banding", "Dynamic subtitles"],
        "video": None,
    },
    {
        "slug": "airline", "label": "Customer Experience", "title": "Airline Passenger Experience",
        "client": "Customer experience survey", "data": "Airline satisfaction survey · 129,880 passengers · 14 touchpoints",
        "summary": "Which parts of the journey drive satisfaction, how it differs by cabin and trip type, and the cost of delays.",
        "pages": [
            ("Experience Overview", "Satisfaction rate, service rating, loyalty, trip mix and punctuality; satisfaction by age, cabin, segment, customer type and distance."),
            ("Service Quality", "Average rating per touchpoint, the top 7 drivers that separate satisfied from dissatisfied passengers, and satisfaction by online boarding score."),
            ("Operations & Punctuality", "Satisfaction by arrival delay and Wi-Fi score, plus a segment scorecard."),
        ],
        "findings": [
            "Overall satisfaction is 43.4%: 69.4% in Business vs. 18.8% in Economy.",
            "Online boarding is the strongest driver: 87% of passengers who score it 5 are satisfied vs. 13% for scores 1–3.",
            "Inflight Wi-Fi is the lowest-rated touchpoint (2.81 / 5).",
            "On-time arrivals: 45.7% satisfied vs. 35.8% when late.",
        ],
        "model": "Passengers table plus a Service Ratings table unpivoted in Power Query (one row per passenger and touchpoint), so every touchpoint is compared on one axis. Train/test files combined; ratings of 0 treated as not applicable. 36 DAX measures.",
        "tools": ["Power BI", "Power Query", "DAX", "Survey analytics", "Driver analysis"],
        "video": None,
    },
    {
        "slug": "restaurant", "label": "Market", "title": "Restaurant Ratings Analysis",
        "client": "Restaurant market", "data": "Zomato restaurant dataset · 9,551 restaurants",
        "summary": "What separates highly rated restaurants from the rest: review volume, price range and the listings nobody rates.",
        "pages": [
            ("Executive Summary", "Restaurants, average rating, share rated 4.0+, votes, cost for two and delivery coverage; rating by country and the distribution of ratings."),
            ("Markets", "Indicators by country, price vs. quality positioning and the top-rated cities."),
            ("Cuisines & Price", "Most offered and best-rated cuisines, the restaurants with most engagement, and services and quality by price level."),
        ],
        "findings": [
            "More than 1 in 5 restaurants (2,148) have no rating at all.",
            "Average rating climbs from 2.97 with fewer than 10 reviews to 4.20 with 1,000+.",
            "Premium restaurants average 3.89 vs. 3.24 for budget ones.",
        ],
        "model": "Restaurant listings cleaned in Power Query with review-volume and price-range bands, analysed in a multi-page Power BI report.",
        "tools": ["Power BI", "Power Query", "DAX", "Market analysis"],
        "video": None,
    },
]

VIDEOS = [
    ("survivorship-bias", "The WWII mistake hiding in your data", "Survivorship bias in customer surveys"),
    ("walmart-poptarts", "What Walmart's data found before hurricanes", "Demand forecasting in retail"),
    ("retail-sales", "Why this store kept losing money", "Walkthrough of the Retail Sales dashboard"),
]

e = html.escape

ICON = {
    "chart": '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
    "model": '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="8.5" y="14" width="7" height="7" rx="1"/><path d="M6.5 10v2h11v-2M12 12v2"/>',
    "clean": '<path d="M3 5h18M6 12h12M10 19h4"/>',
    "brief": '<path d="M9 11h6M9 15h4"/><path d="M6 3h9l4 4v14H6z"/><path d="M15 3v4h4"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
}
def icon(name, size=22):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON[name]}</svg>'

def head(title, desc, prefix=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="https://d8ta-solutions.github.io/assets/img/og.png">
<link rel="icon" href="{prefix}assets/img/logo-mark.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Poppins:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}assets/style.css">
</head>
<body>
"""

def nav(prefix=""):
    home = prefix or "./"
    return f"""<header class="nav">
  <div class="wrap nav-row">
    <a class="brand" href="{home}"><img src="{prefix}assets/img/logo-mark.png" alt=""><span class="bname">d8ta<span>.solutions</span></span></a>
    <nav class="links">
      <a href="{home}#about">About</a>
      <a href="{home}#projects">Projects</a>
      <a href="{home}#stories">Data stories</a>
      <a class="btn btn-sm" href="{home}#contact">Contact</a>
    </nav>
  </div>
</header>
"""

def footer(prefix=""):
    LINKEDIN_LINK = f'<a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a>' if LINKEDIN else ""
    return f"""<section class="contact" id="contact">
  <div class="wrap contact-row">
    <div>
      <h2>Have data you're not using?</h2>
      <p>Tell me about your business and the files you have. I reply within 24 hours with an honest view of what a dashboard could show you.</p>
    </div>
    <div class="contact-actions">
      <a class="btn" href="mailto:{EMAIL}?subject=Dashboard%20project">{icon("mail", 18)} {EMAIL}</a>
      <div class="social">{LINKEDIN_LINK}<a href="{TIKTOK}" target="_blank" rel="noopener">TikTok</a></div>
    </div>
  </div>
</section>
<footer class="foot"><div class="wrap foot-row"><span>© 2026 d8ta.solutions · Lima, Peru · Remote</span><span>Portfolio projects use public datasets.</span></div></footer>
</body>
</html>
"""

def project_card(p):
    return f"""      <article class="card">
        <a class="thumb" href="projects/{p['slug']}.html"><img src="assets/img/dash-{p['slug']}-1.png" alt="{e(p['title'])} dashboard" loading="lazy"></a>
        <div class="card-body">
          <div class="kicker">{e(p['client'])}</div>
          <h3>{e(p['title'])}</h3>
          <p>{e(p['summary'])}</p>
          <a class="more" href="projects/{p['slug']}.html">View details {icon("arrow", 16)}</a>
        </div>
      </article>
"""

def build_index():
    cards = "".join(project_card(p) for p in PROJECTS)
    vids = "".join(f"""      <figure class="vid">
        <video src="assets/video/{s}.mp4" poster="assets/img/poster-{s}.jpg" controls preload="none" playsinline></video>
        <figcaption><b>{e(t)}</b><span>{e(d)}</span></figcaption>
      </figure>
""" for s, t, d in VIDEOS)
    out = head("d8ta.solutions · Power BI dashboards for small businesses",
               "Power BI dashboards for small and mid-sized businesses: sales, customers, churn, HR and operations.")
    out += nav()
    out += f"""<main>
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <p class="tag">Power BI Developer · Remote from Lima, Peru</p>
      <h1>Dashboards that show you where your business is making and losing money.</h1>
      <p class="sub">I turn the spreadsheets and exports you already have into clear Power BI reports for small and mid-sized businesses in the US, Europe and Australia.</p>
      <div class="actions">
        <a class="btn" href="#projects">See projects</a>
        <a class="btn btn-line" href="#contact">Free data review</a>
      </div>
    </div>
    <a class="hero-shot" href="projects/retail.html"><img src="assets/img/dash-retail-1.png" alt="Retail Sales Performance dashboard"></a>
  </div>
</section>

<section class="about" id="about">
  <div class="wrap about-grid">
    <div class="stat"><b>5</b><span>end-to-end Power BI projects<br>150+ DAX measures</span></div>
    <div>
      <h2>About me</h2>
      <p>I'm Kevin, a data analyst working with Power BI, Excel and SQL. I like taking messy, scattered data and turning it into one report a business owner opens every Monday, with numbers that match and a clear story about what to do next.</p>
      <p>Every project below goes from raw files to a multi-page report: data cleaned in Power Query, a proper model, DAX measures and findings written in plain language.</p>
    </div>
  </div>
</section>

<section class="skills">
  <div class="wrap">
    <h2>What I can help with</h2>
    <div class="skill-grid">
      <div class="skill accent">{icon("chart")}<h3>Dashboards &amp; KPIs</h3><p>Sales, profit, customers, churn, HR or operations, built around the questions you ask every week.</p></div>
      <div class="skill">{icon("clean")}<h3>Data preparation</h3><p>Excel, CSV, Google Sheets and exports from your tools, cleaned once in Power Query so the report refreshes itself.</p></div>
      <div class="skill">{icon("model")}<h3>Data modeling &amp; DAX</h3><p>Star schemas, time intelligence and measures you can trust: YoY, margins, rankings, cohorts.</p></div>
      <div class="skill">{icon("brief")}<h3>Insight reports</h3><p>A short write-up with what the data says, where money is leaking and what to focus on next.</p></div>
    </div>
  </div>
</section>

<section class="projects" id="projects">
  <div class="wrap">
    <h2>Selected projects</h2>
    <p class="intro">Built on public datasets, the same way I'd build yours.</p>
    <div class="card-grid">
{cards}      <article class="card card-cta">
        <div class="card-body">
          <div class="kicker">Your business</div>
          <h3>Your dashboard here</h3>
          <p>Have sales, customer or operations data sitting in spreadsheets? Let's see what it can tell you.</p>
          <a class="btn" href="#contact">Start a conversation</a>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="stories" id="stories">
  <div class="wrap">
    <h2>Data stories</h2>
    <p class="intro">One-minute videos on how data changes business decisions.</p>
    <div class="vid-grid">
{vids}    </div>
  </div>
</section>
</main>
"""
    out += footer()
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(out)

def build_project(i, p):
    pre = "../"
    pages = "".join(f"<li><b>{e(t)}</b><span>{e(d)}</span></li>" for t, d in p["pages"])
    findings = "".join(f"<li>{e(f)}</li>" for f in p["findings"])
    tools = "".join(f"<span>{e(t)}</span>" for t in p["tools"])
    nxt = PROJECTS[(i + 1) % len(PROJECTS)]
    shots = [n for n in (1, 2, 3) if os.path.exists(os.path.join(ROOT, "assets", "img", f"dash-{p['slug']}-{n}.png"))]
    gallery = ""
    if len(shots) > 1:
        names = [t for t, _ in p["pages"]] or [f"Page {n}" for n in shots]
        thumbs = "".join(
            f'<button class="thumb-btn{" active" if k == 0 else ""}" data-src="{pre}assets/img/dash-{p["slug"]}-{n}.png">'
            f'<img src="{pre}assets/img/dash-{p["slug"]}-{n}.png" alt="" loading="lazy"><span>{e(names[k] if k < len(names) else f"Page {n}")}</span></button>'
            for k, n in enumerate(shots))
        gallery = f'''<div class="gallery">{thumbs}</div>
    <script>document.querySelectorAll(".thumb-btn").forEach(b=>b.addEventListener("click",()=>{{document.getElementById("main-shot").src=b.dataset.src;document.querySelectorAll(".thumb-btn").forEach(x=>x.classList.toggle("active",x===b));}}));</script>'''
    video = ""
    if p["video"]:
        s, t = p["video"]
        video = f"""<div class="block"><h2>Video walkthrough</h2><figure class="vid vid-single"><video src="{pre}assets/video/{s}.mp4" poster="{pre}assets/img/poster-{s}.jpg" controls preload="none" playsinline></video><figcaption><b>{e(t)}</b></figcaption></figure></div>"""
    out = head(f"{p['title']} · d8ta.solutions", p["summary"], pre)
    out += nav(pre)
    out += f"""<main class="detail">
  <div class="wrap">
    <a class="back" href="../#projects">← All projects</a>
    <div class="detail-head">
      <div class="kicker">{e(p['client'])}</div>
      <h1>{e(p['title'])}</h1>
      <p class="sub">{e(p['summary'])}</p>
      <p class="data-line">{e(p['data'])}</p>
    </div>
    <div class="detail-shot"><img id="main-shot" src="{pre}assets/img/dash-{p['slug']}-1.png" alt="{e(p['title'])} dashboard"></div>
    {gallery}
    <div class="detail-grid">
      <div>
        <div class="block"><h2>Key findings</h2><ul class="findings">{findings}</ul></div>
        {f'<div class="block"><h2>Report pages</h2><ul class="pages">{pages}</ul></div>' if pages else ''}
        {video}
      </div>
      <aside>
        <div class="block side"><h2>How it's built</h2><p>{e(p['model'])}</p><div class="tools">{tools}</div></div>
        <div class="block side"><h2>Want one like this?</h2><p>I can build the same kind of report on your own data.</p><a class="btn" href="#contact">Get in touch</a></div>
      </aside>
    </div>
    <a class="next" href="{nxt['slug']}.html"><span>Next project</span><b>{e(nxt['title'])} →</b></a>
  </div>
</main>
"""
    out += footer(pre)
    os.makedirs(os.path.join(ROOT, "projects"), exist_ok=True)
    open(os.path.join(ROOT, "projects", f"{p['slug']}.html"), "w", encoding="utf-8").write(out)

build_index()
for i, p in enumerate(PROJECTS):
    build_project(i, p)
print("built index.html +", len(PROJECTS), "project pages")
