'use client'
import { useRouter } from 'next/navigation'
import { useState } from 'react'

export default function SearchBar() {
  const [query, setQuery] = useState('')
  const [loading, setLoading] = useState(false)
  const router = useRouter()

  const handleSearch = () => {
    const trimmed = query.trim()
    if (!trimmed || loading) 
      return
    setLoading(true)
    router.push(`/player/${encodeURIComponent(trimmed)}`)
  }

  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter') {
      e.preventDefault()
      handleSearch()
    }
  }

  return (
    <div className="flex gap-2 items-center">
      <input
        type="text"
        placeholder="Search a player..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        onKeyDown={handleKeyDown}
        className="border p-2 rounded w-full focus:outline-none focus:ring-2 focus:ring-blue-400 transition"
      />
      <button
        onClick={handleSearch}
        disabled={loading || !query.trim()}
        className={`
          px-4 py-2 rounded transition-all duration-150
          ${loading ? 'bg-gray-400 cursor-not-allowed' : 'bg-blue-600 hover:bg-blue-700 active:scale-95'}
          text-white shadow
        `}
      >
        {loading ? 'Loading...' : 'Go'}
      </button>
    </div>
  )
}