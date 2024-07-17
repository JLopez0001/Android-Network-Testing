import { Route, Routes } from "react-router-dom"
import './App.css'
import Landing from "./Pages/Landing/Landing.jsx"

function App() {

  return (
    <>
      <Routes>
        <Route path="/" element={<Landing/>}/>
      </Routes>
    </>
  )
}

export default App
