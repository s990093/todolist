import React, { ReactNode } from "react";

interface TitleProps {
  children: ReactNode;
  className?: string;
}

const BaseTitle = ({ children, className }: TitleProps) => {
  return (
    <div className={`${className} text-2xl font-bold m-4`}>{children}</div>
  );
};

export default BaseTitle;
