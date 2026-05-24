 ---
  Tax-Bot — 소득세법 전문 챗봇
  
  소득세법 문서를 기반으로 사용자 질문에 조항을 인용하며 답변하는 RAG 기반 챗봇입니다.

  ---
  핵심 설계

  Dictionary Chain

  세법 특유의 용어 불일치 문제를 해결하기 위해 사용자 질문을 법률 용어로 변환한 뒤 검색합니다.
  (예: "사람" → "거주자")

  History-Aware Retriever

  이전 대화 맥락을 반영하여 질문을 재구성한 후 검색하므로 멀티턴 대화가 가능합니다.

  Few-Shot Prompting

  실제 소득세법 조항 인용 형식의 예시 답변을 프롬프트에 포함하여 일관된 답변 형식을 유지합니다.

  ---
  아키텍처

  [사용자 질문]
      └── Dictionary Chain  →  법률 용어로 쿼리 재작성
      └── History-Aware Retriever  →  대화 맥락 반영 검색
      └── Pinecone  →  소득세법 문서 벡터 검색
      └── GPT-4o + Few-shot Prompt  →  조항 인용 답변 생성

  ---
  기술 스택

  ┌───────────┬─────────────────────────────────┐
  │   분류    │              기술               │
  ├───────────┼─────────────────────────────────┤
  │ Language  │ Python                          │
  ├───────────┼─────────────────────────────────┤
  │ LLM       │ GPT-4o (OpenAI)                 │
  ├───────────┼─────────────────────────────────┤
  │ Embedding │ text-embedding-3-large (OpenAI) │
  ├───────────┼─────────────────────────────────┤
  │ Vector DB │ Pinecone                        │
  ├───────────┼─────────────────────────────────┤
  │ Framework │ LangChain                       │
  ├───────────┼─────────────────────────────────┤
  │ UI        │ Streamlit                       │
  └───────────┴─────────────────────────────────┘

  ---
  프로젝트 구조

  chat.py      # Streamlit 챗봇 UI
  llm.py       # RAG 체인 구성 (Dictionary Chain + History-Aware Retriever)
  config.py    # Few-shot 예시 답변
  evaluate.ipynb  # 평가 노트북

  ---
