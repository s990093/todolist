import { EveuateTag } from "@/app/interface";
import Tags from "./tags";
import BaseCard from "./base_card";

const EveuateCard: React.FC<{ eveuateTags: EveuateTag[] }> = ({
  eveuateTags,
}) => {
  return (
    <BaseCard className={`bg-secondary bg-opacity-60  p-4`}>
      <div className="flex flex-col space-x-4">
        <h2 className="text-xl font-bold">大家都在看</h2>
        <div className="grid grid-cols-4">
          {eveuateTags.map((bannertag, index) => (
            <Tags key={index} title={bannertag.title} />
          ))}
        </div>
      </div>
    </BaseCard>
  );
};

export default EveuateCard;
