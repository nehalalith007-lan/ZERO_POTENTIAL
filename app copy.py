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
    layout="centered",
    initial_sidebar_state="collapsed"
)


# =================================================
# CUSTOM CSS / BACKGROUND DESIGN
# =================================================

st.markdown("""
<style>

/* Main background */

.stApp {
    background:
        radial-gradient(circle at top left, #2b1055, transparent 40%),
        radial-gradient(circle at top right, #0f4c5c, transparent 40%),
        linear-gradient(135deg, #0b1026, #151b3d, #101827);
    color: white;
}


/* Main content */

.main .block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* Headers */

h1 {
    color: #ffffff !important;
    text-align: center;
    font-weight: 800;
}

h2, h3 {
    color: #ffffff !important;
}


/* Caption */

[data-testid="stCaptionContainer"] {
    text-align: center;
    color: #b8c7ff !important;
}


/* Buttons */

.stButton > button {
    width: 100%;
    border-radius: 12px;
    border: none;
    background: linear-gradient(
        90deg,
        #6c63ff,
        #00c6ff
    );
    color: white;
    font-weight: bold;
    padding: 0.7rem;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.02);
    background: linear-gradient(
        90deg,
        #00c6ff,
        #6c63ff
    );
}


/* Input boxes */

.stTextInput input,
.stTextArea textarea,
.stSelectbox div[data-baseweb="select"] {
    border-radius: 10px;
}


/* Metrics */

[data-testid="stMetric"] {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    padding: 15px;
    border-radius: 15px;
}


/* Divider */

hr {
    border-color: rgba(255,255,255,0.2);
}


/* Progress bar */

.stProgress > div > div > div > div {
    background-color: #00c6ff;
}


/* Cards */

.card {
    background: rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 15px;
    border: 1px solid rgba(255,255,255,0.15);
    margin-bottom: 15px;
}


/* Footer */

.footer {
    text-align: center;
    color: #aab4d4;
    padding-top: 20px;
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

if "believability" not in st.session_state:
    st.session_state.believability = 0

if "laziness" not in st.session_state:
    st.session_state.laziness = 0

if "excuse_type" not in st.session_state:
    st.session_state.excuse_type = ""


# =================================================
# HEADER
# =================================================

st.title("🤖 HOMEWORK 404")

st.subheader("The AI That Refuses To Do Your Homework 😂")

st.caption(
    "We analyze your excuses, pretend to use advanced AI, and still tell you to do your homework yourself."
)

st.divider()


# =================================================
# PAGE INDICATOR
# =================================================

page_col1, page_col2, page_col3 = st.columns(3)

with page_col1:

    if st.session_state.page == 1:
        st.markdown("### 🔵 Step 1")
        st.caption("Your Excuse")
    else:
        st.markdown("### ⚪ Step 1")
        st.caption("Your Excuse")


with page_col2:

    if st.session_state.page == 2:
        st.markdown("### 🔵 Step 2")
        st.caption("Homework")
    else:
        st.markdown("### ⚪ Step 2")
        st.caption("Homework")


with page_col3:

    if st.session_state.page == 3:
        st.markdown("### 🔵 Step 3")
        st.caption("AI Analysis")
    else:
        st.markdown("### ⚪ Step 3")
        st.caption("AI Analysis")


st.divider()


# =================================================
# PAGE 1
# EXCUSE SELECTION
# =================================================

if st.session_state.page == 1:

    st.header("😴 Step 1: Why Didn't You Do Your Homework?")

    st.markdown("""
    <div class="card">
    🤖 <b>Our advanced AI system needs to understand your situation.</b><br><br>
    Please select the reason why your homework mysteriously disappeared from your priorities.
    </div>
    """, unsafe_allow_html=True)


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
        "Select your excuse:",
        reasons,
        index=0
    )


    custom_reason = ""


    if reason == "📝 Other reason":

        custom_reason = st.text_input(
            "Tell us your excuse:"
        )


    st.divider()


    st.markdown("### 🤔 AI Preliminary Opinion")

    funny_messages = [

        "🤖 Interesting... Our AI has heard this excuse approximately one billion times.",

        "🧠 Analyzing excuse credibility... please remain suspicious.",

        "📚 Homework Department has been notified.",

        "😂 This excuse has entered our advanced procrastination database."

    ]


    st.info(
        random.choice(funny_messages)
    )


    st.divider()


    if st.button(
        "➡️ Continue to Homework Details",
        width="stretch"
    ):

        st.session_state.reason = reason
        st.session_state.custom_reason = custom_reason

        st.session_state.page = 2

        st.rerun()


# =================================================
# PAGE 2
# HOMEWORK DETAILS
# =================================================

elif st.session_state.page == 2:


    st.header("📚 Step 2: Show Us The Homework")

    st.markdown("""
    <div class="card">
    🤖 Now our extremely powerful AI needs to examine your homework.
    <br><br>
    Don't worry...
    <br>
    We definitely won't solve it for you. 😂
    </div>
    """, unsafe_allow_html=True)


    # ---------------------------------------------
    # HOMEWORK QUESTION
    # ---------------------------------------------

    st.subheader("✏️ Homework Question")


    question = st.text_area(

        "Enter your homework question:",

        value=st.session_state.question,

        placeholder="""
Example:

Explain Ohm's Law.

OR

Solve: 2x + 5 = 15

OR

Describe the process of photosynthesis.
"""

    )


    # ---------------------------------------------
    # UPLOAD IMAGE
    # ---------------------------------------------

    st.subheader("📷 Upload Homework Image")


    uploaded_file = st.file_uploader(

        "Upload an image of your homework:",

        type=["png", "jpg", "jpeg"]

    )


    if uploaded_file is not None:

        st.image(

            uploaded_file,

            caption="📷 Homework successfully detected by the AI 🤖",

            width="stretch"

        )


    st.divider()


    # ---------------------------------------------
    # BUTTONS
    # ---------------------------------------------

    col1, col2 = st.columns(2)


    with col1:

        if st.button(
            "⬅️ Back",
            width="stretch"
        ):

            st.session_state.question = question

            st.session_state.uploaded_file = uploaded_file

            st.session_state.page = 1

            st.rerun()


    with col2:

        if st.button(
            "🤖 Analyze with Advanced AI",
            width="stretch"
        ):


            if not question and uploaded_file is None:

                st.warning(
                    "⚠️ Please enter a homework question or upload an image first!"
                )


            else:

                st.session_state.question = question

                st.session_state.uploaded_file = uploaded_file


                # Generate analysis results

                st.session_state.excuse_type = random.choice([

                    "🏆 Certified Homework Avoider",

                    "📱 Phone Addiction Specialist",

                    "🎮 Gaming Emergency Survivor",

                    "😴 Sleep Department Employee",

                    "🧠 Motivation Missing",

                    "😂 Professional Procrastinator",

                    "📚 Last-Minute Assignment Expert"

                ])


                st.session_state.believability = random.randint(
                    5,
                    70
                )


                st.session_state.laziness = random.randint(
                    50,
                    100
                )


                st.session_state.page = 3


                st.rerun()


# =================================================
# PAGE 3
# AI ANALYSIS
# =================================================

elif st.session_state.page == 3:


    st.header("🤖 Step 3: Advanced AI Analysis")


    st.markdown("""
    <div class="card">
    ⚠️ <b>WARNING:</b> Our extremely advanced AI is now analyzing your excuse.
    <br><br>
    Please do not close this page while absolutely nothing useful happens.
    </div>
    """, unsafe_allow_html=True)


    # ---------------------------------------------
    # FAKE AI PROCESSING
    # ---------------------------------------------

    progress_bar = st.progress(0)

    message_box = st.empty()


    processing_messages = [

        "🔍 Understanding your homework...",

        "🧠 Activating extremely advanced AI brain...",

        "📚 Searching millions of books...",

        "⚡ Processing advanced algorithms...",

        "🤖 Consulting intelligent models...",

        "📷 Analyzing uploaded homework...",

        "📊 Calculating excuse quality...",

        "🕵️ Detecting procrastination levels...",

        "🎁 Preparing completely useless results..."

    ]


    for i in range(100):


        progress_bar.progress(i + 1)


        if i < 12:

            message_box.info(
                processing_messages[0]
            )


        elif i < 24:

            message_box.info(
                processing_messages[1]
            )


        elif i < 36:

            message_box.info(
                processing_messages[2]
            )


        elif i < 48:

            message_box.info(
                processing_messages[3]
            )


        elif i < 60:

            message_box.info(
                processing_messages[4]
            )


        elif i < 72:

            message_box.info(
                processing_messages[5]
            )


        elif i < 84:

            message_box.info(
                processing_messages[6]
            )


        elif i < 93:

            message_box.info(
                processing_messages[7]
            )


        else:

            message_box.info(
                processing_messages[8]
            )


        time.sleep(0.02)


    progress_bar.empty()

    message_box.empty()


    # ---------------------------------------------
    # SUCCESS
    # ---------------------------------------------

    st.balloons()


    st.success(
        "✅ AI ANALYSIS COMPLETE!"
    )


    st.divider()


    # ---------------------------------------------
    # SURPRISE
    # ---------------------------------------------

    st.header("🎁 SURPRISE!")


    st.markdown("""

### 😂 We have successfully analyzed your homework.

After using our extremely advanced artificial intelligence...

# 📚 DO YOUR HOMEWORK YOURSELF! 🧠😂

### Your brain is still the best AI available. 😎

""")


    st.divider()


    # ---------------------------------------------
    # EXCUSE REPORT
    # ---------------------------------------------

    st.header("🤖 Excuse Analysis Report")


    believability = st.session_state.believability

    laziness = st.session_state.laziness

    excuse_type = st.session_state.excuse_type


    # ---------------------------------------------
    # METRICS
    # ---------------------------------------------

    col1, col2, col3 = st.columns(3)


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

            "📚 Homework Solved",

            "0"

        )


    st.divider()


    # ---------------------------------------------
    # AI VERDICT
    # ---------------------------------------------

    st.subheader("📝 AI Verdict")


    if st.session_state.custom_reason:


        st.info(

            f"""
🤖 Our AI carefully analyzed your excuse:

**"{st.session_state.custom_reason}"**

Conclusion: Extremely suspicious. 😂
"""

        )


    else:


        st.info(

            f"""
🤖 Your selected excuse:

**{st.session_state.reason}**

Our AI has stored this excuse in the highly classified
Procrastination Database. 😂
"""

        )


    st.warning(

        f"""
🏷️ Excuse Type:

**{excuse_type}**
"""

    )


    # Funny recommendation based on laziness

    if laziness >= 85:

        recommendation = (
            "🚨 CRITICAL LAZINESS DETECTED! "
            "Please locate your notebook immediately."
        )


    elif laziness >= 70:

        recommendation = (
            "⚠️ High procrastination levels detected. "
            "Homework should begin soon."
        )


    else:

        recommendation = (
            "😎 Your laziness level is surprisingly manageable. "
            "Maybe there is still hope!"
        )


    st.error(
        recommendation
    )


    # =================================================
    # EXCUSE ANALYSIS CHART
    # =================================================

    st.divider()


    st.subheader(
        "📊 Advanced Excuse Analysis"
    )


    chart_data = {

        "Believability": believability,

        "Laziness": laziness,

        "Homework Solved": 0

    }


    # Bright visible chart

    fig = go.Figure()


    fig.add_trace(

        go.Bar(

            x=list(chart_data.keys()),

            y=list(chart_data.values()),


            # BRIGHT COLORS FOR DARK BACKGROUND

            marker=dict(

                color=[

                    "#00E5FF",  # Cyan

                    "#FF4B4B",  # Red

                    "#FFD700"   # Gold

                ],


                line=dict(

                    color="#FFFFFF",

                    width=1

                )

            ),


            text=[

                f"{believability}%",

                f"{laziness}%",

                "0%"

            ],


            textposition="outside",


            textfont=dict(

                color="white",

                size=16

            )

        )

    )


    fig.update_layout(


        title={

            "text": "🤖 AI Excuse Analysis Results",

            "x": 0.5,

            "font": {

                "color": "white",

                "size": 22

            }

        },


        yaxis=dict(

            title="Percentage (%)",

            range=[0, 110],

            color="white",

            gridcolor="#444444",

            zerolinecolor="#888888"

        ),


        xaxis=dict(

            color="white",

            tickfont=dict(

                size=14,

                color="white"

            )

        ),


        plot_bgcolor="#111827",

        paper_bgcolor="#111827",


        font=dict(

            color="white"

        ),


        height=450,


        margin=dict(

            l=40,

            r=40,

            t=80,

            b=50

        )

    )


    st.plotly_chart(

        fig,

        width="stretch"

    )


    st.caption(
        "⚠️ These statistics were generated using absolutely questionable AI technology. 😂"
    )


    # =================================================
    # ADVANCED AI STATISTICS
    # =================================================

    st.divider()


    st.subheader(
        "📊 Advanced AI Statistics"
    )


    stat1, stat2 = st.columns(2)


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


    stat3, stat4 = st.columns(2)


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


    # =================================================
    # FINAL MESSAGE
    # =================================================

    st.divider()


    st.markdown("""

<div class="card">

<h3 style="text-align:center;">
🎓 FINAL AI RECOMMENDATION
</h3>

<p style="text-align:center; font-size:18px;">

You spent several minutes using an advanced AI system
to avoid your homework.

<br><br>

The AI has reached a final conclusion:

<br><br>

<b>📚 PLEASE DO YOUR HOMEWORK 😂</b>

</p>

</div>

""", unsafe_allow_html=True)


    # =================================================
    # BUTTONS
    # =================================================

    st.divider()


    col1, col2 = st.columns(2)


    with col1:

        if st.button(

            "⬅️ Change Homework",

            width="stretch"

        ):

            st.session_state.page = 2

            st.rerun()


    with col2:

        if st.button(

            "🔄 Start Again",

            width="stretch"

        ):


            # Reset everything

            st.session_state.page = 1

            st.session_state.reason = ""

            st.session_state.custom_reason = ""

            st.session_state.question = ""

            st.session_state.uploaded_file = None

            st.session_state.believability = 0

            st.session_state.laziness = 0

            st.session_state.excuse_type = ""


            st.rerun()


# =================================================
# FOOTER
# =================================================

st.divider()


st.markdown("""

<div class="footer">

🤖 <b>Homework 404</b>

<br>

The world's most advanced system for not solving your homework. 😂

<br><br>

© 2026 | Powered by questionable AI technology 🚀

</div>

""", unsafe_allow_html=True)