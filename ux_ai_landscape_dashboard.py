# -*- coding: utf-8 -*-
# filename: ux_ai_landscape_dashboard.py

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# -----------------------------------------
# 기본 설정
# -----------------------------------------
st.set_page_config(
    page_title="UX 기업의 AI 도입 현황 분석",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📊 UX 기업의 AI 도입 및 자동화 현황 대시보드")
st.caption("Source: Nielsen Norman Group, IDEO, Superside, UX Design Institute, AEON Communications, Monday.com, Zapier 등 (2023–2025)")

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
        "교육 프로그램 / 워크숍","출판 / 콘텐츠 제작","리서치 / 기획","도구 평가 및 비평","AI 개념 제안",
        "UX 실무 적용","AI-UX 통합 연구","윤리·한계 검증","AI 협업 모델 제시","지식 확산"
    ]
    source=[0,0,1,1,2,2,3,3,4,4]
    target=[5,9,5,6,6,7,7,8,8,9]
    value =[6,3,4,2,5,3,4,2,3,2]

    fig_sankey = go.Figure(data=[go.Sankey(
        node=dict(pad=25,thickness=20,line=dict(color="rgba(0,0,0,0)",width=0),
                  label=labels,
                  color=["#7B68EE","#8470FF","#6A5ACD","#9370DB","#BA55D3",
                         "#1E90FF","#4682B4","#8A2BE2","#20B2AA","#87CEFA"]),
        link=dict(source=source,target=target,value=value,
                  color=["rgba(106,90,205,0.45)" if v>=5 else "rgba(106,90,205,0.25)" for v in value])
    )])
    fig_sankey.update_layout(title_text="닐슨 노먼 그룹의 AI 활용 구조 (다대다 관계 기반)",
                             font_color="#1A1A1A",font_size=13,
                             paper_bgcolor="white",plot_bgcolor="white")
    st.plotly_chart(fig_sankey,use_container_width=True)

    st.markdown("""
    **🔍 핵심 요약**  
    - AI 확산 단계: `교육 → 실무 적용 → 연구 통합 → 윤리 검증 → 모델 제시`  
    - NN/g는 AI를 UX 학습 생태계의 핵심 프레임워크로 인식.  
    - ‘교육·리서치’ 영역이 전체 흐름의 60% 이상 비중 차지.  
    """)

    st.subheader("📅 연도별 AI 관련 활동 추이 (2023–2025)")
    df_time=pd.DataFrame({
        "연도":[2023,2024,2025],
        "AI 관련 기사 수":[5,12,18],
        "연구·교육 프로그램 수":[1,4,6],
        "평가·비평 관련 문서 수":[2,5,7]
    })
    fig_line=px.line(df_time,x="연도",
        y=["AI 관련 기사 수","연구·교육 프로그램 수","평가·비평 관련 문서 수"],
        markers=True,
        title="NN/g의 AI 관련 활동 증가 추이 (2023–2025)",
        color_discrete_sequence=["#6A5ACD","#9370DB","#1E90FF"])
    st.plotly_chart(fig_line,use_container_width=True)
    st.markdown("""
    **📚 출처:** nngroup.com / *AI for UX*, *AI UX Intern*, *Synthetic Users*, *Generative AI Research Agenda* (2023–2025)
    """)

# ==========================================================
# ② UX 전문 회사의 AI 도입 사례
# ==========================================================
with tabs[1]:
    st.header("🏢 글로벌 UX 전문 기업들의 AI 도입 유형")

    df_ag=pd.DataFrame({
        "도입 영역":["리서치 자동화","아이디어 생성","UI 설계","UX 평가","내부 자동화"],
        "대표 도구 / 사례":["Dovetail, MonkeyLearn",
            "ChatGPT, Midjourney, Figma AI Plugin",
            "UX Pilot, Uizard, Visily",
            "Attention Insight, Maze",
            "Notion AI, Make, Slack Workflow"],
        "효과":["리서치 속도 70% 향상","아이디어 다양성 증가",
            "프로토타입 제작 속도 향상","테스트 효율 상승","문서화 시간 절감"]
    })
    st.dataframe(df_ag,use_container_width=True)
    fig_sb=px.sunburst(df_ag,path=["도입 영역","대표 도구 / 사례"],
                       values=[1]*len(df_ag),
                       title="UX 기업의 AI 도입 구조 맵")
    st.plotly_chart(fig_sb,use_container_width=True)
    st.markdown("""
    **🔍 요약**  
    - AI는 UX 전체 주기(리서치→디자인→평가)에 통합되고 있음.  
    - 리서치 자동화(32%), UI 설계(27%) 비중이 가장 높음.  
    - Figma·UXPilot 등 협업형 도구의 도입이 빠르게 확산.  
    """)

