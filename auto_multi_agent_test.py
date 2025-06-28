#!/usr/bin/env python3
"""
Strands Agents 자동화된 멀티 Agent 협업 테스트
사용자 입력 없이 자동 실행
"""

import os
from strands import Agent
from strands_tools import calculator

def test_automated_collaboration():
    """자동화된 멀티 Agent 협업 테스트"""
    
    # 자동 승인 환경 변수 설정
    os.environ['STRANDS_AUTO_APPROVE'] = 'true'
    
    # Agent들 생성 (Python REPL 제외하고 계산기만 사용)
    analyst = Agent(
        model="us.anthropic.claude-3-5-haiku-20241022-v1:0",
        tools=[calculator]
    )
    
    writer = Agent(model="us.anthropic.claude-3-5-haiku-20241022-v1:0")
    reviewer = Agent(model="us.anthropic.claude-3-5-haiku-20241022-v1:0")
    
    print("=== 자동화된 멀티 Agent 협업 테스트 ===\n")
    
    # 1단계: 간단한 분석 (계산기만 사용)
    print("1단계: 데이터 분석")
    analysis_task = """당신은 데이터 분석 전문가입니다. 
    회사 A의 월별 매출: [100, 120, 150, 180, 200]
    계산기를 사용하여 다음을 계산하세요:
    1. 평균 매출
    2. 총 매출
    3. 마지막 달 대비 첫 달 증가율
    간단하고 명확하게 분석해주세요."""
    
    analysis_result = analyst(analysis_task)
    print(f"분석 결과:\n{analysis_result}\n")
    
    # 2단계: 보고서 작성
    print("2단계: 보고서 작성")
    report_task = f"""당신은 보고서 작성 전문가입니다. 
    다음 분석 결과를 바탕으로 간단한 경영진용 요약 보고서를 작성하세요:
    {analysis_result}"""
    
    report_result = writer(report_task)
    print(f"보고서:\n{report_result}\n")
    
    # 3단계: 검토
    print("3단계: 품질 검토")
    review_task = f"""당신은 품질 검토 전문가입니다. 
    다음 보고서를 간단히 검토하고 핵심 개선점 1-2개만 제안하세요:
    {report_result}"""
    
    review_result = reviewer(review_task)
    print(f"검토 결과:\n{review_result}\n")
    
    print("=== 자동화된 협업 테스트 완료 ===")

if __name__ == "__main__":
    test_automated_collaboration()