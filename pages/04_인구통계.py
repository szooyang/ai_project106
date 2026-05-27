import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os
import re

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="서울시 인구 분석",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# 한글 폰트 설정
# -----------------------------
font_path = "NanumGothic.ttf"

if os.path.exists(font_path):
    font_name = fm.FontProperties(fname=font_path).get_name()
    plt.rc('font', family=font_name)

plt.rcParams['axes.unicode_minus'] = False

# -----------------------------
# 제목
# -----------------------------
st.title("📊 서울시 연령별 인구 분석")

# -----------------------------
# 데이터 불러오기
# -----------------------------
@st.cache_data
def load_data():

    try:
        df = pd.read_csv("population.csv", encoding="utf-8")
    except:
        df = pd.read_csv("population.csv", encoding="cp949")

    return df

df = load_data()

# -----------------------------
# 행정구 컬럼
# -----------------------------
district_col = df.columns[0]

# -----------------------------
# 연령 컬럼 추출
# -----------------------------
age_columns = []

for col in df.columns:

    if "세" in str(col):
        age_columns.append(col)

# -----------------------------
# 행정구 선택
# -----------------------------
districts = df[district_col].unique()

selected_district = st.selectbox(
    "행정구를 선택하세요",
    districts
)

# -----------------------------
# 선택 데이터
# -----------------------------
selected_row = df[df[district_col] == selected_district].iloc[0]

ages = []
population = []

for col in age_columns:

    try:
        col_text = str(col)

        # 마지막 숫자 찾기
        matches = re.findall(r'(\d+)세', col_text)

        if matches:

            age = int(matches[-1])

            value = str(selected_row[col])

            # 쉼표 제거
            value = value.replace(',', '')

            pop = int(float(value))

            ages.append(age)
            population.append(pop)

    except:
        pass

# -----------------------------
# 나이순 정렬
# -----------------------------
sorted_data = sorted(zip(ages, population))

ages = [x[0] for x in sorted_data]
population = [x[1] for x in sorted_data]

# -----------------------------
# 그래프
# -----------------------------
fig, ax = plt.subplots(figsize=(15, 6))

ax.plot(
    ages,
    population,
    color='hotpink',
    linewidth=3
)

# 제목
ax.set_title(
    f"{selected_district} 연령별 인구 분석",
    fontsize=20
)

# 축 이름
ax.set_xlabel("나이", fontsize=14)
ax.set_ylabel("인구수", fontsize=14)

# x축 범위
ax.set_xlim(0, 100)

# x축 눈금
ax.set_xticks(range(0, 101, 10))

# 세로 구분선
ax.grid(
    axis='x',
    linestyle='--',
    alpha=0.6
)

# 전체 격자
ax.grid(
    True,
    linestyle='--',
    alpha=0.3
)

# 그래프 출력
st.pyplot(fig)

# -----------------------------
# 데이터 표
# -----------------------------
st.subheader("📋 연령별 인구 데이터")

chart_df = pd.DataFrame({
    "나이": ages,
    "인구수": population
})

st.dataframe(
    chart_df,
    use_container_width=True
)
