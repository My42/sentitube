export default function Landing() {
  return (
    <main style={{ padding: '2rem', fontFamily: 'sans-serif', textAlign: 'center' }}>
      <h1
        style={{
          fontSize: '3rem',
          fontWeight: 'bold',
          background: 'linear-gradient(90deg, red, white)',
          WebkitBackgroundClip: 'text',
          WebkitTextFillColor: 'transparent',
          marginBottom: '2rem',
        }}
      >
        Sentitube
      </h1>
      <form style={{ display: 'flex', justifyContent: 'center', gap: '0.5rem' }}>
        <input
          type="text"
          placeholder="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
          style={{ flex: '1 0 300px', padding: '0.5rem', fontSize: '1rem' }}
        />
        <button
          type="submit"
          style={{
            padding: '0.5rem 1rem',
            backgroundColor: '#ff0000',
            color: 'white',
            border: 'none',
            borderRadius: '4px',
            fontSize: '1rem',
            cursor: 'pointer',
          }}
        >
          Lancer l'analyse
        </button>
      </form>
      <section style={{ marginTop: '2rem', maxWidth: '600px', marginLeft: 'auto', marginRight: 'auto' }}>
        <p>
          Sentitube analyse en temps réel les commentaires YouTube afin de vous
          donner un aperçu clair de l'opinion des spectateurs. Entrez simplement
          l'URL d'une vidéo pour découvrir si le ressenti est plutôt positif,
          neutre ou négatif.
        </p>
      </section>
    </main>
  )
}
