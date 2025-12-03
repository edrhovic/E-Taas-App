import { Route, Routes } from "react-router-dom"
import './index.css'
import { Home } from "./features/general/pages/Home"
import { Profile } from "./features/user/pages/Profile"

function App() {

  return (
    <>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/profile" element={<Profile />} />
      </Routes>
    </>
  )
}

export default App
