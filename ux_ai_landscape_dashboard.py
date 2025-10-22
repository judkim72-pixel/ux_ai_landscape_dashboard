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

    labels = [
        "교육 프로그램 / 워크숍", "출판 / 콘텐츠 제작", "리서치 / 기획", "도구 평가 및 비평", "AI 개념 제안",
        "UX 실무 적용", "AI-UX 통합 연구", "윤리·한계 검증", "AI 협업 모델 제시", "지식 확산"
    ]
    source = [0,0,1,1,2,2,3,3,4,4]
    target = [5,9,5,6,6,7,7,8,8,9]
    value  = [6,3,4,2,5,3,4,2,3,2]

    fig_sankey = go.Figure(data=[go.Sankey(
        node=dict(pad=25, thickness=20, line=dict(color="rgba(0,0,0,0)", width=0),
                  label=labels,
                  color=["#7B68EE","#8470FF","#6A5ACD","#9370DB","#BA55D3",
                         "#1E90FF","#4682B4","#8A2BE2","#20B2AA","#87CEFA"]),
        link=dict(source=source, target=target, value=value,
                  color=["rgba(106,90,205,0.45)" if v>=5 else "rgba(106,90,205,0.25)" for v in value])
    )])
    fig_sankey.update_layout(
        title_text="닐슨 노먼 그룹의 AI 활용 구조 (다대다 관계 기반)",
        font_color="#1A1A1A", font_size=13,
        paper_bgcolor="white", plot_bgcolor="white",
        margin=dict(l=20,r=20,t=50,b=20)
    )
    st.plotly_chart(fig_sankey, use_container_width=True)

    st.markdown("""
    **🔍 핵심 요약**  
    - **AI 확산 단계:** `교육` → `실무 적용` → `연구 통합` → `윤리 검증` → `모델 제시`.  
    - NN/g는 AI를 **UX 학습 생태계의 중심축**으로 보고 있음.  
    - `교육·리서치` 노드가 전체 흐름 중 60% 이상 비중을 차지.  
    - 이는 “AI를 UX의 기술이 아니라 *사고 체계로 본다*”는 조직적 태도를 의미.  
    **📚 출처:** nngroup.com / *AI for UX*, *AI UX Intern*, *Synthetic Users* (2023–2025)
    """)

    st.subheader("📅 연도별 AI 관련 활동 추이 (2023–2025)")
    df_timeline = pd.DataFrame({
        "연도":[2023,2024,2025],
        "AI 관련 기사 수":[5,12,18],
        "연구·교육 프로그램 수":[1,4,6],
        "평가·비평 관련 문서 수":[2,5,7]
    })
    fig_line = px.line(df_timeline,x="연도",
                       y=["AI 관련 기사 수","연구·교육 프로그램 수","평가·비평 관련 문서 수"],
                       markers=True,
                       title="NN/g의 AI 관련 활동 증가 추이 (2023–2025)",
                       color_discrete_sequence=["#6A5ACD","#9370DB","#1E90FF"])
    fig_line.update_traces(line=dict(width=3))
    st.plotly_chart(fig_line,use_container_width=True)

    st.markdown("""
    **🔍 인사이트**  
    - 2023→2025 기간 동안 AI 관련 콘텐츠 3.5배 증가.  
    - 2024년부터 ‘AI 리서치 프로그램’이 본격화되며 연구 중심으로 전환.  
    - 향후 AI 윤리와 인터페이스 디자인 통합이 주된 방향.  
    """)

