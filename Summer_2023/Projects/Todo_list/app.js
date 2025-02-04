// Variables
let id = 0;
let updateInputShowing = false;
let todoCompleted = false;
let filterSelected = "all";
let todoList = [];
let uncompletedList = [];
let completedList = [];
let weatherData = [];
// Select Elements
const addInput = document.querySelector("#addInput");
const addTodoButton = document.querySelector("#addTodoButton");
const todosContainer = document.querySelector("#todosContainer");
const allFilterButton = document.querySelector("#allFilter");
const completedFilterButton = document.querySelector("#completedFilter");
const uncompletedFilterButton = document.querySelector("#uncompletedFilter");

// Functions 

// This function takes care of rendering todo items on screen based on the filter selected by the user

// CODE #1
const renderTodos = (todoList, todosContainer, filter) => {
    while (todosContainer.firstChild) {
        todosContainer.removeChild(todosContainer.firstChild);
    }

    if (filter === "completed") {
        const completedTodos = todoList.filter(todoItem => todoItem.status === "completed");
        completedTodos.map((todoItem) => {
            todosContainer.appendChild(todoItem.element);
        });
        return;
    } if (filter === "uncompleted") {
        const uncompletedTodos = todoList.filter(todoItem => todoItem.status === "uncompleted");
        uncompletedTodos.map((todoItem) => {
            todosContainer.appendChild(todoItem.element);
        });
        return;
    }

    todoList.map((todoItem) => {
        todosContainer.appendChild(todoItem.element);
    });
    return;
}

// This function creates the todo item that will be added to the todo list
const createElement = (todoId, todoValue, elementIds) => {
    const [
        editInputId, updateTodoButtonId, buttonsContainerId, todoTextId,
        editButtonId, deleteButtonId, inputContainerId,
        checkButtonId, unCheckButtonId
    ] = elementIds;

    const newTodoItem = document.createElement("div");
    newTodoItem.classList.add("todo");
    newTodoItem.setAttribute('id', `todo-${todoId}`);
    newTodoItem.innerHTML = `
        <div id=${inputContainerId} class="inputContainer hidden">
            <input id=${editInputId} class="addInput" type="text" placeholder="Enter to do here" />
            <button id=${updateTodoButtonId} class="addTodoButton">Update</button>
        </div>
        <div class="text-check">
            <button id=${unCheckButtonId}>
                <i class="fa-regular fa-circle"></i>
            </button>
            <button id=${checkButtonId}>
                <i  class="fa-regular fa-circle-check"></i>
            </button>
            <p id=${todoTextId} class="todoText">${todoValue}</p>
        </div>
        <div id=${buttonsContainerId} class="buttonsContainer">
            <span id=${editButtonId}>Edit</span>
            <span id=${deleteButtonId}>Delete</span>
        </div>
    `;

    return newTodoItem;
};

// This functions updates the status of the todo items
const updateTodoStatus = (todoCompleted, unCheckButton, checkButton, todoText) => {
    if (todoCompleted) {
        checkButton.classList.remove("hidden");
        unCheckButton.classList.add("hidden");
        todoText.classList.add("completed");
        return;
    } else {
        unCheckButton.classList.remove("hidden");
        checkButton.classList.add("hidden");
        todoText.classList.remove("completed");
        return;
    }
};

// This function toggles the visibility of the input element that is used to update the todo item
const updateInputVisibility = (
    updateInputShowing, todoContainer,
    todoText, buttonsContainer, inputContainer
) => {
    if (updateInputShowing) {
        todoContainer.classList.add("todo2");
        todoContainer.classList.remove("todo");
        todoText.classList.add("hidden");
        buttonsContainer.classList.add("hidden");
        inputContainer.classList.remove("hidden");
        return;
    } else {
        todoContainer.classList.add("todo");
        todoContainer.classList.remove("todo2");
        todoText.classList.remove("hidden");
        buttonsContainer.classList.remove("hidden");
        inputContainer.classList.add("hidden");
        return;
    }
};

