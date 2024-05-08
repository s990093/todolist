import React from "react";
import Tags from "./tags";
import { BannertTag } from "@/app/interface";
import BaseCard from "./base_card";

const BannerCard: React.FC<{ bannertags: BannertTag[] }> = ({ bannertags }) => {
  return (
    <BaseCard className={` bg-secondary bg-opacity-60 p-4`}>
      <h2 className="text-xl font-bold">專屬高科大</h2>
      <div className="grid grid-cols-4">
        {bannertags.map((bannertag, index) => (
          <Tags key={index} title={bannertag.title} />
        ))}
      </div>
    </BaseCard>
  );
};

export default BannerCard;
