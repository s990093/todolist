import React from "react";
import Image from "next/image";
import { solid } from "@fortawesome/fontawesome-svg-core/import.macro";
import { SvgIcon } from "../base";

interface EvaluateProps {
  title: string;
  rating: number;
  iconColor: string;
  iconRegular?: string;
  iconSolid?: string;
}

const CourseEvaluate: React.FC<EvaluateProps> = ({
  title,
  rating,
  iconColor,
  iconRegular = "heart-regular",
  iconSolid = "heart-solid",
}) => {
  const range = 5;
  const iconPx = 15;
  const difference = range - rating;

  return (
    <div className="flex flex-row space-x-2">
      <div className="font-bold text-[#475569]">{title}</div>
      {/* Mapping for regular icons */}

      {/* Mapping for solid icons */}
      {Array.from({ length: rating }).map((_, index) => (
        <Image
          key={`solid-${index}`}
          src={`./svg/${iconSolid}.svg`}
          width={iconPx}
          height={iconPx}
          alt={iconSolid}
        />
        // <SvgIcon key={`solid-${index}`} iconSolid={iconSolid} iconPx={iconPx} />
      ))}
      {Array.from({ length: difference }).map((_, index) => (
        <Image
          key={`regular-${index}`}
          src={`./svg/${iconRegular}.svg`}
          width={iconPx}
          height={iconPx}
          alt={iconRegular}
          style={{ color: "red" }}
        />
      ))}
    </div>
  );
};

export default CourseEvaluate;
