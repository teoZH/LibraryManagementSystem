function navEvent(event) {
    let ulElem = document.querySelector('nav ul')
    Array.from(ulElem.children).forEach(elem => {
        if (paths[elem.firstChild.innerHTML] === window.location.pathname) {
            elem.firstChild.className = 'active';
        } else {
            elem.firstChild.className = ''
        }
    })
}
const paths = {
    'Home': '/',
    'Offer a book!': '/make-offer/',
    'Book Catalog':'/catalog/',
    'Password Change': '/auth/password-change/',
    'Login': '/auth/login/',
    'Logout': '/auth/logout/',
    'Register': '/auth/register/'
}



function paginationActive() {
    let page;
    let elements = document.querySelectorAll('.pagination .pages a')
    if (window.location.search.includes('page')) {
        page = window.location.search.split('page=')[1]
    } else {
        page = '1'
    }
    Array.from(elements).forEach(elem => {
        if (elem.innerHTML === page) {
            elem.className = 'active'
        } else {
            elem.className = ''
        }
    })
}


window.addEventListener('load', navEvent)
window.addEventListener('load',paginationActive)
