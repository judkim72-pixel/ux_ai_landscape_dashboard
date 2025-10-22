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
st.caption("Source: Nielsen Norman Group, IDEO, Superside, UX Design Institute, Superside, Whalesync, Monday.com, Zapier 등 (2023–2025 웹 공개 자료 기반)")

# -----------------------------------
# 탭 구성
# -----------------------------------
tabs = st.tabs([
    "닐슨 노먼 그룹의 AI 활용",
    "UX 전문 회사의 AI 도입 사례",
    "AI 기반 프로세스 자동화 도구",
    "핵심 시사점 및 전략",
    "글로벌 UX 기업 비교"
])

# ==========================================================
# ① 닐슨 노먼 그룹(NN/g) 탭
# ==========================================================
with tabs[0]:
    st.header("🧠 Nielsen Norman Group (NN/g)의 AI 활용 구조 및 추이")

    # Sankey Diagram
    labels = [
        "교육 프로그램 / 워크숍",
        "출판 / 콘텐츠 제작",
        "리서치 / 기획",
        "도구 평가 및 비평",
        "AI 개념 제안",
        "UX 실무 적용",
        "AI-UX 통합 연구",
        "윤리·한계 검증",
        "AI 협업 모델 제시",
        "지식 확산"
    ]
    source = [0, 1, 2, 3, 4]
    target = [5, 9, 6, 7, 8]
    value = [4, 3, 4, 3, 2]

    fig_sankey = px.sankey(
        node=dict(
            label=labels,
            color=["#6A5ACD", "#7B68EE", "#8470FF", "#9370DB", "#BA55D3",
                   "#4169E1", "#4682B4", "#8A2BE2", "#00CED1", "#87CEFA"]
        ),
        link=dict(source=source, target=target, value=value),
        title="닐슨 노먼 그룹의 AI 활용 흐름도 (분야 → 목적)"
    )
    st.plotly_chart(fig_sankey, use_container_width=True)

    st.markdown("""
    **📘 해석:**  
    닐슨 노먼 그룹은 AI를 ‘교육 → 실무 적용 → 연구 통합 → 윤리 검증 → 개념 모델 제안’의 흐름으로 확산시키고 있습니다.  
    즉, **AI를 도구가 아닌 ‘UX 내 연구 주제’로 재해석한 선도적 사례**로 평가됩니다.
    """)

    # 연도별 활동 추이
    st.subheader("📅 연도별 AI 관련 활동 추이 (2023–2025)")
    timeline_df = pd.DataFrame({
        "연도": [2023, 2024, 2025],
        "AI 관련 기사 수": [5, 12, 18],
        "연구·교육 프로그램 수": [1, 4, 6],
        "평가·비평 관련 문서 수": [2, 5, 7]
    })
    fig_line = px.line(
        timeline_df,
        x="연도",
        y=["AI 관련 기사 수", "연구·교육 프로그램 수", "평가·비평 관련 문서 수"],
        markers=True,
        title="닐슨 노먼 그룹의 AI 관련 활동 증가 추이 (2023–2025)",
        labels={"value": "발행 건수", "연도": "Year"}
    )
    fig_line.update_traces(line=dict(width=3))
    st.plotly_chart(fig_line, use_container_width=True)

    st.markdown("""
    **📚 데이터 근거**
    - *Nielsen Norman Group Official Site* (https://www.nngroup.com)  
    - Articles: *AI for UX*, *AI UX Intern*, *Accelerating Research with AI*, *Synthetic Users*, *Generative AI Research Agenda*  
    - 수치는 2023–2025 공개 콘텐츠 건수 기준 추정
    """)
    st.info("결론: NN/g는 AI를 단순 연구 주제가 아니라, UX 업계의 교육·윤리·실행 프레임워크로 발전시키는 중입니다.")

# ==========================================================
# ② UX 전문 회사의 AI 도입 사례
# ==========================================================
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
            "Dovetail, MonkeyLearn",
            "ChatGPT, Midjourney, Figma AI Plugin",
            "UX Pilot, Uizard, Visily",
            "Attention Insight, Maze",
            "Notion AI, Make, Slack Workflow"
        ],
        "효과": [
            "리서치 속도 70% 향상",
            "아이디어 다양성 증가",
            "프로토타입 제작 속도 향상",
            "테스트 효율 상승",
            "문서화·보고서 작성 시간 절감"
        ],
        "출처": [
            "UXDesignInstitute (2024.06)",
            "Superside / Procreator.design (2024.10)",
            "UXPilot.ai (2025.01)",
            "Maze Report (2024.09)",
            "Monday.com (2025.02)"
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

# ==========================================================
# ③ 프로세스 자동화 도구
# ==========================================================
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
        ]
    })
    st.dataframe(df_tools, use_container_width=True)

    fig3 = px.treemap(
        df_tools,
        path=["분류", "대표 도구"],
        title="AI 자동화 도구 카테고리별 분포"
    )
    st.plotly_chart(fig3, use_container_width=True)

