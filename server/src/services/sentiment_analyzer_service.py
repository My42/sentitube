from injector import inject
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from src.models.analyze import Analyze
from src.repositories.youtube_repository import YoutubeRepository

from server.src.repositories.analyze_repository import AnalyzeRepository


class SentimentAnalyserService:
    @inject
    def __init__(
        self,
        youtube_repository: YoutubeRepository,
        analyze_repository: AnalyzeRepository,
    ):
        self.__llm = ChatOpenAI(model="gpt-4o", temperature=0)
        self.__youtube_repository = youtube_repository
        self.__analyze_repository = analyze_repository

    async def analyze_comments(self, yt_video_id: str) -> list[Analyze]:
        prompt = """
        You are an AI specialized in sentiment analysis of YouTube comments. Your goal is to analyze the sentiment of each comment in the context of the video's title. The sentiment score must be a float between -1 and 1, where:

        * -1 represents a highly negative sentiment
        * 0 represents a neutral sentiment
        * 1 represents a highly positive sentiment
        
        If a comment is irrelevant to the video's title, assign null as the score.
        You will receive the video title as a string and the comments as a list.

        Instructions:
        Contextual Analysis: Evaluate each comment based on the meaning and sentiment in relation to the video title.
        Sentiment Scoring: Assign a sentiment score between -1 and 1. Use intermediate values (e.g., -0.5, 0.3) for nuanced sentiment.
        Relevance Check: If a comment is unrelated to the video’s topic, set its sentiment score to null.
        Explain Your Score: Provide a short justification for each score based on the comment's content and its relation to the title. Don't need to rewrite the comment in the justification and starts it with "It"
        
        The video title is: {video_title}
        The comments are: {comments}

        Return a JSON object for each comment too prevent error when displaying it. beetween each "json" block add "--"
        """

        yt_video = await self.__youtube_repository.get_video_by_id(yt_video_id)
        yt_comments = await self.__youtube_repository.get_comments_by_video_id(
            yt_video_id,
            count=10,
        )

        parser = JsonOutputParser()
        prompt_template = PromptTemplate.from_template(
            prompt,
        )

        chain = prompt_template | self.__llm
        response = await chain.ainvoke(
            {
                "video_title": yt_video.title,
                "comments": [
                    {"id": comment.id, "text": comment.text} for comment in yt_comments
                ],
            }
        )

        comment_group_by_id = {
            yt_comment.id: yt_comment.text for yt_comment in yt_comments
        }
        analyzes: list[Analyze] = [
            Analyze(
                justification=analyze["justification"],
                sentiment_score=analyze["sentiment_score"],
                yt_comment_id=analyze["id"],
                yt_comment_text=comment_group_by_id[analyze["id"]],
            )
            for json in response.content.split("--")
            if (analyze := parser.parse(json))
        ]

        await self.save_analyzes(analyzes)

        return analyzes

    async def save_analyzes(self, analyses: list[Analyze]) -> None:
        self.__analyze_repository.save(analyses)