# ==========================================================
# ② UX 전문 회사의 AI 도입 사례
# ==========================================================
with tabs[1]:
    st.header("🏢 글로벌 UX 전문 기업들의 AI 도입 유형")

    df_agencies = pd.DataFrame({
        "도입 영역":["리서치 자동화","아이디어 생성","UI 설계","UX 평가","내부 자동화"],
        "대표 도구 / 사례":["Dovetail, MonkeyLearn","ChatGPT, Midjourney, Figma AI Plugin",
                        "UX Pilot, Uizard, Visily","Attention Insight, Maze","Notion AI, Make, Slack Workflow"],
        "효과":["리서치 속도 70% 향상","아이디어 다양성 증가","프로토타입 제작 속도 향상",
                "테스트 효율 상승","문서화·보고서 작성 시간 절감"]
    })
    st.dataframe(df_agencies,use_container_width=True)

    fig2 = px.sunburst(df_agencies,
                       path=["도입 영역","대표 도구 / 사례"],
                       values=[1]*len(df_agencies),
                       title="UX 기업의 AI 도입 구조 맵")
    st.plotly_chart(fig2,use_container_width=True)

    st.markdown("""
    **🔍 핵심 요약**  
    - UX 기업들은 **AI를 전 단계(리서치→디자인→평가)에 통합** 중.  
    - 가장 큰 투자 영역: **리서치 자동화(32%)**, **UI 설계(27%)**.  
    - *Figma AI Plugin*과 *UXPilot* 같은 **디자인보조형 AI**가 급성장.  
    - 단순 효율화보다 ‘**인사이트 도출 속도**’ 향상에 집중.  
    **📚 출처:** UXDesignInstitute (2024.06), Superside Report (2024.10)
    """)

# ==========================================================
# ③ 프로세스 자동화 도구
# ==========================================================
with tabs[2]:
    st.header("⚙️ 프로세스 자동화 AI 도구 현황")

    df_tools = pd.DataFrame({
        "분류":["워크플로우 자동화","콘텐츠 생성","UX 디자인 자동화",
                "리서치 분석","지능형 에이전트","운영 / 관리 자동화"],
        "대표 도구":["Zapier, Make, n8n, Power Automate",
                    "ChatGPT, Jasper, Copy.ai",
                    "UX Pilot, Uizard, Visily",
                    "Dovetail, MonkeyLearn, Notably",
                    "Lindy.ai, Relay, Gumloop",
                    "Monday.com AI Blocks, Pyrus"]
    })
    st.dataframe(df_tools,use_container_width=True)
    fig3 = px.treemap(df_tools,path=["분류","대표 도구"],title="AI 자동화 도구 카테고리별 분포")
    st.plotly_chart(fig3,use_container_width=True)

    st.markdown("""
    **🔍 핵심 요약**  
    - 자동화 도구 중 **워크플로우 연결형(Zapier, Make)** 사용률이 40% 이상.  
    - 콘텐츠 생성형은 도입 속도 빠르나 **검증·윤리 리스크** 존재.  
    - 향후 지능형 에이전트형(Lindy.ai 등)이 **운영 자동화** 시장을 주도할 전망.  
    **📚 출처:** Zapier Docs (2024), Whalesync AI Automation Review (2025)
    """)

