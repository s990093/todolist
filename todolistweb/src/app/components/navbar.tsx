"use client";
import React, { useContext, useState } from "react";
import { Context } from "../hooks/provider";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faBars, faHome, faChartBar } from "@fortawesome/free-solid-svg-icons";

// Example of a functional Navbar component
const Navbar = () => {
  const { state } = useContext(Context);
  const [isSidebar, setIsSidebar] = useState(true); // State to track if the navbar is a sidebar

  const toggleNavbarPosition = () => {
    setIsSidebar(!isSidebar); // Toggle the navbar position
  };

  return (
    <div>
      {state.isRegistered && <RegisteredNavbar isSidebar={isSidebar} />}
    </div>
  );
};

const menuItems = [
  { name: "Home", href: "/", icon: faHome },
  { name: "Analyze", href: "analyze", icon: faChartBar },
  // { name: "Services", href: "#services", icon: faCogs },
  // { name: "Contact", href: "#contact", icon: faEnvelope },
];

function RegisteredNavbar({ isSidebar }: { isSidebar: boolean }) {
  return (
    <>
      {isSidebar ? (
        <div className="w-30 h-full fixed bg-blue-500 text-white flex flex-col p-4">
          <div className="fixed top-0 left-0 h-screen bg-blue-700 text-white  p-4 transition-transform duration-300 ease-in-out transform translate-x-0">
            <h2 className="text-lg mb-4">
              <FontAwesomeIcon icon={faBars} /> Menu
            </h2>
            <ul>
              {menuItems.map((item) => (
                <li
                  key={item.name}
                  className="mb-2 hover:bg-blue-600 p-2 rounded"
                >
                  <a href={item.href}>
                    <FontAwesomeIcon icon={item.icon} /> {item.name}
                  </a>
                </li>
              ))}
            </ul>
          </div>
        </div>
      ) : (
        <div className="w-full fixed top-0 bg-blue-500 text-white flex flex-row p-4">
          <div className="w-full bg-blue-700 text-white p-4">
            <ul className="flex space-x-4">
              {menuItems.map((item) => (
                <li key={item.name} className="hover:bg-blue-600 p-2 rounded">
                  <a href={item.href}>
                    <FontAwesomeIcon icon={item.icon} /> {item.name}
                  </a>
                </li>
              ))}
            </ul>
          </div>
        </div>
      )}
    </>
  );
}

export default Navbar;
