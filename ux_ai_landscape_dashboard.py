# filename: ux_ai_landscape_dashboard.py
# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="UX 기업의 AI 도입 현황 분석",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📊 UX 기업의 AI 도입 및 자동화 현황 대시보드")
st.caption("Source: Nielsen Norman Group, UX Design Institute, Superside, Whalesync, Monday.com, Zapier 등")

# 탭 구성
tabs = st.tabs([
    "닐슨 노먼 그룹의 AI 활용",
    "UX 전문 회사의 AI 도입 사례",
    "AI 기반 프로세스 자동화 도구",
    "전략 및 시사점"
])

# --- 1️⃣ 닐슨 노먼 그룹의 AI 활용 탭 ---
with tabs[0]:
    st.header("🧠 Nielsen Norman Group (NN/g)의 AI 활용 현황")

    data_nng = pd.DataFrame({
        "활용 영역": [
            "교육 프로그램 / 워크숍",
            "출판 / 콘텐츠 제작",
            "UX 리서치 / 기획",
            "도구 평가 및 비평",
            "AI 개념 모델 제시"
        ],
        "주요 활동": [
            "Practical AI for UX Professionals 교육 과정 운영",
            "AI 관련 아티클 다수 발행 (AI-UX, AI-Research 등)",
            "Generative AI 연구 어젠다 제시",
            "AI UX 도구의 한계와 위험성 분석",
            "‘AI UX Intern (Ari)’ 개념 제안"
        ],
        "활용 목적": [
            "AI를 UX 실무에 통합",
            "AI와 UX의 관계를 교육",
            "AI의 UX 연구 적용 가능성 탐색",
            "기술의 한계 및 윤리성 검토",
            "AI 보조자의 UX 역할 모델 제안"
        ]
    })

    st.dataframe(data_nng, use_container_width=True)

    # 시각화
    fig1 = px.bar(data_nng,
                  x="활용 영역", y=["활용 목적"],
                  title="닐슨 노먼 그룹의 AI 활용 분야",
                  color_discrete_sequence=["#6A5ACD"])
    st.plotly_chart(fig1, use_container_width=True)

# --- 2️⃣ UX 전문 회사의 AI 도입 사례 ---
with tabs[1]:
    st.header("🏢 UX 전문 회사들의 AI 도입 유형 및 사례")

    data_ux_ai = pd.DataFrame({
        "도입 영역": [
            "리서치 / 사용자 조사",
            "아이디어 발상 / 컨셉 생성",
            "UI / 화면 설계",
            "UX 평가 / 사용성 분석",
            "클라이언트 서비스 설계",
            "내부 운영 자동화"
        ],
        "대표 도구 / 사례": [
            "Dovetail, Notably, MonkeyLearn",
            "ChatGPT, Midjourney, Figma AI Plugin",
            "UX Pilot, Uizard, Visily",
            "Attention Insight, Maze, Hotjar AI",
            "AI 기반 챗봇 UX, 추천 시스템 설계",
            "Notion AI, Slack Workflow, Make"
        ],
        "효과": [
            "리서치 시간 단축, 텍스트 요약 자동화",
            "발산적 사고 지원, 아이디어 다양성 강화",
            "프로토타입 제작 속도 향상",
            "사용자 인사이트 도출 속도 향상",
            "클라이언트 제품의 UX 경쟁력 강화",
            "운영 효율성 및 반복 업무 자동화"
        ]
    })
    st.dataframe(data_ux_ai, use_container_width=True)

    fig2 = px.sunburst(
        data_ux_ai,
        path=["도입 영역", "대표 도구 / 사례"],
        values=[1]*len(data_ux_ai),
        title="UX 기업들의 AI 도입 구조 맵"
    )
    st.plotly_chart(fig2, use_container_width=True)

# --- 3️⃣ 프로세스 자동화용 AI 도구 ---
with tabs[2]:
    st.header("⚙️ AI 기반 프로세스 자동화 도구")

    data_auto = pd.DataFrame({
        "분류": [
            "워크플로우 자동화",
            "문서 / 콘텐츠 생성",
            "디자인 자동화",
            "리서치 분석 자동화",
            "지능형 에이전트",
            "경영 / 운영 자동화"
        ],
        "대표 도구": [
            "Zapier, Make, n8n, Power Automate",
            "ChatGPT, Jasper, Copy.ai",
            "UX Pilot, Uizard, Visily",
            "Dovetail, MonkeyLearn, Notably",
            "Lindy.ai, Relay, Gumloop",
            "Monday.com AI Blocks, Pyrus"
        ],
        "기대 효과": [
            "앱 간 데이터 자동 연결 및 조건 실행",
            "보고서, 이메일, 번역 등 자동 생성",
            "UI/UX 설계 속도 향상",
            "리서치 데이터 요약 및 감정 분석",
            "복합 판단형 자동 에이전트 실행",
            "조직 내 승인 및 알림 자동화"
        ]
    })
    st.dataframe(data_auto, use_container_width=True)

    fig3 = px.treemap(
        data_auto,
        path=["분류", "대표 도구"],
        title="AI 자동화 도구 카테고리별 분포"
    )
    st.plotly_chart(fig3, use_container_width=True)

# --- 4️⃣ 전략 및 시사점 ---
with tabs[3]:
    st.header("🧭 UX 기업의 AI 도입 전략 및 시사점")

    st.markdown("""
    ### ✅ 주요 전략
    1. **점진적 도입 (Pilot → 확장)**  
       리스크가 낮은 영역부터 실험적으로 적용하고 검증 후 확장.
    2. **휴먼-인-더-루프(HITL)**  
       AI의 판단을 인간이 반드시 검토하는 구조로 설계.
    3. **설명 가능성과 투명성 확보**  
       사용자에게 AI 결정 근거를 설명할 수 있도록 구성.
    4. **윤리적 고려와 편향 검증**  
       입력 데이터와 결과물의 편향성을 지속적으로 모니터링.
    5. **내부 역량 강화 및 문화 변화**  
       디자이너, 리서처 모두가 AI 활용 역량을 습득하도록 교육.
    """)

    st.markdown("---")
    st.markdown("**결론:** UX 전문 조직의 AI 도입은 기술의 문제가 아니라, *문화적 전환과 책임 있는 활용*의 문제이다. "
                "AI는 UX 전문가의 자리를 대체하기보다, 경험 설계의 새로운 동반자로 작용하고 있다.")

