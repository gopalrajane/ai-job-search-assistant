from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.security import PromptInjectionDetector, PIIRedaction
from app.agents import OrchestratorAgent
from app.models import Conversation
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

orchestrator = OrchestratorAgent()

@router.post("/chat")
async def chat(message: str, user_id: int, db: Session = Depends(get_db)):
    """Chat with the orchestrator agent"""
    
    # Security checks
    is_injection, injection_msg = PromptInjectionDetector.detect(message)
    if is_injection:
        logger.warning(f"Prompt injection detected for user {user_id}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Suspicious input detected"
        )
    
    # Redact PII
    redacted_message, detected_pii = PIIRedaction.redact(message)
    if detected_pii:
        logger.warning(f"PII detected and redacted for user {user_id}: {list(detected_pii.keys())}")
    
    try:
        response = await orchestrator.process_request(redacted_message)
        
        # Save conversation
        conversation = Conversation(
            user_id=user_id,
            agent_type="orchestrator",
            messages=[
                {"role": "user", "content": message},
                {"role": "assistant", "content": response["response"]}
            ]
        )
        db.add(conversation)
        db.commit()
        
        return {"response": response["response"], "detected_pii": bool(detected_pii)}
    except Exception as e:
        logger.error(f"Chat error: {e}")
        raise HTTPException(status_code=500, detail="Chat processing failed")

@router.get("/health")
async def health_check():
    return {"status": "healthy", "agents": list(orchestrator.specialized_agents.keys())}
