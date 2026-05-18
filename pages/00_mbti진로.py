import streamlit as st

st.set_page_config(
    page_title="MBTI 진로 추천 🎯",
    page_icon="✨",
    layout="centered"
)

st.title("✨ MBTI 진로 추천 시스템")
st.write("나의 MBTI에 어울리는 진로를 알아보자! 😎")

# MBTI별 진로 데이터
mbti_data = {
    "INTJ": [
        {
            "job": "🧠 데이터 과학자",
            "major": "인공지능학과, 컴퓨터공학과",
            "personality": "논리적이고 전략적으로 생각하는 사람",
            "salary": "평균 연봉 약 6,500만원"
        },
        {
            "job": "📈 경영 컨설턴트",
            "major": "경영학과, 경제학과",
            "personality": "문제 해결 능력이 뛰어난 사람",
            "salary": "평균 연봉 약 7,000만원"
        }
    ],
    "INTP": [
        {
            "job": "💻 프로그래머",
            "major": "소프트웨어학과, 컴퓨터공학과",
            "personality": "호기심이 많고 분석적인 사람",
            "salary": "평균 연봉 약 5,500만원"
        },
        {
            "job": "🔬 연구원",
            "major": "물리학과, 화학과",
            "personality": "탐구를 좋아하는 사람",
            "salary": "평균 연봉 약 5,800만원"
        }
    ],
    "ENTJ": [
        {
            "job": "🏢 CEO",
            "major": "경영학과",
            "personality": "리더십이 강하고 추진력이 있는 사람",
            "salary": "평균 연봉 약 8,000만원"
        },
        {
            "job": "⚖️ 변호사",
            "major": "법학과",
            "personality": "논리적으로 설득하는 사람",
            "salary": "평균 연봉 약 7,500만원"
        }
    ],
    "ENTP": [
        {
            "job": "🚀 창업가",
            "major": "경영학과",
            "personality": "아이디어가 많고 도전을 좋아하는 사람",
            "salary": "평균 연봉 약 6,000만원"
        },
        {
            "job": "📢 마케터",
            "major": "광고홍보학과",
            "personality": "창의적이고 말하기를 좋아하는 사람",
            "salary": "평균 연봉 약 4,800만원"
        }
    ],
    "INFJ": [
        {
            "job": "🧑‍🏫 상담교사",
            "major": "교육학과, 심리학과",
            "personality": "공감 능력이 뛰어난 사람",
            "salary": "평균 연봉 약 4,900만원"
        },
        {
            "job": "✍️ 작가",
            "major": "국문학과",
            "personality": "상상력이 풍부한 사람",
            "salary": "평균 연봉 약 4,500만원"
        }
    ],
    "INFP": [
        {
            "job": "🎨 일러스트레이터",
            "major": "디자인학과",
            "personality": "감수성이 풍부한 사람",
            "salary": "평균 연봉 약 4,200만원"
        },
        {
            "job": "🎵 음악 프로듀서",
            "major": "실용음악과",
            "personality": "창의력이 뛰어난 사람",
            "salary": "평균 연봉 약 4,800만원"
        }
    ],
    "ENFJ": [
        {
            "job": "🎤 아나운서",
            "major": "미디어커뮤니케이션학과",
            "personality": "사람들과 소통을 잘하는 사람",
            "salary": "평균 연봉 약 5,500만원"
        },
        {
            "job": "👨‍🏫 교사",
            "major": "교육학과",
            "personality": "다른 사람을 돕는 걸 좋아하는 사람",
            "salary": "평균 연봉 약 5,000만원"
        }
    ],
    "ENFP": [
        {
            "job": "🎬 콘텐츠 크리에이터",
            "major": "영상학과",
            "personality": "에너지가 넘치고 창의적인 사람",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "job": "🌍 여행 기획자",
            "major": "관광학과",
            "personality": "새로운 경험을 좋아하는 사람",
            "salary": "평균 연봉 약 4,300만원"
        }
    ],
    "ISTJ": [
        {
            "job": "🏦 회계사",
            "major": "회계학과",
            "personality": "꼼꼼하고 책임감 있는 사람",
            "salary": "평균 연봉 약 6,500만원"
        },
        {
            "job": "👮 경찰관",
            "major": "경찰행정학과",
            "personality": "원칙을 중요하게 생각하는 사람",
            "salary": "평균 연봉 약 5,200만원"
        }
    ],
    "ISFJ": [
        {
            "job": "💉 간호사",
            "major": "간호학과",
            "personality": "배려심이 깊은 사람",
            "salary": "평균 연봉 약 5,000만원"
        },
        {
            "job": "🏫 초등교사",
            "major": "초등교육과",
            "personality": "책임감이 강한 사람",
            "salary": "평균 연봉 약 5,100만원"
        }
    ],
    "ESTJ": [
        {
            "job": "📊 공무원",
            "major": "행정학과",
            "personality": "체계적이고 리더십 있는 사람",
            "salary": "평균 연봉 약 5,300만원"
        },
        {
            "job": "🏭 생산관리자",
            "major": "산업공학과",
            "personality": "관리 능력이 뛰어난 사람",
            "salary": "평균 연봉 약 6,000만원"
        }
    ],
    "ESFJ": [
        {
            "job": "🏨 호텔리어",
            "major": "호텔관광학과",
            "personality": "친절하고 사교적인 사람",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "job": "🍽️ 영양사",
            "major": "식품영양학과",
            "personality": "사람을 챙기는 걸 좋아하는 사람",
            "salary": "평균 연봉 약 4,300만원"
        }
    ],
    "ISTP": [
        {
            "job": "🔧 자동차 엔지니어",
            "major": "기계공학과",
            "personality": "손으로 만드는 걸 좋아하는 사람",
            "salary": "평균 연봉 약 6,200만원"
        },
        {
            "job": "🛠️ 파일럿",
            "major": "항공운항학과",
            "personality": "침착하고 판단력이 좋은 사람",
            "salary": "평균 연봉 약 7,000만원"
        }
    ],
    "ISFP": [
        {
            "job": "📸 사진작가",
            "major": "사진학과",
            "personality": "예술 감각이 뛰어난 사람",
            "salary": "평균 연봉 약 4,000만원"
        },
        {
            "job": "💄 뷰티 디자이너",
            "major": "뷰티미용학과",
            "personality": "섬세하고 감각적인 사람",
            "salary": "평균 연봉 약 4,200만원"
        }
    ],
    "ESTP": [
        {
            "job": "⚽ 스포츠 마케터",
            "major": "스포츠경영학과",
            "personality": "활동적이고 도전적인 사람",
            "salary": "평균 연봉 약 5,000만원"
        },
        {
            "job": "🎙️ 방송 PD",
            "major": "방송영상학과",
            "personality": "빠른 판단력이 있는 사람",
            "salary": "평균 연봉 약 5,800만원"
        }
    ],
    "ESFP": [
        {
            "job": "🎭 배우",
            "major": "연극영화과",
            "personality": "표현력이 풍부한 사람",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "job": "🎤 이벤트 플래너",
            "major": "이벤트학과",
            "personality": "사람들과 어울리는 걸 좋아하는 사람",
            "salary": "평균 연봉 약 4,300만원"
        }
    ]
}

mbti_list = list(mbti_data.keys())

selected_mbti = st.selectbox(
    "🧩 너의 MBTI를 선택해봐!",
    mbti_list
)

st.divider()

st.subheader(f"✨ {selected_mbti} 추천 진로")

for career in mbti_data[selected_mbti]:
    st.markdown(f"""
    ### {career['job']}
    
    📚 **추천 학과**  
    {career['major']}
    
    😄 **잘 어울리는 성격**  
    {career['personality']}
    
    💰 **평균 연봉**  
    {career['salary']}
    
    ---
    """)

st.success("🎉 진로는 참고용이야! 가장 중요한 건 네가 좋아하고 즐길 수 있는 일이야 😊")
