import streamlit as st
import time
import random
import plotly.graph_objects as go


# =================================================
# PAGE CONFIGURATION
# =================================================

st.set_page_config(
    page_title="Homework 404",
    page_icon="🤖",
    layout="wide"
)


# =================================================
# HIGH-CONTRAST CUSTOM CSS
# =================================================

st.markdown("""
<style>

/* =================================================
   MAIN BACKGROUND
================================================= */

.stApp {
    background: linear-gradient(
        135deg,
        #0f172a 0%,
        #172554 45%,
        #111827 100%
    );
    color: #ffffff;
}


/* =================================================
   GENERAL TEXT
================================================= */

.stApp p,
.stApp span,
.stApp label {
    color: #ffffff !important;
}


/* =================================================
   HEADINGS
================================================= */

h1 {
    color: #ffffff !important;
    font-weight: 800 !important;
}

h2 {
    color: #ffffff !important;
}

h3 {
    color: #f1f5f9 !important;
}


/* =================================================
   CAPTIONS
================================================= */

.stCaption {
    color: #d1d5db !important;
}


/* =================================================
   BUTTONS
================================================= */

.stButton > button {
    width: 100%;
    background: linear-gradient(
        90deg,
        #2563eb,
        #7c3aed
    );
    color: #ffffff !important;
    border: none;
    border-radius: 12px;
    font-size: 17px;
    font-weight: 700;
    padding: 12px;
    transition: 0.3s;
}

.stButton > button:hover {
    background: linear-gradient(
        90deg,
        #1d4ed8,
        #6d28d9
    );
    transform: scale(1.02);
}


/* =================================================
   SELECT BOX
================================================= */

div[data-baseweb="select"] > div {
    background-color: #ffffff !important;
    color: #000000 !important;
    border: 2px solid #facc15 !important;
    border-radius: 10px !important;
}

/* Selected option text */

div[data-baseweb="select"] span {
    color: #000000 !important;
    font-weight: 600 !important;
}


/* =================================================
   USER TEXT INPUT
================================================= */

input {
    background-color: #ffffff !important;
    color: #000000 !important;
    font-weight: 600 !important;
    border: 2px solid #facc15 !important;
    border-radius: 10px !important;
}


/* =================================================
   HOMEWORK QUESTION BOX
================================================= */

textarea {
    background-color: #ffffff !important;
    color: #000000 !important;
    font-weight: 600 !important;
    border: 2px solid #facc15 !important;
    border-radius: 10px !important;
}


/* =================================================
   PLACEHOLDER TEXT
================================================= */

input::placeholder,
textarea::placeholder {
    color: #475569 !important;
    opacity: 1 !important;
}


/* =================================================
   METRIC CARDS
================================================= */

[data-testid="stMetric"] {
    background-color: #1e293b;
    border: 1px solid #475569;
    border-radius: 15px;
    padding: 20px;
}


/* =================================================
   METRIC LABELS - BRIGHT RED
================================================= */

[data-testid="stMetricLabel"] {
    color: #ff4d4d !important;
    font-weight: 800 !important;
}


/* =================================================
   METRIC VALUES - BRIGHT RED
================================================= */

[data-testid="stMetricValue"] {
    color: #ff0000 !important;
    font-weight: 900 !important;
}


/* =================================================
   FILE UPLOADER
================================================= */

[data-testid="stFileUploader"] {
    background-color: #1e293b;
    padding: 15px;
    border-radius: 15px;
    border: 1px solid #facc15;
}


/* =================================================
   ALERTS
================================================= */

[data-testid="stAlert"] {
    border-radius: 12px;
}


/* =================================================
   DIVIDERS
================================================= */

hr {
    border-color: #64748b !important;
}


/* =================================================
   PROGRESS BAR
================================================= */

[data-testid="stProgressBar"] > div > div {
    background-color: #facc15;
}


/* =================================================
   CUSTOM CARD
================================================= */

.custom-card {
    background-color: #1e293b;
    border: 1px solid #475569;
    border-radius: 20px;
    padding: 25px;
    margin-bottom: 20px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.3);
}


/* =================================================
   HERO SECTION
================================================= */

.hero {
    text-align: center;
    padding: 30px;
    border-radius: 20px;
    background: linear-gradient(
        135deg,
        #1e3a8a,
        #581c87
    );
    margin-bottom: 30px;
}

.hero h1 {
    font-size: 55px !important;
    color: #ffffff !important;
}

.hero h3 {
    color: #facc15 !important;
}


/* =================================================
   RESULT TEXT - BRIGHT RED
================================================= */

.result-reading {
    color: #ff0000 !important;
    font-weight: bold;
    font-size: 22px;
}


/* =================================================
   FOOTER
================================================= */

.footer {
    text-align: center;
    padding: 25px;
    color: #ffffff !important;
}

</style>
""", unsafe_allow_html=True)


