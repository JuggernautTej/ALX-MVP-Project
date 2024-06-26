document.addEventListener('DOMContentLoaded', () => {
    loadHome();
});

function loadHome() {
    fetch('/news/top')
        .then(response => response.json())
        .then(data => {
            const content = document.getElementById('content');
            content.innerHTML = createNewsGrid(data.news, 5);
        })
        .catch(error => console.error('Error fetching news:', error));
}

function loadTesla() {
    fetch('/news/tesla')
        .then(response => response.json())
        .then(data => {
            const content = document.getElementById('content');
            content.innerHTML = createNewsGrid(data.news, 10);
        })
        .catch(error => console.error('Error fetching news:', error));
}

function loadApple() {
    fetch('/news/apple')
        .then(response => response.json())
        .then(data => {
            const content = document.getElementbyId('content');
            content.innerHTML = createNewsGrid(data.news, 10);
        })
        .catch(error => console.error('Error fetching news;', error));
}

function loadAbout() {
    const content = document.getElementById('content');
    content.innerHTML = `
    <div class="about>
        <h2>About</h2>
        <p>Tech with Tej is a web service that provides the latest technology news, with focus on the most releavant headlines in the tech industry. Als, we provide the latest updates on Tesla and Apple.</p>
    </div>
    `;
}

function createNewsGrid(news, count) {
    const gridContainer = document.createElement('div');
    gridContainer.className = 'grid-container';
    news.slice(0, count). forEach(article => {
        const newsItem = document.createElement('div');
        newsItem.className = 'news-item';
        newsItem.innerHTML = `
        <img src="${article.urlToImage}" alt="${article.title}">
        <h2>${article.title}</h2>
        <p><small>By ${article.author} on ${new Date(article.publishedAt).toLocaleDateString()}</small></p>
        <a href="${article.url}" target="_blank">Read more</a>
        `;
        gridContainer.appendChild(newsItem);
    });
    return gridContainer.outerHTML;
}
