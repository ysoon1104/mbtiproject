import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="MBTI 발로란트 요원 매칭 🎯",
    page_icon="🔫",
    layout="centered"
)

# MBTI별 발로란트 요원 데이터
mbti_agent = {
    "INTJ": {
        "agent": "바이퍼 (Viper)",
        "role": "통제관 ☠️",
        "emoji": "🐍💚",
        "image": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt9015c8f8e85b2a96/5eb7cdc1b1f2e27c790d9b67/V_AGENTS_587x900_Viper.png",
        "description": "치밀한 전략가 당신! 독을 다루는 화학자 바이퍼처럼 계산된 플레이로 상대를 압박해요.",
        "traits": ["🧪 전략적", "🎯 계산적", "👑 냉철함"],
        "ability": "독성 스크린으로 시야를 차단하고 적을 약화시키는 능력자! ☣️"
    },
    "INTP": {
        "agent": "사이퍼 (Cypher)",
        "role": "감시자 🕵️",
        "emoji": "🎩📹",
        "image": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt5dd1c4448ecbcc4a/5ebc4cb1b1f2e27c790da3b5/V_AGENTS_587x900_Cypher.png",
        "description": "정보 분석의 달인 당신! 모든 것을 파악하는 사이퍼처럼 상대의 움직임을 꿰뚫어봐요.",
        "traits": ["🔍 분석적", "🧩 지능적", "📊 관찰력"],
        "ability": "트립와이어와 카메라로 적의 모든 움직임을 감시하는 정보 마스터! 👁️"
    },
    "ENTJ": {
        "agent": "브림스톤 (Brimstone)",
        "role": "통제관 💼",
        "emoji": "🚬💥",
        "image": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt25f4dac9fcfd2a91/5ebc4cf1b1f2e27c790da3bd/V_AGENTS_587x900_Brimstone.png",
        "description": "타고난 사령관 당신! 베테랑 지휘관 브림스톤처럼 팀을 승리로 이끄는 카리스마가 있어요.",
        "traits": ["👔 리더십", "🎖️ 카리스마", "💪 결단력"],
        "ability": "정확한 스모크와 강력한 궤도 폭격으로 전장을 지배하는 사령관! 🚀"
    },
    "ENTP": {
        "agent": "레이즈 (Raze)",
        "role": "타격대 💣",
        "emoji": "🎨💥",
        "image": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt4afe73f765b9ad42/5ebc4cd0b1f2e27c790da3b9/V_AGENTS_587x900_Raze.png",
        "description": "창의적인 폭발 그 자체! 자유로운 영혼의 레이즈처럼 기발한 플레이로 상대를 놀라게 해요.",
        "traits": ["💥 창의적", "🎉 에너지틱", "🎨 자유로움"],
        "ability": "폭탄과 로켓 런처로 화려하게 적을 날려버리는 폭발 아티스트! 🎆"
    },
    "INFJ": {
        "agent": "세이지 (Sage)",
        "role": "전령 🌿",
        "emoji": "❄️💚",
        "image": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt8163d5ce5ec07fb2/5ebc4d11b1f2e27c790da3c1/V_AGENTS_587x900_Sage.png",
        "description": "지혜로운 치유자 당신! 팀의 정신적 지주 세이지처럼 따뜻한 마음으로 동료를 보살펴요.",
        "traits": ["💚 치유력", "🧘 평화로움", "✨ 통찰력"],
        "ability": "회복과 부활로 팀을 살리고 얼음 벽으로 보호하는 수호자! 🛡️"
    },
    "INFP": {
        "agent": "요루 (Yoru)",
        "role": "타격대 🌀",
        "emoji": "👤🌌",
        "image": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt5538f29c0eccae3c/5fefe43e133eb40912b03c8a/V_AGENTS_587x900_Yoru.png",
        "description": "신비로운 잠입자 당신! 차원을 넘나드는 요루처럼 자신만의 세계를 가진 몽환적 매력의 소유자!",
        "traits": ["🌙 신비로움", "🎭 개성적", "🌀 자유영혼"],
        "ability": "차원 이동과 변장으로 적을 농락하는 환상의 닌자! 🥷"
    },
    "ENFJ": {
        "agent": "스카이 (Skye)",
        "role": "전령 🦅",
        "emoji": "🌿🦊",
        "image": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt94c1535adfbc05ee/5f6ce8b89cce7a3ba12dde07/V_AGENTS_587x900_Skye.png",
        "description": "따뜻한 자연주의자 당신! 동물들과 교감하는 스카이처럼 팀원들을 이끌고 치유하는 리더예요.",
        "traits": ["🌟 카리스마", "💖 배려심", "🌱 협력적"],
        "ability": "동물 정령으로 적을 정찰하고 팀을 회복시키는 자연의 가이드! 🐺"
    },
    "ENFP": {
        "agent": "네온 (Neon)",
        "role": "타격대 ⚡",
        "emoji": "⚡💙",
        "image": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt812d29acedc056b9/61ea2231cee0c10e7c00fa31/V_AGENTS_587x900_Neon.png",
        "description": "에너지 폭발 그 자체! 빛처럼 빠른 네온처럼 어디서나 빛나는 활기 넘치는 매력의 소유자!",
        "traits": ["⚡ 활발함", "✨ 긍정적", "🎉 사교적"],
        "ability": "초고속 질주와 전기 공격으로 전장을 누비는 스피드스터! 🏃‍♀️"
    },
    "ISTJ": {
        "agent": "킬조이 (Killjoy)",
        "role": "감시자 🔧",
        "emoji": "🤖💛",
        "image": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt6da64c976cb5cd6e/5f23d486f4c4e577ad292df8/V_AGENTS_587x900_Killjoy.png",
        "description": "체계적인 엔지니어 당신! 정교한 장치를 다루는 킬조이처럼 완벽한 계획과 준비로 승리를 만들어요.",
        "traits": ["⚙️ 체계적", "📋 책임감", "🎯 정확함"],
        "ability": "터렛과 알람봇으로 거점을 완벽하게 방어하는 천재 엔지니어! 🛠️"
    },
    "ISFJ": {
        "agent": "오멘 (Omen)",
        "role": "통제관 🌑",
        "emoji": "👻💜",
        "image": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blta23a2e0c5fd363f8/5ebc4d22b1f2e27c790da3c5/V_AGENTS_587x900_Omen.png",
        "description": "조용한 수호자 당신! 그림자 속에서 팀을 지키는 오멘처럼 묵묵히 자신의 역할을 다하는 헌신적인 타입!",
        "traits": ["🌙 신중함", "🛡️ 헌신적", "🤫 차분함"],
        "ability": "그림자로 순간이동하며 시야를 차단하는 미스터리한 존재! 👁️‍🗨️"
    },
    "ESTJ": {
        "agent": "소바 (Sova)",
        "role": "전령 🏹",
        "emoji": "🏹❄️",
        "image": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt84e4c30c4a48abaa/5ebc4d3eb1f2e27c790da3c9/V_AGENTS_587x900_Sova.png",
        "description": "정확한 지휘관 당신! 베테랑 사냥꾼 소바처럼 정보를 모으고 팀을 효율적으로 이끄는 리더!",
        "traits": ["🎯 정확함", "📊 분석적", "👔 리더십"],
        "ability": "정찰 화살과 충격 화살로 적의 위치를 파악하고 처치하는 마스터 헌터! 🎯"
    },
    "ESFJ": {
        "agent": "피닉스 (Phoenix)",
        "role": "타격대 🔥",
        "emoji": "🔥👑",
        "image": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blta55135b7c2422e23/5ebc4d52b1f2e27c790da3cd/V_AGENTS_587x900_Phoenix.png",
        "description": "밝은 카리스마의 소유자! 화려한 피닉스처럼 모두의 시선을 사로잡고 분위기를 띄우는 인기쟁이!",
        "traits": ["🔥 열정적", "💝 사교적", "🌟 인기쟁이"],
        "ability": "불꽃으로 자신을 치유하고 부활하는 화려한 영국 신사! 🇬🇧"
    },
    "ISTP": {
        "agent": "제트 (Jett)",
        "role": "타격대 💨",
        "emoji": "🌬️🗡️",
        "image": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt2cb91204c8ef64e1/5ebc4d627c5f1568a06d551d/V_AGENTS_587x900_Jett.png",
        "description": "쿨한 실력자 당신! 바람처럼 자유로운 제트처럼 혼자서도 멋지게 활약하는 독립적인 에이스!",
        "traits": ["💨 민첩함", "🧊 쿨함", "⚔️ 독립적"],
        "ability": "바람을 타고 날아다니며 정확한 칼날을 던지는 한국 출신 에이스! 🇰🇷"
    },
    "ISFP": {
        "agent": "하버 (Harbor)",
        "role": "통제관 🌊",
        "emoji": "🌊💙",
        "image": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt812bdf7c8d3acd57/6363b242d201d92670b50e87/V_AGENTS_587x900_Harbor.png",
        "description": "예술적 감성의 소유자! 물을 다루는 하버처럼 유연하고 아름다운 플레이로 매료시키는 타입!",
        "traits": ["🎨 예술적", "🌊 유연함", "💫 감성적"],
        "ability": "물의 장벽과 해일로 우아하게 전장을 지배하는 물의 마술사! 🌀"
    },
    "ESTP": {
        "agent": "레이나 (Reyna)",
        "role": "타격대 👁️",
        "emoji": "💜🦇",
        "image": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltf24e873c8c6ce10c/5f00d3fed5cc1357205aae64/V_AGENTS_587x900_Reyna.png",
        "description": "공격적인 모험가 당신! 적을 사냥하는 레이나처럼 강렬하고 도전적인 플레이를 즐기는 파이터!",
        "traits": ["⚔️ 공격적", "🔥 도전적", "💪 자신감"],
        "ability": "적을 처치할수록 강해지는 흡혈귀 같은 멕시코 여전사! 🩸"
    },
    "ESFP": {
        "agent": "게코 (Gekko)",
        "role": "전령 🦎",
        "emoji": "🦎💚",
        "image": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt3623a37cdd9762a1/63dc37c69e8cd512573b8a01/V_AGENTS_587x900_Gekko.png",
        "description": "친구가 많은 인기쟁이! 귀여운 생명체들과 함께하는 게코처럼 모두에게 사랑받는 밝은 매력의 소유자!",
        "traits": ["🎉 활발함", "🤗 친화력", "😄 낙천적"],
        "ability": "귀여운 친구들과 함께 적을 정찰하고 제압하는 LA 출신 매력쟁이! 🌴"
    }
}

