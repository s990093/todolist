export interface TaskType {
  id: number; // Unique identifier for the task
  text: string; // Description of the task
  completed: boolean; // Status of the task
}

// Define the props for the Task component
export interface TaskProps {
  task: TaskType; // A single task object
  onRemove: (id: number) => void; // Function to remove a task by ID
  onToggleComplete: (id: number) => void; // Function to toggle task completion
}
