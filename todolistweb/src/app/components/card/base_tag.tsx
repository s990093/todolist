import Image from "next/image";
import React from "react";

interface BaseTagprops {
  title: string;
  icon?: string;
  className?: string;
}

const BaseTag: React.FC<BaseTagprops> = ({ title, icon, className }) => {
  return (
    <div
      className={`${className} flex items-center bg-[#a855f7] rounded-lg p-2 mb-2 border m-1 h-8 overflow-hidden`}
    >
      {icon && (
        <div className="h-6 w-6 mr-2">
          <Image src={icon} alt="Icon" width={15} height={15} />
        </div>
      )}

      <div className="truncate">{title}</div>
    </div>
  );
};

export default BaseTag;
