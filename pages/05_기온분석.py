import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="날짜별 기온 분석",
    layout="wide"
)

st.title("🌡️ 날짜별 기온 분석")

# -----------------------------
# 데이터 불러오기
# -----------------------------
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("seoul.csv", encoding="cp949")
    except:
        df = pd.read_csv("seoul.csv", encoding="utf-8")

    df["날짜"] = pd.to_datetime(df["날짜"])

    df["연도"] = df["날짜"].dt.year
    df["월"] = df["날짜"].dt.month
    df["일"] = df["날짜"].dt.day

    return df


df = load_data()

# -----------------------------
# 월 선택
# -----------------------------
month = st.selectbox(
    "월 선택",
    sorted(df["월"].unique())
)

# -----------------------------
# 일 선택
# -----------------------------
available_days = sorted(
    df[df["월"] == month]["일"].unique()
)

day = st.selectbox(
    "일 선택",
    available_days
)

# -----------------------------
# 데이터 필터링
# -----------------------------
filtered = df[
    (df["월"] == month) &
    (df["일"] == day)
].copy()

filtered = filtered.sort_values("연도")

filtered = filtered.dropna(
    subset=["최고기온(℃)", "최저기온(℃)"]
)

if filtered.empty:
    st.warning("해당 날짜의 데이터가 없습니다.")
    st.stop()

# -----------------------------
# 그래프
# -----------------------------
fig = go.Figure()

# 최고기온 (분홍색)
fig.add_trace(
    go.Scatter(
        x=filtered["연도"],
        y=filtered["최고기온(℃)"],
        mode="lines+markers",
        name="최고기온",
        line=dict(
            color="hotpink",
            width=4
        ),
        marker=dict(size=7),
        hovertemplate=
        "연도: %{x}<br>" +
        "최고기온: %{y:.1f}℃<extra></extra>"
    )
)

# 최저기온 (연한 파란색)
fig.add_trace(
    go.Scatter(
        x=filtered["연도"],
        y=filtered["최저기온(℃)"],
        mode="lines+markers",
        name="최저기온",
        line=dict(
            color="skyblue",
            width=4
        ),
        marker=dict(size=7),
        hovertemplate=
        "연도: %{x}<br>" +
        "최저기온: %{y:.1f}℃<extra></extra>"
    )
)

fig.update_layout(
    title=f"{month}월 {day}일의 연도별 기온 변화",
    xaxis_title="연도",
    yaxis_title="기온(℃)",
    hovermode="x unified",
    legend_title="범례",
    height=650
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# 통계 정보
# -----------------------------
st.subheader("📊 통계 정보")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "최고기온 평균",
        f"{filtered['최고기온(℃)'].mean():.1f}℃"
    )

with col2:
    st.metric(
        "최고기온 최대",
        f"{filtered['최고기온(℃)'].max():.1f}℃"
    )

with col3:
    st.metric(
        "최저기온 평균",
        f"{filtered['최저기온(℃)'].mean():.1f}℃"
    )

with col4:
    st.metric(
        "최저기온 최소",
        f"{filtered['최저기온(℃)'].min():.1f}℃"
    )

# -----------------------------
# 데이터 보기
# -----------------------------
with st.expander("📋 데이터 보기"):
    st.dataframe(
        filtered[
            ["연도", "최고기온(℃)", "최저기온(℃)"]
        ].reset_index(drop=True),
        use_container_width=True
    )
