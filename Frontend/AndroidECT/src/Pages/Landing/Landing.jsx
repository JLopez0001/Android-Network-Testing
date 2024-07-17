import { useState } from 'react'
import "./Landing.css"
import TestRan from '../../Components/TestRan/TestRan.jsx'
import TestResults from '../../Components/TestResults/TestResults.jsx'
import PhoneDetector from '../../Components/PhoneDetetor/PhoneDetector.jsx'


function Landing() {

    const [apiKey, setApiKey] = useState("")
    const [testNames, setTestNames] = useState([])
    const [testResults, setTestResults] = useState([])

    let InitiateTest = () => {
        if(apiKey){
            localStorage.setItem('apiKey', apiKey)
        } else {
            alert("Please input your OpenAI API Key")
        }
    }

  return (
    <div className='app-container'>
        <main>Welcome to Android Application Testing</main>
        <div>
            <input 
                type="text"
                value={apiKey}
                placeholder="Paste OpenA.I API Key Here"
                onChange={(e) => setApiKey(e.target.value)}
            />
        <div>
            <button onClick={InitiateTest}>Initiate Test</button>
        </div>
        <div>
            {testNames && (
            <TestRan/>
            )}
        </div>
        <div>
            {testResults && (
            <TestResults/>
            )}
        </div>
        <div>
            <PhoneDetector/>
        </div>
        </div>
    </div>
  )
}

export default Landing