from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from models.youtube_comment import YoutubeComment
from models.youtube_video import YoutubeVideo


class SentimentAnalyserService:
    def __init__(self):
        self.__llm = ChatOpenAI(model="gpt-4o")

    async def analyze_comments(
        self, yt_video: YoutubeVideo, yt_comments: list[YoutubeComment]
    ):
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
        scores = [
            {**score, "text": comment_group_by_id[score["id"]]}
            for json in response.content.split("--")
            if (score := parser.parse(json))
        ]

        return scores
