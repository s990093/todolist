"use client";
import React, { useContext, useState } from "react";
import { Context } from "../hooks/provider";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faBars,
  faChartBar,
  faCog,
  faEnvelope,
  faHome,
  faInfoCircle,
  faStickyNote,
  faUser,
} from "@fortawesome/free-solid-svg-icons"; // Add appropriate icons

// Example of a functional Navbar component
const Navbar = () => {
  const { state } = useContext(Context);
  const [isSidebarOpen, setIsSidebarOpen] = useState(true);

  const toggleSidebar = () => {
    setIsSidebarOpen(!isSidebarOpen);
  };

  return (
    <div>
      {state.isRegistered && <RegisteredNavbar isSidebar={isSidebarOpen} />}
    </div>
  );
};

const menuItems = [
  { name: "Home", href: "/", icon: faHome },
  { name: "memo", href: "/memo", icon: faStickyNote },
  { name: "Analyze", href: "analyze", icon: faChartBar },
  { name: "Settings", href: "/settings", icon: faCog },
  { name: "Friend", href: "/profile", icon: faUser },
  // { name: "Services", href: "#services", icon: faCogs },
  // { name: "Contact", href: "#contact", icon: faEnvelope },
];

function RegisteredNavbar({ isSidebar }: { isSidebar: boolean }) {
  const [isSidebarOpen, setIsSidebarOpen] = useState(true);

  const toggleSidebar = () => {
    setIsSidebarOpen(!isSidebar);
  };
  return (
    <>
      {isSidebarOpen ? (
        <div className="w-30 h-full fixed bg-blue-500 text-white flex flex-col p-4">
          <div className="fixed top-0 left-0 h-screen bg-blue-700 text-white p-4 transition-transform duration-300 ease-in-out transform translate-x-0">
            <h2 className="text-lg mb-4 cursor-pointer">
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
            <div className="ml-2">
              <div className="absolute inset-x-0 bottom-2 left-1">
                <button className="w-[120px] mt-2 bg-blue-600 hover:bg-blue-700 p-2 rounded flex items-center justify-center">
                  <FontAwesomeIcon icon={faEnvelope} className="mr-2" />
                  Contact
                </button>
                <button className="w-[120px] mt-2 bg-blue-600 hover:bg-blue-700 p-2 rounded flex items-center justify-center">
                  <FontAwesomeIcon icon={faInfoCircle} className="mr-2" />
                  About
                </button>
              </div>
            </div>
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
            <div className="ml-auto flex space-x-4">
              <button className="bg-blue-600 hover:bg-blue-700 p-2 rounded flex items-center justify-center">
                <FontAwesomeIcon icon={faEnvelope} className="mr-2" />
                Contact Us
              </button>
              <button className="bg-blue-600 hover:bg-blue-700 p-2 rounded flex items-center justify-center">
                <FontAwesomeIcon icon={faInfoCircle} className="mr-2" />
                About Us
              </button>
            </div>
          </div>
        </div>
      )}
    </>
  );
}

export default Navbar;
