import './globals.css'
import type { ReactNode } from 'react'

export const metadata = {
  title: 'Sentitube',
  description: 'Analyse de sentiment pour YouTube',
}

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="fr">
      <body className="min-h-screen bg-gray-50 text-gray-900">{children}</body>
    </html>
  )
}