const addToDo = (todoId, todoValue, todosContainer) => {
    const editInputId = `editInput-${todoId}`;
    const updateTodoButtonId = `updateTodoButton-${todoId}`;
    const buttonsContainerId = `buttonsContainer-${todoId}`;
    const todoTextId = `todoText-${todoId}`;
    const editButtonId = `editButton-${todoId}`;
    const deleteButtonId = `deleteButton-${todoId}`;
    const inputContainerId = `inputContainer-${todoId}`;
    const todoContainerId = `todo-${todoId}`;
    const checkButtonId = `completed-${todoId}`;
    const unCheckButtonId = `uncompleted-${todoId}`;

    const elementIds = [
        editInputId, updateTodoButtonId, buttonsContainerId, todoTextId,
        editButtonId, deleteButtonId, inputContainerId,
        checkButtonId, unCheckButtonId
    ];

    const newTodo = {
        id: todoId,
        status: "uncompleted",
        element: createElement(todoId, todoValue, elementIds)
    };

    todoList.push(newTodo);

    todoList.map((todoItem) => {
        todosContainer.prepend(todoItem.element);
    });

    const checkButton = document.querySelector(`#${checkButtonId}`);
    const unCheckButton = document.querySelector(`#${unCheckButtonId}`);
    const todoContainer = document.querySelector(`#${todoContainerId}`);
    const editButton = document.querySelector(`#${editButtonId}`);
    const deleteButton = document.querySelector(`#${deleteButtonId}`);
    const updateTodoButton = document.querySelector(`#${updateTodoButtonId}`);
    const editInput = document.querySelector(`#${editInputId}`);
    const todoText = document.querySelector(`#${todoTextId}`);
    const buttonsContainer = document.querySelector(`#${buttonsContainerId}`);
    const inputContainer = document.querySelector(`#${inputContainerId}`);

    checkButton.classList.add("hidden");
    checkButton.addEventListener("click", () => {
        const todoRef = todoId;
        todoCompleted = false;
        todoList.forEach((todoItem) => {
            if (todoItem.id === todoRef) todoItem.status = "uncompleted";
            return;
        });
        updateTodoStatus(todoCompleted, unCheckButton, checkButton, todoText);
        renderTodos(todoList, todosContainer, filterSelected);
    });

    unCheckButton.addEventListener("click", () => {
        const todoRef = todoId;
        todoCompleted = true;
        todoList.forEach((todoItem) => {
            if (todoItem.id === todoRef) todoItem.status = "completed";
            return;
        });
        updateTodoStatus(todoCompleted, unCheckButton, checkButton, todoText);
        renderTodos(todoList, todosContainer, filterSelected);
    });

    editButton.addEventListener("click", () => {
        updateInputVisibility(updateInputShowing, todoContainer, todoText, buttonsContainer, inputContainer);
        updateInputShowing = true; // Activer l'état d'édition
        editInput.focus(); // Focus sur l'input pour permettre l'édition
    });

    updateTodoButton.addEventListener("click", () => {
        todoText.innerHTML = editInput.value;
        updateInputShowing = false;
        updateInputVisibility(updateInputShowing, todoContainer, todoText, buttonsContainer, inputContainer);
    });

    deleteButton.addEventListener("click", () => {
        const todoIndex = todoList.findIndex(todoItem => todoItem.id === todoId);
        if (todoIndex !== -1) {
            const todoToRemove = todoList[todoIndex];
            todoList.splice(todoIndex, 1); // Supprimer la tâche de la liste
            todosContainer.removeChild(todoToRemove.element); // Supprimer l'élément de tâche du DOM
            renderTodos(todoList, todosContainer, filterSelected); // Mettre à jour l'affichage en fonction du filtre actuel
        }
    });
};

addTodoButton.addEventListener("click", () => {
    const value = addInput.value;
    if (value.length === 0) return;
    addToDo(id, value, todosContainer);
    console.log(filterSelected);
    renderTodos(todoList, todosContainer, filterSelected);
    id++;
    addInput.value = "";
});
//Code 4*****Mauvaise assignation******/
allFilterButton.addEventListener("click", () => {
    filterSelected = "all";
    allFilterButton.classList.add("selected");
    allFilterButton.classList.remove("unselected");
    uncompletedFilterButton.classList.add("unselected");
    uncompletedFilterButton.classList.remove("selected");
    completedFilterButton.classList.add("unselected");
    completedFilterButton.classList.remove("selected");
    renderTodos(todoList, todosContainer, filterSelected);
});

