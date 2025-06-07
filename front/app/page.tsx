"use client"

import { useState } from "react"
import { useRouter } from "next/navigation"

export default function Landing() {
  const router = useRouter()
  const [url, setUrl] = useState("")
  const [error, setError] = useState(false)

  const validate = (input: string) => {
    const regex = /^(https?:\/\/)?(www\.)?(youtube\.com\/watch\?v=|youtu\.be\/)[\w-]{11}/
    return regex.test(input.trim())
  }

  const onSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    if (!validate(url)) {
      setError(true)
      return
    }
    setError(false)
    router.push("/results")
  }

  return (
    <main className="flex flex-col items-center p-8 text-center space-y-10">
      <h1 className="text-6xl md:text-7xl font-extrabold bg-gradient-to-r from-red-700 via-red-500 to-red-400 bg-clip-text text-transparent drop-shadow-sm">
        Sentitube
      </h1>
      <form onSubmit={onSubmit} className="flex w-full max-w-xl flex-col gap-2">
        <div className="flex gap-2">
          <input
            type="text"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            placeholder="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            className={`flex-grow rounded-md border px-3 py-2 text-base shadow-sm focus:outline-none focus:ring-2 focus:ring-red-500 ${
              error ? "border-red-600 animate-shake" : "border-gray-300"
            }`}
          />
          <button
            type="submit"
            className="rounded-md bg-red-600 px-4 py-2 font-medium text-white transition-colors hover:bg-red-700"
          >
            Lancer l'analyse
          </button>
        </div>
        {error && (
          <p className="text-left text-sm text-red-600">URL YouTube invalide</p>
        )}
      </form>
      <section className="max-w-xl text-gray-700 space-y-6">
        <p className="text-lg font-medium">
          Analysez instantanément le ressenti des spectateurs grâce à notre outil
          de sentiment AI pour YouTube.
        </p>
        <ul className="grid gap-4 sm:grid-cols-3">
          <li className="flex flex-col items-center space-y-2">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 24 24"
              fill="currentColor"
              className="h-8 w-8 text-red-600"
            >
              <path
                fillRule="evenodd"
                d="M2.25 12a9.75 9.75 0 1119.5 0 9.75 9.75 0 01-19.5 0zm14.72-2.28a.75.75 0 00-1.06-1.06L10.5 14.06l-2.41-2.41a.75.75 0 00-1.06 1.06l3 3a.75.75 0 001.06 0l6.93-6.93z"
                clipRule="evenodd"
              />
            </svg>
            <span className="text-sm">Analyse instantanée</span>
          </li>
          <li className="flex flex-col items-center space-y-2">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 24 24"
              fill="currentColor"
              className="h-8 w-8 text-red-600"
            >
              <path
                fillRule="evenodd"
                d="M2.25 4.5A2.25 2.25 0 014.5 2.25h15a2.25 2.25 0 012.25 2.25v15A2.25 2.25 0 0119.5 21.75h-15A2.25 2.25 0 012.25 19.5v-15zM6 7.5a.75.75 0 000 1.5h12a.75.75 0 000-1.5H6zm0 4.5a.75.75 0 000 1.5h12a.75.75 0 000-1.5H6zm0 4.5a.75.75 0 000 1.5h7.5a.75.75 0 000-1.5H6z"
                clipRule="evenodd"
              />
            </svg>
            <span className="text-sm">Rapports clairs</span>
          </li>
          <li className="flex flex-col items-center space-y-2">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 24 24"
              fill="currentColor"
              className="h-8 w-8 text-red-600"
            >
              <path
                fillRule="evenodd"
                d="M12 2.25a.75.75 0 01.75.75v8.25h8.25a.75.75 0 010 1.5h-8.25v8.25a.75.75 0 01-1.5 0v-8.25H3.75a.75.75 0 010-1.5h8.25V3a.75.75 0 01.75-.75z"
                clipRule="evenodd"
              />
            </svg>
            <span className="text-sm">Gratuit et open-source</span>
          </li>
        </ul>
      </section>
    </main>
  )
}
