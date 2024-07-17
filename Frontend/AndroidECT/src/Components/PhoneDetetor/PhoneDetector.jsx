import { useEffect, useState } from 'react'
import io from 'socket.io-client'


function PhoneDetector() {

    const socket = io('http://localhost:3773')
    const [device, setDevice] = useState([])
    console.log("this is ur phone", device)

    useEffect(() => {
        socket.on('device-connected', (phone) => {
            setDevice((prev) => [...prev, {...phone, status: 'connected'}])
        })
        return () => {
            socket.off('device-connected')
        }
    }, [socket])
  return (
    <div>
        <h3>PhoneDetected:</h3>
        <div>
            {device.map((device, index) => (
                <ul key={index}>
                    <div>
                        {Object.entries(device).map(([key, value]) => (
                            <li key={key}>
                                <strong>{key}:</strong> {value}
                            </li>
                        ))}
                    </div>
                </ul>
            ))}
        </div>
    </div>
  )
}

export default PhoneDetector