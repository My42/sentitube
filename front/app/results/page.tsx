export default function Results() {
  const analyses = [
    {
      yt_comment_id: '1',
      yt_comment_text: 'Great video, loved it!',
      sentiment_score: 0.8,
      justification: 'It expresses very positive feelings about the video.',
    },
    {
      yt_comment_id: '2',
      yt_comment_text: 'I did not like the sound quality.',
      sentiment_score: -0.4,
      justification: 'It states a clear negative opinion.',
    },
    {
      yt_comment_id: '3',
      yt_comment_text: 'Nice, thanks for sharing.',
      sentiment_score: 0.5,
      justification: 'The comment is appreciative though short.',
    },
  ]

  return (
    <main className="p-8 space-y-4">
      <h1 className="text-2xl font-semibold">Analyses fictives</h1>
      <ul className="space-y-4">
        {analyses.map((a) => (
          <li key={a.yt_comment_id} className="rounded-md border p-4">
            <p>
              <strong>Commentaire:</strong> {a.yt_comment_text}
            </p>
            <p>
              <strong>Score:</strong> {a.sentiment_score}
            </p>
            <p>
              <strong>Justification:</strong> {a.justification}
            </p>
          </li>
        ))}
      </ul>
    </main>
  )
}