uncompletedFilterButton.addEventListener("click", () => {
    filterSelected = "uncompleted";
    allFilterButton.classList.remove("selected");
    allFilterButton.classList.add("unselected");
    uncompletedFilterButton.classList.remove("unselected");
    uncompletedFilterButton.classList.add("selected");
    completedFilterButton.classList.add("unselected");
    completedFilterButton.classList.remove("selected");
    renderTodos(todoList, todosContainer, filterSelected);
});

completedFilterButton.addEventListener("click", () => {
    filterSelected = "completed";
    allFilterButton.classList.remove("selected");
    allFilterButton.classList.add("unselected");
    uncompletedFilterButton.classList.add("unselected");
    uncompletedFilterButton.classList.remove("selected");
    completedFilterButton.classList.remove("unselected");
    completedFilterButton.classList.add("selected");
    renderTodos(todoList, todosContainer, filterSelected);
});
//***********Fin code 4*************** */

const months = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December",
};



const currentDate = new Date();
const year = currentDate.getFullYear();
const month = (currentDate.getMonth() + 1).toString().padStart(2, '0');
const day = currentDate.getDate().toString().padStart(2, '0');

const formattedDate = `${months[month]} ${day}, ${year}`;


const fetchWeatherData = async (city = "Montreal") => {
    const data = await fetch(`http://api.weatherapi.com/v1/forecast.json?key=f59a323ce8ad472a9dd213908231908&q=${city}`);
    const response = await data.json();
    const location = `${response.location.name}, ${response.location.country}`;
    const currTemp = `${response.current.temp_c}`;
    const highTemp = `${response.forecast.forecastday[0].day.maxtemp_c}`;
    const lowTemp = `${response.forecast.forecastday[0].day.mintemp_c}`;
    const condition = `${response.current.condition.text}`
    const cleanedData = [location, currTemp, condition, highTemp, lowTemp]
    return cleanedData;
}

const editCityButton = document.querySelector("#editCityButton");
const city = document.querySelector("#city");
const cityUpdateContainer = document.querySelector("#cityUpdateContainer");
const cityInput = document.querySelector("#cityInput");
const updateCityButton = document.querySelector("#updateCityButton");
const date = document.querySelector("#date");
const currTemp = document.querySelector("#currTemp");
const condition = document.querySelector("#condition");
const highTemp = document.querySelector("#highTemp");
const lowTemp = document.querySelector("#lowTemp");
date.innerHTML = formattedDate;

window.addEventListener("load", async () => {
    weatherData = await fetchWeatherData();
    city.innerHTML = weatherData[0];
    currTemp.innerHTML = `${weatherData[1]} <sup>o</sup>C`;
    condition.innerHTML = weatherData[2];
    highTemp.innerHTML = `H: ${weatherData[3]} <sup>o</sup>C`;
    lowTemp.innerHTML = `L: ${weatherData[4]} <sup>o</sup>C`;
});


editCityButton.addEventListener("click", () => {
    // Cacher le texte de la ville et le bouton "Change"
    city.classList.add("hidden");
    editCityButton.classList.add("hidden");

    // Afficher l'input de la ville et le bouton "Update"
    cityUpdateContainer.classList.remove("hidden");
    cityInput.value = city.innerHTML; // Pré-remplir l'input avec la ville actuelle
});

updateCityButton.addEventListener("click", async () => {
    // Mettre à jour les données météo avec la nouvelle ville
    weatherData = await fetchWeatherData(cityInput.value);

    // Mettre à jour les éléments HTML avec les nouvelles données météo
    city.innerHTML = weatherData[0];
    currTemp.innerHTML = `${weatherData[1]} <sup>o</sup>C`;
    condition.innerHTML = weatherData[2];
    highTemp.innerHTML = `H: ${weatherData[3]} <sup>o</sup>C`;
    lowTemp.innerHTML = `L: ${weatherData[4]} <sup>o</sup>C`;

    // Rétablir la visibilité du texte de la ville et du bouton "Change"
    city.classList.remove("hidden");
    editCityButton.classList.remove("hidden");

    // Cacher l'input de la ville et le bouton "Update"
    cityUpdateContainer.classList.add("hidden");
});

