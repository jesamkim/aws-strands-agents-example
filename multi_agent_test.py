#!/usr/bin/env python3
"""
Strands Agents 멀티 Agent 협업 테스트
목적: Strands Agent의 기본 동작과 협업 기능 확인
"""

from strands import Agent
from strands_tools import calculator, python_repl

def test_multi_agent_collaboration():
    """멀티 Agent 협업 테스트"""
    
    # Agent 1: 데이터 분석가
    analyst = Agent(
        model="us.anthropic.claude-3-5-haiku-20241022-v1:0",
        tools=[calculator, python_repl]
    )
    
    # Agent 2: 보고서 작성자
    writer = Agent(
        model="us.anthropic.claude-3-5-haiku-20241022-v1:0"
    )
    
    # Agent 3: 검토자
    reviewer = Agent(
        model="us.anthropic.claude-3-5-haiku-20241022-v1:0"
    )
    
    print("=== Strands Agents 멀티 Agent 협업 테스트 ===\n")
    
    # 1단계: 분석가가 데이터 분석
    print("1단계: 데이터 분석")
    analysis_task = "당신은 데이터 분석 전문가입니다. 회사 A의 월별 매출: [100, 120, 150, 180, 200]. 성장률과 평균을 계산하고 트렌드를 분석하세요."
    
    try:
        analysis_result = analyst(analysis_task)
        print(f"분석 결과:\n{analysis_result}\n")
    except Exception as e:
        print(f"분석 단계 오류: {e}")
        return
    
    # 2단계: 작성자가 보고서 작성
    print("2단계: 보고서 작성")
    report_task = f"당신은 보고서 작성 전문가입니다. 다음 분석 결과를 바탕으로 경영진용 요약 보고서를 작성하세요:\n{analysis_result}"
    
    try:
        report_result = writer(report_task)
        print(f"보고서:\n{report_result}\n")
    except Exception as e:
        print(f"보고서 작성 단계 오류: {e}")
        return
    
    # 3단계: 검토자가 최종 검토
    print("3단계: 품질 검토")
    review_task = f"당신은 품질 검토 전문가입니다. 다음 보고서를 검토하고 개선점을 제안하세요:\n{report_result}"
    
    try:
        review_result = reviewer(review_task)
        print(f"검토 결과:\n{review_result}\n")
    except Exception as e:
        print(f"검토 단계 오류: {e}")
        return
    
    print("=== 멀티 Agent 협업 테스트 완료 ===")

def test_simple_agent():
    """단일 Agent 기본 동작 테스트"""
    print("=== 단일 Agent 기본 테스트 ===\n")
    
    try:
        simple_agent = Agent(model="us.anthropic.claude-3-5-haiku-20241022-v1:0")
        result = simple_agent("안녕하세요! Strands Agent가 정상 동작하는지 확인하는 테스트입니다.")
        print(f"응답: {result}\n")
        print("=== 단일 Agent 테스트 완료 ===\n")
    except Exception as e:
        print(f"단일 Agent 테스트 오류: {e}\n")

if __name__ == "__main__":
    # 기본 동작 테스트
    test_simple_agent()
    
    # 멀티 Agent 협업 테스트
    test_multi_agent_collaboration()