import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ----------------------------------
# 페이지 설정
# ----------------------------------
st.set_page_config(
    page_title="날짜별 기온 분석",
    layout="wide"
)

st.title("🌡️ 날짜별 기온 분석")

# ----------------------------------
# 데이터 불러오기
# ----------------------------------
@st.cache_data
def load_data():

    # CSV 읽기
    try:
        df = pd.read_csv("seoul.csv", encoding="cp949")
    except:
        try:
            df = pd.read_csv("seoul.csv", encoding="utf-8")
        except:
            df = pd.read_csv("seoul.csv", encoding="utf-8-sig")

    # 컬럼명 공백 제거
    df.columns = df.columns.str.strip()

    # 날짜 컬럼 찾기
    if "날짜" in df.columns:
        date_col = "날짜"
    elif "일시" in df.columns:
        date_col = "일시"
    else:
        st.error(f"날짜 컬럼을 찾을 수 없습니다.\n현재 컬럼: {df.columns.tolist()}")
        st.stop()

    # 날짜 변환
    df[date_col] = pd.to_datetime(
        df[date_col],
        errors="coerce"
    )

    # 날짜 변환 실패 행 제거
    df = df.dropna(subset=[date_col])

    # 연도/월/일 생성
    df["연도"] = df[date_col].dt.year
    df["월"] = df[date_col].dt.month
    df["일"] = df[date_col].dt.day

    return df


df = load_data()

# ----------------------------------
# 기온 컬럼 찾기
# ----------------------------------
max_col = None
min_col = None

for col in df.columns:
    if "최고기온" in col:
        max_col = col
    if "최저기온" in col:
        min_col = col

if max_col is None or min_col is None:
    st.error("최고기온 또는 최저기온 컬럼을 찾을 수 없습니다.")
    st.write(df.columns.tolist())
    st.stop()

# ----------------------------------
# 월 선택
# ----------------------------------
month = st.selectbox(
    "월 선택",
    sorted(df["월"].unique())
)

# ----------------------------------
# 일 선택
# ----------------------------------
available_days = sorted(
    df[df["월"] == month]["일"].unique()
)

day = st.selectbox(
    "일 선택",
    available_days
)

# ----------------------------------
# 데이터 필터링
# ----------------------------------
filtered = df[
    (df["월"] == month) &
    (df["일"] == day)
].copy()

filtered = filtered.sort_values("연도")

filtered = filtered.dropna(
    subset=[max_col, min_col]
)

if filtered.empty:
    st.warning("선택한 날짜의 데이터가 없습니다.")
    st.stop()

# ----------------------------------
# 그래프
# ----------------------------------
fig = go.Figure()

# 최고기온 (분홍색)
fig.add_trace(
    go.Scatter(
        x=filtered["연도"],
        y=filtered[max_col],
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
        y=filtered[min_col],
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

# ----------------------------------
# 통계
# ----------------------------------
st.subheader("📊 통계 정보")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "최고기온 평균",
    f"{filtered[max_col].mean():.1f}℃"
)

c2.metric(
    "최고기온 최대",
    f"{filtered[max_col].max():.1f}℃"
)

c3.metric(
    "최저기온 평균",
    f"{filtered[min_col].mean():.1f}℃"
)

c4.metric(
    "최저기온 최소",
    f"{filtered[min_col].min():.1f}℃"
)

# ----------------------------------
# 데이터 보기
# ----------------------------------
with st.expander("📋 데이터 보기"):
    st.dataframe(
        filtered[
            ["연도", max_col, min_col]
        ].reset_index(drop=True),
        use_container_width=True
    )
