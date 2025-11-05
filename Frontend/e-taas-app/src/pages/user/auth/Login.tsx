
import type { LoginData } from "../../../types/Auth"
import { loginUser } from "../../../services/auth/Login";
import { useEffect, useState } from "react";
import { refreshUserToken } from "../../../services/auth/Token";
import { useAuth } from "../../../context/AuthContext";
import { useUserSession } from "../../../hooks/userSession";

const Login = () => {

  useUserSession();

  const [formData, setFormData] = useState<LoginData>({
    email: "",
    password: "",
  });

  const { isAuthenticated, setIsAuthenticated, navigate } = useAuth();

  useEffect(() => {
    if (isAuthenticated) {
      navigate("/");
    }
  }, [isAuthenticated, navigate]);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({ ...prevData, [name]: value }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      const res = await loginUser(formData);
      if(res.status === 200){
        setIsAuthenticated(true);
        alert("Successful Login")
      }
    }catch (e) {
      console.log(e);
      alert("Failed to login. Please try again.");
    }
  };


  return (
    <>
      <div className="min-h-screen bg-gray-100 flex items-center justify-center p-8">
        <div className="w-full max-w-md">
          <div className="bg-white rounded-2xl shadow-lg p-8">
            <h2 className="text-2xl font-bold mb-6 text-center">Login to Your Account</h2>
            <form onSubmit={handleSubmit}>
              <div className="mb-4">
                <label className="block text-gray-700 mb-2" htmlFor="email">
                  Email Address
                </label>
                <input
                  type="email"
                  id="email"
                  name="email"
                  value={formData.email}
                  onChange={handleChange}
                  required
                  className="w-full px-4 py-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
              </div>
              <div className="mb-6">
                <label className="block text-gray-700 mb-2" htmlFor="password">
                  Password
                </label>
                <input
                  type="password"
                  id="password"
                  name="password"
                  value={formData.password}
                  onChange={handleChange}
                  required
                  className="w-full px-4 py-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
              </div>
              <button
                type="submit"
                className="w-full bg-blue-500 text-white py-3 rounded-lg hover:bg-blue-600 transition-colors"
              >
                Login
              </button>
            </form>
          </div>
        </div>
      </div>
      { isAuthenticated &&(
        <div className="fixed bottom-4 right-4">
          <button onClick={refreshUserToken} className="bg-blue-500 text-white py-2 px-4 rounded-lg">
            Refresh Token
          </button>
        </div>
      )}
    </>
  )
}

export default Login