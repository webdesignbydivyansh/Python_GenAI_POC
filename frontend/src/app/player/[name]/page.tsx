'use client'
import { useEffect, useState } from 'react'
import { useParams } from 'next/navigation'
import axios from 'axios'

export default function PlayerPage() {
  const params = useParams()
  const name = decodeURIComponent(params.name as string)
  const [data, setData] = useState<{ video_url: string } | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    let cancelled = false
    setLoading(true)
    axios.post(`/api/video`, { player: name })
      .then(res => {
        if (!cancelled) setData(res.data)
      })
      .catch(console.error)
      .finally(() => {
        if (!cancelled) setLoading(false)
      })

    return () => {
      cancelled = true
    }
  }, [name])

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-4">Video for: {name}</h2>
      {loading ? (
        <p>Loading...</p>
      ) : data ? (
        <video src={data.video_url} controls className="w-full max-w-xl rounded shadow" playsInline/>
      ) : (
        <p>Video not available.</p>
      )}
    </div>
  )
}
