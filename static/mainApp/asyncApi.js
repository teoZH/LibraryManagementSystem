import {html, render} from 'https://unpkg.com/lit-html?module';


const divTemplate = (data) => {
    return html`
    ${data.length > 0 ? data.map(divElementTemplate) : noElementsTemplate()}
    `
}

const noElementsTemplate= () => {
    return html`<h1>No elements in the database!<h1>`
}

const divElementTemplate = (data) => {
    return html`
    <div class="last-3">
        <img src=${data.image} alt="some image">
        <h1>${data.title}</h1>
    </div>
    `
}


async function loadElements() {
    let element = document.getElementsByClassName('last')[0]
    const response = await fetch('http://127.0.0.1:8000/api/')
    if (response.ok) {
        let data = await response.json()
        data = Object.values(data)
        render(divTemplate(data),element)
    } else {
        console.log('Could not retrieve information!')
        alert('Some error happened, please reload!')
    }
}


window.addEventListener('load',loadElements)