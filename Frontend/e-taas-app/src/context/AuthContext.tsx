import React from 'react'
import { useContext, createContext } from 'react'
import { useState } from 'react';
import type { User } from '../types/User';
import { useNavigate } from 'react-router-dom';

export const AuthContext = createContext<any | null>(null);

export const AuthProvider: React.FC<{children: React.ReactNode}> = ({ children }) => {

  const navigate = useNavigate();

  const [isAuthenticated, setIsAuthenticated] = useState<boolean>(false);
  const [user, setUser] = useState<User | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(true);

  return (
    <AuthContext.Provider value={{ isAuthenticated, setIsAuthenticated, user, setUser, isLoading, setIsLoading, navigate}}>
      {children}
    </AuthContext.Provider>
  )
}

export const useAuth = () => {
  return useContext(AuthContext);
}
