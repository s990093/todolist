import { Course } from "./course";
import { Tag } from "./tags";

export interface BannertTag {
  title: string;
}

export interface EveuateTag extends BannertTag {
  query: string;
}
export interface AnaylsisTag extends BannertTag {
  numbers: number;
  unit: string;
}

export interface HomePageData {
  courses: Course[];
  forNKUST: Tag[];
  everyoneWatch: Tag[];
  newsInfo: Tag[];
  bannertTags: BannertTag[];
  eveuateTags: EveuateTag[];
  anaylsisTags: AnaylsisTag[];
}
