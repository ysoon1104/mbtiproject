import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="MBTI 포켓몬 매칭 ✨",
    page_icon="🎮",
    layout="centered"
)

# MBTI별 포켓몬 데이터
mbti_pokemon = {
    "INTJ": {
        "pokemon": "뮤츠",
        "emoji": "🧠💜",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png",
        "description": "전략적이고 카리스마 넘치는 당신! 천재적인 두뇌를 가진 뮤츠처럼 깊이 사고하는 타입이에요.",
        "traits": ["🎯 목표 지향적", "🔮 통찰력 있음", "👑 독립적"]
    },
    "INTP": {
        "pokemon": "polygon (포리곤)",
        "emoji": "🤖💡",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/137.png",
        "description": "논리적이고 호기심 많은 당신! 데이터를 분석하는 포리곤처럼 지적 탐구를 즐겨요.",
        "traits": ["🔬 분석적", "💭 창의적", "🧩 문제 해결사"]
    },
    "ENTJ": {
        "pokemon": "리자몽",
        "emoji": "🔥👑",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png",
        "description": "타고난 리더 당신! 강력하고 위엄있는 리자몽처럼 카리스마 넘쳐요.",
        "traits": ["🏆 리더십", "💪 강인함", "🎯 결단력"]
    },
    "ENTP": {
        "pokemon": "겐가",
        "emoji": "👻😈",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/94.png",
        "description": "기발한 아이디어로 가득한 당신! 장난기 많고 영리한 겐가처럼 재치 있어요.",
        "traits": ["💡 창의적", "🎭 재치있음", "🌪️ 자유로움"]
    },
    "INFJ": {
        "pokemon": "루카리오",
        "emoji": "🐺✨",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/448.png",
        "description": "통찰력 있는 당신! 파동을 읽는 루카리오처럼 사람의 마음을 잘 이해해요.",
        "traits": ["💖 공감능력", "🌟 직관적", "🛡️ 신념있음"]
    },
    "INFP": {
        "pokemon": "이브이",
        "emoji": "🦊💝",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/133.png",
        "description": "순수하고 따뜻한 당신! 무한한 가능성의 이브이처럼 가능성이 가득해요.",
        "traits": ["🌈 이상주의", "🎨 감성적", "🌱 가능성"]
    },
    "ENFJ": {
        "pokemon": "행복",
        "emoji": "💕🌸",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/113.png",
        "description": "따뜻한 카리스마의 당신! 모두를 치유하는 행복(라키)처럼 사랑이 넘쳐요.",
        "traits": ["💗 배려심", "🌟 카리스마", "🤝 협력적"]
    },
    "ENFP": {
        "pokemon": "피카츄",
        "emoji": "⚡💛",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png",
        "description": "에너지 넘치는 당신! 사랑스럽고 활발한 피카츄처럼 모두에게 사랑받아요.",
        "traits": ["⚡ 활발함", "🎉 사교적", "✨ 긍정적"]
    },
    "ISTJ": {
        "pokemon": "거북왕",
        "emoji": "🐢🛡️",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/9.png",
        "description": "신뢰감의 아이콘 당신! 듬직한 거북왕처럼 책임감이 강해요.",
        "traits": ["📋 체계적", "🛡️ 책임감", "💎 신뢰감"]
    },
    "ISFJ": {
        "pokemon": "이상해꽃",
        "emoji": "🌸🌿",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/3.png",
        "description": "다정한 수호자 당신! 모두를 보호하는 이상해꽃처럼 따뜻한 마음을 가졌어요.",
        "traits": ["🌷 헌신적", "🤗 따뜻함", "🛡️ 보호자"]
    },
    "ESTJ": {
        "pokemon": "한카리아스",
        "emoji": "🦈⚔️",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/445.png",
        "description": "강력한 리더 당신! 압도적인 한카리아스처럼 추진력이 대단해요.",
        "traits": ["💼 실용적", "⚔️ 추진력", "📊 조직적"]
    },
    "ESFJ": {
        "pokemon": "푸린",
        "emoji": "🎀🎵",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/39.png",
        "description": "사랑스러운 분위기 메이커! 노래로 모두를 행복하게 하는 푸린 같아요.",
        "traits": ["💝 다정함", "🎵 사교적", "🌟 인기쟁이"]
    },
    "ISTP": {
        "pokemon": "갸라도스",
        "emoji": "🐉💧",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/130.png",
        "description": "쿨한 실력자 당신! 조용하지만 강력한 갸라도스처럼 숨은 실력자예요.",
        "traits": ["🛠️ 실용적", "🧊 쿨함", "💪 독립적"]
    },
    "ISFP": {
        "pokemon": "이브이의 진화형 - 샤미드",
        "emoji": "💙🌊",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/134.png",
        "description": "예술가적 감성의 당신! 우아한 샤미드처럼 섬세한 아름다움을 지녔어요.",
        "traits": ["🎨 예술적", "🌊 평화로움", "💫 감성적"]
    },
    "ESTP": {
        "pokemon": "파이리",
        "emoji": "🔥🦎",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/4.png",
        "description": "모험을 즐기는 당신! 열정 가득한 파이리처럼 도전을 두려워하지 않아요.",
        "traits": ["🎢 모험심", "⚡ 즉흥적", "🔥 열정적"]
    },
    "ESFP": {
        "pokemon": "이상해씨",
        "emoji": "🌱😊",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/1.png",
        "description": "밝고 사랑스러운 당신! 귀엽고 활기찬 이상해씨처럼 분위기를 밝게 만들어요.",
        "traits": ["🎉 활발함", "😄 낙천적", "🌟 매력적"]
    }
}

