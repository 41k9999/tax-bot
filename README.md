<h1>Tax-Bot — 소득세법 전문 챗봇</h1>

  <p>소득세법 문서를 기반으로 사용자 질문에 조항을 인용하며 답변하는 RAG 기반 챗봇입니다.</p>
 
  <hr>

  <h2>핵심 설계</h2>
  
  <h3>Dictionary Chain</h3>
  <p>세법 특유의 용어 불일치 문제를 해결하기 위해 사용자 질문을 법률 용어로 변환한 뒤 검색합니다.<br>
  (예: "사람" → "거주자")</p>

  <h3>History-Aware Retriever</h3>
  <p>이전 대화 맥락을 반영하여 질문을 재구성한 후 검색하므로 멀티턴 대화가 가능합니다.</p>

  <h3>Few-Shot Prompting</h3>
  <p>실제 소득세법 조항 인용 형식의 예시 답변을 프롬프트에 포함하여 일관된 답변 형식을 유지합니다.</p>

  <hr>

  <h2>아키텍처</h2>

  <pre>
  [사용자 질문]
      └── Dictionary Chain        →  법률 용어로 쿼리 재작성
      └── History-Aware Retriever →  대화 맥락 반영 검색
      └── Pinecone                →  소득세법 문서 벡터 검색
      └── GPT-4o + Few-shot Prompt →  조항 인용 답변 생성
  </pre>

  <hr>

  <h2>기술 스택</h2>
  
  <table>
    <tr><th>분류</th><th>기술</th></tr>
    <tr><td>Language</td><td>Python</td></tr>
    <tr><td>LLM</td><td>GPT-4o (OpenAI)</td></tr>
    <tr><td>Embedding</td><td>text-embedding-3-large (OpenAI)</td></tr>
    <tr><td>Vector DB</td><td>Pinecone</td></tr>
    <tr><td>Framework</td><td>LangChain</td></tr>
    <tr><td>UI</td><td>Streamlit</td></tr>
  </table>
  
  <hr>

  <h2>프로젝트 구조</h2>

  <pre>
  chat.py        # Streamlit 챗봇 UI
  llm.py         # RAG 체인 구성 (Dictionary Chain + History-Aware Retriever)
  config.py      # Few-shot 예시 답변
  evaluate.ipynb # 평가 노트북
  </pre>