# CSS 스타일
st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 3rem;
        background: linear-gradient(90deg, #ff4655, #0f1923, #ff4655);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        padding: 20px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .agent-card {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #ff4655 100%);
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(255, 70, 85, 0.3);
        margin: 20px 0;
        color: white;
    }
    .agent-card h1, .agent-card h2 {
        color: white;
    }
    .role-badge {
        background: linear-gradient(90deg, #ff4655, #ff6b7a);
        color: white;
        border-radius: 15px;
        padding: 10px 20px;
        display: inline-block;
        font-weight: bold;
        margin: 10px 0;
        box-shadow: 0 4px 10px rgba(255, 70, 85, 0.4);
    }
    .trait-badge {
        background: white;
        border: 2px solid #ff4655;
        color: #ff4655;
        border-radius: 20px;
        padding: 8px 16px;
        margin: 5px;
        display: inline-block;
        font-weight: bold;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .stSelectbox label {
        font-size: 1.2rem;
        font-weight: bold;
    }
    .ability-box {
        background: linear-gradient(135deg, #0f1923 0%, #1a1a2e 100%);
        color: #ff4655;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #ff4655;
        margin: 15px 0;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# 메인 타이틀
st.markdown('<h1 class="main-title">🎯 MBTI 발로란트 요원 매칭 🔫</h1>', unsafe_allow_html=True)
st.markdown("### ✨ 당신의 MBTI에 어울리는 발로란트 요원을 찾아보세요! 💥")

st.markdown("---")

# 사이드바
with st.sidebar:
    st.markdown("## 🎮 사용 방법")
    st.info("1️⃣ 당신의 MBTI를 선택하세요\n\n2️⃣ '요원 찾기' 버튼을 눌러주세요\n\n3️⃣ 당신의 운명의 요원을 만나보세요!")
    
    st.markdown("## 🎯 발로란트 역할군")
    st.markdown("""
    - 💥 **타격대 (Duelist)**: 공격형
    - 🛡️ **감시자 (Sentinel)**: 수비형
    - ☠️ **통제관 (Controller)**: 시야 차단
    - 🦅 **전령 (Initiator)**: 정보 수집
    """)
    
    st.markdown("---")
    st.caption("Made with 💖 by 당곡고")

# MBTI 선택
col1, col2 = st.columns([2, 1])
with col1:
    mbti_list = ["선택해주세요"] + list(mbti_agent.keys())
    selected_mbti = st.selectbox(
        "🔮 당신의 MBTI는 무엇인가요?",
        mbti_list
    )

with col2:
    st.write("")
    st.write("")
    search_button = st.button("🎯 요원 찾기!", use_container_width=True)

# 결과 표시
if selected_mbti != "선택해주세요" and search_button:
    agent_info = mbti_agent[selected_mbti]
    
    st.balloons()
    
    st.markdown(f"""
    <div class="agent-card">
        <h2>🎉 {selected_mbti}의 운명의 요원은... 🎉</h2>
        <h1 style="font-size: 3rem;">{agent_info['emoji']}</h1>
        <h1 style="color: #ff4655;">{agent_info['agent']}</h1>
        <div class="role-badge">{agent_info['role']}</div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        try:
            st.image(agent_info['image'], use_container_width=True)
        except:
            st.info("🖼️ 이미지를 불러올 수 없어요!")
    
    st.markdown("### 💌 매칭 설명")
    st.success(f"✨ {agent_info['description']}")
    
    st.markdown("### ⚡ 시그니처 능력")
    st.markdown(f'<div class="ability-box">🎯 {agent_info["ability"]}</div>', unsafe_allow_html=True)
    
    st.markdown("### 🌟 당신의 특징")
    traits_html = ""
    for trait in agent_info['traits']:
        traits_html += f'<span class="trait-badge">{trait}</span>'
    st.markdown(f'<div style="text-align: center;">{traits_html}</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 재미있는 메시지
    fun_messages = [
        "🎊 정말 잘 어울리는 한 쌍이에요! 한 판 가시죠?",
        "💫 운명의 요원을 찾았네요! 랭크 올리러 가요!",
        "🔥 이 요원과 함께 에이스를 노려보세요!",
        "✨ 당신만의 특별한 파트너 발견!",
        "🏆 이번 시즌은 레디언트 가즈아!",
        "💥 다음 매치에서 MVP 가능성 200%!"
    ]
    st.markdown(f"### {random.choice(fun_messages)}")
    
    # 추천 플
