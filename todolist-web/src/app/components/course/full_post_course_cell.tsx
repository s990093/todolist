"use client";
import React from "react";
import { Course } from "../../interface";
// components
import { Tags, BaseTag, BaseCard } from "..";
import CourseEvaluate from "./course_evaluate";
import SeriaNumber from "./serial_number";

const FullCoursePostCell = ({ course }: { course: Course }) => {
  const [showFullText, setShowFullText] = React.useState<boolean>(false);

  const toggleShowFullText = () => {
    setShowFullText(!showFullText);
  };
  const year = course.timestamp.getFullYear();
  const month = course.timestamp.getMonth();
  const day = course.timestamp.getDate();

  // const board_style = "#0ea5e9";

  const handleClick = () => {
    console.log("Card clicked");
  };

  return (
    <BaseCard
      onClick={handleClick}
      className={`bg-opacity-60 border-2 border-[#0ea5e9] m-3 max-w-[700px]`}
    >
      <div className={`divide-y divide-[#0ea5e9]`}>
        <div className="p-4">
          <div className="flex flex-row justify-between">
            {/* title */}
            <div className="flex flex-row items-center">
              <div className="text-xl font-bold">
                {course.info.course} / {course.info.teacher}
              </div>
              <div className="ml-3">
                <BaseTag className="bg-[#a78bfax]" title={course.info.type} />
              </div>
            </div>
            {/* time */}
            <div className="flex items-center">
              <div className="italic text-pretty">
                時間: {year}/{month}/{day}
              </div>
            </div>
          </div>
        </div>

        {/* bottom content */}
        <div className={`grid grid-cols-2 gap-4 divide-x divide-[#0ea5e9]`}>
          {/* renderedEvaluates */}
          <div className="p-4">
            {/* quality */}
            <CourseEvaluate
              title={course.quality.title}
              rating={course.quality.rating}
              iconRegular={"heart-regular"}
              iconSolid={"heart-solid"}
              iconColor="#22d3ee"
            />
            {/* sweetness */}
            <CourseEvaluate
              title={course.sweetness.title}
              rating={course.sweetness.rating}
              iconColor="#22d3ee"
            />
            {/* coolness */}
            <CourseEvaluate
              title={course.coolness.title}
              rating={course.coolness.rating}
              iconColor="#22d3ee"
            />
            {/* homework */}
            <CourseEvaluate
              title={course.homework.title}
              rating={course.homework.rating}
              iconSolid="pen-to-square-solid"
              iconRegular="pen-to-square-regular"
              iconColor="#22d3ee"
            />
            {/* 課號 */}
            <SeriaNumber number={course.id} />
          </div>
          <div className=" p-4 ">
            {/* comment*/}
            <div className="text-base overflow-hidden">
              <div className={showFullText ? "" : "line-clamp-5"}>
                {course.comments}
              </div>
            </div>
            {showFullText ? (
              <button
                onClick={toggleShowFullText}
                className="text-blue-500 hover:underline"
              >
                收起
              </button>
            ) : (
              <button
                onClick={toggleShowFullText}
                className="text-blue-500 hover:underline"
              >
                閱讀更多
              </button>
            )}
          </div>
        </div>
      </div>
    </BaseCard>
  );
};

export default FullCoursePostCell;
