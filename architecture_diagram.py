#!/usr/bin/env python3
"""
Strands Agents 아키텍처 다이어그램 생성
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.aws.ml import Bedrock
from diagrams.programming.language import Python
from diagrams.onprem.client import User
from diagrams.generic.compute import Rack

def create_architecture_diagram():
    """Strands Agents 멀티 Agent 협업 아키텍처 다이어그램 생성"""
    
    with Diagram("Strands Agents 멀티 Agent 협업", show=False, direction="TB"):
        user = User("사용자")
        
        with Cluster("Strands Agents Framework"):
            with Cluster("단일 Agent 테스트"):
                simple_agent = Bedrock("Claude 3.5 Haiku\n기본 응답")
            
            with Cluster("멀티 Agent 협업"):
                with Cluster("1단계: 데이터 분석"):
                    analyst = Bedrock("분석가 Agent\nClaude 3.5 Haiku")
                    calc_tool = Python("계산기 도구")
                    repl_tool = Python("Python REPL")
                    
                    analyst >> Edge(label="사용") >> [calc_tool, repl_tool]
                
                with Cluster("2단계: 보고서 작성"):
                    writer = Bedrock("작성자 Agent\nClaude 3.5 Haiku")
                
                with Cluster("3단계: 품질 검토"):
                    reviewer = Bedrock("검토자 Agent\nClaude 3.5 Haiku")
        
        result = Rack("최종 결과")
        
        # 연결 관계
        user >> simple_agent
        user >> analyst
        analyst >> Edge(label="분석 결과") >> writer
        writer >> Edge(label="보고서") >> reviewer
        reviewer >> Edge(label="검토 완료") >> result

if __name__ == "__main__":
    create_architecture_diagram()
    print("아키텍처 다이어그램이 생성되었습니다: strands_agents_멀티_agent_협업.png")