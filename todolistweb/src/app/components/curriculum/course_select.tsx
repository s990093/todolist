import * as React from "react";
import Box from "@mui/material/Box";
import InputLabel from "@mui/material/InputLabel";
import MenuItem from "@mui/material/MenuItem";
import FormControl from "@mui/material/FormControl";
import Select, { SelectChangeEvent } from "@mui/material/Select";
import Button from "@mui/material/Button";
import DeleteIcon from "@mui/icons-material/Delete";
import ArrowForwardOutlinedIcon from "@mui/icons-material/ArrowForwardOutlined";
import Stack from "@mui/material/Stack";

const CourseSelection = () => {
  const [age, setAge] = React.useState("");

  const handleChange = (event: SelectChangeEvent) => {
    setAge(event.target.value as string);
  };

  return (
    <div className="flex flex-col  space-y-4 justify-between p-4">
      <Box sx={{ minWidth: 120 }}>
        <FormControl fullWidth>
          <InputLabel id="demo-simple-select-label">選擇課程</InputLabel>
          <Select
            labelId="demo-simple-select-label"
            id="demo-simple-select"
            value={age}
            label="選擇課程"
            onChange={handleChange}
          >
            <MenuItem value={10}>核心</MenuItem>
            <MenuItem value={20}>博雅</MenuItem>
            <MenuItem value={30}>體育</MenuItem>
          </Select>
        </FormControl>
      </Box>
      <Box sx={{ minWidth: 120 }}>
        <FormControl fullWidth>
          <InputLabel id="demo-simple-select-label">排序</InputLabel>
          <Select
            labelId="demo-simple-select-label"
            id="demo-simple-select"
            value={10}
            label="排序"
          >
            <MenuItem value={10}>點擊率</MenuItem>
            <MenuItem value={20}>時間</MenuItem>
            <MenuItem value={30}>自動推薦</MenuItem>
          </Select>
        </FormControl>
      </Box>
      <Button
        fullWidth
        variant="outlined"
        endIcon={<ArrowForwardOutlinedIcon />}
      >
        搜索
      </Button>
    </div>
  );
};

export default CourseSelection;
