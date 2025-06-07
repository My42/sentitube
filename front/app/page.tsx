export default function Landing() {
  return (
    <main className="flex flex-col items-center p-8 text-center space-y-6">
      <h1 className="text-5xl font-extrabold bg-gradient-to-r from-red-600 via-red-300 to-white bg-clip-text text-transparent">
        Sentitube
      </h1>
      <form className="flex w-full max-w-xl gap-2">
        <input
          type="text"
          placeholder="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
          className="flex-grow rounded-md border border-gray-300 px-3 py-2 text-base"
        />
        <button
          type="submit"
          className="rounded-md bg-red-600 px-4 py-2 text-white hover:bg-red-700"
        >
          Lancer l'analyse
        </button>
      </form>
      <section className="max-w-xl text-gray-700">
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