# =================================================
# SESSION STATE
# =================================================

if "page" not in st.session_state:
    st.session_state.page = 1

if "reason" not in st.session_state:
    st.session_state.reason = ""

if "custom_reason" not in st.session_state:
    st.session_state.custom_reason = ""

if "question" not in st.session_state:
    st.session_state.question = ""

if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None


# =================================================
# PAGE 1
# EXCUSE SELECTION
# =================================================

if st.session_state.page == 1:

    st.markdown("""
    <div class="hero">
        <h1>🤖 HOMEWORK 404</h1>
        <h3>Your Homework Could Not Be Found.</h3>
    </div>
    """, unsafe_allow_html=True)


    st.markdown("""
    <div class="custom-card">

    <h2>😂 Welcome to Homework 404!</h2>

    <p>
    This is the world's most advanced AI platform designed for
    one extremely important purpose:
    </p>

    <h3>Not doing your homework for you. 🤖😂</h3>

    <p>
    But before we refuse to help, we need to investigate something
    very important...
    </p>

    </div>
    """, unsafe_allow_html=True)


    st.header("📚 Step 1: Why didn't you do your homework?")


    reasons = [

        "😴 I was sleepy",
        "📱 I was using my phone",
        "🎮 I was gaming",
        "📺 I was watching a movie",
        "🏃 I forgot",
        "🧠 I had no motivation",
        "😭 I didn't understand it",
        "🐶 My pet distracted me",
        "🌐 Internet wasn't working",
        "✍️ I just didn't feel like it",
        "📝 Other reason"

    ]


    reason = st.selectbox(
        "Choose your excuse carefully 👀",
        reasons
    )


    custom_reason = ""


    if reason == "📝 Other reason":

        custom_reason = st.text_input(
            "Tell us your excuse:",
            placeholder="Enter your completely believable excuse here..."
        )


    st.divider()


    if st.button("➡️ Continue to Homework Investigation"):

        st.session_state.reason = reason
        st.session_state.custom_reason = custom_reason
        st.session_state.page = 2

        st.rerun()


# =================================================
# PAGE 2
# HOMEWORK INVESTIGATION
# =================================================

elif st.session_state.page == 2:


    st.markdown("""
    <div class="hero">

        <h1>🔎 HOMEWORK INVESTIGATION</h1>

        <h3>Let's pretend we're going to solve it.</h3>

    </div>
    """, unsafe_allow_html=True)


    st.header("✏️ Step 2: Enter Your Homework Question")


    question = st.text_area(

        "What homework question needs our extremely advanced AI?",

        placeholder="Example: Explain Ohm's Law.",

        height=180

    )


    st.divider()


    # -------------------------------------------------
    # UPLOAD HOMEWORK
    # -------------------------------------------------

    st.header("📷 Step 3: Upload Your Homework")


    uploaded_file = st.file_uploader(

        "Upload an image of your homework",

        type=["png", "jpg", "jpeg"]

    )


    if uploaded_file is not None:


        st.success(
            "✅ Homework image detected!"
        )


        st.image(

            uploaded_file,

            caption="🤖 Homework successfully located.",

            use_container_width=True

        )


    st.divider()


    # -------------------------------------------------
    # BUTTONS
    # -------------------------------------------------

    col1, col2 = st.columns(2)


    with col1:

        if st.button("⬅️ Back"):

            st.session_state.page = 1

            st.rerun()


    with col2:

        if st.button("🚀 Analyze with Advanced AI"):


            if not question and uploaded_file is None:

                st.warning(
                    "⚠️ Please enter a homework question or upload an image!"
                )


            else:

                st.session_state.question = question

                st.session_state.uploaded_file = uploaded_file

                st.session_state.page = 3

                st.rerun()


