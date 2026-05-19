import streamlit as st
import folium
from streamlit_folium import st_folium

# 페이지 설정
st.set_page_config(
    page_title="서울 관광지 TOP10",
    page_icon="🗺️",
    layout="wide"
)

st.title("🗺️ 외국인들이 좋아하는 서울 관광지 TOP10")
st.markdown("폴리움(Folium)으로 만든 인터랙티브 서울 관광 지도입니다.")

# 서울 지도 생성
m = folium.Map(
    location=[37.5665, 126.9780],
    zoom_start=11,
    tiles="CartoDB positron"
)

# 관광지 데이터
tourist_spots = [
    {
        "name": "경복궁",
        "location": [37.5796, 126.9770],
        "description": "조선 왕조의 대표 궁궐 🏯"
    },
    {
        "name": "N서울타워",
        "location": [37.5512, 126.9882],
        "description": "서울 야경 명소 🌃"
    },
    {
        "name": "명동",
        "location": [37.5637, 126.9827],
        "description": "쇼핑과 길거리 음식 🛍️"
    },
    {
        "name": "북촌한옥마을",
        "location": [37.5826, 126.9830],
        "description": "전통 한옥 거리 🏡"
    },
    {
        "name": "홍대거리",
        "location": [37.5563, 126.9236],
        "description": "젊음과 예술의 거리 🎨"
    },
    {
        "name": "동대문디자인플라자(DDP)",
        "location": [37.5665, 127.0092],
        "description": "미래형 건축 랜드마크 ✨"
    },
    {
        "name": "롯데월드타워",
        "location": [37.5131, 127.1025],
        "description": "서울 초고층 전망대 🌆"
    },
    {
        "name": "인사동",
        "location": [37.5740, 126.9850],
        "description": "한국 전통 문화 거리 🍵"
    },
    {
        "name": "청계천",
        "location": [37.5692, 126.9784],
        "description": "도심 속 힐링 산책로 🌊"
    },
    {
        "name": "코엑스 별마당도서관",
        "location": [37.5102, 127.0590],
        "description": "SNS 인기 실내 명소 📚"
    }
]

# 마커 추가
for spot in tourist_spots:
    folium.Marker(
        location=spot["location"],
        popup=f"""
        <b>{spot['name']}</b><br>
        {spot['description']}
        """,
        tooltip=spot["name"],
        icon=folium.Icon(
            color="red",
            icon="star"
        )
    ).add_to(m)

# 지도 출력
st_folium(m, width=1400, height=700)

# 관광지 리스트 출력
st.subheader("📍 관광지 목록")

for idx, spot in enumerate(tourist_spots, start=1):
    st.markdown(
        f"""
        **{idx}. {spot['name']}**
        - {spot['description']}
        """
    )

st.caption("Made with Streamlit + Folium")
