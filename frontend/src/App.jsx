
import React, {useState} from 'react'
import QueryBox from './components/QueryBox'

export default function App(){
  const [answer, setAnswer] = useState(null)
  return (
    <div style={{padding:20, fontFamily:'sans-serif'}}>
      <h2>KAG Demo</h2>
      <QueryBox onAnswer={setAnswer} />
      <pre style={{whiteSpace:'pre-wrap', background:'#f6f6f6', padding:10}}>{answer && JSON.stringify(answer, null, 2)}</pre>
    </div>
  )
}
