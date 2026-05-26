import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="세계 MBTI 분석",
    page_icon="🌍",
    layout="wide"
)

# -----------------------------
# 제목
# -----------------------------
st.title("🌍 국가별 MBTI 비율 분석")
st.markdown("국가를 선택하면 MBTI 유형 비율을 그래프로 보여줍니다.")

# -----------------------------
# 데이터 불러오기
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

# -----------------------------
# 국가 선택
# -----------------------------
countries = sorted(df["Country"].unique())

selected_country = st.selectbox(
    "📌 국가를 선택하세요",
    countries
)

# -----------------------------
# 선택 국가 데이터
# -----------------------------
country_data = df[df["Country"] == selected_country]

# MBTI 컬럼만 추출
mbti_columns = [
    'ISTJ', 'ISFJ', 'INFJ', 'INTJ',
    'ISTP', 'ISFP', 'INFP', 'INTP',
    'ESTP', 'ESFP', 'ENFP', 'ENTP',
    'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ'
]

values = country_data[mbti_columns].iloc[0]

# 데이터프레임 변환
chart_df = pd.DataFrame({
    "MBTI": mbti_columns,
    "비율": values.values
})

# -----------------------------
# 색상 설정
# -----------------------------
# 가장 높은 값 찾기
max_value = chart_df["비율"].max()

# 색상 리스트
colors = []

for v in chart_df["비율"]:
    if v == max_value:
        colors.append("gold")  # 1등 노란색
    else:
        # 하늘색 계열 그라데이션
        alpha = 0.3 + (v / max_value) * 0.7
        colors.append(f"rgba(135,206,250,{alpha})")

# -----------------------------
# 그래프
# -----------------------------
fig = px.bar(
    chart_df,
    x="MBTI",
    y="비율",
    text="비율",
    title=f"{selected_country}의 MBTI 비율"
)

# 막대 색상 적용
fig.update_traces(
    marker_color=colors,
    texttemplate='%{text:.2%}',
    textposition='outside'
)

# 레이아웃 설정
fig.update_layout(
    height=600,
    title_font_size=28,
    xaxis_title="MBTI 유형",
    yaxis_title="비율",
    plot_bgcolor="white",
    paper_bgcolor="white",
    font=dict(
        family="Malgun Gothic",
        size=14
    )
)

# y축 퍼센트 표시
fig.update_yaxes(tickformat=".0%")

# 출력
st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# 최고 유형 표시
# -----------------------------
top_mbti = chart_df.sort_values(
    by="비율",
    ascending=False
).iloc[0]

st.success(
    f"🏆 {selected_country}에서 가장 높은 유형은 "
    f"'{top_mbti['MBTI']}' "
    f"({top_mbti['비율']:.2%}) 입니다!"
)

# -----------------------------
# 데이터 테이블
# -----------------------------
with st.expander("📊 원본 데이터 보기"):
    st.dataframe(chart_df, use_container_width=True)
