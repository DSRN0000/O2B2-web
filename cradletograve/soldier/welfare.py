import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="노세老世",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 카드 의미 정의
card_meanings = {
    "1월 홍단": "새로운 시작을 알리는 카드입니다. 오늘은 새로운 도전을 시작하기 좋은 날입니다.",
    "1월 초단": "초심을 잃지 말라는 경고입니다. 꾸준함이 필요한 하루입니다.",
    "1월 말단": "끝맺음을 잘하라는 의미입니다. 일을 마무리 짓는 데 집중하세요.",
    "1월 끗": "작은 성공이 예상됩니다. 작은 것에서 기쁨을 찾아보세요.",
    "2월 홍단": "사랑과 우정을 상징합니다. 소중한 사람과 시간을 보내세요.",
    "2월 초단": "행운이 따르는 날입니다. 기회를 놓치지 마세요.",
    "2월 말단": "유혹에 주의하세요. 신중함이 필요한 하루입니다.",
    "2월 끗": "작은 기쁨을 찾는 날입니다. 소소한 행복을 즐기세요.",
    "3월 홍단": "성장이 예상됩니다. 새로운 것을 배우기에 좋은 날입니다.",
    "3월 초단": "긍정적인 변화가 올 것입니다. 변화에 대비하세요.",
    "3월 말단": "과거의 일에 연연하지 마세요. 앞으로 나아가세요.",
    "3월 끗": "작은 성취가 있을 것입니다. 목표를 향해 한 걸음 더 나아가세요.",
    "4월 흑단": "어두운 기운이 감돌 수 있습니다. 주의가 필요한 하루입니다.",
    "4월 초단": "신중하게 행동하세요. 실수를 줄이는 것이 중요합니다.",
    "4월 말단": "결정을 내리기 어려운 날입니다. 조언을 구하세요.",
    "4월 끗": "작은 어려움을 극복해야 합니다. 인내심이 필요합니다.",
    "5월 흑단": "금전운이 좋지 않습니다. 지출을 줄이세요.",
    "5월 초단": "건강에 주의하세요. 무리하지 마세요.",
    "5월 말단": "집중력이 필요합니다. 한 가지 일에 집중하세요.",
    "5월 끗": "작은 장애물이 있을 것입니다. 침착하게 대처하세요.",
    "6월 청단": "행운이 따르는 날입니다. 원하는 것을 얻을 수 있습니다.",
    "6월 초단": "좋은 소식이 올 것입니다. 기쁜 마음으로 받아들이세요.",
    "6월 말단": "친구와의 관계가 좋아집니다. 함께 시간을 보내세요.",
    "6월 끗": "작은 선물이 있을 것입니다. 감사한 마음을 가지세요.",
    "7월 청단": "여행을 가기에 좋은 날입니다. 새로운 곳을 탐험하세요.",
    "7월 초단": "휴식이 필요합니다. 몸과 마음을 쉬게 하세요.",
    "7월 말단": "감정을 잘 다스리세요. 차분한 마음이 필요합니다.",
    "7월 끗": "작은 성취가 있을 것입니다. 목표를 향해 나아가세요.",
    "8월 청단": "좋은 기회가 찾아올 것입니다. 기회를 잡으세요.",
    "8월 초단": "새로운 인연이 생길 것입니다. 사람을 만나는 데 주저하지 마세요.",
    "8월 말단": "결정을 내리기 좋은 날입니다. 용기를 내세요.",
    "8월 끗": "작은 행복을 찾으세요. 소소한 즐거움을 누리세요.",
    "9월 초단": "위험이 도사리고 있습니다. 주의하세요.",
    "9월 말단": "변화를 두려워하지 마세요. 긍정적인 변화가 올 것입니다.",
    "9월 끗": "작은 어려움을 극복할 것입니다. 힘내세요.",
    "9월 특수": "특별한 일이 생길 것입니다. 기대하세요.",
    "10월 청단": "평온한 하루입니다. 마음의 안정을 찾으세요.",
    "10월 초단": "작은 성취가 있을 것입니다. 기쁨을 누리세요.",
    "10월 말단": "도전에 나서기 좋은 날입니다. 새로운 것을 시도해보세요.",
    "10월 끗": "작은 행복을 찾으세요. 소소한 기쁨을 누리세요.",
    "11월 청단": "좋은 소식이 올 것입니다. 기쁜 마음으로 받아들이세요.",
    "11월 초단": "행운이 따르는 날입니다. 원하는 것을 얻을 수 있습니다.",
    "11월 말단": "친구와의 관계가 좋아집니다. 함께 시간을 보내세요.",
    "11월 끗": "작은 선물이 있을 것입니다. 감사한 마음을 가지세요.",
    "12월 청단": "여행을 가기에 좋은 날입니다. 새로운 곳을 탐험하세요.",
    "12월 말단": "휴식이 필요합니다. 몸과 마음을 쉬게 하세요.",
    "12월 끗": "감정을 잘 다스리세요. 차분한 마음이 필요합니다.",
    "12월 특수": "특별한 일이 생길 것입니다. 기대하세요."
}

