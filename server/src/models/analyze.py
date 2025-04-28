from pydantic import BaseModel


class Analyze(BaseModel):
    sentiment_score: float
    justification: str
    yt_comment_id: str
    yt_comment_text: str
