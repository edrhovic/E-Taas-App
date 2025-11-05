import { useEffect } from 'react';
import { useAuth } from '../../../context/AuthContext'
import { logoutUser } from '../../../services/auth/Logout';


const Home: React.FC = () => {

  const { isAuthenticated, navigate } = useAuth();

  useEffect(() => {
    if (!isAuthenticated) {
      navigate("/login");
    }
  }, [isAuthenticated, navigate]);

  const handleLogout = async () => {
    try {
      await logoutUser();
      navigate("/login");
    } catch (error) {
      console.error("Error logging out:", error);
    }
  };

  return (
    <>
      {isAuthenticated ? (
        <div className="min-h-screen flex items-center justify-center bg-green-100">
          <h1 className="text-4xl font-bold text-green-800">Welcome Back, User!</h1>
          <a onClick={handleLogout}>Logout</a>
        </div>
      ) : (
        <div className="min-h-screen flex items-center justify-center bg-blue-100">
          <h1 className="text-4xl font-bold text-blue-800">Please Log In</h1>
        </div>
      )}
    </>
  )
}

export default Home