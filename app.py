import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------
# PAGE SETTINGS
# ---------------------------------------------------

st.set_page_config(
    page_title="Social Media Engagement Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

df = pd.read_csv("data/youtube_data.csv")

df["Views"] = pd.to_numeric(df["Views"])
df["Likes"] = pd.to_numeric(df["Likes"])
df["Comments"] = pd.to_numeric(df["Comments"])

df["Engagement Rate (%)"] = (
    (df["Likes"] + df["Comments"]) / df["Views"] * 100
).round(2)

df["Published"] = pd.to_datetime(df["Published"])

df["Day"] = df["Published"].dt.day_name()
df["Hour"] = df["Published"].dt.hour

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.title("📊 Dashboard")

st.sidebar.info(
"""
Project:
Social Media Engagement Dashboard

Platform:
YouTube

Tools Used:
• Python
• Pandas
• Streamlit
• Matplotlib
• YouTube Data API

Developer:
Arya Kamdi
"""
)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.title("📊 Social Media Engagement Dashboard")

st.write(
"""
Analyze YouTube video performance and discover the best posting strategy
using engagement metrics such as views, likes and comments.
"""
)

# ---------------------------------------------------
# KPI CARDS
# ---------------------------------------------------

st.subheader("📈 Overall Statistics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("🎬 Videos", len(df))

col2.metric(
    "👀 Total Views",
    f"{df['Views'].sum():,}"
)

col3.metric(
    "❤️ Total Likes",
    f"{df['Likes'].sum():,}"
)

col4.metric(
    "💬 Comments",
    f"{df['Comments'].sum():,}"
)

# ---------------------------------------------------
# SEARCH
# ---------------------------------------------------

st.divider()

search = st.text_input(
    "🔍 Search Video Title"
)

if search:

    filtered_df = df[
        df["Title"].str.contains(
            search,
            case=False
        )
    ]

else:

    filtered_df = df

# ---------------------------------------------------
# DATASET
# ---------------------------------------------------

st.subheader("📄 Video Dataset")

st.dataframe(
    filtered_df,
    use_container_width=True
)

# ---------------------------------------------------
# DOWNLOAD BUTTON
# ---------------------------------------------------

st.download_button(
    label="📥 Download Dataset",
    data=filtered_df.to_csv(index=False),
    file_name="youtube_data.csv",
    mime="text/csv"
)

# ---------------------------------------------------
# TOP VIDEOS
# ---------------------------------------------------

st.divider()

st.subheader("🏆 Top 10 Videos by Views")

top = df.sort_values(
    "Views",
    ascending=False
).head(10)

fig, ax = plt.subplots(figsize=(12,5))

ax.bar(
    top["Title"],
    top["Views"]
)

plt.xticks(
    rotation=75,
    fontsize=8
)

plt.tight_layout()

st.pyplot(fig)
# ---------------------------------------------------
# PIE CHART
# ---------------------------------------------------

st.divider()

st.subheader("📊 Likes vs Comments")

fig2, ax2 = plt.subplots(figsize=(6,6))

ax2.pie(
    [df["Likes"].sum(), df["Comments"].sum()],
    labels=["Likes", "Comments"],
    autopct="%1.1f%%",
    startangle=90
)

ax2.axis("equal")

st.pyplot(fig2)

# ---------------------------------------------------
# BEST POSTING DAY
# ---------------------------------------------------

st.divider()

st.subheader("📅 Average Engagement by Day")

day_order = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

best_day = (
    df.groupby("Day")["Engagement Rate (%)"]
    .mean()
    .reindex(day_order)
)

st.bar_chart(best_day)

# ---------------------------------------------------
# BEST POSTING HOUR
# ---------------------------------------------------

st.divider()

st.subheader("⏰ Average Engagement by Hour")

best_hour = (
    df.groupby("Hour")["Engagement Rate (%)"]
    .mean()
    .sort_index()
)

st.line_chart(best_hour)

# ---------------------------------------------------
# TOP ENGAGEMENT VIDEOS
# ---------------------------------------------------

st.divider()

st.subheader("🔥 Top 5 Videos by Engagement Rate")

top_engagement = df.sort_values(
    "Engagement Rate (%)",
    ascending=False
).head(5)

st.dataframe(
    top_engagement[
        [
            "Title",
            "Views",
            "Likes",
            "Comments",
            "Engagement Rate (%)"
        ]
    ],
    use_container_width=True
)

# ---------------------------------------------------
# RECOMMENDATIONS
# ---------------------------------------------------

st.divider()

st.subheader("💡 Content Strategy Recommendations")

best_day_name = best_day.idxmax()
best_hour_value = best_hour.idxmax()

st.success(f"✅ Best day to post: {best_day_name}")

st.success(f"⏰ Best posting hour: {best_hour_value}:00")

highest_video = df.sort_values(
    "Views",
    ascending=False
).iloc[0]["Title"]

st.info(
f"""
### Recommendations

• Upload videos on **{best_day_name}**.

• Try posting around **{best_hour_value}:00**.

• Analyze why **'{highest_video}'** performed well and create similar content.

• Encourage viewers to like and comment.

• Upload consistently every week.

• Monitor engagement regularly to improve future performance.
"""
)

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.divider()

st.caption(
    "Developed by Arya Kamdi | Machine Learning Internship Project"
)