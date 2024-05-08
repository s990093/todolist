import React from "react";

const SvgIcon = ({
  iconSolid,
  iconPx,
}: {
  iconSolid: string;
  iconPx: number;
}) => {
  return (
    <svg width={iconPx} height={iconPx} viewBox="0 0 24 24">
      <title>{iconSolid}</title>
      <use xlinkHref={"./svg/heart-regular.svg"} fill="red" />
    </svg>
  );
};

export default SvgIcon;
