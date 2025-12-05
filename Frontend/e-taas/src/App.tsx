import { Route, Routes } from "react-router-dom"
import './index.css'
import { Home } from "./features/general/pages/Home"
import { Profile } from "./features/user/pages/Profile"
import { Products } from "./features/general/pages/Products"

function App() {

  return (
    <>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/profile" element={<Profile />} />
        <Route path="/products" element={<Products />} />
      </Routes>
    </>
  )
}

export default App
