import './App.css'
import { Routes, Route } from 'react-router-dom'
import Register from './pages/user/auth/Register'
import Login from './pages/user/auth/Login'
import { AuthProvider } from './context/AuthContext'
import Home from './pages/user/home/Home'

function App() {

  return (
    <>
    <AuthProvider>
      <Routes>
        <Route path='/' element={<Home />}/>
        <Route path='/register' element={<Register />}/>
        <Route path='/login' element={<Login />}/>
      </Routes>
    </AuthProvider>
    </>
  )
}

export default App
