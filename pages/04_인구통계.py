import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import platform

# -----------------------------
# 한글 폰트 설정
# -----------------------------
if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')
elif platform.system() == 'Darwin':
    plt.rc('font', family='AppleGothic')
else:
    plt.rc('font', family='NanumGothic')

plt.rcParams['axes.unicode_minus'] = False

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="서울시 인구 분석",
    page_icon="📊",
    layout="wide"
)

st.title("📊 서울시 연령별 인구 분석")

# -----------------------------
# 데이터 불러오기
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("population.csv", encoding="utf-8")
    return df

df = load_data()

# -----------------------------
# 데이터 전처리
# -----------------------------
# 첫 번째 컬럼 이름 확인
district_col = df.columns[0]

# 연령 컬럼 추출
age_columns = df.columns[3:]

# 행정구 선택
districts = df[district_col].unique()

selected_district = st.selectbox(
    "행정구를 선택하세요",
    districts
)

# 선택한 행정구 데이터
selected_row = df[df[district_col] == selected_district].iloc[0]

# 나이 데이터
ages = []
population = []

for col in age_columns:
    try:
        age = ''.join(filter(str.isdigit, col))
        if age != '':
            ages.append(int(age))
            population.append(int(str(selected_row[col]).replace(',', '')))
    except:
        pass

# -----------------------------
# 그래프 그리기
# -----------------------------
fig, ax = plt.subplots(figsize=(14, 6))

ax.plot(
    ages,
    population,
    color='hotpink',
    linewidth=3
)

# 제목 및 라벨
ax.set_title(f"{selected_district} 연령별 인구 분석", fontsize=18)
ax.set_xlabel("나이", fontsize=13)
ax.set_ylabel("인구수", fontsize=13)

# x축 10살 단위 구분선
ax.set_xticks(range(0, 101, 10))

# 격자 표시
ax.grid(True, linestyle='--', alpha=0.5)

# 그래프 출력
st.pyplot(fig)

# -----------------------------
# 데이터 일부 출력
# -----------------------------
st.subheader("📋 선택한 행정구 데이터")

chart_df = pd.DataFrame({
    "나이": ages,
    "인구수": population
})

st.dataframe(chart_df, use_container_width=True)
