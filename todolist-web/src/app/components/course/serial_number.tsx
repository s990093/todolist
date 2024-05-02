import React from "react";
import Image from "next/image";

interface SerialNumberProps {
  number: number;
}

const SerialNumber: React.FC<SerialNumberProps> = ({ number }) => {
  const iconPx = 15;
  const copyToClipboard = () => {
    navigator.clipboard.writeText(number.toString());
    // Optionally, you can provide feedback to the user that the number has been copied
    // 需要做更改
    alert("Number copied to clipboard!");
  };
  return (
    <div className="rounded-lg mt-2 border-solid border-2 border-[#020617] p-2 max-w-[200px]">
      <div className="flex flex-rows space-x-4">
        <div>課號</div>
        <div className="flex flex-rows items-center space-x-1">
          <div>
            <Image
              src={`./svg/hashtag-solid.svg`}
              width={iconPx}
              height={iconPx}
              alt={"iconSolid"}
            />
          </div>
          <div>{number}</div>
        </div>
        <div className="flex right-0">
          <button onClick={copyToClipboard}>
            <Image
              className="right-0"
              src={`./svg/copy-solid.svg`}
              width={iconPx}
              height={iconPx}
              alt="複製"
            />
          </button>
        </div>
      </div>
    </div>
  );
};

export default SerialNumber;
