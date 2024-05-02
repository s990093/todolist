import { Course } from "../../interface";
import Tags from "../card/tags";
import { count } from "console";

const HalfCoursePostCell = ({ course }: { course: Course }) => {
  return (
    <div className="bg-[#9ca3af] rounded-lg shadow-lg p-4 cursor-pointer  transition duration-300">
      <h2 className="text-xl font-bold">
        {course.info.course} # {course.id} {course.info.type}
      </h2>
      <div className="grid grid-cols-2 gap-4">
        <div className="p-4 rounded-lg">
          {/* 第一部分 - 課程內容 */}
          <h2 className="text-lg font-bold mb-4">課程內容</h2>
          {/* 这里添加你的課程內容 */}
          <div className="grid gird-rows-2">
            <Tags />
            <Tags />
            <Tags />
            <Tags />
          </div>
        </div>
        <div className=" p-4 rounded-lg">
          {/* 第二部分 - 評論 */}
          <h2 className="text-lg font-bold mb-4">評論</h2>
          <div>{course.comments}</div>
        </div>
      </div>
    </div>
  );
};

export default HalfCoursePostCell;