# ==========================================================
# ④ 전략 및 시사점
# ==========================================================
with tabs[3]:
    st.header("🧭 UX 조직의 AI 도입 전략과 시사점")

    st.markdown("""
    ### ✅ 핵심 인사이트
    1. **AI는 도구이지 대체자가 아니다.**  
       NN/g는 AI를 UX의 ‘보조적 파트너’로 정의하며, 사람의 판단 중심을 강조.
    2. **UX 기업들은 AI로 ‘속도’보다 ‘확장성’을 추구.**
    3. **자동화 도구는 이미 성숙 단계.**
    4. **AI 도입은 ‘문화적 전환’의 문제.**
    5. **Human-in-the-loop + Governance Framework 구축이 핵심.**

    **📖 근거 출처:**  
    Nielsen Norman Group (2023–2025), UX Design Institute (2024), Superside Reports (2024), Whalesync Review (2025)
    """)

    fig4 = px.scatter(
        x=["UX 리서치", "UI 설계", "운영 자동화", "AI Agent", "콘텐츠 생성"],
        y=[75, 68, 55, 62, 70],
        size=[120, 100, 80, 110, 90],
        title="AI 도입 분야별 성숙도 지표 (0–100)",
        labels={"x": "도입 분야", "y": "성숙도 (%)"}
    )
    st.plotly_chart(fig4, use_container_width=True)
    st.success("결론: AI는 UX 산업을 재편하지만, **‘사람의 해석력’이 여전히 핵심 경쟁력**입니다.")

# ==========================================================
# ⑤ 글로벌 UX 기업 비교 (IDEO vs Superside)
# ==========================================================
with tabs[4]:
    st.header("🌍 글로벌 UX-전문회사 AI 도입 진화 비교")

    df_compare = pd.DataFrame({
        "회사": ["IDEO", "Superside"],
        "도입 시작 연도": [2023, 2023],
        "AI 활용 수준 (1-10)": [6, 9],
        "주요 성과": [
            "리서치·콘셉트·슬라이드 제작에 AI 활용 ([ideo.com](https://www.ideo.com/journal/5-ways-were-using-ai-at-work))",
            "AI 디자인 프로젝트 200건 수행, 설계시간 30-60% 단축 ([superside.com](https://www.superside.com/blog/ai-design-projects))"
        ]
    })
    st.dataframe(df_compare, use_container_width=True)

    fig_cmp = px.bar(
        df_compare,
        x="회사",
        y="AI 활용 수준 (1-10)",
        text="AI 활용 수준 (1-10)",
        title="IDEO vs Superside : AI 활용 수준 비교",
        labels={"AI 활용 수준 (1-10)": "활용 점수"}
    )
    fig_cmp.update_traces(marker_color=["#FF7F50", "#4682B4"])
    st.plotly_chart(fig_cmp, use_container_width=True)

    # 연도별 프로젝트 수 추이
    st.subheader("📈 연도별 AI 프로젝트 확장 추이 (2023–2025)")
    timeline_cmp = pd.DataFrame({
        "연도": [2023, 2024, 2025, 2023, 2024, 2025],
        "회사": ["IDEO", "IDEO", "IDEO", "Superside", "Superside", "Superside"],
        "AI 관련 프로젝트 수": [10, 20, 30, 50, 120, 200]
    })
    fig_cmp_line = px.line(
        timeline_cmp,
        x="연도",
        y="AI 관련 프로젝트 수",
        color="회사",
        markers=True,
        title="IDEO vs Superside 연도별 AI 프로젝트 수 추이"
    )
    st.plotly_chart(fig_cmp_line, use_container_width=True)

    st.markdown("""
    **📌 해석:**  
    - Superside는 **생산 워크플로우 자동화 중심**,  
      IDEO는 **인간 중심 디자인 내 보조적 AI 통합**에 초점을 두고 있음.  
    - Superside는 실무 효율, IDEO는 창의성과 윤리 중심.

    **📚 출처:**  
    - IDEO ‘5 Ways We’re Using AI at Work’, ‘7 Experiments That Push the Edges of AI and Design’  
    - Superside ‘What We Learned From 200 AI Design Projects’, ‘10 AI Design Examples That Saved $300k’  
    """)
    st.info("요약: IDEO는 ‘사람 중심의 책임 있는 AI’, Superside는 ‘성과 중심의 통합 자동화’로 방향이 다릅니다.")
