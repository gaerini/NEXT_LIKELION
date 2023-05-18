const todoForm = document.getElementById('todo-form');
const todoList = document.getElementById('todo-list');
const submitBtn = document.querySelector('.submitBtn');

const Todokey = '할 일';
const TodoArr = [];

const inputTag = document.getElementById('content');

temp = window.localStorage.getItem(Todokey);
if (temp != null) {
    const currentLists = JSON.parse(temp);
    
    currentLists.forEach((item) =>{
        paintTodo(item);
    })
}

function submitAddTodo(event) {
    event.preventDefault();
    const todo = inputTag.value;
    obj = {
        text: todo,
        id: Date.now(),
    };
    TodoArr.push(obj);
    // window.localStorage.setItem(Todokey, TodoArr);
    paintTodo(obj);
    saveTodos();
};

function paintTodo(newTodo) {
    const newLi = document.createElement('li');
    newLi.id = newTodo.id;
    const newSpan = document.createElement('span');
    const newBtn = document.createElement('button');
    newBtn.innerText = 'X';
    newSpan.innerText = newTodo.text;
    newBtn.id = 'deleteBtn'
    newBtn.addEventListener('click', deleteTodo);
    newLi.appendChild(newSpan);
    newLi.appendChild(newBtn);
    todoList.appendChild(newLi);
}

function deleteTodo(event) {
    const li = event.target.parentElement;
    li.remove();
}

function saveTodos() {
    window.localStorage.setItem(Todokey ,JSON.stringify(TodoArr));
}


todoForm.addEventListener("submit", submitAddTodo);
