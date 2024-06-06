"use client";
import React, { useState } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faUser } from "@fortawesome/free-solid-svg-icons";

interface AvatarWidgetProps {
  name: string;
  title: string;
  avatarUrl: string;
}

const AvatarWidget: React.FC<AvatarWidgetProps> = ({
  name,
  title,
  avatarUrl,
}) => {
  const [isExpanded, setIsExpanded] = useState(false);

  const handleAvatarClick = () => {
    setIsExpanded(!isExpanded);
  };

  return (
    <div className="relative group">
      <img
        src={avatarUrl}
        alt={name}
        className="w-10 h-10 rounded-full cursor-pointer transition-transform transform group-hover:scale-110 border-2 border-sky-600"
        onClick={handleAvatarClick} // Handle click to toggle expansion
      />
      {isExpanded && (
        <div className="absolute top-12 transform -translate-x-1/2 w-32 p-4 bg-white border rounded-lg shadow-lg opacity-0 group-hover:opacity-100 group-hover:translate-y-2 transition-all duration-300 ease-in-out">
          <div className="text-sm flex items-center">
            <FontAwesomeIcon icon={faUser} className="text-gray-500 mr-2" />
            <div>
              <h3 className="font-bold">{name}</h3>
              <p className="text-gray-500">{title}</p>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default AvatarWidget;
