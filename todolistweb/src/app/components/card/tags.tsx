import Image from "next/image";
import TagOutlinedIcon from "@mui/icons-material/TagOutlined";
import BaseCard from "./base_card";
const Tags = ({ title }: { title: string }) => {
  return (
    <BaseCard className="m-1 p-1 bg-[#14b8a6] outline outline-1	">
      <div className="h-6 w-6 mr-2">
        <TagOutlinedIcon />
      </div>
      <div className="truncate">{title}</div>
    </BaseCard>
  );
};

export default Tags;
