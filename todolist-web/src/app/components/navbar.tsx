"use client";

import React, { useState } from "react";
import Image from "next/image";
import { NavbarConfig } from "../../../config/index";
import { useRouter } from "next/navigation";
import { Search } from "@mui/icons-material";
Search;
const Searchbar = () => {
  const router = useRouter();

  const [searchValue, setSearchValue] = useState("");

  const handleSearchChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setSearchValue(event.target.value);
    // router.push(`$/result?query=${searchValue}`);
  };

  const handleKeyDown = (event: React.KeyboardEvent<HTMLInputElement>) => {
    if (event.key === "Enter") {
      router.push(`/result?query=${searchValue}`);
    }
  };
  const handleSubmit = () => {
    // console.log("执行搜索:", searchValue);
    router.push(`/result?query=${searchValue}`);
  };

  return (
    <div className="flex items-center mr-1">
      <input
        type="text"
        value={searchValue}
        onChange={handleSearchChange}
        onKeyDown={handleKeyDown}
        placeholder="查詢..."
        className="border border-gray-300 rounded px-2 py-1 mr-1"
      />
      <button
        onClick={handleSubmit}
        className="border border-gray-300 rounded px-2 py-1 hover:bg-[#94a3b8]"
      >
        <Image
          src="/svg/magnifying-glass-solid.svg"
          alt="Logo"
          width={20}
          height={20}
        />
      </button>
    </div>
  );
};
const Navbar = () => {
  return (
    <div className="bg-primary py-4">
      <div className="container mx-auto flex justify-between items-center">
        <div className="flex items-center">
          {/* title */}
          <a
            href={NavbarConfig.navItemTitle.navItems.url}
            className="flex flex-row items-center justify-center"
          >
            <div className="mr-4">
              <Image src="/logo.png" alt="Logo" width={40} height={40} />
            </div>
            <div className=" font-bold">
              {NavbarConfig.navItemTitle.navItems.title}
            </div>
          </a>
        </div>

        <ul className="flex space-x-4 m-1">
          {NavbarConfig.navItems.map((item, index) => (
            <li key={index}>
              <a
                href={item.url}
                className=" hover:text-gray-400 transition duration-300"
              >
                {item.title}
              </a>
            </li>
          ))}
          <li>
            <Searchbar />
          </li>
        </ul>
      </div>
    </div>
  );
};

export default Navbar;
