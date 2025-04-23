from pyscript import document
from pyodide.ffi import create_proxy

display = document.getElementById('display')
inputField = document.getElementById('uinput')
inputBtn = document.getElementById('input-btn')

# Example: generate 10 starting paragraphs
for i in range(5):
    parag = document.createElement("p")
    parag.textContent = f"Bot Message: {i+1}"
    display.appendChild(parag)

def showInput(event = None):
    userInput = inputField.value
    user_p = document.createElement("p")
    user_p.textContent = "User: " + userInput
    display.appendChild(user_p)
    document.getElementById('uinput').value = ""

def submitKey(event):
    if event.key == "Enter":  # Check if the Enter key was pressed
        showInput()


proxy_showInput = create_proxy(showInput)
proxy_submit_key = create_proxy(submitKey)

inputBtn.addEventListener("click", proxy_showInput)
inputField.addEventListener("keydown", proxy_submit_key)