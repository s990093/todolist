import React, { ReactNode } from "react";
import Head from "next/head";

type Props = {
  children?: ReactNode;
  className?: string;
};

const PageLayout = ({ children, className }: Props) => {
  return (
    <div className={`${className} flex justify-center m-4`}>{children}</div>
  );
};

export default PageLayout;