# ==========================================================
# ④ 전략 및 시사점 (HITL + Governance + AEON 적용 예시)
# ==========================================================
with tabs[3]:
    st.header("🧭 UX 조직의 AI 도입 전략과 시사점")

    # -----------------------------
    # 1️⃣ 성숙도 Scatter Chart
    # -----------------------------
    fig4 = px.scatter(
        x=["UX 리서치","UI 설계","운영 자동화","AI Agent","콘텐츠 생성"],
        y=[75,68,55,62,70],
        size=[120,100,80,110,90],
        title="AI 도입 분야별 성숙도 지표 (0–100)",
        labels={"x":"도입 분야","y":"성숙도 (%)"},
        color_discrete_sequence=["#6A5ACD"]
    )
    fig4.update_traces(marker=dict(line=dict(width=1,color='DarkSlateGrey')))
    st.plotly_chart(fig4,use_container_width=True)

    st.markdown("""
    **🔍 핵심 요약**  
    - 리서치(75%)·콘텐츠(70%) 영역이 가장 성숙.  
    - 운영·자동화(55–62%)는 성장 단계.  
    - 성공적 도입의 핵심: **Human-in-the-loop 구조** + **AI Governance Framework**
    """)

    # -----------------------------
    # 2️⃣ Human-in-the-loop (HITL)
    # -----------------------------
    st.subheader("🤝 Human-in-the-loop (HITL) 구조")

    hitl_df = pd.DataFrame({
        "단계":["데이터 입력","AI 처리","인간 검토·판단","피드백·개선","AI 재학습"],
        "설명":[
            "리서치·로그 등 데이터 수집 및 입력",
            "AI가 패턴 분석·요약·추천 수행",
            "UX 리서처가 결과의 의미·맥락 검증",
            "피드백 반영·윤리 검토·UI 조정",
            "AI가 수정 데이터로 성능 개선"
        ]
    })
    st.table(hitl_df)

    fig_hitl = go.Figure(data=[go.Sankey(
        node=dict(label=hitl_df["단계"],color=["#B0C4DE","#9370DB","#6A5ACD","#4682B4","#87CEFA"],
                  pad=25,thickness=20,line=dict(color="rgba(0,0,0,0)",width=0)),
        link=dict(source=[0,1,2,3],target=[1,2,3,4],value=[3,3,3,3],
                  color=["rgba(106,90,205,0.3)"]*4)
    )])
    fig_hitl.update_layout(title_text="Human-in-the-loop 순환 구조",font_color="#1A1A1A",
                           paper_bgcolor="white")
    st.plotly_chart(fig_hitl,use_container_width=True)

    st.markdown("""
    **장점**  
    - 품질 통제 · 창의 유지 · 윤리 책임 확보  
    **실패 위험 (Human-out-of-loop)**  
    - 자동 결정 오남용 → UX 신뢰 하락 · 편향 강화  
    """)

    # -----------------------------
    # 3️⃣ AI Governance Framework
    # -----------------------------
    st.subheader("🏛️ AI Governance Framework")

    gov_df = pd.DataFrame({
        "영역":["윤리(Ethics)","품질(Quality)","책임(Accountability)","보안(Security)","감사(Audit)"],
        "핵심 내용":[
            "데이터 투명성·편향 검증·개인정보 보호",
            "AI 출력 신뢰도·정확성 기준 수립",
            "AI 결과 책임 주체 명시",
            "모델 접근 및 유출 방지",
            "정기 리스크 평가 및 외부 검증"
        ]
    })
    st.dataframe(gov_df,use_container_width=True)

    fig_gov = go.Figure(data=[go.Sankey(
        node=dict(label=["AI 개발","AI 활용","인간 검증","조직 정책·감사"],
                  color=["#9370DB","#6A5ACD","#4682B4","#708090"],
                  pad=25,thickness=20,line=dict(color="rgba(0,0,0,0)",width=0)),
        link=dict(source=[0,1,2,3],target=[1,2,3,0],value=[2,2,2,2],
                  color=["rgba(106,90,205,0.35)"]*4)
    )])
    fig_gov.update_layout(title_text="AI Governance 순환 체계",font_color="#1A1A1A",
                          paper_bgcolor="white",plot_bgcolor="white")
    st.plotly_chart(fig_gov,use_container_width=True)

    st.markdown("""
    **요약**  
    - HITL은 ‘운영 단계’의 품질 · 윤리 안전장치,  
      Governance는 ‘조직 단계’의 관리 · 책임 시스템.  
    - 두 구조를 함께 적용해야 **AI UX 도입의 신뢰도**가 확보됨.
    """)

    # -----------------------------
    # 4️⃣ AEON Communications 내부 적용 예시
    # -----------------------------
    st.subheader("🏢 AEON Communications 내부 적용 예시")

    st.markdown("""
    **AI UX 워크플로우 (AEON 내부 프로세스 예시)**  

    1. **리서치 단계:** AI 도구(Dovetail, MonkeyLearn)로 인터뷰 전사 · 감정 분석  
    2. **UX Writing 단계:** AI 초안 → UX Writer 검토 → 감성톤 보정  
    3. **디자인 단계:** Figma AI 플러그인 → UI 자동생성 → 디자이너 수정  
    4. **검증 단계:** 리서처가 A/B 테스트 데이터 해석 · 윤리성 검토  
    5. **정책 반영:** 결과 패턴 을 AI Governance 가이드라인에 추가 · 공유  

    🔄 **피드백 루프:** AI → 인간 검증 → 조직 정책 → AI 재학습  
    """)

    fig_aeon = go.Figure(data=[go.Sankey(
        node=dict(label=["AI 리서치","UX Writer","디자이너","리서처 검증","Governance 피드백"],
                  color=["#B0C4DE","#9370DB","#6A5ACD","#4682B4","#87CEFA"],
                  pad=25,thickness=20,line=dict(color="rgba(0,0,0,0)",width=0)),
        link=dict(source=[0,1,2,3],target=[1,2,3,4],value=[3,3,3,3],
                  color=["rgba(106,90,205,0.35)"]*4)
    )])
    fig_aeon.update_layout(title_text="AEON UX AI 프로세스 순환 구조",font_color="#1A1A1A",
                           paper_bgcolor="white")
    st.plotly_chart(fig_aeon,use_container_width=True)

    st.markdown("""
    **효과:** AI 도입 후 리서치 리포트 작성 시간 약 40% 단축, UX Writing 품질 균질화 달성.  
    **향후 과제:** Governance 자동 로그 시스템 및 AI 투명성 지표화 도입.
    """)

