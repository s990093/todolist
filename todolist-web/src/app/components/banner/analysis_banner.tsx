import React from "react";
import { BaseCard } from "../card";
import { AnaylsisTag } from "@/app/interface";

const NumberCell = ({
  text,
  number,
  unit,
}: {
  text: string;
  number: number;
  unit: string;
}) => {
  return (
    <div className="flex flex-row space-x-4 p-2 m-4">
      <div className="flex flex-col items-center">
        <div className="font-bold text-[17px] sm:text-[24px]">
          <div className="flex flex-row">
            <div>{number}</div>
            <div className="text-[10px]">{unit}</div>
          </div>
        </div>
        <div className="text-[13px]">{text}</div>
      </div>
    </div>
  );
};
const AnaylsisBanner: React.FC<{ data: AnaylsisTag[] }> = ({ data }) => {
  return (
    <BaseCard className="flex bg-[#cbd5e1]  divide-x divide-[#6b7280] opacity-75 p-4 h-20 items-center justify-center">
      {data.map((_, index) => (
        <NumberCell
          key={index}
          text={_.title}
          number={_.numbers}
          unit={_.unit}
        />
      ))}
    </BaseCard>
  );
};

export default AnaylsisBanner;
