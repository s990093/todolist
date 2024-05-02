"use client";
import React, { useState } from "react";

// Example of a functional Navbar component
const Navbar = () => {
  // const [isOpen, setIsOpen] = useState(true); // State to track if the side navbar is open

  const isOpen = true;

  // const toggleNavbar = () => {
  //   setIsOpen(!isOpen); // Toggle the state
  // };

  return (
    <div>
      {/* Top navigation bar with a menu button to open/close the side navbar */}

      {/* Side navigation bar */}
      <div
        className={`fixed top-0 left-0 h-screen bg-blue-700 text-white w-64 p-4 transition-transform duration-300 ease-in-out ${
          isOpen ? "transform translate-x-0" : "transform -translate-x-full"
        }`}
      >
        <h2 className="text-lg mb-4">Menu</h2>
        <ul>
          <li className="mb-2 hover:bg-blue-600 p-2 rounded">
            <a href="#home">Home</a>
          </li>
          <li className="mb-2 hover:bg-blue-600 p-2 rounded">
            <a href="#about">About</a>
          </li>
          <li className="mb-2 hover:bg-blue-600 p-2 rounded">
            <a href="#services">Services</a>
          </li>
          <li className="mb-2 hover:bg-blue-600 p-2 rounded">
            <a href="#contact">Contact</a>
          </li>
          {/* <li>
            <button className="text-xl" onClick={toggleNavbar}>
              open {isOpen ? <>{isOpen}</> : <>{isOpen}</>}{" "}
            </button>
          </li> */}
        </ul>
      </div>
    </div>
  );
};

export default Navbar;