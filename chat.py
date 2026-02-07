import streamlit as st


from dotenv import load_dotenv # 환경변수 로드


from llm import get_ai_response

# streamlit은 채팅을 칠 때마다 전체 코드가 다시 실행되는 방식
# 재실행되니까 처음부터 구조잡지 말고 다 때려박은 다음에 구조잡기


st.set_page_config(page_title="소득세 챗봇", page_icon="🤖")

st.title("🤖 소득세 챗봇")
st.caption("소득세에 관련된 모든 것을 답해드립니다!")

load_dotenv()

if 'message_list' not in st.session_state:
    st.session_state.message_list = []

for message in st.session_state.message_list:
    with st.chat_message(message["role"]):
        st.write(message["content"]) 



if user_question := st.chat_input(placeholder="소득세에 관련된 궁금한 내용들을 말씀해주세요!"):
    with st.chat_message("user"): # 사용자 채팅이 입력되는 부분
        st.write(user_question)
    st.session_state.message_list.append({"role" : "user", "content" : user_question})

    with st.spinner("답변을 생성하는 중입니다..."):
        ai_response = get_ai_response(user_question)
        with st.chat_message("ai"): # 사용자 채팅이 입력되는 부분
            ai_message = st.write_stream(ai_response)
            st.session_state.message_list.append({"role" : "ai", "content" : ai_message})

 
# 채팅에 입력된 내용들은 Session state에 저장됨 (한 세션 안에 유지되는 정보)
# 세션이 살아있는 동안에 유지되는  전역변수 (정도로 생각)