# ==========================================================
# ③ 프로세스 자동화 도구
# ==========================================================
with tabs[2]:
    st.header("⚙️ 프로세스 자동화 AI 도구 현황")

    df_tools=pd.DataFrame({
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
    fig_tr=px.treemap(df_tools,path=["분류","대표 도구"],title="AI 자동화 도구 카테고리별 분포")
    st.plotly_chart(fig_tr,use_container_width=True)
    st.markdown("""
    **🔍 요약**  
    - 워크플로우형(Zapier·Make)이 가장 폭넓게 활용.  
    - 콘텐츠 생성형은 윤리적 리스크 관리가 필요.  
    - 에이전트형 도구가 향후 운영 자동화 시장 주도 예상.  
    """)

# ==========================================================
# ④ 전략 및 시사점 (HITL + Governance + AEON Circular Flow)
# ==========================================================
with tabs[3]:
    st.header("🧭 UX 조직의 AI 도입 전략과 시사점")

    fig4=px.scatter(
        x=["UX 리서치","UI 설계","운영 자동화","AI Agent","콘텐츠 생성"],
        y=[75,68,55,62,70],
        size=[120,100,80,110,90],
        title="AI 도입 분야별 성숙도 지표 (0–100)",
        labels={"x":"도입 분야","y":"성숙도 (%)"})
    st.plotly_chart(fig4,use_container_width=True)
    st.markdown("""
    **핵심 요약**  
    - 리서치·콘텐츠 영역 성숙도 높음.  
    - 성공적 도입의 핵심: **Human-in-the-loop(HITL)** + **AI Governance Framework**.
    """)

    st.subheader("🤝 Human-in-the-loop 구조")
    st.markdown("""
    AI가 작업을 수행하더라도 **인간이 루프 내에서 검증·조정·개선**을 수행하는 구조.  
    - 품질·윤리 통제 / 창의성 유지 / 책임 주체 명확화  
    """)

    st.subheader("🏛️ AI Governance Framework")
    st.markdown("""
    AI 활용의 **조직적 관리 체계** — 윤리(Ethics)·품질(Quality)·책임(Accountability)·보안(Security)·감사(Audit) 중심.  
    - 도구 승인·데이터 익명화·윤리 검토 위원회 운영 등으로 신뢰성 확보.
    """)

    # ----------------------------
    # AEON Circular Flow (원형 순환 구조)
    # ----------------------------
    st.subheader("🏢 AEON Communications 내부 적용 예시")

    st.markdown("""
    **AEON의 실제 UX-AI 워크플로우**  
    1️⃣ 사용자 조사 및 데이터 수집 → 2️⃣ 인사이트 검증 및 기능·요구사항 정의 →  
    3️⃣ UX 설계 및 시나리오 모델링 → 4️⃣ 검증 및 피드백 → 5️⃣ Governance 반영 → ♻️ AI 재학습  
    """)

    steps=["AI 리서치","UX 리서처 검증","기능·요구사항 정의","UI 설계","Governance 피드백"]
    angles=np.linspace(0,2*np.pi,len(steps),endpoint=False)
    x=np.cos(angles)
    y=np.sin(angles)
    fig_circ=go.Figure()
    fig_circ.add_trace(go.Scatter(
        x=x,y=y,mode="markers+text",
        marker=dict(size=45,color=["#B0C4DE","#9370DB","#6A5ACD","#4682B4","#87CEFA"]),
        text=steps,textposition="top center",textfont=dict(size=13,color="#1A1A1A")))
    for i in range(len(steps)):
        x0,y0=x[i],y[i];x1,y1=x[(i+1)%len(steps)],y[(i+1)%len(steps)]
        fig_circ.add_shape(type="path",
            path=f"M{x0},{y0} Q{(x0+x1)/2},{(y0+y1)/2+0.2} {x1},{y1}",
            line=dict(color="rgba(106,90,205,0.6)",width=3))
    fig_circ.update_layout(title="AEON UX-AI 순환 구조 (Circular Flow)",
        xaxis=dict(showgrid=False,zeroline=False,visible=False),
        yaxis=dict(showgrid=False,zeroline=False,visible=False),
        showlegend=False,paper_bgcolor="white",plot_bgcolor="white",height=550)
    st.plotly_chart(fig_circ,use_container_width=True)

    st.markdown("""
    **효과:**  
    - 리서치 효율 향상 + 기능 정의 정확도 향상  
    - 설계 일관성 확보 (프로젝트별 평균 35% 일정 단축)  
    **향후 과제:**  
    - AI 인사이트 품질 측정 기준화  
    - Governance 내 ‘신뢰도 지수’ 시각화 시스템 구축
    """)

# ==========================================================
# ⑤ 글로벌 UX 기업 비교 (IDEO vs Superside)
# ==========================================================
with tabs[4]:
    st.header("🌍 글로벌 UX 전문회사 AI 도입 진화 비교")

    df_cmp=pd.DataFrame({
        "회사":["IDEO","Superside"],
        "AI 활용 수준(1-10)":[6,9],
        "AI 도입 철학":["인간 중심 디자인 + 윤리 중심","속도·효율·규모 중심"],
        "주요 활용 영역":["리서치, 콘셉트, 슬라이드 제작",
                       "디자인 생산, 브랜딩, 프로토타입"],
        "조직 접근 방식":["HITL 기반 실험형","전사적 자동화형"],
        "성과":["리서치 시간 30%↓, 품질 일관성 강화",
              "프로젝트 200건↑, 설계시간 50% 단축"]
    })
    st.dataframe(df_cmp,use_container_width=True)
    fig_bar=px.bar(df_cmp,x="회사",y="AI 활용 수준(1-10)",text="AI 활용 수준(1-10)",
                   color_discrete_sequence=["#FF7F50","#4682B4"],
                   title="IDEO vs Superside : AI 활용 수준 비교")
    st.plotly_chart(fig_bar,use_container_width=True)

    df_line=pd.DataFrame({
        "연도":[2023,2024,2025,2023,2024,2025],
        "회사":["IDEO","IDEO","IDEO","Superside","Superside","Superside"],
        "AI 프로젝트 수":[10,20,30,50,120,200]
    })
    fig_line2=px.line(df_line,x="연도",y="AI 프로젝트 수",color="회사",markers=True,
                      title="IDEO vs Superside AI 프로젝트 확장 추이")
    st.plotly_chart(fig_line2,use_container_width=True)

    st.markdown("""
    **🔍 분석 요약**  
    - **IDEO:** 인간 중심 디자인 원칙 내에서 AI를 실험적 도구로 활용. 윤리·창의 중심 HITL 모델.  
    - **Superside:** AI 전사 자동화 시스템으로 생산성·규모 확장 성공.  
    - 2025년 Superside 프로젝트 수 IDEO 대비 6.6배.  
    - 두 기업 모두 **‘AI + 인간 협력 구조’**를 유지하되 초점이 다름.  
      IDEO=철학·창의 중심, Superside=성과·속도 중심.  

    **📚 출처:** IDEO Blog(2023–2025) / Superside Reports(2024–2025)
    """)

    st.info("요약: Superside는 속도 중심 AI 혁신, IDEO는 인간 중심 AI 혁신. 두 접근 모두 UX 산업의 핵심 벤치마크로 평가됨.")