st.subheader("노세老世 | 오늘의 운세 :crystal_ball:", divider='orange')
st.markdown("")
st.markdown("### :sparkles: 마음에 드는 카드를 선택하세요 :sparkles:")
st.markdown("")
# 카드 이미지 파일명 리스트
card_images = [
    "images/1월 홍단.png", "images/1월 초단.png", "images/1월 말단.png", "images/1월 끗.png",
    "images/2월 홍단.png", "images/2월 초단.png", "images/2월 말단.png", "images/2월 끗.png",
    "images/3월 홍단.png", "images/3월 초단.png", "images/3월 말단.png", "images/3월 끗.png",
    "images/4월 흑단.png", "images/4월 초단.png", "images/4월 말단.png", "images/4월 끗.png",
    "images/5월 흑단.png", "images/5월 초단.png", "images/5월 말단.png", "images/5월 끗.png",
    "images/6월 청단.png", "images/6월 초단.png", "images/6월 말단.png", "images/6월 끗.png",
    "images/7월 청단.png", "images/7월 초단.png", "images/7월 말단.png", "images/7월 끗.png",
    "images/8월 청단.png", "images/8월 초단.png", "images/8월 말단.png", "images/8월 끗.png",
    "images/9월 초단.png", "images/9월 말단.png", "images/9월 끗.png", "images/9월 특수.png",
    "images/10월 청단.png", "images/10월 초단.png", "images/10월 말단.png", "images/10월 끗.png",
    "images/11월 청단.png", "images/11월 초단.png", "images/11월 말단.png", "images/11월 끗.png",
    "images/12월 청단.png", "images/12월 말단.png", "images/12월 끗.png", "images/12월 특수.png"
]

# 이미지 파일과 카드 이름 매핑
card_names = [
    "1월 홍단", "1월 초단", "1월 말단", "1월 끗",
    "2월 홍단", "2월 초단", "2월 말단", "2월 끗",
    "3월 홍단", "3월 초단", "3월 말단", "3월 끗",
    "4월 흑단", "4월 초단", "4월 말단", "4월 끗",
    "5월 흑단", "5월 초단", "5월 말단", "5월 끗",
    "6월 청단", "6월 초단", "6월 말단", "6월 끗",
    "7월 청단", "7월 초단", "7월 말단", "7월 끗",
    "8월 청단", "8월 초단", "8월 말단", "8월 끗",
    "9월 초단", "9월 말단", "9월 끗", "9월 특수",
    "10월 청단", "10월 초단", "10월 말단", "10월 끗",
    "11월 청단", "11월 초단", "11월 말단", "11월 끗",
    "12월 청단", "12월 말단", "12월 끗", "12월 특수"
]


# 모든 카드 이미지 표시
cols = st.columns(5)
for i, img_path in enumerate(card_images):
    with cols[i % 5]:
        img = Image.open(img_path)
        st.image(img, caption=card_names[i], use_column_width=True)

# 이미지 표시 및 선택
selected_card = st.selectbox(
    '당신의 선택은:',
    card_names
)

# 선택된 카드의 의미 출력
st.markdown("---")
st.markdown("# :rainbow[오늘의 운세]")
st.markdown(f"<h4>{card_meanings[selected_card]}</h4>", unsafe_allow_html=True)