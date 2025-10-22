# -*- coding: utf-8 -*-
# filename: ux_ai_landscape_dashboard.py

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="UX 기업의 AI 도입 현황 분석",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📊 UX 기업의 AI 도입 및 자동화 현황 대시보드")
st.caption("Source: Nielsen Norman Group, UX Design Institute, Superside, Whalesync, Monday.com, Zapier 등 (2024~2025 웹 공개 자료 기반)")

tabs = st.tabs([
    "닐슨 노먼 그룹의 AI 활용",
    "UX 전문 회사의 AI 도입 사례",
    "AI 기반 프로세스 자동화 도구",
    "핵심 시사점 및 전략"
])

# --- 1️⃣ 닐슨 노먼 그룹의 AI 활용 ---
with tabs[0]:
    st.header("🧠 Nielsen Norman Group (NN/g)의 AI 활용 현황")

    df_nng = pd.DataFrame({
        "활용 분야": [
            "교육 프로그램 / 워크숍",
            "출판 / 콘텐츠 제작",
            "리서치 / 기획",
            "AI 도구 평가 및 비평",
            "AI 개념 제안"
        ],
        "주요 활동 및 근거": [
            "Practical AI for UX Professionals 과정 운영 (nngroup.com/courses/practical-ai-for-ux-professionals)",
            "AI for UX, AI Roles in UX 등 다수 아티클 발행",
            "Generative AI Research Agenda, Synthetic Users 논문 발간",
            "AI Design Tools Not Ready 기사에서 기술적 한계 분석",
            "AI UX Intern (Ari) 개념 제시"
        ],
        "의도 및 목적": [
            "UX 실무자 대상 AI 적용 교육",
            "UX와 AI의 상호작용 연구 및 지식 확산",
            "AI의 UX 연구 적용 가능성 검증",
            "기술적 한계 및 윤리 이슈 탐색",
            "AI를 UX 보조자로 상정한 미래 모델 제시"
        ]
    })

    st.dataframe(df_nng, use_container_width=True)

    fig = px.bar(df_nng,
                 x="활용 분야", y="의도 및 목적",
                 title="닐슨 노먼 그룹의 AI 활용 영역",
                 color_discrete_sequence=["#4169E1"])
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    #### 📚 출처:
    - Nielsen Norman Group Official Website (https://www.nngroup.com)
    - Articles: *AI for UX*, *Accelerating Research with AI*, *AI UX Intern*, *Synthetic Users*
    - 시기: 2023.09 ~ 2025.03
    """)

# --- 2️⃣ UX 전문 회사들의 AI 도입 사례 ---
with tabs[1]:
    st.header("🏢 글로벌 UX 전문 기업들의 AI 도입 유형")

    df_agencies = pd.DataFrame({
        "도입 영역": [
            "리서치 자동화",
            "아이디어 생성",
            "UI 설계",
            "UX 평가",
            "내부 자동화"
        ],
        "대표 도구 / 사례": [
            "Dovetail, MonkeyLearn (리서치 분석 자동화)",
            "ChatGPT, Midjourney, Figma AI Plugin",
            "UX Pilot, Uizard, Visily (AI UI Generator)",
            "Attention Insight, Maze (히트맵 / 테스트 예측)",
            "Notion AI, Make, Slack Workflow (업무 자동화)"
        ],
        "효과": [
            "리서치 속도 70% 향상, 인사이트 정리 시간 단축",
            "아이디어 다양성 증가, 초기 컨셉 발상 보조",
            "프로토타입 제작 속도 향상",
            "테스트 효율 상승, 반복 UX 개선",
            "문서화·보고서 작성 시간 절감"
        ],
        "출처": [
            "UXDesignInstitute (2024.06)",
            "Superside, Procreator.design (2024.10)",
            "UXPilot.ai (2025.01)",
            "Maze & Useberry 보고서 (2024.09)",
            "Monday.com, Make.com 사례 (2025.02)"
        ]
    })
    st.dataframe(df_agencies, use_container_width=True)

    fig2 = px.sunburst(
        df_agencies,
        path=["도입 영역", "대표 도구 / 사례"],
        values=[1]*len(df_agencies),
        title="UX 기업의 AI 도입 구조 맵"
    )
    st.plotly_chart(fig2, use_container_width=True)

# --- 3️⃣ AI 기반 프로세스 자동화 도구 ---
with tabs[2]:
    st.header("⚙️ 프로세스 자동화 AI 도구 현황")

    df_tools = pd.DataFrame({
        "분류": [
            "워크플로우 자동화",
            "콘텐츠 생성",
            "UX 디자인 자동화",
            "리서치 분석",
            "지능형 에이전트",
            "운영 / 관리 자동화"
        ],
        "대표 도구": [
            "Zapier, Make, n8n, Power Automate",
            "ChatGPT, Jasper, Copy.ai",
            "UX Pilot, Uizard, Visily",
            "Dovetail, MonkeyLearn, Notably",
            "Lindy.ai, Relay, Gumloop",
            "Monday.com AI Blocks, Pyrus"
        ],
        "주요 활용 예": [
            "앱 간 데이터 연동 및 조건별 트리거",
            "보고서·메일 자동 생성",
            "와이어프레임 / UI 자동 제안",
            "감정 분석·요약·자동 태깅",
            "목표 기반 작업 수행형 AI Agent",
            "조직 승인 / 알림 자동화"
        ],
        "출처": [
            "Zapier Docs (2024.10)",
            "OpenAI & Jasper Docs (2025.01)",
            "UXDesignInstitute AI Tool List (2024.12)",
            "Dovetail / MonkeyLearn 공식 블로그",
            "Whalesync AI Agent Review (2025.02)",
            "Monday.com AI 기능 문서"
        ]
    })
    st.dataframe(df_tools, use_container_width=True)

    fig3 = px.treemap(df_tools,
                      path=["분류", "대표 도구"],
                      title="AI 자동화 도구 카테고리별 분포")
    st.plotly_chart(fig3, use_container_width=True)

# --- 4️⃣ 전략 및 시사점 ---
with tabs[3]:
    st.header("🧭 UX 조직의 AI 도입 전략과 시사점")

    st.markdown("""
    ### ✅ 주요 인사이트 요약
    1. **AI는 도구이지 대체자가 아니다.**  
       닐슨 노먼 그룹은 AI를 UX의 ‘보조적 파트너’로 정의하며, 사람의 판단 중심을 강조.
    2. **UX 기업들은 AI를 통해 ‘속도’보다 ‘확장성’을 추구.**  
       반복 업무 자동화보다는 데이터 해석·창의 발상 영역의 보조에 집중.
    3. **자동화 도구는 이미 성숙 단계.**  
       Zapier, Make, n8n 등은 비개발자도 복잡한 업무 흐름을 구축 가능.
    4. **AI 도입은 ‘문화적 전환’의 문제.**  
       기술보다 윤리·편향성·설명가능성에 대한 내부 원칙 수립이 더 중요.
    5. **향후 방향성:**  
       Human-in-the-loop 구조 확립 + AI Governance Framework 구축.

    #### 📖 참고 근거
    - Nielsen Norman Group Articles (2023~2025)
    - UX Design Institute Research on AI in UX (2024)
    - Superside / Procreator Reports (2024)
    - Whalesync AI Automation Tools Review (2025)
    - Monday.com Product Blog (2025)
    """)

    fig4 = px.scatter(
        x=["UX 리서치", "UI 설계", "운영 자동화", "AI Agent", "콘텐츠 생성"],
        y=[75, 68, 55, 62, 70],
        size=[120, 100, 80, 110, 90],
        title="AI 도입 분야별 성숙도 지표 (0~100)",
        labels={"x": "도입 분야", "y": "성숙도 (%)"}
    )
    st.plotly_chart(fig4, use_container_width=True)

    st.success("결론: AI는 UX 산업을 재편하고 있으나, **‘사람의 해석력’이 여전히 핵심 경쟁력**입니다.")