# =================================================
# PAGE 3
# AI ANALYSIS
# =================================================

elif st.session_state.page == 3:


    st.markdown("""
    <div class="hero">

        <h1>🤖 AI ANALYSIS CENTER</h1>

        <h3>Running extremely unnecessary calculations...</h3>

    </div>
    """, unsafe_allow_html=True)


    # -------------------------------------------------
    # PROCESSING
    # -------------------------------------------------

    st.subheader(
        "⚙️ Advanced AI Processing Started"
    )


    progress_bar = st.progress(0)

    message_box = st.empty()


    processing_messages = [

        "🔍 Detecting homework...",

        "🧠 Activating advanced AI brain...",

        "📚 Searching millions of books...",

        "⚡ Running unnecessary algorithms...",

        "🤖 Consulting intelligent systems...",

        "📷 Analyzing homework data...",

        "📊 Calculating excuse quality...",

        "🎁 Preparing shocking results..."

    ]


    for i in range(100):


        progress_bar.progress(i + 1)


        if i < 12:

            message_box.info(
                processing_messages[0]
            )


        elif i < 25:

            message_box.info(
                processing_messages[1]
            )


        elif i < 38:

            message_box.info(
                processing_messages[2]
            )


        elif i < 50:

            message_box.info(
                processing_messages[3]
            )


        elif i < 63:

            message_box.info(
                processing_messages[4]
            )


        elif i < 75:

            message_box.info(
                processing_messages[5]
            )


        elif i < 88:

            message_box.info(
                processing_messages[6]
            )


        else:

            message_box.info(
                processing_messages[7]
            )


        time.sleep(0.02)


    message_box.empty()

    progress_bar.empty()


    # -------------------------------------------------
    # RANDOM RESULTS
    # -------------------------------------------------

    excuse_type = random.choice([

        "Professional Procrastinator 😂",

        "Phone Addiction Expert 📱",

        "Gaming Emergency 🎮",

        "Sleep Department Employee 😴",

        "Motivation Missing 🧠",

        "Certified Homework Avoider 🏆"

    ])


    believability = random.randint(
        5,
        70
    )


    laziness = random.randint(
        50,
        100
    )


    effort = random.randint(
        0,
        25
    )


    brain_usage = random.randint(
        10,
        45
    )


    # -------------------------------------------------
    # SURPRISE
    # -------------------------------------------------

    st.balloons()


    st.success(
        "✅ AI ANALYSIS COMPLETE!"
    )


    st.divider()


    st.markdown("""

    <div class="custom-card">

    <h1 style="text-align:center;">
    🎁 SURPRISE!
    </h1>

    <h2 style="text-align:center;">
    😂 We have successfully analyzed your homework.
    </h2>

    <br>

    <h1 style="
        text-align:center;
        color:#ff0000 !important;
    ">

    📚 DO YOUR HOMEWORK YOURSELF! 🧠😂

    </h1>

    <p style="
        text-align:center;
        font-size:20px;
    ">

    Your brain is still the best AI available. 😎

    </p>

    </div>

    """, unsafe_allow_html=True)


    st.divider()


    # -------------------------------------------------
    # EXCUSE ANALYSIS REPORT
    # -------------------------------------------------

    st.header(
        "🤖 Excuse Analysis Report"
    )


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(

            "📊 Believability",

            f"{believability}%"

        )


    with col2:

        st.metric(

            "😴 Laziness Level",

            f"{laziness}%"

        )


    with col3:

        st.metric(

            "💪 Effort Detected",

            f"{effort}%"

        )


    with col4:

        st.metric(

            "🧠 Brain Usage",

            f"{brain_usage}%"

        )


    st.divider()


    # =================================================
    # EXCUSE ANALYSIS CHART
    # =================================================

    st.subheader(
        "📊 Advanced Excuse Analysis Chart"
    )


    categories = [

        "Believability",

        "Laziness",

        "Effort",

        "Brain Usage"

    ]


    values = [

        believability,

        laziness,

        effort,

        brain_usage

    ]


    fig = go.Figure()


    fig.add_trace(

        go.Bar(

            x=categories,

            y=values,


            marker_color=[

                "#ff0000",   # Bright Red

                "#ff3333",   # Light Bright Red

                "#ff6666",   # Light Red

                "#cc0000"    # Deep Bright Red

            ],


            text=[

                f"{believability}%",

                f"{laziness}%",

                f"{effort}%",

                f"{brain_usage}%"

            ],


            textposition="outside",


            # BRIGHT RED READINGS

            textfont=dict(

                color="#ff0000",

                size=18

            )

        )

    )


    fig.update_layout(


        paper_bgcolor="#0f172a",

        plot_bgcolor="#1e293b",


        font=dict(

            color="#ff0000",

            size=15

        ),


        title=dict(

            text="🤖 Official Homework Avoidance Statistics",

            font=dict(

                color="#ff0000",

                size=24

            ),

            x=0.5

        ),


        xaxis=dict(

            title="Analysis Category",


            tickfont=dict(

                color="#ff0000",

                size=14

            ),


            title_font=dict(

                color="#ff0000",

                size=16

            ),


            gridcolor="#475569"

        ),


        yaxis=dict(

            title="Percentage (%)",

            range=[0, 115],


            tickfont=dict(

                color="#ff0000",

                size=14

            ),


            title_font=dict(

                color="#ff0000",

                size=16

            ),


            gridcolor="#475569"

        ),


        margin=dict(

            l=40,

            r=40,

            t=90,

            b=60

        )

    )


    st.plotly_chart(

        fig,

        use_container_width=True

    )


    st.divider()


    # -------------------------------------------------
    # AI VERDICT
    # -------------------------------------------------

    st.header(
        "📝 AI Verdict"
    )


    if st.session_state.custom_reason:


        st.info(

            f"""
🤖 Our advanced AI carefully investigated your excuse:

**"{st.session_state.custom_reason}"**
"""

        )


    else:


        st.info(

            f"""
🤖 Our advanced AI carefully investigated your excuse:

**{st.session_state.reason}**
"""

        )


    st.warning(

        f"""
🏷️ Excuse Classification:

**{excuse_type}**
"""

    )


    st.error(

        """
📚 FINAL RECOMMENDATION

Stop searching for AI shortcuts.

🧠 DO YOUR HOMEWORK YOURSELF! 😂
"""

    )


    st.divider()


    # -------------------------------------------------
    # USELESS AI STATISTICS
    # -------------------------------------------------

    st.header(
        "📊 Extremely Important AI Statistics"
    )


    stat1, stat2, stat3, stat4 = st.columns(4)


    with stat1:

        st.metric(

            "🤖 AI Confidence",

            "100%"

        )


    with stat2:

        st.metric(

            "📚 Homework Solved",

            "0"

        )


    with stat3:

        st.metric(

            "🧠 Brain Required",

            "YES"

        )


    with stat4:

        st.metric(

            "😂 Uselessness",

            "∞"

        )


    st.divider()


    # -------------------------------------------------
    # RESTART
    # -------------------------------------------------

    if st.button(
        "🔄 Try Another Excuse"
    ):


        st.session_state.page = 1

        st.session_state.reason = ""

        st.session_state.custom_reason = ""

        st.session_state.question = ""

        st.session_state.uploaded_file = None


        st.rerun()


# =================================================
# FOOTER
# =================================================

st.markdown("""

<div class="footer">

🤖 <b>Homework 404</b>

<br><br>

The world's most advanced system for not solving your homework. 😂

</div>

""", unsafe_allow_html=True)