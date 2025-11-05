import { useAuth } from "../context/AuthContext";
import { useEffect } from "react";
import { getUserDetails } from "../services/user/UserDetails";

export const useUserSession = () => {
  const { setIsAuthenticated, setUser, setIsLoading } = useAuth();

  useEffect (() => {
    const checkUserSession = async () => {
      setIsLoading(true);
      try {
        const userDetails =  await getUserDetails();
        if (userDetails) {
          setUser(userDetails);
          setIsAuthenticated(true);
        } else {
          setIsAuthenticated(false);
          setUser(null);
        }
      } catch (error) {
        console.error("Error checking user session:", error);
        setIsAuthenticated(false);
      } finally {
        setIsLoading(false);
      }
    }
    checkUserSession();
  }, [])
}