
import streamlit as st
import datetime
from datetime import datetime, timedelta
import hashlib

# 페이지 설정
st.set_page_config(
    page_title="2025 새(AI)로고침! 우리 교실 앱 공모전",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS 스타일
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .info-card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        border-left: 5px solid #667eea;
    }
    .prize-card {
        background-color: #fff;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 0.5rem;
        border: 2px solid #f0f2f6;
    }
    .deadline-alert {
        background-color: #ff6b6b;
        color: white;
        padding: 1rem;
        border-radius: 5px;
        text-align: center;
        font-weight: bold;
    }
    .success-box {
        background-color: #51cf66;
        color: white;
        padding: 1rem;
        border-radius: 5px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# 헤더
st.markdown("""
<div class="main-header">
    <h1>🤖 2025 새(AI)로고침! 우리 교실 앱 공모전</h1>
    <h3>AI 활용 교육용 앱 개발 공모전</h3>
    <p>주최: 경상북도교육청</p>
</div>
""", unsafe_allow_html=True)

# 사이드바
with st.sidebar:
    st.markdown("## 🔍 빠른 메뉴")
    menu = st.radio(
        "원하는 정보를 선택하세요",
        ["📋 공모전 개요", "💰 상금 및 시상", "📅 일정 및 마감", 
         "💡 공모 주제", "📝 제출 방법", "⚖️ 심사 기준", 
         "❓ 자주 묻는 질문", "💬 커뮤니티", "📧 문의하기"]
    )

# 메인 컨텐츠
if menu == "📋 공모전 개요":
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 🎯 공모전 목적")
        st.info("""
        - **AI 기술을 활용한 교육용 앱 개발**을 통한 교실 수업 혁신
        - 교직원과 예비교사가 참여하는 **현장 중심** 교육 실천 문화 조성
        - 공공성과 실용성을 갖춘 앱으로 **AI 교육 생태계** 기반 마련
        """)
        
        st.markdown("### 👥 참가 자격")
        st.success("""
        ✅ 전국 초·중·고·특수학교 **교직원**  
        ✅ **교육전문직원**  
        ✅ 교육대학교 및 사범대학 **재학생(예비교사)**  
        
        ⚠️ **개인 단위로만 참가 가능** (팀 참가 불가)
        """)
    
    with col2:
        # 마감일 계산
        deadline = datetime(2025, 7, 18)
        today = datetime.now()
        days_left = (deadline - today).days
        
        if days_left > 0:
            st.markdown(f"""
            <div class="deadline-alert">
                📅 마감까지<br>
                <h2>{days_left}일</h2>
                남았습니다!
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="deadline-alert">
                ⏰ 접수 마감
            </div>
            """, unsafe_allow_html=True)

elif menu == "💰 상금 및 시상":
    st.markdown("### 🏆 시상 내역")
    
    prizes = [
        {"상급": "대상", "인원": "1명", "상금": "100만원", "icon": "🥇"},
        {"상급": "금상", "인원": "2명", "상금": "50만원", "icon": "🥈"},
        {"상급": "은상", "인원": "3명", "상금": "30만원", "icon": "🥉"},
        {"상급": "동상", "인원": "5명", "상금": "10만원", "icon": "🏅"},
        {"상급": "장려상", "인원": "10명 내외", "상금": "소정의 상품", "icon": "🎖️"}
    ]
    
    for prize in prizes:
        st.markdown(f"""
        <div class="prize-card">
            <h4>{prize['icon']} {prize['상급']}</h4>
            <p>인원: {prize['인원']} | 부상: 경상북도교육감상 및 상금 {prize['상금']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.warning("💡 상금은 제세공과금 공제 후 지급됩니다.")

elif menu == "📅 일정 및 마감":
    st.markdown("### 📅 공모전 일정")
    
    timeline = {
        "공고 및 접수 시작": "2025년 6월 25일(수)",
        "접수 마감": "2025년 7월 18일(금)",
        "심사 기간": "2025년 7월 21일(월) ~ 7월 25일(금)",
        "결과 발표": "2025년 7월 30일(수)"
    }
    
    for event, date in timeline.items():
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown(f"**{event}**")
        with col2:
            st.markdown(f"📌 {date}")
        st.divider()

elif menu == "💡 공모 주제":
    st.markdown("### 🎯 공모 주제 (AI 요소 필수 포함)")
    
    topics = {
        "① 수업 및 학습 지원": [
            "개별 맞춤형 학습 경로 추천",
            "AI를 활용한 질의응답, 요약, 퀴즈 생성",
            "학생의 학습 패턴 분석 및 피드백 제공"
        ],
        "② 생활·정서 지원": [
            "AI 기반 자기성찰, 감정일기, 스트레스 진단",
            "생활 습관 관리, 학습 동기 유발 도우미",
            "교실 속 SEL(Social Emotional Learning) 도구"
        ],
        "③ 평가 및 피드백": [
            "서술형/논술형 문항 채점 보조",
            "학습 진단 및 성취 피드백 자동화",
            "교사용 평가 보조 앱"
        ],
        "④ 교육행정 및 업무 경감": [
            "가정통신문 자동 작성, 학급 일정 자동 정리",
            "수업 계획서/자료 추천, 보고서 초안 생성",
            "상담 기록 자동 정리 및 요약"
        ],
        "⑤ 기타 AI 기술 기반의 창의적 교육활용": [
            "교실 속 생성형 AI 도구",
            "AI 윤리교육을 위한 시뮬레이션 앱",
            "지역/학교 맥락에 맞춘 문제 해결형 앱"
        ]
    }
    
    for topic, details in topics.items():
        with st.expander(topic):
            for detail in details:
                st.write(f"• {detail}")
    
    st.info("💡 위 범주를 참고하여 교육현장의 실제 필요에 기반한 앱을 자유롭게 기획·개발하세요!")

elif menu == "📝 제출 방법":
    st.markdown("### 📤 제출 방법")
    
    st.markdown("#### 1️⃣ 제출 서류")
    requirements = {
        "필수 제출": [
            "✅ 앱 실행 파일 또는 웹앱 접속 링크",
            "✅ 앱 소개서 1부 (PDF, 5쪽 이내)",
            "✅ 소스코드 전체 (zip 압축 파일)",
            "✅ 개인정보 수집 및 이용 동의서 1부"
        ],
        "선택 제출": [
            "📹 시연 영상 (3분 이내)"
        ]
    }
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**필수 제출 서류**")
        for item in requirements["필수 제출"]:
            st.write(item)
    
    with col2:
        st.markdown("**선택 제출 서류**")
        for item in requirements["선택 제출"]:
            st.write(item)
    
    st.markdown("#### 2️⃣ 제출 방법")
    st.markdown("""
    <div class="info-card">
        <h4>📧 이메일 접수</h4>
        <p><strong>접수 이메일:</strong> chs0601@gbe.kr</p>
        <p><strong>접수 기간:</strong> 2025. 6. 25.(수) ~ 7. 18.(금)</p>
        <p>💡 파일 용량이 클 경우 클라우드 링크(Google Drive, OneDrive 등) 첨부</p>
    </div>
    """, unsafe_allow_html=True)

elif menu == "⚖️ 심사 기준":
    st.markdown("### ⚖️ 심사 기준")
    
    criteria = [
        {"항목": "창의성", "내용": "기존과 차별화된 문제 해결 방식인가", "배점": 25},
        {"항목": "교육 효과성", "내용": "수업, 생활, 행정 등 교육현장 활용 가능성", "배점": 25},
        {"항목": "실현 가능성", "내용": "기술적 완성도와 사용 안정성", "배점": 20},
        {"항목": "AI 활용성", "내용": "AI 기술 적용의 적절성과 기능적 의미", "배점": 20},
        {"항목": "완성도", "내용": "앱 구성의 논리성, 디자인, 사용자 편의성", "배점": 10}
    ]
    
    # 표로 표시
    st.markdown("| 평가 항목 | 평가 내용 | 배점 |")
    st.markdown("|---------|---------|------|")
    for c in criteria:
        st.markdown(f"| **{c['항목']}** | {c['내용']} | {c['배점']}점 |")
    st.markdown("| **합계** | | **100점** |")

elif menu == "❓ 자주 묻는 질문":
    st.markdown("### ❓ 자주 묻는 질문")
    
    faqs = {
        "팀으로 참가할 수 있나요?": 
            "아니요. 개인 단위로만 참가 가능하며, 팀 단위 접수는 불가합니다.",
        
        "예비교사도 참가할 수 있나요?": 
            "네! 교육대학교 및 사범대학 재학생이라면 참가 가능합니다.",
        
        "AI 기술을 꼭 사용해야 하나요?": 
            "네, 모든 응모작은 AI 요소를 반드시 포함해야 합니다. AI 모델은 자유롭게 선택할 수 있습니다.",
        
        "오픈소스를 활용해도 되나요?": 
            "네, 가능합니다. 단, 라이선스 확인 및 출처 명시는 필수입니다.",
        
        "제출한 앱의 저작권은 어떻게 되나요?": 
            "출품작의 저작재산권은 경상북도교육청에 귀속되며, 향후 비영리적 교육 목적으로 활용됩니다.",
        
        "파일 용량이 너무 큰데 어떻게 제출하나요?": 
            "Google Drive, OneDrive 등 클라우드 링크를 이메일에 첨부하여 제출하시면 됩니다."
    }
    
    for q, a in faqs.items():
        with st.expander(f"Q. {q}"):
            st.write(f"A. {a}")

elif menu == "💬 커뮤니티":
    st.markdown("### 💬 참가자 커뮤니티")
    
    # 관리자 로그인 상태 초기화
    if 'is_admin' not in st.session_state:
        st.session_state.is_admin = False
    if 'show_admin_login' not in st.session_state:
        st.session_state.show_admin_login = False
    
    # 관리자 로그인 버튼 (우측 상단)
    col1, col2 = st.columns([5, 1])
    with col2:
        if not st.session_state.is_admin:
            if st.button("🔐 관리자", use_container_width=True, key="admin_login_btn"):
                st.session_state.show_admin_login = not st.session_state.show_admin_login
        else:
            st.success("관리자")
            if st.button("로그아웃", use_container_width=True, key="admin_logout_btn"):
                st.session_state.is_admin = False
                st.session_state.show_admin_login = False
                st.rerun()
    
    # 관리자 로그인 폼
    if st.session_state.show_admin_login and not st.session_state.is_admin:
        with st.container():
            st.markdown("---")
            with st.form("admin_login"):
                st.markdown("#### 🔐 관리자 로그인")
                password = st.text_input("비밀번호", type="password")
                col1, col2 = st.columns(2)
                with col1:
                    if st.form_submit_button("로그인", use_container_width=True):
                        # 실제로는 secrets이나 환경변수 사용
                        if hashlib.sha256(password.encode()).hexdigest() == hashlib.sha256("thohkom1566*".encode()).hexdigest():
                            st.session_state.is_admin = True
                            st.session_state.show_admin_login = False
                            st.success("관리자로 로그인되었습니다!")
                            st.rerun()
                        else:
                            st.error("비밀번호가 틀렸습니다.")
                with col2:
                    if st.form_submit_button("취소", use_container_width=True):
                        st.session_state.show_admin_login = False
                        st.rerun()
            st.markdown("---")
    
    # 데이터 초기화
    if 'comments' not in st.session_state:
        st.session_state.comments = []
    if 'notices' not in st.session_state:
        st.session_state.notices = []
    if 'blocked_users' not in st.session_state:
        st.session_state.blocked_users = []
    
    # 관리자 모드
    if st.session_state.is_admin:
        st.info("🔐 관리자 모드로 접속 중입니다.")
        
        admin_menu = st.tabs(["📝 게시물 관리", "📢 공지사항", "🚫 차단 관리", "📊 통계"])
        
        with admin_menu[0]:  # 게시물 관리
            st.markdown("#### 📝 게시물 관리")
            
            if st.session_state.comments:
                for i, comment in enumerate(st.session_state.comments):
                    with st.container():
                        col1, col2 = st.columns([4, 1])
                        with col1:
                            # 질문 상태 표시
                            status_icon = ""
                            if comment['type'] == '질문':
                                if comment.get('status') == 'answered':
                                    status_icon = "✅ "
                                else:
                                    status_icon = "⏳ "
                            
                            st.markdown(f"{status_icon}**{comment['name']}** ({comment['type']}) - {comment['time']}")
                            st.write(comment['text'])
                            
                            # 답변 표시
                            if comment.get('replies'):
                                for reply in comment['replies']:
                                    st.success(f"↳ **관리자 답변**: {reply['text']}")
                                    st.caption(f"답변 시간: {reply['time']}")
                            
                            # 관리자 답변 작성
                            if comment['type'] == '질문' and comment.get('status') != 'answered':
                                with st.expander("답변 작성"):
                                    reply_text = st.text_area("답변", key=f"reply_{comment['id']}")
                                    if st.button("답변 등록", key=f"reply_btn_{comment['id']}"):
                                        if reply_text:
                                            comment['replies'].append({
                                                'text': reply_text,
                                                'time': datetime.now().strftime("%Y-%m-%d %H:%M")
                                            })
                                            comment['status'] = 'answered'
                                            st.success("답변이 등록되었습니다!")
                                            st.rerun()
                        
                        with col2:
                            if st.button("🗑️ 삭제", key=f"admin_del_{i}"):
                                st.session_state.comments.remove(comment)
                                st.rerun()
                            if comment['name'] not in [u['name'] for u in st.session_state.blocked_users]:
                                if st.button("🚫 차단", key=f"block_{i}"):
                                    st.session_state.blocked_users.append({
                                        'name': comment['name'],
                                        'date': datetime.now().strftime("%Y-%m-%d")
                                    })
                                    st.success(f"{comment['name']}님을 차단했습니다.")
                        st.divider()
            else:
                st.info("아직 게시물이 없습니다.")
        
        with admin_menu[1]:  # 공지사항
            st.markdown("#### 📢 공지사항 작성")
            with st.form("notice_form"):
                notice_type = st.selectbox("공지 유형", ["일반", "중요", "긴급"])
                notice_content = st.text_area("공지 내용")
                if st.form_submit_button("공지 등록"):
                    if notice_content:
                        st.session_state.notices.append({
                            'type': notice_type,
                            'content': notice_content,
                            'time': datetime.now().strftime("%Y-%m-%d %H:%M")
                        })
                        st.success("공지사항이 등록되었습니다!")
                        st.rerun()
            
            # 공지사항 목록
            if st.session_state.notices:
                st.markdown("#### 등록된 공지사항")
                for notice in st.session_state.notices:
                    col1, col2 = st.columns([4, 1])
                    with col1:
                        if notice['type'] == '긴급':
                            st.error(f"[{notice['type']}] {notice['content']}")
                        elif notice['type'] == '중요':
                            st.warning(f"[{notice['type']}] {notice['content']}")
                        else:
                            st.info(f"[{notice['type']}] {notice['content']}")
                        st.caption(notice['time'])
                    with col2:
                        if st.button("삭제", key=f"del_notice_{notice['time']}"):
                            st.session_state.notices.remove(notice)
                            st.rerun()
        
        with admin_menu[2]:  # 차단 관리
            st.markdown("#### 🚫 차단된 사용자")
            if st.session_state.blocked_users:
                for user in st.session_state.blocked_users:
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.write(f"**{user['name']}** - 차단일: {user['date']}")
                    with col2:
                        if st.button("차단 해제", key=f"unblock_{user['name']}"):
                            st.session_state.blocked_users.remove(user)
                            st.rerun()
                    st.divider()
            else:
                st.info("차단된 사용자가 없습니다.")
        
        with admin_menu[3]:  # 통계
            st.markdown("#### 📊 커뮤니티 통계")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("전체 게시물", len(st.session_state.comments))
            with col2:
                st.metric("차단된 사용자", len(st.session_state.blocked_users))
            with col3:
                st.metric("공지사항", len(st.session_state.notices))
            
            # 게시물 유형별 통계
            if st.session_state.comments:
                st.markdown("##### 게시물 유형별 현황")
                type_counts = {}
                for comment in st.session_state.comments:
                    type_counts[comment['type']] = type_counts.get(comment['type'], 0) + 1
                
                for type_name, count in type_counts.items():
                    st.write(f"- {type_name}: {count}개")
    
    # 일반 사용자 모드
    else:
        # 공지사항 표시
        if st.session_state.notices:
            for notice in st.session_state.notices:
                if notice['type'] == '긴급':
                    st.error(f"📢 [{notice['type']}] {notice['content']}")
                elif notice['type'] == '중요':
                    st.warning(f"📢 [{notice['type']}] {notice['content']}")
                else:
                    st.info(f"📢 {notice['content']}")
        
        st.info("공모전 관련 질문, 아이디어 공유, 네트워킹을 위한 공간입니다.")
        
        # 댓글 작성 폼
        with st.form("community_form", clear_on_submit=True):
            col1, col2 = st.columns([3, 1])
            with col1:
                comment_name = st.text_input("이름 또는 닉네임")
            with col2:
                comment_type = st.selectbox("구분", ["질문", "정보공유", "아이디어", "기타"])
            
            comment_text = st.text_area("내용을 입력하세요", height=100)
            
            if st.form_submit_button("✏️ 작성하기", use_container_width=True):
                if comment_name and comment_text:
                    # 차단된 사용자 확인
                    if comment_name in [u['name'] for u in st.session_state.blocked_users]:
                        st.error("차단된 사용자입니다. 관리자에게 문의하세요.")
                    else:
                        st.session_state.comments.append({
                            'id': len(st.session_state.comments) + 1,
                            'name': comment_name,
                            'type': comment_type,
                            'text': comment_text,
                            'time': datetime.now().strftime("%Y-%m-%d %H:%M"),
                            'replies': [],  # 답변 저장용
                            'status': 'waiting' if comment_type == '질문' else 'none'
                        })
                        st.success("✅ 작성되었습니다!")
                        st.balloons()
                else:
                    st.error("이름과 내용을 모두 입력해주세요.")
        
        # 댓글 통계
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("전체 글", f"{len(st.session_state.comments)}개")
        with col2:
            questions = len([c for c in st.session_state.comments if c['type'] == '질문'])
            st.metric("질문", f"{questions}개")
        with col3:
            ideas = len([c for c in st.session_state.comments if c['type'] == '아이디어'])
            st.metric("아이디어", f"{ideas}개")
        
        st.divider()
        
        # 댓글 표시
        if st.session_state.comments:
            for i, comment in enumerate(reversed(st.session_state.comments)):
                with st.container():
                    col1, col2, col3 = st.columns([1, 4, 1])
                    
                    with col1:
                        if comment['type'] == '질문':
                            if comment.get('status') == 'answered':
                                st.markdown("✅ **답변완료**")
                            else:
                                st.markdown("❓ **질문**")
                        elif comment['type'] == '정보공유':
                            st.markdown("📢 **정보**")
                        elif comment['type'] == '아이디어':
                            st.markdown("💡 **아이디어**")
                        else:
                            st.markdown("💬 **기타**")
                    
                    with col2:
                        st.markdown(f"**{comment['name']}** · {comment['time']}")
                        st.write(comment['text'])
                        
                        # 관리자 답변 표시
                        if comment.get('replies'):
                            for reply in comment['replies']:
                                st.success(f"↳ **관리자 답변**: {reply['text']}")
                                st.caption(f"답변 시간: {reply['time']}")
                    
                    with col3:
                        # 일반 사용자는 자신의 글만 삭제 가능하도록 할 수도 있음
                        pass
                    
                    st.divider()
        else:
            st.markdown("""
            <div style="text-align: center; padding: 50px; color: gray;">
                <h4>아직 작성된 글이 없습니다.</h4>
                <p>첫 번째 글을 작성해보세요! 💬</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.warning("⚠️ 현재는 임시 저장 방식으로, 페이지를 새로고침하면 내용이 사라집니다.")

elif menu == "📧 문의하기":
    st.markdown("### 📞 문의처")
    
    st.markdown("""
    <div class="info-card">
        <h4>경상북도교육청 기획예산관</h4>
        <p>📧 이메일: chs0601@gbe.kr</p>
        <p>👤 담당자: 공모전 담당자</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 💬 문의 양식")
    with st.form("contact_form"):
        name = st.text_input("이름")
        email = st.text_input("이메일")
        category = st.selectbox("문의 유형", 
            ["참가 자격", "제출 방법", "심사 기준", "기타"])
        message = st.text_area("문의 내용", height=150)
        
        if st.form_submit_button("문의 보내기"):
            st.success("""
            문의가 접수되었습니다! 
            담당자가 확인 후 이메일로 답변 드리겠습니다.
            """)

# 푸터
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: gray;">
    <p>2025 새(AI)로고침! 우리 교실 앱 공모전 | 경상북도교육청</p>
</div>
""", unsafe_allow_html=True)
