import { useEffect } from "react";
import { getUserDetails } from "../../../services/user/UserDetails";

export const Profile: React.FC = () => {
  useEffect(() => {
    const fetchUserDetails = async () => {
      try {
        const userDetails = await getUserDetails();
        console.log("User Details:", userDetails);
      } catch (error) {
        console.error("Error fetching user details:", error);
      }
    };

    fetchUserDetails();
  }, []);
  return (
    <>
      <div className="text-3xl">User Profile Page</div>
    </>
  );
}
