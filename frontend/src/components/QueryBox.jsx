
import React, {useState} from 'react'

export default function QueryBox({onAnswer}){
  const [q, setQ] = useState('Which suppliers contributed to order ORD-123 delays?')
  const [loading, setLoading] = useState(false)
  async function send(){
    setLoading(true)
    try{
      const resp = await fetch('/query', {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({query:q})})
      const data = await resp.json()
      onAnswer(data)
    }catch(e){
      onAnswer({error: e.toString()})
    }
    setLoading(false)
  }
  return (
    <div>
      <textarea value={q} onChange={e=>setQ(e.target.value)} rows={4} style={{width:'100%'}} />
      <button onClick={send} disabled={loading}>{loading? 'Running...':'Run Query'}</button>
    </div>
  )
}
