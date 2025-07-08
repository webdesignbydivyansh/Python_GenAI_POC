import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'

export async function POST(req: NextRequest) {
  const body = await req.json()
  const player = body.player || ''

  try {
    const response = await fetch('http://localhost:8000/api/video', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ player })
    })
    const data = await response.json()
    return NextResponse.json(data)
  } catch (error) {
    console.error(error)
    return NextResponse.json({ error: 'Failed to fetch video' }, { status: 500 })
  }
}