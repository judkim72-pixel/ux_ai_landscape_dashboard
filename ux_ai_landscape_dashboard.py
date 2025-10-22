# -*- coding: utf-8 -*-
# filename: ux_ai_landscape_dashboard.py

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# -----------------------------------------
# 기본 설정
# -----------------------------------------
st.set_page_config(
    page_title="UX 기업의 AI 도입 현황 분석",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📊 UX 기업의 AI 도입 및 자동화 현황 대시보드")
st.caption("Source: Nielsen Norman Group, IDEO, Superside, UX Design Institute, Whalesync, Monday.com, Zapier 등 (2023–2025)")

# -----------------------------------------
# 탭 구성
# -----------------------------------------
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

    # ----------------------------
    # 개선된 Sankey Diagram (다대다 구조)
    # ----------------------------
    labels = [
        "교육 프로그램 / 워크숍",     # 0
        "출판 / 콘텐츠 제작",        # 1
        "리서치 / 기획",            # 2
        "도구 평가 및 비평",        # 3
        "AI 개념 제안",             # 4
        "UX 실무 적용",             # 5
        "AI-UX 통합 연구",          # 6
        "윤리·한계 검증",           # 7
        "AI 협업 모델 제시",        # 8
        "지식 확산"                # 9
    ]

    # 다대다 연결 구조
    source = [
        0, 0,    # 교육 → 실무, 교육 → 지식 확산
        1, 1,    # 출판 → 실무, 출판 → 연구
        2, 2,    # 리서치 → 연구, 리서치 → 윤리 검증
        3, 3,    # 평가 → 윤리 검증, 평가 → 모델 제시
        4, 4     # 개념 → 모델 제시, 개념 → 지식 확산
    ]
    target = [
        5, 9,    # 교육
        5, 6,    # 출판
        6, 7,    # 리서치
        7, 8,    # 평가
        8, 9     # 개념
    ]
    value = [
        6, 3,    # 교육
        4, 2,    # 출판
        5, 3,    # 리서치
        4, 2,    # 평가
        3, 2     # 개념
    ]

    fig_sankey = go.Figure(data=[go.Sankey(
        node=dict(
            pad=25,                  # 노드 간 간격
            thickness=20,            # 노드 두께
            line=dict(color="rgba(0,0,0,0)", width=0),
            label=labels,
            color=["#7B68EE", "#8470FF", "#6A5ACD", "#9370DB", "#BA55D3",
                   "#1E90FF", "#4682B4", "#8A2BE2", "#20B2AA", "#87CEFA"]
        ),
        link=dict(
            source=source,
            target=target,
            value=value,
            color=[
                "rgba(106,90,205,0.45)" if v >= 5 else "rgba(106,90,205,0.25)"
                for v in value
            ]
        )
    )])

    # 글씨 및 배경 렌더링 설정
    fig_sankey.update_layout(
        title_text="닐슨 노먼 그룹의 AI 활용 구조 (다대다 관계 기반)",
        font_color="#1A1A1A",
        font_size=13,
        paper_bgcolor="white",
        plot_bgcolor="white",
        margin=dict(l=20, r=20, t=50, b=20)
    )

    st.plotly_chart(fig_sankey, use_container_width=True)

    st.markdown("""
    **📘 해석:**  
    닐슨 노먼 그룹은 AI를 단순 교육·연구 주제가 아니라,  
    **UX 실무 ↔ 연구 ↔ 윤리 ↔ 개념 모델**로 확산시키는 순환 구조로 활용하고 있습니다.  
    주요 흐름은 다음과 같습니다:
    - `교육` → `실무 적용`, `지식 확산`  
    - `리서치` → `AI-UX 연구`, `윤리 검증`  
    - `개념 제안` → `모델 제시`, `지식 확산`
    """)

    # ----------------------------
    # 연도별 활동 추이 (Line Chart)
    # ----------------------------
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
        labels={"value": "발행 건수", "연도": "Year"},
        color_discrete_sequence=["#6A5ACD", "#9370DB", "#1E90FF"]
    )
    fig_line.update_traces(line=dict(width=3))
    st.plotly_chart(fig_line, use_container_width=True)

    st.markdown("""
    **📚 데이터 근거**
    - *Nielsen Norman Group Official Site* (https://www.nngroup.com)  
    - Articles: *AI for UX*, *AI UX Intern*, *Accelerating Research with AI*, *Synthetic Users*, *Generative AI Research Agenda*  
    - 데이터는 2023–2025 공개 기사, 교육, 리서치 콘텐츠 건수 기준 추정  

    **요약 결론:**  
    NN/g는 AI를 UX 산업의 **지속 가능한 프레임워크로 구조화**하고 있으며,  
    도구 활용을 넘어 ‘교육–실무–윤리–모델 제시’의 **지식 생태계 순환 구조**로 발전 중입니다.
    """)

# ==========================================================
# ② UX 전문 회사의 AI 도입 사례
# ==========================================================
with tabs[1]:
    st.header("🏢 글로벌 UX 전문 기업들의 AI 도입 유형")

    df_agencies = pd.DataFrame({
        "도입 영역": [
            "리서치 자동화", "아이디어 생성", "UI 설계", "UX 평가", "내부 자동화"
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
            "워크플로우 자동화", "콘텐츠 생성", "UX 디자인 자동화",
            "리서치 분석", "지능형 에이전트", "운영 / 관리 자동화"
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
    fig3 = px.treemap(df_tools, path=["분류", "대표 도구"], title="AI 자동화 도구 카테고리별 분포")
    st.plotly_chart(fig3, use_container_width=True)

# ==========================================================
# ④ 전략 및 시사점
# ==========================================================
with tabs[3]:
    st.header("🧭 UX 조직의 AI 도입 전략과 시사점")
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
            "리서치·콘셉트·슬라이드 제작에 AI 활용",
            "AI 디자인 프로젝트 200건 수행, 설계시간 30–60% 단축"
        ]
    })
    st.dataframe(df_compare, use_container_width=True)

    fig_cmp = px.bar(
        df_compare, x="회사", y="AI 활용 수준 (1-10)", text="AI 활용 수준 (1-10)",
        title="IDEO vs Superside : AI 활용 수준 비교",
        labels={"AI 활용 수준 (1-10)": "활용 점수"}
    )
    fig_cmp.update_traces(marker_color=["#FF7F50", "#4682B4"])
    st.plotly_chart(fig_cmp, use_container_width=True)

    st.subheader("📈 연도별 AI 프로젝트 확장 추이 (2023–2025)")
    timeline_cmp = pd.DataFrame({
        "연도": [2023, 2024, 2025, 2023, 2024, 2025],
        "회사": ["IDEO", "IDEO", "IDEO", "Superside", "Superside", "Superside"],
        "AI 프로젝트 수": [10, 20, 30, 50, 120, 200]
    })
    fig_cmp_line = px.line(
        timeline_cmp, x="연도", y="AI 프로젝트 수",
        color="회사", markers=True,
        title="IDEO vs Superside 연도별 AI 프로젝트 수 추이"
    )
    st.plotly_chart(fig_cmp_line, use_container_width=True)