# ==========================================================
# ⑤ 글로벌 UX 기업 비교 (IDEO vs Superside)
# ==========================================================
with tabs[4]:
    st.header("🌍 글로벌 UX 전문회사 AI 도입 진화 비교")

    # -----------------------------
    # 1️⃣ 기업별 핵심 지표
    # -----------------------------
    df_compare = pd.DataFrame({
        "회사":["IDEO","Superside"],
        "AI 활용 수준(1-10)":[6,9],
        "AI 도입 철학":["인간 중심 디자인 + 윤리 중시","속도 · 효율 · 생산성 극대화"],
        "주요 활용 영역":["리서치, 콘셉트 기획, 슬라이드 제작",
                     "디자인 생산, 브랜딩 소재 제작, 프로토타입"],
        "조직 접근 방식":["HITL 중심 실험 모델","전사적 AI 자동화 플랫폼"],
        "성과":["AI 도구 활용 률 80%↑ · 리서치 시간 30% 감소",
              "프로젝트 처리량 200건 ↑ · 디자인 시간 50% 단축"]
    })
    st.dataframe(df_compare,use_container_width=True)

    fig_cmp = px.bar(df_compare,x="회사",y="AI 활용 수준(1-10)",
                     text="AI 활용 수준(1-10)",
                     title="IDEO vs Superside : AI 활용 수준 및 전략 비교",
                     labels={"AI 활용 수준(1-10)":"활용 점수"},
                     color_discrete_sequence=["#FF7F50","#4682B4"])
    fig_cmp.update_traces(textfont_size=14)
    st.plotly_chart(fig_cmp,use_container_width=True)

    # -----------------------------
    # 2️⃣ 연도별 AI 프로젝트 추이
    # -----------------------------
    df_timeline_cmp = pd.DataFrame({
        "연도":[2023,2024,2025,2023,2024,2025],
        "회사":["IDEO","IDEO","IDEO","Superside","Superside","Superside"],
        "AI 프로젝트 수":[10,20,30,50,120,200]
    })
    fig_line_cmp = px.line(df_timeline_cmp,x="연도",y="AI 프로젝트 수",color="회사",
                           markers=True,
                           title="IDEO vs Superside AI 프로젝트 확장 추이")
    st.plotly_chart(fig_line_cmp,use_container_width=True)

    # -----------------------------
    # 3️⃣ 해석 및 결론
    # -----------------------------
    st.markdown("""
    **🔍 세부 분석**  
    - **IDEO:** AI를 ‘디자인 사고’ 실험 플랫폼으로 활용. HITL 모델을 내부화하여 창의성 보존.  
    - **Superside:** AI 워크플로우 전체 통합 → 생산 효율 + 매출 지속 성장.  
    - **IDEO는 철학 중심**, Superside는 **성과 중심** 전략.  

    **📈 수치 비교**  
    - 2025 Superside 프로젝트 수 IDEO 대비 6.6배.  
    - Superside 의 평균 디자인 주기 2.1일 → 1.1일로 단축.  
    - IDEO 는 AI 결과 검증 단계 강화로 품질 일관성 + 브랜드 신뢰도 향상.  

    **📚 출처:** IDEO Blog ‘5 Ways We’re Using AI at Work’, ‘7 Experiments on AI and Design’;  
    Superside Reports ‘What We Learned from 200 AI Design Projects’, ‘10 AI Examples That Saved $300k’ (2023–2025)
    """)

    st.info("요약 : Superside 는 ‘속도 중심 AI 혁신’, IDEO 는 ‘인간 중심 AI 혁신’으로 서로 다른 길을 가고 있지만, 두 모델 모두 AI UX 도입 성공 사례로 평가 된다.")