# CSS 스타일
st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 3rem;
        background: linear-gradient(90deg, #ff6b6b, #feca57, #48dbfb, #ff9ff3);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        padding: 20px;
    }
    .pokemon-card {
        background: linear-gradient(135deg, #fff5f5 0%, #fef3c7 100%);
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin: 20px 0;
    }
    .trait-badge {
        background: white;
        border-radius: 20px;
        padding: 8px 16px;
        margin: 5px;
        display: inline-block;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .stSelectbox label {
        font-size: 1.2rem;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# 메인 타이틀
st.markdown('<h1 class="main-title">✨ MBTI 포켓몬 매칭 ✨</h1>', unsafe_allow_html=True)
st.markdown("### 🎮 당신의 MBTI에 어울리는 포켓몬을 찾아보세요! 🌟")

st.markdown("---")

# 사이드바
with st.sidebar:
    st.markdown("## 🎀 사용 방법")
    st.info("1️⃣ 당신의 MBTI를 선택하세요\n\n2️⃣ '포켓몬 찾기' 버튼을 눌러주세요\n\n3️⃣ 당신과 닮은 포켓몬을 만나보세요!")
    st.markdown("## 💡 MBTI란?")
    st.write("성격 유형을 16가지로 분류하는 검사예요! 🌈")
    st.markdown("---")
    st.caption("Made with 💖 by 당곡고")

# MBTI 선택
col1, col2 = st.columns([2, 1])
with col1:
    mbti_list = ["선택해주세요"] + list(mbti_pokemon.keys())
    selected_mbti = st.selectbox(
        "🔮 당신의 MBTI는 무엇인가요?",
        mbti_list
    )

with col2:
    st.write("")
    st.write("")
    search_button = st.button("🎯 포켓몬 찾기!", use_container_width=True)

# 결과 표시
if selected_mbti != "선택해주세요" and search_button:
    pokemon_info = mbti_pokemon[selected_mbti]
    
    st.balloons()
    
    st.markdown(f"""
    <div class="pokemon-card">
        <h2>🎉 {selected_mbti}의 운명의 포켓몬은... 🎉</h2>
        <h1 style="font-size: 3rem;">{pokemon_info['emoji']}</h1>
        <h2 style="color: #ff6b6b;">{pokemon_info['pokemon']}</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(pokemon_info['image'], use_container_width=True)
    
    st.markdown("### 💌 매칭 설명")
    st.success(f"✨ {pokemon_info['description']}")
    
    st.markdown("### 🌟 당신의 특징")
    traits_html = ""
    for trait in pokemon_info['traits']:
        traits_html += f'<span class="trait-badge">{trait}</span>'
    st.markdown(f'<div style="text-align: center;">{traits_html}</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 재미있는 메시지
    fun_messages = [
        "🎊 정말 잘 어울리는 한 쌍이에요!",
        "💫 운명의 포켓몬을 찾았네요!",
        "🌈 이 포켓몬과 함께 모험을 떠나보세요!",
        "✨ 당신만의 특별한 파트너!",
        "🎁 멋진 매칭이에요!"
    ]
    st.markdown(f"### {random.choice(fun_messages)}")

elif selected_mbti == "선택해주세요" and search_button:
    st.warning("⚠️ MBTI를 먼저 선택해주세요!")

st.markdown("---")
st.markdown("<p style='text-align: center;'>🎮 Gotta Catch 'Em All! 🎮</p>", unsafe_allow_html=True)
