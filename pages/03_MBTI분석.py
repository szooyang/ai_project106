import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------------
# 페이지 설정
# -----------------------------------
st.set_page_config(
    page_title="세계 MBTI 분석",
    page_icon="🌍",
    layout="wide"
)

# -----------------------------------
# 제목
# -----------------------------------
st.title("🌍 국가별 MBTI 분석 시스템")
st.markdown("국가별 MBTI 비율과 유형별 상위 국가를 확인해보세요!")

# -----------------------------------
# 데이터 불러오기
# -----------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

# -----------------------------------
# MBTI 컬럼
# -----------------------------------
mbti_columns = [
    'ISTJ', 'ISFJ', 'INFJ', 'INTJ',
    'ISTP', 'ISFP', 'INFP', 'INTP',
    'ESTP', 'ESFP', 'ENFP', 'ENTP',
    'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ'
]

# ===================================
# 1️⃣ 국가별 MBTI 분석
# ===================================
st.header("📊 국가별 MBTI 비율 분석")

countries = sorted(df["Country"].unique())

selected_country = st.selectbox(
    "🌎 국가를 선택하세요",
    countries
)

# 선택 국가 데이터
country_data = df[df["Country"] == selected_country]

# MBTI 데이터 추출
values = country_data[mbti_columns].iloc[0]

chart_df = pd.DataFrame({
    "MBTI": mbti_columns,
    "비율": values.values
})

# -----------------------------------
# 비율 높은 순 정렬
# -----------------------------------
chart_df = chart_df.sort_values(
    by="비율",
    ascending=False
)

# -----------------------------------
# 초록색 그라데이션 색상
# -----------------------------------
max_value = chart_df["비율"].max()

colors = []

for i, v in enumerate(chart_df["비율"]):

    if i == 0:
        # 1등 진한 초록색
        colors.append("rgb(0,128,0)")
    else:
        alpha = 0.25 + (v / max_value) * 0.75
        colors.append(f"rgba(34,139,34,{alpha})")

# -----------------------------------
# 그래프 생성
# -----------------------------------
fig = px.bar(
    chart_df,
    x="MBTI",
    y="비율",
    text="비율",
    title=f"{selected_country}의 MBTI 비율 순위"
)

fig.update_traces(
    marker_color=colors,
    texttemplate='%{text:.2%}',
    textposition='outside'
)

fig.update_layout(
    height=600,
    plot_bgcolor="white",
    paper_bgcolor="white",
    font=dict(
        family="Malgun Gothic",
        size=14
    ),
    title_font_size=28,
    xaxis_title="MBTI 유형",
    yaxis_title="비율"
)

fig.update_yaxes(tickformat=".0%")

st.plotly_chart(fig, use_container_width=True)

# -----------------------------------
# TOP MBTI 표시
# -----------------------------------
top_mbti = chart_df.iloc[0]

st.success(
    f"🏆 {selected_country}에서 가장 높은 MBTI는 "
    f"{top_mbti['MBTI']} "
    f"({top_mbti['비율']:.2%}) 입니다!"
)

# ===================================
# 2️⃣ MBTI별 상위 국가 분석
# ===================================
st.header("🌟 MBTI 유형별 상위 국가 TOP 10")

selected_mbti = st.selectbox(
    "🧠 MBTI 유형을 선택하세요",
    mbti_columns
)

# 선택 MBTI 기준 정렬
top10_df = df[["Country", selected_mbti]].sort_values(
    by=selected_mbti,
    ascending=False
).head(10)

# 컬럼 이름 변경
top10_df.columns = ["국가", "비율"]

# -----------------------------------
# 색상 설정
# -----------------------------------
max_value2 = top10_df["비율"].max()

colors2 = []

for i, v in enumerate(top10_df["비율"]):

    if i == 0:
        colors2.append("rgb(0,128,0)")
    else:
        alpha = 0.25 + (v / max_value2) * 0.75
        colors2.append(f"rgba(50,205,50,{alpha})")

# -----------------------------------
# TOP10 그래프
# -----------------------------------
fig2 = px.bar(
    top10_df,
    x="국가",
    y="비율",
    text="비율",
    title=f"{selected_mbti} 비율이 높은 국가 TOP 10"
)

fig2.update_traces(
    marker_color=colors2,
    texttemplate='%{text:.2%}',
    textposition='outside'
)

fig2.update_layout(
    height=600,
    plot_bgcolor="white",
    paper_bgcolor="white",
    font=dict(
        family="Malgun Gothic",
        size=14
    ),
    title_font_size=28,
    xaxis_title="국가",
    yaxis_title="비율"
)

fig2.update_yaxes(tickformat=".0%")

st.plotly_chart(fig2, use_container_width=True)

# ===================================
# 데이터 보기
# ===================================
with st.expander("📄 원본 데이터 보기"):
    st.dataframe(df, use_container_width=True)
