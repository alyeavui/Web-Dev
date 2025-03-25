const taskInput = document.querySelector("#newTodo");
const addTaskBtn = document.querySelector("#addTodo");
const taskList = document.querySelector("#tasks");

let tasks = [];

function addTask(){
    if (taskInput.value.trim() === "") return;
    tasks.push({ name: taskInput.value, done: false });
    renderTasks();
    taskInput.value = "";
}

function renderTasks(){
  taskList.innerHTML = "";
  tasks.forEach((task, index) => {
    const taskItem = document.createElement("li");
    taskItem.classList.add("task-item");
    taskItem.innerHTML =
      `<div class="task-container">
        <input type="checkbox" class="task-done" ${task.done ? "checked" : ""} />
        <span class="item ${task.done ? "done" : ""}">${task.name}</span>
        <button class="delete-btn" onclick="deleteTask(${index})"><i class="fa-solid fa-trash" style="color:red;"></i></button>
      </div>`;
    
    taskItem.querySelector(".task-done").addEventListener("click", () => {
      markTaskDone(index);
    });
    taskList.appendChild(taskItem);
  });
}

function deleteTask(index){
  tasks.splice(index, 1);
  renderTasks();
}

function markTaskDone(index){
    tasks[index].done = !tasks[index].done;
    renderTasks();
}

addTaskBtn.addEventListener("click", addTask);

taskInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") {
        addTask();
    }
});

renderTasks();