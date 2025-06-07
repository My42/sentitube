"use client"

import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from 'recharts'

export default function MetricsPage() {
  const sentimentBreakdown = [
    { label: 'Positif', value: 62 },
    { label: 'Neutre', value: 24 },
    { label: 'Négatif', value: 14 },
  ]

  const processingDuration = 12 // secondes
  const commentCount = 150

  const sentimentTrend = [
    { time: 'Jour 1', score: 0.2 },
    { time: 'Jour 2', score: 0.3 },
    { time: 'Jour 3', score: 0.1 },
    { time: 'Jour 4', score: 0.4 },
    { time: 'Jour 5', score: 0.35 },
  ]

  const sentimentByDay = [
    { date: 'Jour 1', positive: 20, neutral: 10, negative: 5 },
    { date: 'Jour 2', positive: 25, neutral: 8, negative: 7 },
    { date: 'Jour 3', positive: 15, neutral: 12, negative: 6 },
    { date: 'Jour 4', positive: 30, neutral: 10, negative: 5 },
    { date: 'Jour 5', positive: 28, neutral: 9, negative: 4 },
  ]

  return (
    <main className="p-8 space-y-8">
      <h1 className="text-3xl font-bold text-red-700">Tableau de bord</h1>
      <div className="grid gap-4 sm:grid-cols-3">
        <div className="rounded-md bg-white p-4 shadow">
          <h2 className="mb-2 text-lg font-semibold">Répartition des sentiments</h2>
          <ul className="space-y-1">
            {sentimentBreakdown.map((s) => (
              <li key={s.label} className="flex justify-between">
                <span>{s.label}</span>
                <span className="font-medium">{s.value}%</span>
              </li>
            ))}
          </ul>
        </div>
        <div className="rounded-md bg-white p-4 shadow">
          <h2 className="mb-2 text-lg font-semibold">Durée du traitement</h2>
          <p className="text-2xl font-bold text-red-600">{processingDuration}s</p>
        </div>
        <div className="rounded-md bg-white p-4 shadow">
          <h2 className="mb-2 text-lg font-semibold">Nombre de commentaires</h2>
          <p className="text-2xl font-bold text-red-600">{commentCount}</p>
        </div>
      </div>

      <div className="rounded-md bg-white p-4 shadow">
        <h2 className="mb-4 text-lg font-semibold">Évolution du sentiment</h2>
        <div className="h-72 w-full">
          <ResponsiveContainer width="100%" height="100%">
            <LineChart data={sentimentTrend} margin={{ top: 5, right: 20, left: 0, bottom: 5 }}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="time" />
              <YAxis domain={[-1, 1]} />
              <Tooltip />
              <Line type="monotone" dataKey="score" stroke="#dc2626" />
            </LineChart>
          </ResponsiveContainer>
        </div>
      </div>

      <div className="rounded-md bg-white p-4 shadow">
        <h2 className="mb-4 text-lg font-semibold">Commentaires par jour</h2>
        <div className="h-72 w-full">
          <ResponsiveContainer width="100%" height="100%">
            <LineChart data={sentimentByDay} margin={{ top: 5, right: 20, left: 0, bottom: 5 }}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="date" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Line type="monotone" dataKey="positive" stroke="#16a34a" name="Positif" />
              <Line type="monotone" dataKey="neutral" stroke="#737373" name="Neutre" />
              <Line type="monotone" dataKey="negative" stroke="#dc2626" name="Négatif" />
            </LineChart>
          </ResponsiveContainer>
        </div>
      </div>
    </main>
  )
}
